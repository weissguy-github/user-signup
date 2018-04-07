from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

@app.route("/check", methods=['POST'])
def check():

    uname = request.form['username']
    if (len(uname) < 3 or 
        len(uname) > 20 or
        uname.find(' ') >= 0):
        uname_error = 'Username must be 3-20 characters with no <space> character'
        uname=''
    else:
        uname_error = ''

    password = request.form['password']
    if (len(password) < 3 or 
        len(password) > 20 or
        password.find(' ') >= 0):
        pwd_error = 'Password must be 3-20 characters with no <space> character'
    else:
        pwd_error = ''

    verify = request.form['verify']
    if password != verify:
        vp_error = 'Passwords do not match'
        password = ''
        verify = ''
    else:
        vp_error = ''

    email = request.form['email']
    email_error = ''
    if len(email) > 0:     # If email entered, verify it is valid
        if (len(email) < 3 or 
            len(email) > 20 or
            email.find(' ') >= 0 or
            email.count('@') != 1 or
            email.count('.') != 1):
            email_error = 'Email must be 3-20 characters with no <space> and one "@" and one "."'
            email = ''


#   If all checks ok, then display Welcome page.
    if (uname_error + pwd_error + vp_error + email_error) == '':
        return redirect('/welcome?uname={0}'.format(uname))
    else:
        return render_template('signup.html', 
            uname=uname,        uname_error=uname_error,
            password=password,  pwd_error=pwd_error,
            verify=verify,      vp_error=vp_error,
            email=email,        email_error=email_error)

@app.route("/welcome")
def welcome():
    uname = request.args.get('uname')
    return render_template('welcome.html', uname=uname)

@app.route("/")
def index():
    encoded_error = request.args.get("error")
    return render_template('signup.html')

app.run()