from flask import Flask, render_template, request

app=Flask(__name__)

@app.route("/")
def hello_world():
    return " This is PJ"
# if __name__ == '__main__':
#     app.run(host='0.0.0.0',port=5000)