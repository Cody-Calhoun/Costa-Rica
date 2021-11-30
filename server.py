from flask import Flask, render_template, request, redirect
import model

app = Flask(__name__) 

# Add routes here
@app.route('/success')
def success():
    print(model.hello())
    return "success"

@app.route('/hello/<string:name>/<int:num>')
def name(name, num):
    return f"Hello {name.capitalize()}, I hear your favorite number is {num}"

@app.route('/')
def dashboard():
    return render_template('index.html')

@app.route('/form', methods=['POST'])
def form():
    value = model.house_details(request.form['bedroom'], request.form['bathroom'], request.form['sqft'])
    print(value)
    house = {
        'bedroom': request.form['bedroom'],
        'bathroom': request.form['bathroom'],
        'sqft': request.form['sqft']
    }
    return render_template('success.html', user_house=house, secret_message = value)


if __name__=="__main__":
    app.run(debug=True)