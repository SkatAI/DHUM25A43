# Your turn

Constitute a dataset of content from
wikipedia pages related to a given topic.

For instance :
- Extract all information related to
  immigration from European capitals
  pages
- Given a list of political parties en
  France, find their position on the
  environment

Think of
- page attributes
- generate list of pages
  beforehand
- tell the LLM to use the
  wikipedia library
- how you output the data

---

# Steps

The method is important. It's a gradual iterative process. build on a series of small actions

- Using the wikipedia api library, find the page for Paris
- In the page of Paris, extract the section titles
- In the section titled Demographics or equivalent, extract the information on immigration

---

# Prompts Precisions

The LLM has a tendency to recreate the whole code from scratch (installing etc ...). To avoid that, state that the libraries are already installed, the page is already available etc

The code is often too complex. I specify : `simple code, not for production, no error handling, python beginner level`

Ask for potential methods first (and no code), then specify the one you want to generate the code.
