from flask import Flask, request, render_template, redirect, url_for
import csv
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/aboutMe.html')
def about():
    return render_template('aboutMe.html')

@app.route('/main.html')
def projects():
    return render_template('main.html')

@app.route('/contact.html', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Ensure the CSV file exists and has headers
        file_exists = os.path.isfile('contact_data.csv')
        with open('contact_data.csv', 'a', newline='') as csvfile:
            fieldnames = ['name', 'email', 'message']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            if not file_exists:
                writer.writeheader()  # Write header if file doesn't exist
            writer.writerow({'name': name, 'email': email, 'message': message})

        return redirect(url_for('contact'))

    return render_template('contact.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
