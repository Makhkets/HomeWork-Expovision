from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/signup")
def render():
    return render_template("index.html")

@app.route("/users", methods=["POST"])
def auth():

    email = request.form.get("email")
    username = request.form.get("username")
    password = request.form.get("password")
    confrim_password = request.form.get("confrim_password")

    if len(username) >= 6:
        if str(password) == str(confrim_password):
            return f"<h1>SUCCESS</h1>Email: {email}<br>Username: {username}<br>Password: {password}"

    return f"<h1>Error</h1><h2>Username должен быть менее 6 символов<br>Пароли должны совпадать!</h2><br>Email: {email}<br>Username: {username}<br>Password: {password}"