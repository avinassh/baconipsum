# -*- coding: utf-8 -*-

import os
import json
from sqlite3 import dbapi2 as sqlite3
from contextlib import closing
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash


BASE_DIR = os.path.abspath( os.path.dirname( __file__ ) )
DATABASE = os.path.join( BASE_DIR, "baconipsum.sqlite3" )
DEBUG = True


app = Flask( __name__ )
app.config.from_object( __name__ )


def connect_db():
    """Returns a new connection to the database."""
    return sqlite3.connect( app.config[ "DATABASE" ] )


def init_db():
    """Creates the database tables."""
    with closing( connect_db() ) as db:
        with app.open_resource( "schema.sql" ) as f:
            db.cursor().executescript( f.read() )
        db.commit()


@app.before_request
def before_request():
    """Make sure we are connected to the database each request."""
    g.db = connect_db()


@app.teardown_request
def teardown_request( exception ):
    """Closes the database again at the end of the request."""
    if hasattr( g, "db" ):
        g.db.close()


@app.route( "/" )
def home():
    return render_template( "home.html" )


@app.route( "/about" )
def about():
    return render_template( "about.html" )


@app.route( "/api" )
def api():
    return render_template( "api.html" )


if __name__ == "__main__":
    app.run()
