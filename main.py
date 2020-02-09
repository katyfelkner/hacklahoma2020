# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_python37_app]
from flask import Flask
from flask import request
from flask import render_template
import pymongo

# TODO: move pw into an environment variable to keep this secure
client = pymongo.MongoClient("mongodb+srv://admin:hackybois@cluster0-o46xu.gcp.mongodb.net/test?retryWrites=true&w=majority")
db = client.test


# this entire application depends on a bunch of globals. Terrible practice.
score_vector = []
rating_vector = []

# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/loadgame')
def load_next_game():
    # read results of last game
    finish_game(request.args.get('score'), request.args.get('rating'))

    # call RL agent to get a decision on next game to run

@app.route('/shapesgame')
def load_shapes_game():
    return render_template('shapes_game.html')
    
def finish_game(score, rating):
    # if not none, add to vectors
    if score:
        score_vector.append(score)
    if rating:
        rating_vector.append(rating)

    # check if it's time to batch learn and reassess
    # call that if needed

    # else return
def batch_learn():
    # time to batch learn 
    pass

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python37_app]


