from models.driver_models import SessionLocal , Drivers , Driver_details

class DriverService :
    def __init__(self):
        self.db = SessionLocal()
    

    # DRIVER 
    def create_driver(self , driver_data):
        driver= Drivers(**driver_data)
        self.db.add(driver)
        self.db.commit()
        return driver
        
    def get_driver(self , driver_id):
        return self.db.query(Drivers).filter(Drivers.driver_id == driver_id).first()
        

    def update_driver(self ,driver_id , driver_data):
        driver = self.get_driver(driver_id)
        if driver:
            for key , value in driver_data.items():
                setattr(driver, key , value)
            self.db.commit()
            return driver
            
        
    def delete_driver(self , driver_id):
        driver = self.get_driver(driver_id)
        if Drivers :
            self.db.delete(driver)
            self.db.commit()
            return driver
            



    def create_driver_details(self , driver_details_data):
        driver_details = Driver_details(**driver_details_data)
        self.db.add(driver_details)
        self.db.commit()
        return driver_details
    


    def get_driver_details(self , driver_id , effective_from):
        return self.db.query(Drivers).filter(Driver_details.driver_id == driver_id & Driver_details.effective_from == effective_from).first()
        

    def update_driver_details(self ,driver_id ,effective_from , driver_data):
        driver_details = self.get_driver_details(driver_id , effective_from)
        if driver_details:
            for key , value in driver_data.items():
                setattr(driver_details, key , value)
            self.db.commit()
            return driver_details
            
        
    def delete_driver_details(self , driver_id , effective_from):
        driver_details = self.get_driver(driver_id , effective_from)
        if Driver_details :
            self.db.delete(driver_details)
            self.db.commit()
            return driver_details
            
