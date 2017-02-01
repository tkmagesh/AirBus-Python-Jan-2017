from flask import request, Flask, render_template, session, redirect, url_for
import json
from io import StringIO

app = Flask(__name__)

bugs = [dict(id=1, name='User data not saved', is_closed=False), dict(id=2, name='Server communication failure', is_closed=True)]

@app.route('/')
def index():
	print([bugs])
	bugs_count = len(bugs)
	return render_template('index.html', bugs=bugs, bugs_count=bugs_count)



@app.route('/new')
def new_bug():
	return render_template('new-bug.html')

@app.route('/new', methods=['POST'])
def save_bug():
	bug_name = request.form['txtbugname']
	new_bug = dict(id=len(bugs) + 1, name=bug_name, is_closed=False)
	bugs.append(new_bug)
	return redirect('/')

@app.route('/toggle/<int:bug_id>')
def toggle_bug(bug_id):
	bug_to_toggle = filter(lambda bug: bug['id']==bug_id, bugs)[0]
	if bug_to_toggle:
		bug_to_toggle['is_closed'] = not bug_to_toggle['is_closed']
	return redirect('/')

@app.route('/removeclosed', methods=['POST'])
def remove_closed():
	global bugs
	bugs = filter(lambda bug: not bug['is_closed'], bugs)
	return redirect('/')

if __name__ == '__main__':
	app.run(port=3000)