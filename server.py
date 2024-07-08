from flask import Flask, render_template, request, redirect
import csv
app = Flask(__name__)

@app.route("/")
def my_home():
    return render_template('index.html')

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)

with open('database.csv', 'w') as csvfile:
    fieldnames = ['email', 'subject', 'message']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter = ';')
    writer.writeheader()

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f'{email}, {subject}{message}')

def write_to_csv(data):
    with open('database.csv', mode='a', newline ='') as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database2, delimiter=";", quoting = csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():

    if request.method == 'POST':
        try:

            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'did not save on the DB'

    else:
        return 'something wrong'


