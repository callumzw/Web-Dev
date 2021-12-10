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

@app.route('/cookies')
def cookies():
    return render_template('cookies.html')


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

@app.route('/topics/economy/agriculture')
def agriculture():
    return render_template('agriculture.html')

@app.route('/topics/economy/fisheries')
def fisheries():
    return render_template('fisheries.html')

@app.route('/topics/economy/finance')
def finance():
    return render_template('finance.html')

@app.route('/topics/economy/livestock')
def livestock():
    return render_template('livestock.html')

@app.route('/topics/economy/tourism')
def tourism():
    return render_template('tourism.html')

@app.route('/topics/economy/protection')
def protection():
    return render_template('protection.html')

@app.route('/topics/education/terms')
def terms():
    return render_template('terms.html')

@app.route('/topics/education/holdiays')
def holidays():
    return render_template('holidays.html')

@app.route('/topics/education/admissions')
def admissions():
    return render_template('admissions.html')

@app.route('/topics/education/curriculum')
def curriculum():
    return render_template('curriculum.html')

@app.route('/topics/education/disabilitySupport')
def disabilitySupport():
    return render_template('disabilitySupport.html')

@app.route('/topics/education/primary')
def primary():
    return render_template('primary.html')

@app.route('/topics/education/secondary')
def secondary():
    return render_template('secondary.html')

@app.route('/topics/education/apprenticeships')
def apprenticeships():
    return render_template('apprentieships.html')

@app.route('/topics/healthcare/insurance')
def insurance():
    return render_template('insurance.html')

@app.route('/topics/healthcare/mentalHealth')
def mentalHealth():
    return render_template('mentalHealth.html')

@app.route('/topics/healthcare/prescriptions')
def prescriptions():
    return render_template('prescriptions.html')

@app.route('/topics/healthcare/drugAwareness')
def drugAwareness():
    return render_template('drugAwareness.html')

@app.route('/topics/healthcare/childcare')
def childcare():
    return render_template('childcare.html')

@app.route('/topics/healthcare/vaccination')
def vaccination():
    return render_template('vaccination.html')

@app.route('/topics/healthcare/food')
def food():
    return render_template('food.html')

@app.route('/topics/healthcare/exercise')
def exercise():
    return render_template('exercise.html')

@app.route('/topics/transport/railway')
def railway():
    return render_template('railway.html')

@app.route('/topics/transport/license')
def license():
    return render_template('license.html')

@app.route('/topics/transport/roads')
def roads():
    return render_template('roads.html')

@app.route('/topics/transport/ecoFriendly')
def ecoFriendly():
    return render_template('ecoFriendly.html')

@app.route('/topics/transport/boating')
def boating():
    return render_template('boating.html')

@app.route('/topics/transport/aviation')
def aviation():
    return render_template('aviation.html')

@app.route('/topics/justice/security')
def security():
    return render_template('security.html')

@app.route('/topics/justice/courts')
def courts():
    return render_template('courts.html')

@app.route('/topics/justice/police')
def police():
    return render_template('police.html')

@app.route('/topics/justice/discrimination')
def discrimination():
    return render_template('discrimination.html')

@app.route('/topics/justice/violentCrimes')
def violentCrimes():
    return render_template('violentCrimes.html')

@app.route('/topics/migration/visas')
def visas():
    return render_template('visas.html')

@app.route('/topics/migration/embassies')
def embassies():
    return render_template('embassies.html')

@app.route('/topics/migration/immigration')
def immigration():
    return render_template('immigration.html')

@app.route('/topics/migration/asylum')
def asylum():
    return render_template('asylum.html')

@app.route('/topics/migration/citizenship')
def citizenship():
    return render_template('citizenship.html')

@app.route('/topics/environment/climate')
def climate():
    return render_template('climate.html')

@app.route('/topics/environment/fauna')
def fauna():
    return render_template('fauna.html')

@app.route('/topics/environment/flora')
def flora():
    return render_template('flora.html')

@app.route('/topics/environment/habitat')
def habitat():
    return render_template('habitat.html')

@app.route('/topics/environment/waterManagement')
def waterManagement():
    return render_template('waterManagement.html')

@app.route('/topics/tax/businesses')
def businesses():
    return render_template('businesses.html')

@app.route('/topics/tax/socialPolicy')
def socialPolicy():
    return render_template('socialPolicy.html')

@app.route('/topics/tax/grants')
def grants():
    return render_template('grants.html')

@app.route('/topics/tax/childbenefits')
def childBenefits():
    return render_template('childBenefits.html')

@app.route('/topics/tax/incomeTax')
def incomeTax():
    return render_template('incomeTax.html')

@app.route('/topics/tax/vat')
def vat():
    return render_template('vat.html')

@app.route('/topics/work/minimumWage')
def minimumWage():
    return render_template('minimumWage.html')

@app.route('/topics/work/healthSafety')
def healthSafety():
    return render_template('healthSafety.html')

@app.route('/topics/work/workHours')
def workHours():
    return render_template('workHours.html')

@app.route('/topics/work/unemployment')
def unemployment():
    return render_template('unemployment.html')

@app.route('/topics/work/pension')
def pension():
    return render_template('pension.html')

@app.route('/topics/work/workLeave')
def workLeave():
    return render_template('workLeave.html')

@app.route('/topics/departments/cabinet')
def cabinet():
    return render_template('cabinet.html')

@app.route('/topics/departments/genralAffairs')
def generalAffairs():
    return render_template('generalAffairs.html')

@app.route('/topics/departments/economicAffairs')
def economicAffairs():
    return render_template('economicAffairs.html')

@app.route('/topics/departments/educationCulture')
def educationCulture():
    return render_template('educationCulture.html')

@app.route('/topics/departments/healthWelfare')
def healthWelfare():
    return render_template('healthWelfare.html')

@app.route('/topics/departments/infrastructure')
def infrastructure():
    return render_template('infrastructure.html')

@app.route('/topics/departments/justiceSecurity')
def justiceSecurity():
    return render_template('justiceSecurity.html')

@app.route('/topics/departments/foreignAffairs')
def foreignAffairs():
    return render_template('foreignAffairs.html')

@app.route('/topics/departments/nature')
def nature():
    return render_template('nature.html')

@app.route('/topics/departments/socialAffairs')
def socialAffairs():
    return render_template('socialAffairs.html')

@app.route('/topics/departments/workPensions')
def workPensions():
    return render_template('workPensions.html')

@app.route('/topics/departments/defense')
def defense():
    return render_template('defense.html')

@app.route('/topics/departments/financeDepartment')
def financeDepartment():
    return render_template('financeDepartment.html')





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
