from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index_dojo.html")

@app.route('/results', methods=['POST'])
def create():
    print(request.form)
    print('Name', request.form['name'])
    print('Dojo Location', request.form['location'])
    print('Favorite Language', request.form['language'])
    print('Comments', request.form['comments'])

    return render_template("created_dojo.html",)

@app.route('/danger')
def danger():
    print("User tried to visit /danger. we have redirected the users to /")

    return redirect('/')

if __name__=="__main__":
    # run our server
    app.run(debug=True) 