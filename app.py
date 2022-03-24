from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "never-tell!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

@app.get("/")
def get_start():
    """Renders Survey Start page"""

    return render_template(
        "survey_start.html",
        title=survey.title,
        survey_instructions=survey.instructions)

@app.post("/begin")
def start_survey():
    """ redirects you to the questions once button is clicked """
    return redirect("/questions/0")

@app.get("/questions/<int:question_id>")
def get_questions(question_id):
    """ show the question page """

    question = survey.questions[question_id]
    choices=survey.questions[question_id].choices

    return render_template(
        "question.html",
        choices=choices,
        question=question,
        id=question_id)

@app.post("/questions/<int:question_id>")
def redirect_nextquestion(question_id):

    session[f"question{q_id}"] = request.form.answer
    q_id = question_id + 1

    if q_id < len(survey.questions):
        return redirect(f"/questions/{q_id}")
    else:
        return redirect("/completion")

@app.get("/completion")
def get_completion():
    """""Renders Completion page after survey is completed"""""


    return render_template("completion.html")


