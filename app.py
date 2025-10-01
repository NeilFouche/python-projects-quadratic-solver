"""
Quadratic Solver
by Neil Fouche

Hosted on: render.com
Address: https://quadratic-solver-vmky.onrender.com
"""

from flask import Flask, render_template, request
from math import sqrt
import matplotlib.pyplot as plt
import io
import base64

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    plot_url = None
    a_input = ''
    b_input = ''
    c_input = ''

    if request.method == "POST":
        a_input = request.form['a']
        b_input = request.form['b']
        c_input = request.form['c']

        try:
            inputs = [
              float(a_input),
              float(b_input),
              float(c_input)
            ]
            a, b, c = inputs

            result = "No real roots (complex roots)."

            discriminant = b ** 2 - 4*a*c

            # If real roots exist, compute them and update the result
            if discriminant >= 0:
                discriminant_rt = sqrt(discriminant)
                root1 = (-b + discriminant_rt) / (2*a)
                root2 = (-b - discriminant_rt) / (2*a)
                nroots = sorted([root1, root2])
                roots = [f"{root:.2f}" for root in nroots]
                result = f"The roots are {' and '.join(sorted(roots))}"

                # Generate plot
                turning_point = -b / (2*a)
                lower, upper = turning_point - max(abs(nroots[0]), 5), turning_point + max(nroots[1], 5)
                samples = 100
                step = (upper - lower) / (samples - 1)
                domain = [lower + n*step for n in range(samples)]
                y = [a*(x**2) + b*x + c for x in domain]

                # Construct equation according mathematical conventions
                coefficients = [str(abs(input)) if input != 1 or i == 2 else '' for i, input in enumerate(inputs)] # drop coefficients = 1 unless constant
                variables = ['x²', 'x', '']
                signs = ['+' if coeff > 0 else '-' for coeff in inputs]
                terms = [
                    f"{signs[i]} {coefficients[i]}{variables[i]}"
                    for i in range(len(inputs)) if inputs[i] != 0   # drop terms where coefficient = 0
                ]
                equation = ' '.join(terms).strip('+')

                plt.figure(figsize=(12,4))
                plt.scatter(nroots, [0, 0], color='#1C649A', s=50, label='Roots', zorder=5)
                plt.plot(domain, y)
                plt.axhline(0, color='black', linewidth=0.5)
                plt.axvline(0, color='black', linewidth=0.5)
                plt.title(f"Graph of {equation}")
                plt.xlabel("x")
                plt.ylabel("f(x)")
                plt.grid(True)
                plt.legend()

                # Save plot to base64
                buf = io.BytesIO()
                plt.savefig(buf, format='png')
                buf.seek(0)
                plot_url = base64.b64encode(buf.getvalue()).decode('utf-8')
                plt.close()

        except ValueError:
            result = "Error: Please enter valid numbers for a, b, c."
    else:
        result = None

    return render_template('index.html', result=result, plot_url=plot_url, a_input=a_input, b_input=b_input, c_input=c_input)

if __name__ == '__main__':
    app.run(debug=True)