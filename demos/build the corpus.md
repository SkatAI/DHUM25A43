# Notebook build the corpus

I want to create an exercise for my students to build a corpus using the NYT API in python.

- they have no coding experience at all
- they will prompt an LLM to generate the code
- I need to break down the overall corpus building exercise into granular tasks
- for each granular task they will write a prompt asking to generate the code, execute that code

Note that they have no prior knowlege of python or librairies and basic computer skills

they will work on google colab. so no need to install anything on their local computers.

I will give them a olab notebook that explains the sequence of tasks
They will clone that notebook and start generating code

please list all the steps they need to do in order to build the corpus
- interrogating the NYT API with key words
- saving the result on their google drive

---

here are the steps to build the corpus
after each step you should check always that what you assume is done ... is really done

for instance when you onnect your google drive to the notebook (also called mounting)
then you should check that the notebook can actually see the files in the google drive
for instance you can add a test file in the folder and ask colab to check for its existence.

working with LLMs is like catching a bar of soap in a ... swimming pool. always double check

## Setup Phase

* Setup Google Colab and Google Drive connection
  * Connect their Google Colab notebook to their Google Drive
  * Create a folder structure to save their corpus data

* Handle NYT API Key
  * Store the API key securely in the notebook
  * advanced / alternative
    + Register for a NYT Developer account
    + Create a new application to obtain an API key

## API Interaction Phase

* Import required libraries
  - Request code to import necessary Python libraries - [will be done automatically, but check that they are available]

* Create a function that makes API requests to the NYT given a keyword or a list of keywords

== python list of keywords: keywords = ['hello', 'world']

The NYT has multiple APIs depending on what you search for.
https://developer.nytimes.com/apis
we're using the article searc api
https://developer.nytimes.com/docs/articlesearch-product/1/overview

Ask the LLM to explain this API to you and how to query it
besides keywords what else can you or do you need to pass along
ask for examples to make things more concrete
test the examples the LLM gives you

note you can also get the results in a browser
https://api.nytimes.com/svc/search/v2/articlesearch.json?q=macron&page=2&sort=newest&api-key=peobAzpzjKGm8GlTy33AVPj3XnQ0Cqj0


the page is not your usual web page. explore the tabs and results

if the results are too braod explore other means of querying the API
spoiler : for instance fq=headline:("keyword") OR lead_paragraph:("keyword")
https://api.nytimes.com/svc/search/v2/articlesearch.json?fq=headline:("macron") or lead_paragraph:("macron")&page=1&sort=newest&api-key=peobAzpzjKGm8GlTy33AVPj3XnQ0Cqj0


* check: Test the API connection
  * Make a simple test request to verify the API key works
  * Print the response to confirm successful connection
  * explore the result you get from the API request



## Search and Collection Phase

ok seems everything is working so far. let's switch back to the colab and building the corpus

- ask the LLM to refine the querying function to suit your neewds and understanding of how to query the API.

- also can you handle a list of keywords instead of just one keyword ?
- what elements in the page interest you ? headline, lead_paragraph ? article body ?

At this point, you would start iterating to refine your list of keywords, making requests, inspecting the results etc

Always start small and expand afterwards.

But to understand the results you are getting you need to find a way to view them

- get basic stats : number of articles, length of articles, ....
- some visualization that help you understand the quality of your data
- this is the subject of the second notebook



1. Extract relevant article information
   - Parse the JSON response from the API
   - Extract useful fields (headline, date, abstract, URL, etc.)
   - Store the extracted data in a structured format

2. Implement pagination for comprehensive results
   - Handle the NYT API pagination system
   - Create a loop to collect multiple pages of results
   - Track progress during collection

## Data Storage Phase

At this point you have a dataset, a corpus and you want to save it.

rememeber that saving it to the local notebook, the data will disappear if you close the notebook of if the runtime stops.

So you want to save the data to you google drive, to make it permanent

You can ask the LLM to "Mount" your google drive
or save the data ina google spreadsheet
and then save the data as a csv or json file

csv if you want to easilty visualize it
json if you don't wan tto deal with sv format (for instane if you data has lotsd of other embedded snippets)




1. Convert collected data to DataFrame
   - Transform the collected articles into a pandas DataFrame
   - Clean and standardize the data fields

2.  Save data to CSV file in Google Drive
    - Create a timestamp-based filename
    - Save the DataFrame as a CSV to their Google Drive folder
    - Verify the file was saved correctly

## Advanced Features (Optional)

