from flask import Flask, request, jsonify

import asyncio
from net.peer import Peer

app = Flask(__name__)


@app.route("/")
def index():
	return "Hello World"


@app.route("/compute", methods=['GET', 'POST'])
def compute():
	if request.method == 'GET': 
		return jsonify([True])
		# receive:
		# {
		#     "workflow_name": "test-workflow",
		#     "dataset_id": "HRI107",
		#     "operation": "std-dev",
		#     "PID": 1,
		#     "other_cardinals": [[1, "23.45.67.89:80"], [2, "34.56.78.90:80"]],
		# }

		# send to connect:
		# {
		#     "PID": "1",
		#     "parties": {
		#     	"1": {
		#     		"host": "23.45.67.89",
		#     		"port": "80",
		#     	},
		#     	"2": {
		#     		"host": "34.56.78.90",
		#     		"port": "80",
		#     	}
		#     }

		# }

	if request.method == 'POST': 
		# if key doesn't exist, returns None
		req = request.json
		peer_cfg = {
			"PID": req["PID"],
			"parties": {}
		}

		for entry in req["other_cardinals"]:
			ip = entry[1].split(":")
			obj = {"host": ip[0], "port": ip[1]}
			peer_cfg["parties"][str(entry[0])] = obj

		peer = setup_peer(peer_cfg)

		return jsonify(peer_cfg), 201

def setup_peer(config):

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    peer = Peer(loop, config)
    peer.connect_to_others()

    return peer


if __name__ == "__main__":
	app.run(host='0.0.0.0')



