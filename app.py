from flask import Flask, request, render_template, redirect, url_for
import csv

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('init.html')

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

        # Guardar los datos en un archivo CSV
        with open('contact_data.csv', 'a', newline='') as csvfile:
            fieldnames = ['name', 'email', 'message']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writerow({'name': name, 'email': email, 'message': message})

        return redirect(url_for('contact'))

    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