11. Add metadata collection
    - Collect additional metadata about the search results
    - Store information about the query parameters used

12. Implement rate limiting
    - Add delays between API requests to avoid hitting rate limits
    - Track usage to stay within free tier limits

13. Build a simple visualization of results
    - Create a basic chart showing article counts by date or section
    - Generate a word frequency analysis of headlines or abstracts

## Suggested Colab Notebook Structure

For your instructor notebook that students will clone, I recommend this structure:

1. Introduction to the exercise
2. Prerequisites (getting an NYT API key)
3. Task breakdown with empty code cells for each step above
4. Example prompts they could use to ask an LLM to generate each piece of code
5. Brief explanations of what each code section does (to build understanding)
6. Checkpoints to verify their code is working as expected

Would you like me to expand on any specific part of this plan or provide sample code for any of these steps?


---

# Building a Corpus with the New York Times API

Welcome to this exercise where you'll build a text corpus using the New York Times (NYT) API! You don't need any prior programming experience - you'll use an AI assistant to help you generate all the code needed.

**Important**: After completing each step, always verify that what you expected to happen actually happened. Working with AI-generated code requires careful checking at each stage.

## API Interaction Phase

### Step 1: Set Up the Environment

**Outcome**: Install and import necessary tools for making web requests and handling data.

**Why**: Your code needs specific tools to communicate with the NYT API and process the data it returns.

### Step 2: Store the NYT API Key

**Outcome**: Your API key is securely stored for use in future requests.

**Why**: The NYT API requires an authentication key to process your requests.

### Step 3: Test the API Connection

**Outcome**: Confirm that you can successfully connect to the NYT API.

**Why**: Before building a corpus, you need to verify that your setup can communicate with the NYT servers.

**Verification**: You should see data returned from the API. If you see an error message, check your API key.

### Step 4: Explore the API Response

**Outcome**: Understand the structure of the data returned by the API.

**Why**: Knowing how the data is organized will help you extract the specific information you need for your corpus.

**Verification**: Try a simple query in your web browser by visiting the API URL directly:
```
https://api.nytimes.com/svc/search/v2/articlesearch.json?q=YOURKEYWORD&api-key=YOURAPIKEY
```
Compare this with your code's output to ensure consistency.

## Search and Collection Phase

### Step 5: Refine the Search Function

**Outcome**: Create a function that finds articles where keywords appear in specific parts of the article.

**Why**: Basic searches may return articles where your keyword appears anywhere on the page, not just in the article itself. You'll want to target your search to headlines or lead paragraphs using the 'fq' parameter.

**Verification**: Compare results from a targeted search (using 'fq') with a general search to see the difference:
```
https://api.nytimes.com/svc/search/v2/articlesearch.json?fq=headline:("YOURKEYWORD")&api-key=YOURAPIKEY
```

### Step 6: Handle Multiple Keywords and Pagination

**Outcome**: Collect multiple pages of results for a list of keywords.

**Why**: The NYT API limits results to 10 articles per page, but you'll want to collect more for a substantial corpus. You'll also want to search for multiple keywords to build a diverse corpus.

**Verification**: Track how many articles are collected for each keyword and across pages.

### Step 7: Extract Relevant Information

**Outcome**: Extract specific fields from each article (headline, date, lead paragraph, URL, etc.).

**Why**: Raw API responses contain many fields you don't need. Extracting only relevant information makes your corpus more usable for analysis.

## Data Storage Phase

### Step 8: Connect to Google Drive

**Outcome**: Connect this notebook to your Google Drive so you can save your work permanently.

**Why**: Data stored only in the notebook will disappear when the session ends. Connecting to Google Drive allows for permanent storage.

**Verification**: Create a test file in your Google Drive through code and verify it appears in your Drive.

### Step 9: Save Corpus to Google Drive

**Outcome**: Save your collected articles as a structured file in Google Drive.

**Why**: Saving your corpus as a file allows you to reuse it later without having to collect the data again.

**Options**:
- CSV format: Good for simple data that you want to view in spreadsheet applications
- JSON format: Better for complex data with nested structures

### Step 10: Basic Corpus Analysis

**Outcome**: Generate basic statistics and visualizations of your corpus.

**Why**: Understanding the characteristics of your corpus (number of articles, publication dates, content length) helps assess its quality and usefulness.

## Troubleshooting Tips

- If you get an error message, ask the AI assistant to explain the error and suggest fixes
- If the API returns no results, try different keywords or check your query syntax
- Always verify each step works as expected before moving on to the next

Good luck building your corpus!