import pandas as pd
import os
BASE_DIR = '/Users/nitinchandekar/udemy-spark/Research/data/retail_db_json'
table_name = 'departments'
file_name = os.listdir(f'{BASE_DIR}/{table_name}')[0]
filepath=f'{BASE_DIR}/{table_name}/{file_name}'
df = pd.read_json(filepath, lines= True)

conn = 'postgresql://retail_user:itversity@localhost:5452/retail_db'
df.to_sql(table_name, conn, if_exists = 'append', index = False)