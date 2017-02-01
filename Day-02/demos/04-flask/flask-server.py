from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/date')
def print_date():
	return render_template('get_date.html', data=str(datetime.today()))


@app.route('/calculator', methods=['GET'])
def get_calculator():
	data = { 'n1' : 0, 'n2' : 0, 'result' : 0}
	return render_template('calculator.html', data=data)

@app.route('/calculator', methods=['POST'])
def post_calculator():
	n1 = int(request.form['n1'])
	n2 = int(request.form['n2'])
	oper = request.form['operation']

	if oper=='add':
		result = n1 + n2

	if oper=='subtract':
		result = n1 - n2

	if oper=='multiply':
		result = n1 * n2

	if oper=='divide':
		result = n1 / n2

	data = { 'n1' : n1, 'n2' : n2, 'result' : result}
	return render_template('calculator.html', data=data)

if __name__ == '__main__':
	app.run(port=3000)