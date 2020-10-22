from flask import Flask, render_template, request
from quiz import Quiz
app = Flask(__name__)

quiz = Quiz()

@app.route("/questions")
def show_all_text():
    return render_template('questions.html', questions=quiz.quiz_data)

@app.route("/progress")
def show_quiz():
    return render_template('progress.html', questions=quiz.quiz_data)

if __name__ == "__main__":
    app.run()
