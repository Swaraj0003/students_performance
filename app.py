from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        student_data = {
            "gender": request.form.get("gender"),
            "race_ethnicity": request.form.get("race_ethnicity"),
            "parental_education": request.form.get("parental_education"),
            "lunch": request.form.get("lunch"),
            "test_prep": request.form.get("test_prep"),
            "math_score": request.form.get("math_score"),
            "reading_score": request.form.get("reading_score"),
            "writing_score": request.form.get("writing_score"),
        }
        return render_template("results.html", student_data=student_data)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

