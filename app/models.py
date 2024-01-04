from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash

db = SQLAlchemy()


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)


    def __init__(self, username, password, email):
        self.username = username
        self.password = generate_password_hash(password)


    def is_active(self):
        return True

    def get_id(self):
        return self.email

    def is_authenticated(self):
        return self.authenticated
    
    
class Van(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    van_number = db.Column(db.Integer)
    milage = db.Column(db.Integer)
    last_oil_change_milage = db.Column(db.Integer)
    last_oil_change_date = db.Column(db.Date)
    last_front_tire_change_date = db.Column(db.Date)
    last_rear_tire_change_date = db.Column(db.Date)
    last_trans_fluid_change_milage = db.Column(db.Integer)
    last_battery_change_date = db.Column(db.Date)
    last_air_filter_change_milage = db.Column(db.Integer)
    last_spark_plug_change_milage = db.Column(db.Integer)
    last_coil_change_milage = db.Column(db.Integer)
    last_state_inspection_date = db.Column(db.Date)
    last_registration_renewal_date = db.Column(db.Date)
    last_front_brake_change_milage = db.Column(db.Integer)
    last_rear_brake_change_milage = db.Column(db.Integer)
    plate = db.Column(db.VARCHAR)
    vin = db.Column(db.VARCHAR)
    van_model = db.Column(db.VARCHAR)
    notes = db.Column(db.VARCHAR)
    active = db.Column(db.Boolean)


    def __init__(self, van_number, milage, last_oil_change_milage, 
                 last_oil_change_date, last_front_tire_change_date, 
                 last_rear_tire_change_date, last_trans_fluid_change_milage,
                last_battery_change_date,last_air_filter_change_milage,last_spark_plug_change_milage,
                last_coil_change_milage, last_state_inspection_date,
                last_registration_renewal_date, last_front_brake_change_milage,
                last_rear_brake_change_milage,plate,vin,van_model,notes,active):
        
        self.van_number = van_number
        self.milage = milage
        self.last_oil_change_milage = last_oil_change_milage
        self.last_oil_change_date = last_oil_change_date
        self.last_front_tire_change_date = last_front_tire_change_date
        self.last_rear_tire_change_date = last_rear_tire_change_date
        self.last_trans_fluid_change_milage = last_trans_fluid_change_milage
        self.last_battery_change_date = last_battery_change_date
        self.last_air_filter_change_milage = last_air_filter_change_milage
        self.last_spark_plug_change_milage = last_spark_plug_change_milage
        self.last_coil_change_milage = last_coil_change_milage
        self.last_state_inspection_date = last_state_inspection_date
        self.last_registration_renewal_date = last_registration_renewal_date
        self.last_front_brake_change_milage = last_front_brake_change_milage
        self.last_rear_brake_change_milage = last_rear_brake_change_milage
        self.plate = plate
        self.vin = vin
        self.van_model = van_model
        self.notes = notes
        self.active = active

    def to_dict(self):
        return {
            'database_id':self.id,
            'van_number':self.van_number,
            'milage':self.milage,     
            'last_oil_change_milage':self.last_oil_change_milage,
            'last_oil_change_date':self.last_oil_change_date.strftime('%B %d %Y'),
            'last_front_tire_change_date':self.last_front_tire_change_date.strftime('%B %d %Y'),
            'last_rear_tire_change_date':self.last_rear_tire_change_date.strftime('%B %d %Y'),
            'last_trans_fluid_change_milage':self.last_trans_fluid_change_milage,
            'last_battery_change_date':self.last_battery_change_date.strftime('%B %d %Y'),            
            'last_air_filter_change_milage':self.last_air_filter_change_milage,                            
            'last_spark_plug_change_milage':self.last_spark_plug_change_milage,                            
            'last_coil_change_milage':self.last_coil_change_milage,                      
            'last_state_inspection_date':self.last_state_inspection_date.strftime('%B %d %Y'),                         
            'last_registration_renewal_date':self.last_registration_renewal_date.strftime('%B %d %Y'),
            'last_front_brake_change_milage':self.last_front_brake_change_milage,
            'last_rear_brake_change_milage':self.last_rear_brake_change_milage,                            
            'plate':self.plate,    
            'vin':self.vin,  
            'van_model':self.van_model,        
            'notes':self.notes,    
            'active':self.active,     
        }

class Menu(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    meal = db.Column(db.VARCHAR)
    driver_add_ons = db.Column(db.VARCHAR)

    def __init__(self,meal, driver_add_ons):
        self.meal = meal,
        self.driver_add_ons = driver_add_ons


class CurrentDate(db.Model):
    id = db.Column(db.Integer, primary_key=True, unique=True)
    date = db.Column(db.VARCHAR)

    def __init__(self,date):
        self.date = date


 


    
