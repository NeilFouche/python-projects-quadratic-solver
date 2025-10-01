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

@app.route('/', methods=['GET', 'POST'])  # type: ignore
def index():
    result = None
    plot_url = None

    if request.method == "POST":
        try:
            a = float(request.form['a'])
            b = float(request.form['b'])
            c = float(request.form['c'])

            result = "No real roots (complex roots)."

            discriminant = b ** 2 - 4*a*c

            # If real roots exist, compute them and update the result
            if discriminant >= 0:
                discriminant_rt = sqrt(discriminant)
                roots = [
                    f"{(-b + discriminant_rt) / (2*a):.2f}",
                    f"{(-b - discriminant_rt) / (2*a):.2f}"
                ]
                result = f"The roots are {' and '.join(roots)}"

                # Generate plot
                turning_point = -b / (2*a)
                lower, upper = turning_point - 5, turning_point + 5
                samples = 100
                step = (upper - lower) / (samples - 1)
                domain = [lower + n*step for n in range(samples)]
                y = [a*(x**2) + b*x + c for x in domain]

                plt.figure(figsize=(12,4))
                plt.plot(domain, y, label=f"{a}x² + {b}x + {c}")
                plt.axhline(0, color='black', linewidth=0.5)
                plt.axvline(0, color='black', linewidth=0.5)
                plt.xlabel("x")
                plt.ylabel("f(x)")
                plt.title("Quadratic plot")
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

    return render_template('index.html', result=result, plot_url=plot_url)

if __name__ == '__main__':
    app.run(debug=True)