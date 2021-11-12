from flask import Flask
app = Flask(__name__)

@app.route('/')
def mainMenu():
    return 'Hello Napier'

@app.errorhandler(404)
def page_not_found(error):
    return "Couldnt find the page you have requested", 4040

@app.route('/private')
def private()
# check if logged in
return redirect(url_for('login'))

@app.route('/login')
def login ():
    return "Fill in username & password"

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
