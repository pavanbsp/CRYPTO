from flask import Flask, render_template, request
from basic_fact import factorize
from pollard_rho import factors
import time

app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
def welcome():
    return render_template('form.html')


@app.route('/', methods=['POST'])
def result():
    start = current_milli_time()
    var_1 = request.form.get("var_1", type=int)

    if request.form['submit_button'] == 'Normal(slow)':
        d = factorize(var_1)
    else:
        d = factors(var_1)
    a = list(d.values())
    no_of_divisors = 1
    sum_of_divisors = 1 

    if var_1 == 1:
        entry = "1 is neither prime nor composite"
        end = current_milli_time()
        return render_template('form.html', inp=var_1, entry=entry, entry1=entry, d1=1, d2=1, t=time_instring(end-start))
    if len(a) == 1 and a[0] == 1:
        entry = str(var_1) + " is a prime number"
        end = current_milli_time()
        return render_template('form.html', inp=var_1, entry=entry, entry1=entry, d1=2, d2=var_1+1, t=time_instring(end-start))

    res = " "
    res2 = " "
    for i in d:
        res2 += str(i)+superscript(d[i]) + "  x  "
        no_of_divisors *= (d[i]+1)
        temp = 0
        for j in range(d[i]):
            temp += pow(i, j+1)
            res += str(i)
            res += " x "
        sum_of_divisors *= (temp+1)
    entry = res[:len(res) - 2]
    entry1 = res2[:len(res2) - 4]

    end = current_milli_time()
    return render_template('form.html', inp=var_1, entry=entry, entry1=entry1, d1=no_of_divisors, d2=sum_of_divisors, t=time_instring(end-start))

def time_instring(t):
    if t<1000:
        return "Completed in "+str(t)+" ms"
    else:
        return "Completed in "+str(round(t/1000,5))+" secs"

def superscript(n):
    return "".join(["⁰¹²³⁴⁵⁶⁷⁸⁹"[ord(c)-ord('0')] for c in str(n)])

def current_milli_time():
    return round(time.time() * 1000)

if __name__ == '__main__':
    app.run(debug=True)
