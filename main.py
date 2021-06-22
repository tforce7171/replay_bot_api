from flask import Flask, request
from flask_restful import Api, Resource
from flask_cors import CORS
import json
import os
import psycopg2

app = Flask(__name__)
api = Api(app)
CORS(app)
replay_data_path = "C:\\Users\\taisei\\programs\\replay_to_movie\\replay_data.json"


class GetReplay(Resource):
    def get(self):
        conn = DBConnect()
        cur = conn.cursor()
        cur.execute('SELECT * FROM replay_data')
        replay_data_list = cur.fetchall()
        replay_data_hash = {}
        for replay_data in replay_data_list:
            replay_data_hash[replay_data[0]] = {
                "time_unix": replay_data[1],
                "file_url": replay_data[2],
                "channel_id": replay_data[3],
                "visibility": replay_data[4],
                "title": replay_data[5],
                "output_channel_id": replay_data[6],
                "playlist": replay_data[7]
            }

        # json_open = open('replay_data.json', 'r')
        # json_load = json.load(json_open)
        # with open(replay_data_path) as file:
        #     replay_data = json.load(file)
        return replay_data_hash

class DeleteReplay(Resource):
    def delete(self, replay_name):
        conn = DBConnect()
        cur = conn.cursor()
        command = "DELETE FROM replay_data WHERE filename=\'" + replay_name + "\'"
        cur.execute(command)
        return {"result":"success"}

def DBConnect():
    DATABASE_URL = os.environ['DATABASE_URL']
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
    return conn

api.add_resource(GetReplay, "/replay")
api.add_resource(DeleteReplay, "/replay/<string:replay_name>")

if __name__ == "__main__":
    # app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
    app.run()
