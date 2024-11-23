from models.car_models import SessionLocal , Cars

class CarService :
    def __init__(self) :
        self.db = SessionLocal()

    def get_car(self , car_id):
        return self.db.query(Cars).filter(Cars.car_id == car_id).first()
    
    def create_car(self , car_data):
        car = Cars(**car_data)
        self.db.add(Cars)
        self.db.commit()
        return car
    
    def update_car(self , car_id , car_data ):
        car = self.get_car(car_id)
        if car :
            for key , value in car_data.items():
                setattr(car , key , value)
            self.db.commit()
            return car
        
    def delete_car(self , car_id):
        car = self.get_car(car_id)
        if car :
            self.db.delete(car)
            self.db.commit()
            return car
        