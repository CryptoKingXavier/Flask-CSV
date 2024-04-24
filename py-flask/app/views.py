# Import required libraries
from app.utils import *
from typing import Literal, Mapping, Union
from flask import Blueprint, render_template, redirect, url_for, request, Response


# Blueprint Object
views: Blueprint = Blueprint('views', __name__)


# Creating URLConf
@views.get("/")
def index() -> tuple[str, Literal[200]]: 
    return render_template("index.html", title="Home Page")


@views.get("/login")
def login() -> tuple[str, Literal[200]]:
    return render_template("data.html", data=import_data(), title="User Info ℹ️")


@views.post("/signup")
def signup() -> Response:    
    data: Mapping[str, Union[str, int]] = dict(
        zip(
            model,
            [
                request.form.get("name"), 
                int(request.form.get("age")), 
                request.form.get("reg_no"), 
                request.form.get("email"), 
                request.form.get("password")
            ]
        )
    )
    
    export_data(data)
    return redirect(url_for('views.login'))
    
