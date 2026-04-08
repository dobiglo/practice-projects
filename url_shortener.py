from flask import Flask, redirect, request
import random
import string

app=Flask(__name__)
url={}

def generate_code(length=5):
    return "".join(random.choices(string.ascii_letters+string.digits, k=length))

@app.route("/",methods=["GET"])
def home():
    return """
    <h2>URL Shortener<h2>
    <form action="/shorten" method="post">
        Long URL: <input name="url">
        <input type="submit">
    """

@app.route("/shorten",methods=["POST"])
def shorten():
    long_url=request.form["url"]
    code=generate_code()
    url[code]=long_url
    return f'Short URL: <a href="/{code}">https://127.0.0.1:5000/{code}</a>'

@app.route('/<code>')
def redirect_to_url(code):
    if code in url:
        return redirect(url[code])
    
    return"URL not found",404

if __name__=="__main__":
    app.run(debug=True)