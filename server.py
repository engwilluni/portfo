from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)


@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_file(data)
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save to database'

    else:
        return 'something went wrong. Try again!'



def write_to_file(data):
    with open('database.txt', mode='a') as file:
        file.write(f'\n{data["email"]}, {data["subject"]}, {data["message"]}')


def write_to_csv(data):
    with open('database.csv', 'a', newline='') as csvfile:
        fieldnames = ['email', 'subject', 'message']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        #writer.writeheader()
        writer.writerow({'email': data['email'], 'subject': data['subject'], 'message': data['message']})


# @app.route('/')
# def my_home():
#     return render_template('index.html')


# @app.route('/index.html')
# def index():
#     return render_template('index.html')
#
#
# @app.route('/about.html')
# def about():
#     return render_template('about.html')
#
#
# @app.route('/works.html')
# def works():
#     return render_template('works.html')
#
#
# @app.route('/contact.html')
# def contact():
#     return render_template('contact.html')
#
#
# @app.route('/components.html')
# def components():
#     return render_template('components.html')
