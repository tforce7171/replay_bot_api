from flask import Flask, request
from flask_restful import Api, Resource
import json

app = Flask(__name__)
api = Api(app)
replay_data_path = "C:\\Users\\taisei\\programs\\replay_to_movie\\replay_data.json"


class GetReplay(Resource):
    def get(self):
        json_open = open('replay_data.json', 'r')
        json_load = json.load(json_open)
        with open(replay_data_path) as file:
            replay_data = json.load(file)
        return replay_data

class DeleteReplay(Resource):
    def delete(self, replay_name):
        with open(replay_data_path) as file:
            replay_data = json.load(file)
            replay_data.pop(replay_name)
        with open(replay_data_path, mode='wt') as file:
          json.dump(replay_data, file, indent=2)
        return {"result":"success"}

api.add_resource(GetReplay, "/replay")
api.add_resource(DeleteReplay, "/replay/<string:replay_name>")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
