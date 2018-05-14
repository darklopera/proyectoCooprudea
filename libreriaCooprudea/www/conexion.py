from flask import Flask
from flask_cors import CORS
import os

class connection:

	def create_connection(self, dbname, localhost , enviroment):
		app = Flask(__name__)
		CORS(app)
		app.config['MONGO_DBNAME'] = dbname
		app.config['MONGO_URI'] = os.environ.get(enviroment, localhost)
		return app
