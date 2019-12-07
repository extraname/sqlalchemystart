import json
from flask import Flask, Response, jsonify, request

app = Flask(__name__)

with open('data.json', 'r') as fh:
    data = json.loads(fh.read())['people']


@app.route("/version")
def version():
    return "1.0"


@app.route("/people")
def get_people():
    country = request.args.get("country")
    if country is not None:
        return jsonify([p for p in data if p["country"] == country])
    return jsonify(data)


@app.route("/people", methods=["POST"])
def post_people():
    person = request.get_json()  # возвращает в джсон тело запроса , котоырй передали
    person_id = len(data)

    data.append({"id": person_id, **person})

    return jsonify({"id": person_id}), 201


@app.route("/people/<int:id>")
def get_person(id: int):
    try:
        return jsonify(data[id])
    except IndexError:
        return Response("Not Found", status=404)


@app.route("/people/<int:id>", methods=["DELETE"])
def delete_person(id: int):
    try:
        data[id] = None
        return Response(status=204)
    except IndexError:
        return Response("Not Found", status=204)


@app.route("/people/<int:id>", methods=["PATCH"])
def update_person(id: int):
    try:
        data[id].update(request.get_json())
        return Response(status=204)
    except IndexError:
        return Response("Not Found", status=404)


if __name__ == "__main__":
    app.run()
