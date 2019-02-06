import datetime
import os
import sys

from flask import Flask, redirect, url_for, request, jsonify, make_response

from models import Medallions
from database import db_session

from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from flask_caching import Cache

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = os.environ['APP_SECRET_KEY']
cache = Cache(app, config={'CACHE_TYPE': 'simple'})


@app.route('/medallion', methods=['POST'])
@cache.cached(timeout=50)
def medallionquery():

	data = request.get_json()
	pickup_date = datetime.datetime.strptime(data['pickup_date'], '%Y-%m-%d').date() # yyyy-mm-dd
	medal_req = data['medallions'] # comma separated string
	medal_req = [x.strip() for x in medal_req.split(',')] # strip whitespace and turn medallions to a list

	medallions = Medallions.query.all()
	
	output = {}
	for m in medallions:
		medallion = {}
		medallion['medalallion'] = m.medallion
		medallion['pickup_date'] = m.pickup_datetime.date()
		if medallion['pickup_date'] == pickup_date and medallion['medalallion'] in medal_req: # if medal and date match
			# then add to or append to result list
			if medallion['medalallion'] not in output:
				output[medallion['medalallion']] = 1
			else:
				output[medallion['medalallion']] += 1
	
	output['response'] = 200
	return jsonify(output)

@app.route('/clearcache')
def clearcache():
	with app.app_context():
		cache.clear()
		
	return jsonify({'result' : "success, cache is cleared", "response": 200})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5090, debug=True)
