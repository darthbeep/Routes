#<Firstname> <Lastname>
#SoftDev1 pd<p>
#HW<n> -- <Title/Topic/Summary>
#<yyyy>-<mm>-<dd>

from flask import Flask, url_for
app = Flask(__name__)


@app.route('/')
def index():
	text = "hi mr brown<br>this is a bad choose your own adventure game<br>to get started click the button <br>"
	text += "<a href='" + url_for('start_journey') + "'><button>click me</button></a>"
	return text

@app.route('/0')
def start_journey():
    return 'welcome to your journey<br>pick a weapon<br>' + makeButton('axe', 'axe') + "<br>" + makeButton('letter', 'strongly worded letter')

@app.route('/1')
def axe():
    return 'you have an axe<br>honestly this isn\'t the path i care about so im not bothing with it<br>so an orc eats you<br>you can restart now'

@app.route('/2')
def letter():
    return 'you chose a piece of paper<br>why would you do that<br>you\'re really stupid for choosing a letter<br>that\'s what the letter says<br>' + makeButton('fight', 'continue onwards with hurt feelings')

@app.route('/3')
def fight():
    return 'oh no you ran into an orc<br>it eats you because you\'re literally using a letter to defend yourself<br>rip you\'re dead now<br>i guess the moral of this story is don\'t play games made by tired students who have other homework to do'

#with app.test_request_context():
#	print url_for('start_journey')

def makeButton(buttonName, buttonText):
	return "<a href='" + url_for(buttonName) + "'><button>" + buttonText + "</button></a>"

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=5000, debug=True)
