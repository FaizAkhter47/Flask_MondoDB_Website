from flask import (
    Flask,
    jsonify,
    request,
    render_template,
    redirect,
    url_for
)

from pymongo import MongoClient
from dotenv import load_dotenv

import os
import json


# Load environment variables from .env file
load_dotenv()


# Create Flask application
app = Flask(__name__)


# ==========================================
# MongoDB Connection
# ==========================================

mongo_uri = os.getenv("MONGO_URI")

client = MongoClient(mongo_uri)


# Database
db = client["flask_mongodb_db"]


# Collection
users = db["users"]


# ==========================================
# HOME ROUTE
# Display frontend form
# ==========================================

@app.route("/")
def home():

    return render_template("index.html")


# ==========================================
# IMPORT DATA ROUTE
# Read data.json and insert into MongoDB
# ==========================================

@app.route("/import-data", methods=["GET"])
def import_data():

    try:

        # Open data.json file
        with open("data.json", "r") as file:

            # Load JSON data
            data = json.load(file)


        # Insert or update every user
        for user in data:

            users.update_one(

                # Check existing user by ID
                {
                    "id": user["id"]
                },

                # Update user data
                {
                    "$set": user
                },

                # Create if user does not exist
                upsert=True

            )


        # Send success response
        return jsonify({

            "message": "Data imported successfully",

            "count": len(data)

        })


    except Exception as e:

        return jsonify({

            "message": "Error importing data",

            "error": str(e)

        }), 500


# ==========================================
# API ROUTE
# Read MongoDB data and return JSON response
# ==========================================

@app.route("/api", methods=["GET"])
def api():

    try:

        # Get all data from MongoDB
        data = list(

            users.find(

                {},

                {
                    "_id": 0
                }

            )

        )


        # Return API response
        return jsonify({

            "message": "Data fetched successfully",

            "count": len(data),

            "data": data

        })


    except Exception as e:

        return jsonify({

            "message": "Error fetching data",

            "error": str(e)

        }), 500


# ==========================================
# SUBMIT ROUTE
# Receive form data and insert into MongoDB
# ==========================================

@app.route("/submit", methods=["POST"])
def submit():

    try:

        # Get data from HTML form
        name = request.form.get("name")

        email = request.form.get("email")

        role = request.form.get("role")


        # Validate form fields
        if not name or not email or not role:

            return render_template(

                "index.html",

                error="All fields are required"

            )


        # Create dictionary
        user_data = {

            "name": name,

            "email": email,

            "role": role

        }


        # Insert form data into MongoDB Atlas
        users.insert_one(user_data)


        # ==================================
        # REDIRECT TO SUCCESS PAGE
        # ==================================

        return redirect(

            url_for("success")

        )


    except Exception as e:

        # Stay on same page if error occurs
        return render_template(

            "index.html",

            error=str(e)

        )


# ==========================================
# SUCCESS ROUTE
# Show success page after successful submission
# ==========================================

@app.route("/success")
def success():

    return render_template(

        "success.html"

    )


# ==========================================
# RUN FLASK APPLICATION
# ==========================================

if __name__ == "__main__":

    app.run(

        debug=True

    )