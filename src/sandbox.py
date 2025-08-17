import os
from crewai import Agent, Task, Crew, Process
from crewai_tools import SerperDevTool

# Set API keys
os.environ["OPENAI_API_KEY"] = "YOUR_OPENAI_API_KEY"
os.environ["SERPER_API_KEY"] = "YOUR_DUCKDUCKGO_API_KEY"

# Step 1: Create the DuckDuckGo Search Tool
search_tool = SerperDevTool(api_key=os.environ["SERPER_API_KEY"])

# Step 2: Create a minimal Researcher Agent (Focus on benefits, syntax, and simple functions)
researcher = Agent(
    role='PostgreSQL Researcher',
    goal='Research benefits of functions in PostgreSQL, PL/pgSQL syntax, and simple functions.',
    backstory="You are an expert researcher in PostgreSQL. Your task is to gather concise information on the benefits of functions in PostgreSQL and the basic syntax of PL/pgSQL functions.",
    tools=[search_tool],
    memory=False,  # No memory for cost savings
    verbose=False  # Limit verbosity to save API calls
)

# Step 3: Create a Writer Agent to summarize the research into a concise introduction
writer = Agent(
    role='Course Writer',
    goal='Write a short introduction chapter on PL/pgSQL functions based on the research.',
    backstory="You excel at writing short, concise technical content. Your task is to write a brief, focused chapter on PL/pgSQL functions.",
    tools=[],  # No additional tools for the writer
    memory=False,  # No memory for cost savings
    verbose=False  # Keep outputs short and simple
)

# Step 4: Define the Research Task (Limit the size and number of API calls)
research_task = Task(
    description="""
    Research three key areas related to PL/pgSQL functions:
    1. Benefits of using functions in PostgreSQL.
    2. The basic syntax of PL/pgSQL.
    3. Examples of simple functions.
    Keep your research brief, with no more than 300 words per section.
    """,
    expected_output="A short summary with the benefits, syntax, and an example of a simple function in PL/pgSQL.",
    agent=researcher,
    api_call_limit=2,  # Limit the number of API calls to reduce cost
    token_limit=500  # Keep the output concise and token usage low
)

# Step 5: Define the Writing Task (Produce concise final content)
write_task = Task(
    description="""
    Based on the research, write an introduction chapter on PL/pgSQL functions.
    Include the following:
    1. Benefits of using functions in PostgreSQL.
    2. A brief explanation of PL/pgSQL syntax.
    3. An example of a simple function.
    The final output should be no longer than 400 words.
    """,
    expected_output="A markdown-formatted introduction chapter, no more than 400 words.",
    agent=writer,
    inputs_from=[research_task],  # Use the researcher's output as input
    output_file="plpgsql-intro.md",  # Save the output to a file
    token_limit=500  # Limit token usage in the writing process
)

# Step 6: Define the crew and execution process
crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, write_task],
    process=Process.sequential  # Run tasks one after the other
)

# Step 7: Kick off the process
result = crew.kickoff(inputs={})
print(result)

# Optional: The final output will be saved in 'plpgsql-intro.md'
