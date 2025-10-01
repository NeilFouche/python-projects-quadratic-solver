from flask import Flask, render_template, request
from math import sqrt

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])  # type: ignore
def index():
    if request.method == "POST":
        try:
            a = float(request.form['a'])
            b = float(request.form['b'])
            c = float(request.form['c'])

            result = "No real roots (complex roots)."

            discriminant = b ** 2 - 4*a*c
            discriminant_rt = sqrt(discriminant)

            # If real roots exist, compute them and update the result
            if discriminant >= 0:
                roots = [
                    f"{(b + discriminant_rt) / (2*a):.2f}",
                    f"{(b - discriminant_rt) / (2*a):.2f}"
                ]
                result = f"The roots are {' and '.join(roots)}"
        except ValueError:
            result = "Error: Please enter valid numbers for a, b, c."
    else:
        result = None

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)