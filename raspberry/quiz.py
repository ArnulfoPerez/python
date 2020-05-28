from guizero import App, TextBox, PushButton, Picture, Text
from random import randrange

questions = ['What is you name?',
             'What is your quest?',
             'What is the air speed velocity of an unladen swallow?']


answers = ['Arthur, King of the Britons',
           'I seek the Grail',
           'An African, or an European swallow?']


def start():
    question.index_value = randrange(len(questions))
    question.value = questions[question.index_value]
    start.text = 'Next'
    check_answer.show()


def check():
    if input_box.value == answers[question.index_value]:
        question.value = 'Correct'
    else:
        question.value = 'Incorrect'


app = App(title='Quiz', width=400, height=300)
question = Text(app, text='Ready to start the quiz?')
input_box = TextBox(app, text='Answer')
check_answer = PushButton(app, command = check, text='Check answer')
check_answer.hide()
start = PushButton(app, command=start, text='Start')

app.display()
