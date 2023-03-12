import pandas as pd
import os


def get_json_reader(BASE_DIR, table_name, chunksize=1000):
    file_name = os.listdir(f'{BASE_DIR}/{table_name}')[0]
    fp = f'{BASE_DIR}/{table_name}/{file_name}'
    print("in get_json_reader, file path is ", fp)
    return pd.read_json(fp, lines=True, chunksize=chunksize)
