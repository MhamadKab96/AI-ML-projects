from flask import Flask, request, jsonify, render_template, make_response
from function import myClass

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_input', methods=['POST'])
def process_input():
    user_input = request.form.get('input')
    output = myClass.enter_prompt(user_input) 
    response = make_response(output)
    response.headers['Content-Type'] = 'text/plain'
    return response

if __name__ == '__main__':
    app.run(debug=True)
