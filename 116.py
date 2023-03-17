from flask import Flask,render_template
app = Flask(__name__)
@app.route('/')
def hello():
    return 'u are ugly'

@app.route('/hello')
def bye():
    name ='flask'
    return render_template('index.html',index_variable =  name)










app.run(debug = True)