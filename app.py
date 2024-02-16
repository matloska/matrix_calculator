from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/", methods=['POST','GET'])
def matrices():
    """Renders a page on which we could add matrices"""
    
    rows_a = int(request.args.get('rows_a','3'))
    cols_a = int(request.args.get('cols_a','3'))
    rows_b = int(request.args.get('rows_b','3'))
    cols_b = int(request.args.get('cols_b','3'))

    if request.method == "POST":
        print(request.form)
        return redirect("/?rows_a="+str(request.form['rows_a']) \
                        +"&cols_a="+str(request.form['cols_a']) \
                        +"&rows_b="+str(request.form['rows_b']) \
                        +"&cols_b="+str(request.form['cols_b'])
                            )
    return render_template('matrices.html', 
                           rows_a=rows_a, cols_a=cols_a,
                           rows_b=rows_b, cols_b=cols_b)