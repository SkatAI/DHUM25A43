# Create a web app visualization

In this workshop, you will learn how to

- extract arguments from a corpus
- create a simple visualization application using streamlit
- [bonus] publish the app online via a public github repo

# start


## Open a github account

- go to github.com and open an account

it's free!

## Hello world

Go to github.dev

This is a smaller version of a real code editor (VS code, ...)

It has everything you need to create applications! Live! Online!

- open the terminal

CTRL + `

control + backtick

- click on

Continue working in Github spaces

This will create a server and your own space on it!

It's entirely another laptop . runs on Linux. Ubuntu!

In the terminal you can install things.
Just like we did in google colab

for instance

```shell
pip install streamlit
```

do that now

- CTRL + `
- pip install streamlit

## Create some code

- create a new folder `demo`
- create a new file `app.py`
- in the file add the following 3 lines

```python
import streamlit as st

st.title("Hello World! 🌍")
st.write("This is my first Streamlit app!")
```

## Launch the app
Then in the terminal write

```shell
streamlit run demo/app.py
```

on my terminal this is what it looks like

```shell
@alexisperrier ➜ /workspaces/dev (main) $ streamlit run streamlit-demo/app.py
```

It should output something like

```shell

Collecting usage statistics. To deactivate, set browser.gatherUsageStats to false.


  You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://10.0.11.52:8501
  External URL: http://172.166.156.167:8501
```

The local URL is the URL where you can see your first streamlit app!

That URL might be different on your machine. Maybe the number 8501 is just 8500 so the url is
`http://localhost:8500` instead of `http://localhost:8501`


so go to `http://localhost:8501`

and marvel at your newly discovered super powers


## ok now a bit more involved


go to your favorite LLM friend (chatGPT is good) and

write down a prompt saying that

```
- you are using github.dev
- you want to develop a simple streamlit app
- to explore the titanic dataset

please write a simple code so that users can

- filter by age or gender
- visualize some data about the titanic
- make sure to color code passengers who have survived (blue) or not (red)
```

Then copy-paste the generated code into the file app.py

You can delete the previous Hello world code.

relaunch your app with `streamlit run demo.app.py` if you have stopped it

and go to your local URL

### better viz

The generated code is using seaborn. A great visualization library but there's a better one.

Plot.ly can create interactive visualization

We can ask chatGPT to improve the code with

- use plot.ly instead of streamlit
- hovering on each dot in the scatterplot should show the name of the passenger

copy paste the code over the previous code

and check the difference

you do not have to stop and restart the app. It should automatically relaunch with the modified code.

# Next Project

Let's recap and start working on your projects


start a google document if you haven't done so already

share it with Andrei and Alexis

- dataset description
- link to the dataset in csv or JSON format
- problem statement : what you want to show, your hypothesis, your exploration plan, ....


process from raw data to enriched data : tagging, labels, summary, arguments etc

- describe the type of analysis you want to do
- prompts and code on google colab
  - links to google colab
- enriched data files

- visualizations

list 2 or 3 data visualization you want to obtain that show what you want to demonstrate











# generate a corpus with arguments


The European parliament

-----------

# Using the terminal

open the terminal : spotlight term
install brew https://brew.sh/
install iterm2 https://iterm2.com/ brew install --cask iterm2

install pip


# Start simple

Let's take a simple dataset and show how we can create a simple application to visualize it

We will use chatGPT to generate the code

We first need a specification file where we will write down the details off what we want to achieve.

The specification file is composed of

- goals: what we want to achieve
- context: description of your laptop and overall tech knowledge
- technical details: language, librairies, ...
- features: what the user can do
- description of the dataset

We will call that file : readme.md and upload it to chat GPT

A readme file is the first file you see on a github repository

## Readme.md

project: a simple data visualization demo of the titanic dataset using streamlit
context:  total beginner with python and streamlit; work on a macbook
tech context: streamlit on local, pandas dataframe, plotly for visualization
features: the user filters the dataset through menus on the sidebar
data vizualization includes
- histograms for continuous variables: age, ticket price

All graphs indicate passenger suvival with blue for survived, blue for did not survive

code: as simple as possible, not production level,

## prompt

please read the readme file
and generate the code for the visualization app
guide me through the installation of libraries, using the terminal and launching the streamlit app




