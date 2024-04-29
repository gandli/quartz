# %%
import pandas as pd

data = pd.read_csv("data.csv")
data.head()

# %%
from langchain_community.llms import Ollama

llm = Ollama(model="llama3")

# %%
from pandasai import SmartDataframe

df = SmartDataframe(data, config={"llm": llm})

# %%
df.chat("What are the top 5 cities for average income?")

# %%
df.chat(
    "Calculate the average income for each occupation and then rank the top 5 occupations from highest to lowest"
)

# %%
df.chat(
    "First, sort the cities by average income from high to low, then create a bar chart displaying the top 10 cities by average income"
)

# %%
df.chat(
    "First, calculate the number of people in each occupation, and then create a pie chart for the top 5 occupations by count"
)

# %%
df.chat("为我分析数据集，先从多维度分析，再提出关键问题和相应的回答")
