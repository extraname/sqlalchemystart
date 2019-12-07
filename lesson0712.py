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
    print(request.get_json())
    return "Its works"


@app.route('/people/<id>')
def get_person(id):
    try:
        return jsonify(PEOPLE[int(id)])
    except IndexError:
        return Response('Not Found', status=404)


if __name__ == "__main__":
    app.run()
