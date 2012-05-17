# -*- coding: utf-8 -*-

import os
from sqlite3 import dbapi2 as sqlite3
from contextlib import closing
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash


BASE_DIR = os.path.abspath( os.path.dirname( __file__ ) )
DATABASE = os.path.join( BASE_DIR, "baconipsum.sqlite3" )
DEBUG = True


app = Flask( __name__ )
app.config.from_object( __name__ )


if app.config[ "DEBUG" ]:
    from werkzeug import SharedDataMiddleware
    app.wsgi_app = SharedDataMiddleware( app.wsgi_app, {
        "/": os.path.join( os.path.dirname( __file__ ), 'static' )
    })


@app.route( "/" )
def home():
    return render_template( "home.html" )


@app.route( "/about" )
def about():
    return render_template( "about.html" )


@app.route( "/api" )
def api():
    return render_template( "api.html" )


@app.errorhandler( 404 )
def page_not_found( e ):
    return render_template( "404.html" ), 404


if __name__ == "__main__":
    app.run()
