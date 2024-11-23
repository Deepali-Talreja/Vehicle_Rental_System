from flask import jsonify , request

from services.driver_services import DriverService

def to_dict(obj):
    return {column.name : getattr(obj , column.name) for column in obj.__table__.columns}


class DriverController :
    def __init__(self):
        self.service = DriverService()

    # DRIVER 

    def create_driver(self , driver_data):
        driver = self.service.create_driver(driver_data)

    
    def get_driver(self , driver_id):
        driver = self.service.get_driver(driver_id)
        return jsonify(to_dict(driver)) if driver else jsonify ({"error" : "Driver not found"})
    
    
    def update_driver(self , driver_id):
        driver_data = request.json
        updated_driver= self.update_driver(driver_id , driver_data)
        return jsonify(to_dict(updated_driver)) if updated_driver else jsonify ({"error" : "Driver not found"})
    

    def delete_driver(self , driver_id):
        deleted_driver = self.service.delete_driver(driver_id)
        return jsonify ({"message" : " Driver deleted "}) if deleted_driver else jsonify ({"error" : "Driver not found"})


# driver rates


    def get_driver_details(self , driver_id , effective_from):
        driver_details = self.service.get_driver_details(driver_id , effective_from)
        return jsonify (to_dict(driver_details)) if driver_details else jsonify ({"error":"Details not found"})
    
    def create_driver_details(self , driver_details_data):
        driver_details= self.service.create_driver_details(driver_details_data)
        return jsonify(to_dict(driver_details))
    
    def update_driver_details(self , driver_id , effective_from):
        driver_details_data = request.json
        updated_driver_details = self.update_user(driver_id , effective_from ,driver_details_data)
        return jsonify(to_dict(updated_driver_details)) if updated_driver_details else jsonify ({"error" : " Details not found"})
    
    def delete_driver_details(self , driver_id , effective_from):
        deleted_driver_details = self.service.delete_driver_details(driver_id , effective_from)
        return jsonify ({"message" : "Details deleted"}) if deleted_driver_details else ({"error" : "Details not found"})
    



