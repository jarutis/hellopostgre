# Toy example of RESTful api

Flask based API with PostgreSQL. Uses
[distroless](https://github.com/GoogleContainerTools/distroless)
docker image for app. 

Using distroless python results in 72 MB image size versus 199 MB
using 3.7-slim-buster.

![demo](https://raw.githubusercontent.com/jarutis/hellopostgre/master/img/crud.gif)

# References
[1] https://hackersandslackers.com/flask-routes/  
[2] https://www.vinaysahni.com/best-practices-for-a-pragmatic-restful-api
