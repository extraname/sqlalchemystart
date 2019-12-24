from flask import jsonify, request
from models import User
from settings import app, db


# В оРМ таблица называется модель

@app.route('/users', methods=['GET'])
def ger_users():
    return jsonify([u.serialize() for u in User.query.all()]), 200


@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    user = User(**data)
    db.session.add(user)
    db.session.commit()

    return jsonify({"id": user.id}), 201


@app.route('/users/<int:userid>', methods=['PATCH'])
def update_user(userid):
    data = request.get_json()
    db.session.query(User).filter_by(id=userid).update(data)
    db.session.commit()
    return {}, 204


@app.route('/users/<int:userid>', methods=['DELETE'])
def delete_user(userid):
    db.session.query(User).filter_by(id=userid).delete()
    db.session.commit()
    return {}, 200


@app.route("/users/<int:userid>", methods=['GET'])
def get_user(userid):
    return User.query.get(userid).serialize()


if __name__ == "__main__":
    app.run()
