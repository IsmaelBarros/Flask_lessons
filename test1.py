from flask import Flask, request
import json

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def index():
    #print('ismael', request.method, request.args)
    t1 = request.args.to_dict()
    t2 = dict(request.args)
    return json.dumps([t1, t2])

    # return json.dumps(request.args['nome'])


if __name__ == '__main__':
    app.run(debug=True)
