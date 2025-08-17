# get a mapping of all the main names in artificial intelligence
# mapping by topic

# list of pages : from links in main AI page
# from each page: NER (Persons)
# sentence embeddings
# main sentences for each persons
# mapping with plotly
import pandas as pd
import numpy as np

import wikipediaapi
import spacy
from sentence_transformers import SentenceTransformer, util

# Load spaCy's English language model
nlp = spacy.load("en_core_web_sm")

# Load the sentence embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")


# Define a user agent string that includes your project name and contact information
user_agent = 'MyPythonApp/1.0 (https://example.com/contact)'

# Initialize the Wikipedia API with the user agent and language
wiki_wiki = wikipediaapi.Wikipedia(user_agent=user_agent, language='en')



# Retrieve the Wikipedia page for Paris
page = wiki_wiki.page('Artificial_intelligence')


import pandas as pd
import numpy as np
import plotly.graph_objects as go
import networkx as nx
from sklearn.metrics.pairwise import cosine_similarity

# Compute sentence similarity matrix
people = df["person"].unique()
embedding_dict = {
    person: np.mean(df[df["person"] == person]["embedding"].tolist(), axis=0)
    for person in people
}
similarity_matrix = cosine_similarity(list(embedding_dict.values()))

# Create a graph
G = nx.Graph()
person_sentences = {person: df[df["person"] == person]["sentence"].tolist() for person in people}

# Add nodes with sentence data
for person in people:
    sentences = "<br>".join(person_sentences[person])  # Format sentences for hover text
    G.add_node(person, label=person, sentences=sentences)

# Add edges based on similarity scores
for i in range(len(people)):
    for j in range(i + 1, len(people)):
        weight = similarity_matrix[i, j]
        if weight > 0.5:  # Similarity threshold
            G.add_edge(people[i], people[j], weight=weight)

# Get node positions using spring layout
pos = nx.spring_layout(G, seed=42)  # Fix seed for consistent layout

# Extract edge positions
edge_x = []
edge_y = []
edge_weights = []
for edge in G.edges(data=True):
    x0, y0 = pos[edge[0]]
    x1, y1 = pos[edge[1]]
    edge_x.extend([x0, x1, None])
    edge_y.extend([y0, y1, None])
    edge_weights.append(edge[2]['weight'])

# Create edge traces
edge_trace = go.Scatter(
    x=edge_x,
    y=edge_y,
    line=dict(width=1, color="gray"),
    hoverinfo="text",
    text=[f"Similarity: {w:.2f}" for w in edge_weights],
    mode="lines"
)

# Extract node positions and labels
node_x = []
node_y = []
node_text = []
for node in G.nodes():
    x, y = pos[node]
    node_x.append(x)
    node_y.append(y)
    node_text.append(f"<b>{node}</b><br>{G.nodes[node]['sentences']}")

# Create node traces with hover text
node_trace = go.Scatter(
    x=node_x,
    y=node_y,
    mode="markers+text",
    text=[n for n in G.nodes()],
    hoverinfo="text",
    hovertext=node_text,
    textposition="top center",
    marker=dict(size=20, color="blue", opacity=0.8, line=dict(width=2, color="black")),
)

# Create figure with zooming enabled
fig = go.Figure(data=[edge_trace, node_trace])
fig.update_layout(
    showlegend=False,
    hovermode="closest",
    title="Sentence Similarity Graph",
    margin=dict(b=0, l=0, r=0, t=40),
    dragmode="zoom",  # Enable zooming
)

fig.show()
