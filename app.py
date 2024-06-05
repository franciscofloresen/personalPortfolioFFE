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

@app.route('/snakeDesc.html')
def snakeInC():
    return render_template('snakeDesc.html')

@app.route('/webPageDesc.html')
def webPage():
    return render_template('webPageDesc.html')

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
            csvfile.flush()  # Ensure data is written to disk

        return redirect(url_for('contact'))

    return render_template('contact.html')

@app.route('/view-contacts')
def view_contacts():
    try:
        with open('contact_data.csv', 'r') as csvfile:
            content = csvfile.read()
        return f"<pre>{content}</pre>"
    except Exception as e:
        return str(e)

# Custom error handlers
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
