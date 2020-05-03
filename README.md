# Toy example of RESTful api

Flask based API with PostgreSQL. Uses
[distroless](https://github.com/GoogleContainerTools/distroless)
docker image for app. 

Using distroless python results in 72 MB image size versus 199 MB
using 3.7-slim-buster.

![demo](https://raw.githubusercontent.com/jarutis/hellopostgre/master/img/crud.gif)

## Usage

Start app with PostgreSQL server:

```bash
docker-compose up
```

Get all phonebook entries:

```bash
curl -X GET localhost:5000/book/entries
```

Get entry by id:

```bash
curl -X GET localhost:5000/book/1
```

Add new entry:
```bash
curl -X POST \
  -d '{"name":"boo", "phone":"+123"}' \
  -H 'Content-Type: application/json' \
  http://0.0.0.0:5000/book
```

Update existing entry:

```bash
curl -X PUT \
  -d '{"name":"bob", "phone":"+432"}' \
  -H 'Content-Type: application/json' \
  http://0.0.0.0:5000/book/1
```

Delete entry:

```bash
curl -X DELETE http://0.0.0.0:5000/book/1
```

# References
[1] https://hackersandslackers.com/flask-routes/  
[2] https://www.vinaysahni.com/best-practices-for-a-pragmatic-restful-api
