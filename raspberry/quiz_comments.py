## Imports
from guizero import App, TextBox, PushButton, Picture, Text
from random import randrange

## Create a list of questions
questions = ['What is you name?',
             'What is your quest?',
             'What is the air speed velocity of an unladen swallow']

## Create a list of answers
answers = ['Arthur, King of the Britons',
           'I seek the Grail',
           'An African or a European swallow']

## Function to call at start of quiz
def start():
    ## Choose a random number between 0 and the number of questions
    question.index_value = randrange(len(questions))
    ## Display the text for the chose question
    question.value = questions[question.index_value]
    ## Change the text in the button to 'Next'
    start.text = 'Next'
    ## Show the check answer button
    check_answer.show()

## Function to call when check_answer button is pressed
def check():
    ## Check if the answer in the box is identical to the answer in the list
    if input_box.value == answers[question.index_value]:
        question.value = 'Correct'
    else:
        question.value = 'Incorrect'

## Create and App
app = App(title='Quiz', width=400, height=300)
## Text for the question
question = Text(app, text='Ready to start the quiz?')
## Box for the answer
input_box = TextBox(app, text='Answer')
## Button to check the answer
check_answer = PushButton(app, command = check, text='Check answer')
## Hide the button until we start
check_answer.hide()
## Button to start the quiz, then used as Next from that point onwards
start = PushButton(app, command=start, text='Start')

app.display()
