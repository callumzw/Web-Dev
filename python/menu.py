import configparser, sqlite3
from flask import Flask, render_template, request, url_for, redirect,g
app = Flask(__name__)
db_location = 'var/sqlite3.db'

def init (app):
    config = configparser.ConfigParser()
    try :
        config_location = "etc/test.cfg"
        config.read(config_location)

        app.config ['DEBUG'] = config.get ("config", "debug")
        app.config ['ip_address'] = config.get ("config", "ip_address")
        app.config ['port'] = config.get ("config", "port")
        app.config ["url"] = config.get ("config", "url")
    except:
        print (" Couldn’t read configs from : ", config_location )

init(app)

def get_db():
    db = getattr(g, 'db', None)
    if db is None:
        db = sqlite3.connect(db_location)
        g.db = db
        return db

@app.teardown_appcontext
def close_db_connection(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
            db.commit()

@app.route('/')
def mainMenu():
    return render_template('menu.html')

@app.errorhandler(404)
def page_not_found(error):
    return "Couldnt find the page you have requested", 4040

@app.route('/private')
def private():
# check if logged in
    return redirect(url_for('login'))

@app.route('/login')
def login():
    db = get_db()
    page = []
    sql = "SELECT * FROM users WHERE user_name=user"
    for row in db.cursor().execute(sql):
        page.append(str(row))
    if (page == bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            return True
        return False
    return "Fill in username & password"

@app.route('/register')
def register():
    db = get_db()
    db.cursor().execute('insert into users values ("username", "password")')
    db.commit()
    return "Create a username and password"

@app.route ('/account')
def account():
    return "Account information, would you like to change any info?"

@app.route ('/acccount/edit')
def edit():
    return "    Edit password   |   Edit Character"

@app.route ('/about')
def about():
    return "This game was developd by C Grant, Click here to learn about the Story @ /n     Click here to learn how to play @"

@app.route ('/about/story')
def story():
    return "Your a ravvller in he Appalachain Mountains searhcing for a new life"

@app.route ('/about/gameplay')
def gameplay():
    return "This ia your standard point-and-click adventure game"

@app.route ('/play')
def play():
    return "Press Play"

@app.route ('/play/game')
def game():
    return "        Welcome tothe Appalachian Trails!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
