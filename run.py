from flask import *
import sqlite3

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

@app.route('/diary_board', methods=["GET", "POST"])
def diary_board():
    conn = sqlite3.connect('database.db')
    cur = conn.cursor()
    if request.args.get("title"):
        print(request.args.get("title"))
        print(request.args.get("content"))
        # cur.execute("INSERT VALUE INTO diary ()")
    diary = cur.fetchall()
    print(diary)
    return render_template('diary_board.html', diary=diary)

@app.route('/diary_write')
def diary_write():
    return render_template('diary_write.html')

@app.route('/calendar')
def calendar():
    return render_template('calendar.html')

@app.route('/logout')
def logout():
    return main()
    
if __name__ == '__main__':
    app.run('127.0.0.1', 5000, debug=True)