from flask import Flask, jsonify

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

engine = create_engine("sqlite:///Murder.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)

fbiData = Base.classes.fbi_db
stateData = Base.classes.state_db

session = Session(engine)
app = Flask(__name__)

@app.route('/')
def home():
    
    return f'Landing Page'

@app.route('/api/v1.0/fbidatabase')
def fbi_api():
    sel = [fbiData]
    return jsonify(fbi_api)

@app.route('/api/v1.0/statedatabase')
def state_api():
    sel = [stateData]
    state_query = session.query(*sel).all()
    state_data = []
    state_dict = dict(state_query)
    state_data.append(state_dict)
    return jsonify (state_data)

