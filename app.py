from flask import Flask, jsonify, render_template


import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

engine = create_engine("sqlite:///Murder.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)

# fbiData = Base.classes.fbi_db
stateData = Base.classes.state_db

session = Session(engine)

app = Flask(__name__)

@app.route('/')
def home():
    
    return render_template('index.html')
    
@app.route('/datacleaning')
def data_cleaning():
    return render_template('data_cleaning.html')

@app.route('/dataanalysis')
def data_analysis():
    return render_template('messing_with_data.html')

@app.route('/api/v1.0/statedatabase')
def state_api():
    sel = [stateData]
    state_query = session.query(*sel).all()
    state_data = []
    state_dict = dict(state_query)
    state_data.append(state_dict)
    return jsonify (state_data)

# @app.route('/api/v1.0/fbidatabase')
# def fbi_api():
#     sel = [fbiData]
#     return jsonify(fbi_api)

if __name__ == "__main__":
    app.run(debug=True)