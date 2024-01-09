from flask import Flask 

app=Flask(__name__)
@app.route('/')
def hello():
    return "heool ,world!This is my first Rest API."

if __name__=='__main__':
    app.run(debug=True)
