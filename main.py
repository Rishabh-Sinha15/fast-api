from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)  # Initialize flask app

with open(r"C:\Users\risha\OneDrive\Documents\rest api\model.pkl","rb") as fileobj:
    iris_model = pickle.load(fileobj)

@app.route("/", methods=["GET"])  # ✅ FIXED HERE
def home():
    return "Welcome to my world"



@app.route("/get_square",methods = ["POST"])

def get_squares():
    data = request.get_json()
    number = data.get("number")
    return jsonify({"square of the number": number**2})

@app.route("/predict", methods=["POST"])  # <-- this is the controller
def iris_prediction():  # <-- this is the view function
    data = request.get_json()
    sepal_length = data.get("sl")
    sepal_width = data.get("sw")
    petal_length = data.get("pl")
    petal_width = data.get("pw")

    flower_type = iris_model.predict([[sepal_length, sepal_width, petal_length, petal_width]])
    return jsonify({"predicted_flower_type": flower_type[0]})




if __name__ == "__main__":
    app.run()