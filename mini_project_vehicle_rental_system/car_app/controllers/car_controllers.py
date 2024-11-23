from flask import jsonify , request 
from services.car_services import CarService

def to_dict(obj):
    return {column.name : getattr(obj , column.name) for column in obj.__table__.columns}



class CarController :

    def __init__(self):
        self.service = CarService()
    
    def get_car(self , car_id):
        car = self.service.get_car(car_id)
        return jsonify (to_dict(car)) if car else jsonify ({"error" : "Car not found"})
    

    def create_car(self , car_data):
        car = self.service.create_car(car_data)
        return jsonify(to_dict(car))
    

    def update_car(self , car_id):
        car_data = request.json
        updated_car = self.update_car(car_id , car_data)
        return jsonify(to_dict(updated_car)) if updated_car else jsonify ({"error" : "Car not found"})
    

    def delete_car(self , car_id):
        deleted_car = self.service.delete_car(car_id)
        return jsonify ({"message" : "Car deleted"}) if deleted_car else ({"error" : "Car not found"})
    
