from flask import Flask
app = Flask(_name_)

@app.route('/hello')
def helloIndex():
    return'Hello world from python from Flask!'
app.run(host='0.0.0',port='5000')
