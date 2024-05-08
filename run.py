from flask import *

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('login.html')

@app.route('/home', methods=['POST', 'GET'])
def home():
    return render_template('main.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/register_check', methods=['POST'])
def register_check():
    return render_template('login.html')

@app.route('/diary_board')
def diary_board():
    return render_template('diary_board.html')

@app.route('/calendar')
def calendar():
    return render_template('calendar.html')

@app.route('/logout')
def logout():
    return main()
    
if __name__ == '__main__':
    app.run('127.0.0.1', 5000, debug=True)