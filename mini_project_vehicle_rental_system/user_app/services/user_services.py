from models.user_models import SessionLocal , Users  , Admins

class UserService :
    def __init__(self) :
        self.db = SessionLocal()

    def get_user(self , user_id) :
        return self.db.query(Users).filter(Users.user_id == user_id).first()

    def create_user(self , user_data):
        user = Users(**user_data)
        self.db.add(user)
        self.db.commit()
        return user
    
    def update_user(self , user_id , user_data):
        user = self.get_user(user_id)
        if user :
            for key , value in user_data.items():
                setattr(user , key , value)
            self.db.commit()
            return user
        
    def delete_user(self , user_id) :
        user = self.get_user(user_id)
        if user:
            self.db.delete(user)
            self.db.commit()
            return user
        


#ADMIN

    def create_admin(self , admin_data):
        admin = Admins(**admin_data)
        self.db.add(admin)
        self.db.commit()
        return admin
        
    def get_admin(self , admin_id):
         return self.db.query(Admins).filter(Admins.admin_id == admin_id).first()
        

    def update_admin(self ,admin_id , admin_data):
        admin = self.get_admin(admin_id)
        if admin:
            for key , value in admin_data.items():
                setattr(admin , key , value)
            self.db.commit()
            return admin
            
        
    def delete_admin(self , admin_id):
        admin = self.get_admin(admin_id)
        if admin :
            self.db.delete(admin)
            self.db.commit()
            return admin
            

