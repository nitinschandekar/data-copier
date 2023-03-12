import pandas as pd
def main():
    fp = '/Users/nitinchandekar/udemy-spark/Research/data/retail_db_json/order_items/part-r-00000-6b83977e-3f20-404b' \
         '-9b5f-29376ab1419e'
    #df = pd.read_json(fp, lines=True)
    json_reader = pd.read_json(fp, lines=True, chunksize=1000)
    for idx , df  in enumerate(json_reader):
        print(f'Numbrt of records in chunk with index {idx} is {df.shape[0]}')
    print(df.count())
    print(df.describe())
    print(df.columns)
  #  df.dtypes
if (__name__ == '__main__'):
    main()