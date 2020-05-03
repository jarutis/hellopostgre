FROM python:3.7-slim-buster AS build
COPY requirements.txt ./
RUN pip install -r requirements.txt

FROM gcr.io/distroless/python3-debian10
COPY --from=build /usr/local/lib/python3.7/site-packages/ /usr/lib/python3.7/.

WORKDIR /usr/src/app
COPY ./src ./src
COPY manage.py manage.py
ENTRYPOINT [ "python" ]
CMD ["manage.py"]
