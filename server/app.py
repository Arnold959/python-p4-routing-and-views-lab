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

@app.route('/count/<int:i>')
def count(i):
    response = ""
    for num in range(i + 1):
        response += str(num) + "\n"
    return response


        
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
