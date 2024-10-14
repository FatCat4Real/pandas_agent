from pandasai import SmartDataframe
from pandasai.llm.local_llm import LocalLLM

model = LocalLLM(api_base="http://localhost:11434/v1", model="llama3.2")

df = SmartDataframe("data/Amazon_Sales_Report.csv", config={"llm": model})

df.chat('How many date columns are in the dataframe?')