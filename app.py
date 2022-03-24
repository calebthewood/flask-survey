from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "never-tell!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

debug = DebugToolbarExtension(app)

RESPONSES = []
question_id = 0

@app.get("/")
def get_start():
    '''Renders Survey Start page'''

    return render_template("survey_start.html",title=survey.title,survey_instructions = survey.instructions)

@app.post("/begin")
def start_survey():
    """ redirects you to the questions once button is clicked """
    return redirect("/questions/0")

@app.get("/questions/<int:question_id>")
def post_questions(question_id):
    """ show the question page """
    RESPONSES.append(request.args)
    print (RESPONSES)
    question = survey.questions[question_id]
    choices=survey.questions[question_id].choices
    return render_template("question.html",choices=choices ,question=question)
    
@app.post("/answer")
def redirect_nextquestion():
    question_id += 1
    return redirect(f"/questions/{question_id}")


