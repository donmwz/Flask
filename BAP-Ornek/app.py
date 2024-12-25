from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'],)
def KayıtOl():
    if request.method == 'POST':
        #name = request.form['name']
        #surname = request.form['surname']
        email = request.form['email']
        password = request.form['password']
        #password_again = request.form['password_again']
        render_template("welcome.html", email=email, password=password)
    return render_template("kayit.html")

@app.route('/giris', methods=['GET', 'POST'])
def giris():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        return redirect(url_for('welcome'))
    return render_template('giris.html')

@app.route('/welcome', methods=['GET', 'POST'])
def welcome():
    return render_template("welcome.html")


if __name__ == '__main__':
    app.run(debug=True)
