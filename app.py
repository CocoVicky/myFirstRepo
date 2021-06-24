"""
Fibonacci suite with Flask
"""

from flask import Flask

app = Flask(__name__)


def fib(count, previous_number, last_number):
    """
    Recursive function generating Fibonacci suite
    """
    return fib(count-1, last_number, previous_number+last_number) if count > 0 else previous_number


@app.route('/')
def fibonacci_suite():
    """
    Handle http requests on root
    """
    return "Fibonacci suite: "+', '.join([str(fib(x, 0, 1)) for x in range(10)])+"\n"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
