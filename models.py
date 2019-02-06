from database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, Float
from sqlalchemy.types import DateTime



from flask import Flask, request, jsonify, make_response

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
db = SQLAlchemy(app)

class Medallions(Base):
	__tablename__ = 'medallions'
	
	id = Column(Integer, primary_key=True)
	medallion = Column(String(50))
	hack_license = Column(String(20))
	vendor_id = Column(String(20))
	rate_code = Column(String(20))
	store_and_fwd_flag = Column(String(20)) 
	pickup_datetime = Column(DateTime)
	dropoff_datetime = Column(DateTime)
	passenger_count = Column(Integer)
	trip_time_in_secs = Column(Integer)
	trip_distance = Column(Float)

