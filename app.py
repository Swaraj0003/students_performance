from flask import Flask, render_template, request
import pickle
import os
import jsonify
import pandas as pd
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        student_data = {
            "gender": request.form.get("gender"),
            "race_ethnicity": request.form.get("race_ethnicity"),
            "parental_education": request.form.get("parental_education"),
            "lunch": request.form.get("lunch"),
            "test_prep": request.form.get("test_prep")
        } 
        df = pd.DataFrame([student_data])
        mapping = {"gender":{"female":0,"male":1},"race_ethnicity": {"group A":0,"group B":1,"group C": 2,"group D":3,"group E":4},"parental_education":{"bachelor's degree":1,"some college":4,"master's degree":3,"associate's degree":0,"high school":2,"some high school":5},"lunch":{"standard":1,"free":0},"test_prep":{"none":1,"completed":0}}
        df.replace(mapping, inplace=True)
        folder=os.path.join("data","models","model.pkl")
        df.rename(columns={"race_ethnicity": "race"}, inplace=True)
         
        with open(folder, "rb") as file:
            l = pickle.load(file)
        predict=l.predict(df)
        
        
        return render_template("results.html", student_data=predict)
    
    
    return render_template("index.html") 

if __name__ == "__main__":
    app.run(debug=True)
