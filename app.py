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

        # Debug prints
        print(f"Received data - Name: {name}, Email: {email}, Message: {message}")

        try:
            # Guardar los datos en un archivo CSV en el directorio raíz
            file_exists = os.path.isfile('contact_data.csv')
            with open('contact_data.csv', 'a', newline='') as csvfile:
                fieldnames = ['name', 'email', 'message']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                if not file_exists:
                    writer.writeheader()  # Escribir el encabezado si el archivo no existe
                writer.writerow({'name': name, 'email': email, 'message': message})
            print("Data written to CSV successfully.")
        except Exception as e:
            print(f"Error writing to CSV: {e}")

        return redirect(url_for('contact'))

    return render_template('contact.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
