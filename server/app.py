#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<string:hello>')
def print_string (hello):
    print (hello)
    return hello

@app.route('/count/<int:parameter>')
def count(parameter):
    count = ''
    for num in range(parameter + 1):
        count += str(num) + '\n'
    return count

        
@app.route ('/math/<num1><operation><num2>')
def math (operation,num1, num2):
    if operation == '+':
        return (num1 + num2)
    elif operation == '-':
        return (num1 - num2)
    elif operation == '*':
        return (num1 * num2)
    elif operation == '%':
        return (num1 % num2)
    

if __name__ == '__main__':
    app.run(port=5555, debug=True)
