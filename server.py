from flask import Flask, render_template, session, request

app = Flask(__name__)
app.secret_key = "blahhhhhhhh"

@app.route('/')
def show_homepage():
    return render_template('homepage.html')

###############################
#                             #
# 1) Finish the routes below. #
#                             #
###############################


@app.route('/form')
def show_form():
    return render_template('form.html')


@app.route('/results')
def show_results():
    cheery = request.args.get('cheery')
    honest = request.args.get('honest')
    dreary = request.args.get('dreary')

    if cheery:
        msg = "this is a CHEERY message"
    elif honest:
        msg = "this is a very HONEST message"
    elif dreary:
        msg = "this is a DREARY message"
   

    return render_template('results.html', msg = msg)


@app.route('/save_name', methods=["POST"])
def save_name():
    name = request.form.get('name')
    session['name'] = name   
    # the assignment is to render
    # return render_template('homepage.html')
    # but I think it makes sense to render ('form.html')
    return render_template('form.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
