from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/")
def index():
	return "Hello World"


@app.route("/compute", methods=['GET', 'POST'])
def compute():
	if request.method == 'GET': 
		return jsonify([True])

	if request.method == 'POST': 
		# if key doesn't exist, returns None
		num = int(request.form['num'])
		ret = num+1
		ret_obj = {'result': ret}

		return jsonify(ret_obj), 201


if __name__ == "__main__":
	app.run()