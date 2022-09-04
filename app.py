
from flask import Flask, render_template, request , jsonify
import joblib

import numpy as np





app= Flask(__name__)
model = joblib.load(open("model.pkl", "rb"))


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/predict", methods=["GET","POST"])
def predict():
    try:
     init=[float(x) for x in request.form.values()]
     final=[np.array(init)]
     prediction=model.predict(final)
     output=round(prediction[0],2)
     return render_template("index.html",prediction_text=f"The price of house {output}/-")
    except:
        return render_template("index.html",prediction_text=f"Invalid input")




if __name__ == "__main__":
    app.run(debug=True)