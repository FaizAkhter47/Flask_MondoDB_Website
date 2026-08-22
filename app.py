from flask import Flask, jsonify, request, render_template, redirect, url_for
from pymongo import MongoClient
from dotenv import load_dotenv
import os
import json

load_dotenv()

app = Flask(__name__)

mongo_uri = os.getenv("MONGO_URI")
client = MongoClient(mongo_uri)

db = client["flask_mongodb_db"]
users = db["users"]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/import-data")
def import_data():
    try:
        with open("data.json", "r") as file:
            data = json.load(file)

        for user in data:
            users.update_one(
                {"id": user["id"]},
                {"$set": user},
                upsert=True
            )

        return jsonify({
            "message": "Data imported successfully",
            "count": len(data)
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


@app.route("/api")
def api():
    try:
        with open("data.json", "r") as file:
            data = json.load(file)

        return jsonify({
            "count": len(data),
            "data": data
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        }), 500


@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name")
    email = request.form.get("email")
    role = request.form.get("role")

    if not name or not email or not role:
        return render_template(
            "index.html",
            error="Please fill all the fields"
        )

    user_data = {
        "name": name,
        "email": email,
        "role": role
    }

    try:
        users.insert_one(user_data)
        return redirect(url_for("success"))

    except Exception as e:
        return render_template(
            "index.html",
            error="Something went wrong: " + str(e)
        )


@app.route("/success")
def success():
    return render_template("success.html")


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(debug=False)