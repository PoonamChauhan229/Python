from flask import Flask, request, jsonify

app = Flask(__name__)

tasks = []
task_id_counter = 1  # to auto-increment IDs


@app.route('/')
def hello_world():
    return jsonify({"message": "Welcome to App without DB performing CRUD"})


@app.route('/tasks', methods=['POST'])
def create_task():
    global task_id_counter
    data = request.json
    data['id'] = task_id_counter  # assign auto id
    task_id_counter += 1
    tasks.append(data)
    return jsonify({"message": "Task Created Successfully", "task": data})


@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)


@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.json
    for task in tasks:
        if task.get('id') == task_id:
            task.update(data)
            task['id'] = task_id  # ensure ID doesn't get overwritten
            return jsonify({"message": "Task Updated", "task": task})
    return jsonify({"error": "Task Not Found"}), 404


@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    for task in tasks:
        if task.get("id") == task_id:
            tasks.remove(task)
            return jsonify({"message": "Task Deleted", "task": task})
    return jsonify({"error": "Task Not Found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
