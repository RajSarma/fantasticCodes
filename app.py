#!flask/bin/python
from flask import Flask, jsonify, abort

app = Flask(__name__)

tasks = [
    {
        'id': 1,
	'name': 'Raj',
        'title': 'Sarma',
        'roll': '1234', 
        'done': False
    },
    {
        'id': 2,
        'name': 'Qwerty',
	'title':'Abcd',
	'roll': '5678',
        'done': False
    }
]

@app.route('/todo/api/v1.0/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})


@app.route('/todo/api/v1.0/tasks/<n>', methods=['GET'])
def get_task(n):
    task = [task for task in tasks if task['name'] == n]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})

if __name__ == '__main__':
    app.run(debug=True)
