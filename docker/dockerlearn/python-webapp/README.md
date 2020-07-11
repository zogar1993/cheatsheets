docker container run --name="webapp" -p=1322:1322 -v="$PWD"/app:/app -d --rm python_webapp
docker-compose up webapp
