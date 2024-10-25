from llama_index.core.tools import FunctionTool
import pandas as pd

def check_date_columns(df, date_column):
    # check lengths
    length = df[date_column].str.len().value_counts()
    print(length)

    if length.shape[0] == 1:
        print('Only one combination, proceed to infer the format.')

check_date = FunctionTool.from_defaults(
    fn=check_date_columns,
    name='date column checker',
    description='this tool can detect how many date combinations are in a column'
)
    
    