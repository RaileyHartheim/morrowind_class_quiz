import os

from flask import Flask, render_template, request
from quiz import Quiz
from class_description import ClassDescription
app = Flask(__name__, static_folder=os.path.join(os.getcwd(), "static"))

quiz = Quiz()
class_information = ClassDescription()

@app.route("/")
@app.route("/greeting")
def show_greeting():
    return render_template('greeting.html')

@app.route("/progress", methods=["GET", "POST"])
def show_quiz():
    if request.method == "GET":
        return render_template('progress.html', questions=quiz.quiz_data)
    elif request.method == "POST":
        user_answers = request.form.to_dict()
        chosen_class = quiz.get_results(user_answers)
        return render_template('results.html', result=chosen_class, information=class_information.description)


if __name__ == "__main__":
    app.run()

