import os

from flask import Flask
from route import pages
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()


app = Flask(__name__)
app.register_blueprint(pages)
client = MongoClient(os.environ.get("MONGODB_URI"))
app.db = client.get_default_database()

if __name__ == '__main__':
    app.run()