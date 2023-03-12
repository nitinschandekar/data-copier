import pandas as pd
import os

BASE_DIR = '/Users/nitinchandekar/udemy-spark/Research/data/retail_db_json'
table_name = 'orders'
file_name = os.listdir(f'{BASE_DIR}/{table_name}')[0]
filepath = f'{BASE_DIR}/{table_name}/{file_name}'
json_reader = pd.read_json(filepath, lines=True, chunksize=1000)
conn = 'postgresql://retail_user:itversity@localhost:5452/retail_db'

for idx , df in enumerate(json_reader):
    df.to_sql(table_name, conn, if_exists='append', index=False)
    print(f'Processed index {idx}')
