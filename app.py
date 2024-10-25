from flask import Flask, render_template, request
import pickle
import pandas as pd

#import salary

app = Flask(__name__)

@app.route("/", methods = ["GET", "POST"])
def hello() :
    sal = None
    if request.method == "POST":
        yoe = float(request.form["years_of_experience"])
        model = pickle.load(open('model.pkl','rb'))
        sal = model.predict(pd.DataFrame({'yoe' : [yoe]})).to_numpy()[0]
        sal = int(sal)
    return render_template("index.html", my_sal = sal)


if __name__ == "__main__":
    app.run(debug=True)