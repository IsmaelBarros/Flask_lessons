from flask import Blueprint, Response, request
from models.estudante import db, Estudante
import json

app = Blueprint('estudantes', __name__)


@app.route('/')
def index():
    estudantes = Estudante.query.all()
    result = [e.to_dict() for e in estudantes]
    return Response(response=json.dumps(result), status=200, content_type='application/json')


@app.route('/view/<int:id>', methods=['GET'])
def view(id):
    row = db.session.execute(
        "SELECT * FROM estudante WHERE id = %s" % id).fetchone()
    return Response(response=json.dumps(dict(row)), status=200, content_type='application/json')


@app.route('/add', methods=['POST'])
def add():
    estudante = Estudante(request.form['nome'], request.form['idade'])
    db.session.add(estudante)
    db.session.commit()
    return Response(response=json.dumps({'status': 'successs', 'data': estudante.to_dict()}), status=200, content_type='application/json')


@app.route('/edit/<int:id>', methods=['PUT', 'POST'])
def edit(id):
    estudante = Estudante.query.get(id)
    estudante.nome = request.form['nome']
    estudante.idade = request.form['idade']
    db.session.commit()
    return Response(response=json.dumps(estudante.to_dict()), status=200, content_type='application/json')


@app.route('/delete/<int:id>', methods=['GET', 'DELETE'])
def delete(id):
    estudante = Estudante.query.get(id)
    db.session.delete(estudante)
    db.session.commit()
    return Response(response=json.dumps(estudante.to_dict()), status=200, content_type='application/json')