from flask import Flask, Response, jsonify, request

app = Flask(__name__)
PEOPLE = [
    {
        'id': 0,
        'name': "Steve",
        'age': 20,
        'country': 'US'
    },
    {
        'id': 1,
        'name': "Jack",
        'age': 11,
        'country': 'Spain'
    },
    {
        'id': 2,
        'name': "John",
        'age': 30,
        'country': 'Poland'
    },
    {
        'id': 3,
        'name': "Selena",
        'age': 21,
        'country': 'US'
    }
]


@app.route('/version')
def version():
    return '1.0'


@app.route('/people')
def get_people():
    country = request.args.get('country')
    if country is not None:
        return jsonify([p for p in PEOPLE if p["country"] == country])
    return jsonify(PEOPLE)


@app.route('/people', methods=['POST'])
def post_people():
    person = request.get_json()  # возвращает в джсон тело запроса , котоырй передали
    person_id = len(PEOPLE)

    PEOPLE.append({'id': person_id, **person})

    return jsonify({"id": person_id}), 201


@app.route('/people/<id>')
def get_person(id):
    try:
        return jsonify(PEOPLE[int(id)])
    except IndexError:
        return Response('Not Found', status=404)


@app.route('/people/<id>', methods=["DELETE"])
def delete_person(id):
    try:
        PEOPLE[int(id)] = None
        return Response(status=204)
    except IndexError:
        return Response('Not Found', status=204)


@app.route('/people/<id>', methods=['PATCH'])
def update_peron(id):
    try:
        PEOPLE[int(id)].update(request.get_json())
        return Response(status=204)
    except IndexError:
        return Response('Not Found', status=404)


if __name__ == "__main__":
    app.run()
