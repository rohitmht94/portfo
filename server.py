from flask import Flask, render_template, url_for, request, redirect
import csv
app = Flask(__name__)



'''
@app.route('/')
def hello_world():
    return 'Hello, World!'
'''

# here we are declaring what must be present is the url of our website by using variable rules for URLs!
#find out more about that in the URLs variable rules section on FLask!
@app.route('/')
#def hello_world(username = None, post_id = None): # here we are passing some default values!
def Home():
    return render_template('index.html')

# dynamic way to do!
@app.route('/<string:page_name>')
def html_pages(page_name = None):
    return render_template(page_name)

'''
# manual way to do!
@app.route('/works.html')
def works():
    return render_template('works.html')


@app.route('/components.html')
def components():
    return render_template('components.html')


@app.route('/contact.html')
def contact():
    return render_template('contact.html')

@app.route('/about.html')
def about():
    return render_template('about.html')
'''
def write_to_file(data):
	with open('database.text', mode = 'a') as database:
		email = data['email']
		subject = data['subject']
		message = data['message']
		file = database.write(f'\n{email},{subject},{message}')


def write_to_csv(data):
	with open('database.csv', mode = 'a', newline='') as database2:
		email = data['email']
		subject = data['subject']
		message = data['message']
		csv_writer =  csv.writer(database2, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
		csv_writer.writerow([email,subject,message])


@app.route('/submit_form', methods=['POST', 'GET']) # post is used to save and get is used to send!
def submit_form():
	if request.method == 'POST':
		try:
			data = request.form.to_dict()
			#data.append('./database.')
			write_to_csv(data)
			return redirect('/thank_you.html')
		except:
			return 'do not add this to database'
	else:
		return 'something went wrong. try again!!'
                           