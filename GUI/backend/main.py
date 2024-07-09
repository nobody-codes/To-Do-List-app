from flask import request, jsonify
from config import app, db
from models import Task


@app.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = Task.query.all()
    json_tasks = list(map(lambda x : x.to_json(), tasks))
    return jsonify({"tasks" : json_tasks})


@app.route("/create_task", methods=["POST"])
def create_task():
    value = request.json.get("value")
    status = request.json.get("status")
    
    if not value or not status:
        return (jsonify({"message" : "ERROR -- Incomplete Data"}), 400)
    
    new_task = Task(value=value, status=status)
    
    try:
        db.session.add(new_task)
        db.session.commit()
    except Exception as e:
        return (jsonify({"message" : str(e)}), 400)
    
    return (jsonify({"message" : "Task Added"}), 201)

@app.route("/update_task/<int:user_id>", methods=["PATCH"])
def update_task(user_id):
    task = Task.query.get(user_id)

    if not task:
        return jsonify({"message": "Task not found"}), 404

    data = request.json
    task.value = data.get("value", task.value)
    task.status = data.get("status", task.status)

    db.session.commit()

    return jsonify({"message": "Task updated."}), 200


@app.route("/delete_task/<int:user_id>", methods=["DELETE"])
def delete_contact(user_id):
    task = Task.query.get(user_id)

    if not task:
        return jsonify({"message": "Task not found"}), 404

    db.session.delete(task)
    db.session.commit()

    return jsonify({"message": "Task deleted!"}), 200
    


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    
    app.run(debug=True)