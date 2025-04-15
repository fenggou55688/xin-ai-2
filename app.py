from flask import Flask, render_template, request, redirect, url_for
import random
from utils import predict_next, update_roads, analyze_patterns

app = Flask(__name__)

history = []

@app.route("/", methods=["GET", "POST"])
def index():
    global history
    suggestion = ""
    prediction = {}

    if request.method == "POST":
        result = request.form.get("result")
        if result in ["B", "P", "T"]:
            history.append(result)
        if request.form.get("action") == "Undo" and history:
            history.pop()

    if history:
        prediction = predict_next(history)
        suggestion = "建議下注：閒" if prediction['P'] > prediction['B'] else "建議下注：莊"

    roads = update_roads(history)
    patterns = analyze_patterns(history)

    return render_template("index.html",
                           history=history,
                           roads=roads,
                           prediction=prediction,
                           suggestion=suggestion,
                           patterns=patterns)

if __name__ == "__main__":
    app.run(debug=True)
