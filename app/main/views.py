from flask import render_template,url_for,request,flash,redirect,abort
from app.main  import main
from app.models import User
from .. import db, photos

from flask_login import login_required,current_user
import secrets
import os


@main.route('/')
def index():
  

    return render_template('index.html')
