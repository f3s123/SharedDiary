from flask import *

app = Flask(__name__)

@app.route('/')
def login():
    return render_template('login.html', methods=['POST'])

@app.route('/main', methods=['POST'])
def main():
    print(request.form.get('id'))
    print(request.form.get('pw'))
    return render_template('main.html')
    
if __name__ == '__main__':
    app.run('127.0.0.1', 5000, debug=True)