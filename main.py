from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, make_response
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
        'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


# Creating model table for our CRUD database
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    description = db.Column(db.String(300))

    def __init__(self, name, description):
        self.name = name
        self.description = description

db.create_all()


@app.route('/get_all_books/')
def get_books():

    data = Book.query.all()

    list = []
    for d in data:
        obj = {
            "id": d.id,
            "name": d.name,
            "description": d.description,
        }
        list.append(obj)
    return make_response(jsonify(books=list), 200)


@app.route('/books/', methods=['POST'])
def books():
    if request.method == 'POST':

        name = request.form['name']
        description = request.form['description']

        # if name == 0:

        # else:
        result = Book.query.filter_by(name=name).update(dict(name=name, description=description))
        if not result:
            my_data = Book(name, description)
            db.session.add(my_data)

        db.session.commit()

        return redirect('/get_all_books/')


@app.route('/search/', methods=['GET'])
def search_book():
    if request.method == 'GET':
        search = request.args.get('search', False)
        if search:
            data = Book.query.filter(Book.name.contains(search))
            list = []
            for d in data:
                obj = {
                    "id": d.id,
                    "name": d.name,
                    "description": d.description,
                }
                list.append(obj)
            return make_response(jsonify(books=list), 200)
        else:
            return make_response(jsonify(books={
                    "name": "No Book Found",
                    "description": None,
                }), 200)


@app.route('/')
def index():
    return render_template("base.html", base_url='http://127.0.0.1:5000')


@app.route('/delete/<id>/')
def delete(id):
    db.session.delete(Book.query.get(id))
    db.session.commit()

    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True)
