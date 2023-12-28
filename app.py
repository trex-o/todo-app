from flask import Flask, render_template, request, url_for, redirect
from pymongo import MongoClient
from bson.objectid import ObjectId

app = Flask(__name__)

client = MongoClient('mongodb', 27017)
db = client.flask_db
todos = db.todos


@app.route('/', methods=('GET', 'POST'))
def home():
    if request.method == 'POST':
        content = request.form['content']
        degree = request.form['degree']
        todos.insert_one({'content': content, 'degree': degree})
        return redirect(url_for('home'))
    elif request.method == 'GET':
        all_todos = todos.find()
        return render_template('index.html', todos = all_todos)

@app.post('/<id>/delete/')
def delete(id):
    todos.delete_one({"_id": ObjectId(id)})
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(host='0.0.0.0')
