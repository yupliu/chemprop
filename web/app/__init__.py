"""Runs the web interface version of chemprop, allowing for training and predicting in a web browser."""
import os
from flask import Flask
from flask_cors import CORS
from flask_restful import Api

app = Flask(__name__)
CORS(app)

app.config.from_object('config')
api = Api(app)

os.makedirs(app.config['CHECKPOINT_FOLDER'], exist_ok=True)
os.makedirs(app.config['DATA_FOLDER'], exist_ok=True)

from app import views

api.add_resource(views.Users, '/users')
api.add_resource(views.User, '/users/<int:user_id>')

api.add_resource(views.Datasets, '/datasets')
api.add_resource(views.Dataset, '/datasets/<int:dataset_id>')
api.add_resource(views.DatasetFile, '/files/datasets/<int:dataset_id>')

api.add_resource(views.Checkpoints, '/checkpoints')
api.add_resource(views.Checkpoint, '/checkpoints/<int:checkpoint_id>')
api.add_resource(views.CheckpointFile, '/files/checkpoints/<int:checkpoint_id>')

api.add_resource(views.Train, '/train')
api.add_resource(views.Predict, '/predict')