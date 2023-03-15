docker run -it \
  --name data-copier --rm \
  --network data-copier-nw \
  -v /Users/nitinchandekar/udemy-spark/Research/data/retail_db_json:/retail_db_json \
  -e BASE_DIR=/retail_db_json \
  -e DB_HOST=e2ae555e6133 \
  -e DB_PORT=5432 \
  -e DB_NAME=retail_db \
  -e DB_USER=retail_user \
  -e DB_PASS=itversity \
  data-copier python /data-copier/src/app.py
