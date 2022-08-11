#!/usr/bin/env python3

from ast import expr_context
from flask import Flask
from flask import request
import requests
import base64

app = Flask(__name__)

session = requests.Session()

@app.route("/upload", methods=['GET', 'POST'])
def upload():
    if request.method == 'POST' :
        filename = request.form.get("filename")
        content = request.form.get("content")
        print(request.get_data())
    else:
        print(request.get_data())
        return '''<form method = "post">
                <p>Enter filename:</p>
                <p><input type = "text" name = "filename" /></p>
                <p>Enter Website:</p>
                <p><textarea type="text" name="content" rows="1" cols="100"></textarea></p>
                <p><input type = "submit" value = "submit" /></p>
                </form>'''
    
    
    # print(f"{filename=}\n{content=}")
    response = upload_image(filename, content)
    if response is True:
        return "<h1>Thanks for the file!</h1>"
    else:
        return response
    
    
@app.route("/another_upload", methods=['GET', 'POST'])
def another_upload_file():
    if request.method == 'POST' :
        filename = request.form.get("filename")
        content = request.form.get("content")
        print(request.get_data())
    else:
        print(request.get_data())
        return '''<form method = "post">
                <p>Enter filename:</p>
                <p><input type = "text" name = "filename" /></p>
                <p>Enter Website:</p>
                <p><textarea type="text" name="content" rows="1" cols="100"></textarea></p>
                <p><input type = "submit" value = "submit" /></p>
                </form>'''
    
    
    # print(f"{filename=}\n{content=}")
    response = upload_image(filename, content)
    if response is True:
        return "<h1>Thanks for the file!</h1>"
    else:
        return response
    

@app.route("/upload_image", methods=['GET', 'POST'])
def upload_image(filename, content):
    try:
        print(request.get_data())
        decoded_content = base64.b64decode(content)
        print(decoded_content)
        with open(f"./files/{filename}", "wb") as h:
            h.write(decoded_content)
        return True
    except Exception as e:
        return "Could not upload", e


def another_upload(filename, content):
    try:
        with open(f"./files/{filename}", "w") as h:
            h.write(content)
            return True
    except Exception as e:
        return "Could not upload", e

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
