from flask import jsonify , request
from services.user_services import UserService

def to_dict(obj) :
    return {column.name: getattr(obj, column.name) for column in obj.__table__.columns}

class UserController :
    def __init__(self) :
        self.service = UserService()

    def get_user(self , user_id):
        user = self.service.get_user(user_id)
        return jsonify (to_dict(user)) if user else jsonify ({"error":"User not found"})
    
    def create_user(self , user_data):
        user = self.service.create_user(user_data)
        return jsonify(to_dict(user))
    
    def update_user(self , user_id):
        user_data = request.json
        updated_user = self.update_user(user_id , user_data)
        return jsonify(to_dict(updated_user)) if updated_user else jsonify ({"error" : "User not found"})
    
    def delete_user(self , user_id):
        deleted_user = self.service.delete_user(user_id)
        return jsonify ({"message" : "User deleted"}) if deleted_user else ({"error" : "User not found"})
    



# ADMIN

    def create_admin(self , admin_data):
        admin = self.service.create_admin(admin_data)
    
    def get_admin(self , admin_id):
        admin = self.service.get_admin(admin_id)
        return jsonify(to_dict(admin)) if admin else jsonify ({"error" : "Admin not found"})
    
    def update_admin(self , admin_id):
        admin_data = request.json
        updated_admin= self.update_admin(admin_id , admin_data)
        return jsonify(to_dict(updated_admin)) if updated_admin else jsonify ({"error" : "Admin not found"})
    
    def delete_admin(self , admin_id):
        deleted_admin = self.service.delete_admin(admin_id)
        return jsonify ({"message" : " Admin deleted "}) if deleted_admin else jsonify ({"error" : "Admin not found"})

