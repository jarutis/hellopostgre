import os

import psycopg2
from psycopg2.extras import RealDictCursor
from flask import Flask, jsonify, request

from .config import dsn

app = Flask(__name__)
conn = psycopg2.connect(dsn)


@app.route("/book", methods=["POST"])
def create():
    data = request.json
    record = {'name': data['name'], 'phone': data['phone']}
    with conn.cursor(cursor_factory = RealDictCursor) as cursor:
        sql = """INSERT INTO phonebook (name, phone)
                 VALUES (%(name)s, %(phone)s)
                 RETURNING id"""
        cursor.execute(sql, record)
        record['id'] = cursor.fetchone()['id']
    return jsonify(record), 201


@app.route("/books", methods=["GET"])
def read_all():
    with conn.cursor(cursor_factory = RealDictCursor) as cursor:
        sql = "SELECT id, name, phone FROM phonebook"
        cursor.execute(sql)
        result = cursor.fetchall()

    if not result:
        return '', 404

    return jsonify(result)


@app.route("/book/<int:id>", methods=["GET"])
def read(id):
    with conn.cursor(cursor_factory = RealDictCursor) as cursor:
        sql = "SELECT id, name, phone FROM phonebook WHERE id = %s"
        cursor.execute(sql, (id, ))
        result = cursor.fetchone()

    if not result:
        return '', 404

    return jsonify(result)


@app.route("/book/<int:id>", methods=["DELETE"])
def delete(id):
    with conn.cursor() as cursor:
        sql = "DELETE FROM phonebook WHERE id = %s"
        cursor.execute(sql, (id, ))
    return '', 204


@app.route("/book/<int:id>", methods=["PUT"])
def update(id):
    data = request.json
    with conn.cursor() as cursor:
        cursor.execute("SELECT id FROM phonebook WHERE id = %s", (id,))
        if not cursor.fetchone():
            return '', 404
        sql = "UPDATE phonebook SET name = %s, phone = %s WHERE id = %s"
        cursor.execute(sql, (data['name'], data['phone'], id))
    return '', 204
