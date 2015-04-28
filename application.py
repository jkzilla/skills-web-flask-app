from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def homepageapp():
	return render_template('/index.html')

@app.route('/submit', methods=['GET', 'POST'])
def applying():
	first = request.form("first-name"), 
	last = request.form("last-name"), 
	salary = request.form("salary"), 
	job = request.form("job")
	return render_template("/submit.html", first=first, last=last, job=job, salary=salary)
if __name__ == "__main__":
	app.debug = True
	app.run()