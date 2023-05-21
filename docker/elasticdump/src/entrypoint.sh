elasticdump --input=/tmp/pokemon_mapping.json --output=http://elasticsearch:9200/pokemon --type=mapping
elasticdump --input=/tmp/pokemon_data.json --output=http://elasticsearch:9200/pokemon --type=data
