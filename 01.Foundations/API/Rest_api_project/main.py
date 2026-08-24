from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# 1. Create Flask app
app = Flask(__name__)

# 2. Configure database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"

# 3. Initialize database
db = SQLAlchemy(app)


# 4. Create your model
class Notebook(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)


class Dataset(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    type = db.Column(db.String)

    


# 5. GET - Get all resources
@app.route("/notebook", methods=["GET"])
def get_notebooks():

    # 1. Fetch all resources from database
    notebooks = Notebook.query.all()

    # 2. Create empty list for response
    result = []

    # 3. Convert each resource into a dictionary
    for notebook in notebooks:
        result.append({
            "id": notebook.id,
            "name": notebook.name
        })

    # 4. Return JSON response
    return jsonify(result), 200


# GET - Get all resources
@app.route("/dataset", methods=["GET"])
def get_datasets():

    # 1. Fetch all resources from database
    datasets = Dataset.query.all()

    # 2. Create empty list for response
    result = []

    # 3. Convert each resource into a dictionary
    for dataset in datasets:
        result.append({
            "id": dataset.id,
            "name": dataset.name,
            "type": dataset.type
        })

    # 4. Return JSON response
    return jsonify(result), 200


#GET - Get only one resource
@app.route("/notebook/<int:id>", methods=["GET"])
def get_notebook(id):

    # 1. Find the resource using the ID from URL
    notebook = Notebook.query.get(id)

    # 2. Check if it exists
    if not notebook:
        return jsonify({
            "message": "Resource not found"
        }), 404

    # 3. Convert it to dictionary
    result = {
        "id": notebook.id,
        "name": notebook.name
    }

    # 4. Return it
    return jsonify(result), 200


@app.route("/dataset/<int:id>", methods=["GET"])
def get_dataset(id):

    # 1. Find the resource using the ID from URL
    dataset = Dataset.query.get(id)

    # 2. Check if it exists
    if not dataset:
        return jsonify({
            "message": "Resource not found"
        }), 404

    # 3. Convert it to dictionary
    result = {
        "id": dataset.id,
        "name": dataset.name,
        "type": dataset.type
    }

    # 4. Return it
    return jsonify(result), 200


# 7. POST - Create a resource
@app.route("/notebook", methods=["POST"])
def create_notebook():

    # 1. Get data from request
    data = request.get_json()

    # 2. Create database object
    for notebook_data in data:
        notebook = Notebook(name=notebook_data["name"])

        db.session.add(notebook)

    # 4. Save permanently
    db.session.commit()

    # 5. Send response
    return jsonify({
        "message": "Resource created"
    }), 201


# 7. POST - Create a resource
@app.route("/dataset", methods=["POST"])
def create_dataset():

    # 1. Get data from request
    data = request.get_json()

    # 2. Create database object
    for dataset_data in data:
        dataset = Dataset(
            name=dataset_data["name"],
            type=dataset_data["type"]
        )

        db.session.add(dataset)

    # 4. Save permanently
    db.session.commit()

    # 5. Send response
    return jsonify({
        "message": "Resource created"
    }), 201


# PUT - to update whole dictionary
@app.route("/notebook/<int:id>", methods=["PUT"])
def replace_notebook(id):

    # 1. Find resource
    notebook = Notebook.query.get(id)

    # 2. Check if resource exists
    if not notebook:
        return jsonify({
            "message": "Resource not found"
        }), 404

    # 3. Get data from request
    data = request.get_json()

    # 4. Replace ALL fields
    notebook.name = data["name"]

    # 5. Save
    db.session.commit()

    # 6. Response
    return jsonify({
        "message": "Resource updated"
    }), 200


# PUT - to update whole dictionary
@app.route("/dataset/<int:id>", methods=["PUT"])
def replace_dataset(id):

    # 1. Find resource
    dataset = Dataset.query.get(id)

    # 2. Check if resource exists
    if not dataset:
        return jsonify({
            "message": "Resource not found"
        }), 404

    # 3. Get data from request
    data = request.get_json()

    # 4. Replace ALL fields
    dataset.name = data["name"]
    dataset.type = data["type"]

    # 5. Save
    db.session.commit()

    # 6. Response
    return jsonify({
        "message": "Resource updated"
    }), 200


# 8. PATCH - Update a resource
@app.route("/notebook/<int:id>", methods=["PATCH"])
def update_notebook(id):

    # 1. Find the resource
    notebook = Notebook.query.get(id)

    # 2. Check if it exists
    if not notebook:
        return jsonify({
            "message": "Resource not found"
        }), 404

    # 3. Get data from request
    data = request.get_json()

    # 4. Update only the fields provided
    if "name" in data:
        notebook.name = data["name"]

    # 5. Save changes
    db.session.commit()

    # 6. Return response
    return jsonify({
        "message": "Resource updated"
    }), 200


# 8. PATCH - Update a resource
@app.route("/dataset/<int:id>", methods=["PATCH"])
def update_dataset(id):

    # 1. Find the resource
    dataset = Dataset.query.get(id)

    # 2. Check if it exists
    if not dataset:
        return jsonify({
            "message": "Resource not found"
        }), 404

    # 3. Get data from request
    data = request.get_json()

    # 4. Update only the fields provided
    if "name" in data:
        dataset.name = data["name"]

    if "type" in data:
        dataset.type = data["type"]

    # 5. Save changes
    db.session.commit()

    # 6. Return response
    return jsonify({
        "message": "Resource updated"
    }), 200


# 9. DELETE - Delete a resource
@app.route("/notebook/<int:id>", methods=["DELETE"])
def delete_notebook(id):

    # 1. Find the resource using the ID
    notebook = Notebook.query.get(id)

    # 2. Check if it exists
    if not notebook:
        return jsonify({
            "message": "Resource not found"
        }), 404

    # 3. Delete the resource
    db.session.delete(notebook)

    # 4. Save the change to database
    db.session.commit()

    # 5. Return response
    return jsonify({
        "message": "Resource deleted"
    }), 200


# 9. DELETE - Delete a resource
@app.route("/dataset/<int:id>", methods=["DELETE"])
def delete_dataset(id):

    # 1. Find the resource using the ID
    dataset = Dataset.query.get(id)

    # 2. Check if it exists
    if not dataset:
        return jsonify({
            "message": "Resource not found"
        }), 404

    # 3. Delete the resource
    db.session.delete(dataset)

    # 4. Save the change to database
    db.session.commit()

    # 5. Return response
    return jsonify({
        "message": "Resource deleted"
    }), 200


# 10. Run the application
if __name__ == "__main__":

    with app.app_context():
        db.create_all()

    app.run(debug=True)