from flask import Flask
from flask import json

app = Flask(__name__)


@app.route("/<restaurant>")
def inspection_failure(restaurant="Default"):
    """
    This REST GET endpoint takes a restaurant name as a URL resource and returns
    :param restaurant:
    :return:
    """
    data = {
        "facility": restaurant,
    }
    if restaurant[0].lower() in "rstlne":
        data["score"] = 0
    else:
        data["score"] = 1
    response = app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype="application/json"
    )
    return response


if __name__ == "__main__":
    app.run()
