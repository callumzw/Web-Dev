import configparser, sqlite3, bcrypt
from flask import Flask, render_template, request, url_for, redirect,g
app = Flask(__name__, template_folder='template')
db_location = 'var/sqlite3.db'

def init (app):
    config = configparser.ConfigParser()
    try :
        config_location = "etc/defaults.cfg"
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
        with app.open_resource('static/sql/schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
            db.commit()

def check_user(password):
    if (valid_password == bcrypt.hashpw(password.encode('utf-8'), bcrpyt.gensalt())):
        return True
    return False
    
def requires_login(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        status = session.get('logged_in', False)
        if not status:
            return redirect(render_template('log.html'))
        return f(*args, **kwargs)
    return decorated

@app.route('/')
def mainMenu():
    return render_template('home.html')

@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html')

@app.route('/covid')
def covid():
    return render_template('covid.html')

@app.route('/news')
def news():
    return render_template('news.html')

@app.route('/topics')
def topics():
    return render_template('topics.html')

@app.route('/departments')
def departments():
    return render_template('departments.html')

@app.route('/government')
def government():
    return render_template('government.html')

@app.route('/topics/economy')
def economy():
    return render_template('economy.html')

@app.route('/topics/education')
def education():
    return render_template('education.html')

@app.route('/topics/healthcare')
def healthcare():
    return render_template('healthcare.html')

@app.route('/topics/transport')
def transport():
    return render_template('transport.html')

@app.route('/topics/justice')
def justice():
    return render_template('justice.html')

@app.route('/topics/migration')
def migration():
    return render_template('migration.html')

@app.route('/topics/environment')
def environment():
    return render_template('environment.html')

@app.route('/topics/tax')
def tax():
    return render_template('tax.html')

@app.route('/topics/work')
def work():
    return render_template('work.html')

@app.route('/news/new-measures')
def newMeasures():
    return render_template('new-measures.html')


@app.route('/news/grinch-police')
def grinchPolice():
    return render_template('grinch-police.html')

@app.route('/news/rising-sea-levels')
def risingSeaLevels():
    return render_template('rising-sea-levels.html')

@app.route('/news/importShortages')
def importShortages():
    return render_template('importShortages.html')

@app.route('/news/cop26')
def cop26():
    return render_template('cop26.html')

@app.route('/news/blitzen')
def blitzen():
    return render_template('blitzen.html')


@app.route('/private')
def private():
# check if logged in
    return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session['logged_in'] = False
    return redirect(render_template('log.html'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    db = get_db()
    if request.method == 'POST':
        user = request.form['username']
        pw = request.form['password']
        sql = ('SELECT user_password FROM usersWHERE user_name="%s"'%(user))
        db.cursor().execute(sql)
        data = db.cursor().fetchall()
        if (data == bcrypt.hashpw(pw.encode('utf-8'), bcrypt.gensalt())):
            return render_template('menu.html')
        else: 
            return ('lol not  %s'%(data))
    return render_template('log.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    db = get_db()
    if request.method == 'POST':
        user = request.form['username']
        pw = request.form['password']
        pw = bcrypt.hashpw(pw.encode('utf-8'), bcrypt.gensalt())
        try:
            db.cursor().execute('INSERT INTO users VALUES ("%s", "%s")'%(user,pw))
            db.commit()
            return render_template('menu.html')
        except:
            return ('Error occured')
    return render_template('log.html')

@app.route ('/account')
def account():
    return "Account information, would you like to change any info?"



if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
