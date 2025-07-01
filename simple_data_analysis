import os
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
from langchain.agents import AgentType
from langchain_openai import ChatOpenAI
from langchain_community.chat_models import ChatOllama
import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

np.random.seed(42)


n_rows = 100 # Generate sample data

start_date = datetime(2022, 1, 1)
dates = [start_date + timedelta(days=i) for i in range(n_rows)]

# Define data categories
makes = ['Toyota', 'Honda', 'Ford', 'Chevrolet', 'Nissan', 'BMW', 'Mercedes', 'Audi', 'Hyundai', 'Kia']
models = ['Sedan', 'SUV', 'Truck', 'Hatchback', 'Coupe', 'Van']
colors = ['Red', 'Blue', 'Black', 'White', 'Silver', 'Gray', 'Green']

# Create the dataset
data = {
    'Date': dates,
    'Make': np.random.choice(makes, n_rows),
    'Model': np.random.choice(models, n_rows),
    'Color': np.random.choice(colors, n_rows),
    'Year': np.random.randint(2015, 2023, n_rows),
    'Price': np.random.uniform(20000, 80000, n_rows).round(2),
    'Mileage': np.random.uniform(0, 100000, n_rows).round(0),
    'EngineSize': np.random.choice([1.6, 2.0, 2.5, 3.0, 3.5, 4.0], n_rows),
    'FuelEfficiency': np.random.uniform(20, 40, n_rows).round(1),
    'SalesPerson': np.random.choice(['Alice', 'Bob', 'Charlie', 'David', 'Eva'], n_rows)
}


df = pd.DataFrame(data).sort_values('Date')
print(df.head(20))


df.info()
df.describe()


llm = ChatOllama(model="mistral", temperature=0.7) 

agent = create_pandas_dataframe_agent(
    llm,
    df,
    verbose=True,
    allow_dangerous_code=True,
)
print("Data Analysis Agent is ready. You can now ask questions about the data.")


def ask_agent(question):
    response = agent.invoke({
        "input": question,
        "agent_scratchpad": f"Human: {question}\nAI: To answer this question, I need to use Python to analyze the dataframe. I'll use the python_repl_ast tool.\n\nAction: python_repl_ast\nAction Input: ",
    },
    config={"handle_parsing_errors": True}                        
                           )
    
    print(f"Question: {question}")
    print(f"Answer: {response}")
    print("---")


ask_agent("What are the column names in this dataset?")
#ask_agent("How many rows are in this dataset?")
#ask_agent("What is the average price of cars sold?")