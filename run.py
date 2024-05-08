from flask import *

app = Flask(__name__)

@app.route('/')
def login_page():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    return render_template('main.html')

@app.route('/register')
def register():
    return render_template('login.html')

@app.route('/diary_board')
def diary_board():
    return render_template('diary_board.html')

@app.route('/logout')
def logout():
    return login_page()
    
if __name__ == '__main__':
    app.run('127.0.0.1', 5000, debug=True)