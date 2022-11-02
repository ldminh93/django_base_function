# chatty
# run elastic search 
docker run -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:7.14.0
# build index
python manage.py search_index --rebuild
# run redis
docker run -p 6379:6379 -d redis:5