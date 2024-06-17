from flask import Flask, render_template, jsonify

app = Flask(__name__)

click_count = 0

@app.route('/')
def index():
    return 'Welcome to the Telegram WebApp Clicker!'

@app.route('/clicker')
def clicker():
    return render_template('clicker.html')

@app.route('/api/click', methods=['POST'])
def click():
    global click_count
    click_count += 1
    return jsonify({'click_count': click_count})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
