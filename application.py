from flask import Flask, render_template, flash, request, send_file, send_from_directory
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from driver import MainDriver
from docx import Document
from io import StringIO
import os

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

 
class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])
 
 
@app.route("/main/<topics>", methods=['GET', 'POST'])
def hello(topics):
    form = ReusableForm(request.form)
    cur_class = MainDriver()
    res = cur_class.article_maker(topics)
    # print(res)
    return send_from_directory(directory = os.getcwd(), filename=res)

@app.route("/")
def world():
	return "Hello WOrld"
 
if __name__ == "__main__":
    app.run()