Flask MongoDB Project

This is a simple Flask project made using Python and MongoDB.

The project reads data from a JSON file and can store that data in MongoDB. It also has a small form where a user can enter their name, email and role. After submitting the form, the data is saved in MongoDB and the user is taken to a success page.

What this project does

- Connects Flask with MongoDB Atlas
- Reads data from data.json
- Shows data through the /api route
- Imports JSON data into MongoDB
- Takes user details through a form
- Saves submitted details in MongoDB
- Shows a success page after submitting the form
- Includes a simple health check

Technologies Used

- Python
- Flask
- MongoDB Atlas
- PyMongo
- HTML
- python-dotenv

Project Files

Flask_MongoDB_Faiz_Akhter/
│
├── app.py
├── data.json
├── requirements.txt
├── .env
├── .env.example
├── .gitignore
├── README.md
│
└── templates/
    ├── index.html
    └── success.html

How to Run

First clone the repository:

git clone YOUR_GITHUB_REPOSITORY_URL

Go inside the project folder:

cd Flask_MongoDB_Faiz_Akhter

Create a virtual environment:

python -m venv venv

For Windows, activate it:

venv\Scripts\activate

Install the required packages:

pip install -r requirements.txt

MongoDB Setup

Create a .env file in the project folder and add your MongoDB connection string:

MONGO_URI=your_mongodb_connection_string

Do not upload the .env file to GitHub because it contains the database connection details.

A sample .env.example file is included in the project.

Start the Application

Run:

python app.py

Then open:

http://127.0.0.1:5000

Routes

Home

GET /

This opens the form page.

API

GET /api

This reads the data from data.json and returns it in JSON format.

Import Data

GET /import-data

This reads data.json and saves the records in MongoDB.

Submit

POST /submit

This receives the form data and stores it in MongoDB.

Success

GET /success

This page is shown after the form is submitted successfully.

Health Check

GET /health

This checks whether the Flask application is running.

Example response:

{
    "status": "ok"
}

Author

Faiz Akhter

BCA Graduate | DevOps & Cloud Computing

About the Project

I made this project to practice Flask, MongoDB, JSON files, API routes, form handling and environment variables.