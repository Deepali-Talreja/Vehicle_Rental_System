from models.city_models import SessionLocal , City

class CityService :
    def __init__(self) :
        self.db = SessionLocal()

    def get_city(self , city_id):
        return self.db.query(City).filter(City.city_id == city_id).first()
    
    def create_city(self , city_data):
        city = City(**city_data)
        self.db.add(City)
        self.db.commit()
        return city
    
    def update_city(self , city_id , city_data ):
        city = self.get_city(city_id)
        if city :
            for key , value in city_data.items():
                setattr(city , key , value)
            self.db.commit()
            return city
        
    def delete_city(self , city_id):
        city = self.get_city(city_id)
        if city :
            self.db.delete(city)
            self.db.commit()
            return city
        