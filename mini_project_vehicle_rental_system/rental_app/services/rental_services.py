from models.rental_models import SessionLocal , Rentals  , RentalDetails

class RentalService :
    def __init__(self) :
        self.db = SessionLocal()

    def get_rental(self , rental_id) :
        return self.db.query(Rentals).filter(Rentals.rental_id == rental_id).first()

    def create_rental(self , rental_data):
        rental= Rentals(**rental_data)
        self.db.add(rental)
        self.db.commit()
        return rental
    
    def update_rental(self , rental_id , rental_data):
        rental = self.get_rental(rental_id)
        if rental :
            for key , value in rental_data.items():
                setattr(rental , key , value)
            self.db.commit()
            return rental
        
    def delete_rental(self , rental_id) :
        rental = self.get_rental(rental_id)
        if rental:
            self.db.delete(rental)
            self.db.commit()
            return rental
        


#RENTAL DETAILS


    def create_rental_details(self , rental_details_data):
        rental_details = RentalDetails(**rental_details_data)
        self.db.add(rental_details)
        self.db.commit()
        return rental_details
        
    def get_rental_details(self , rental_id):
         return self.db.query(RentalDetails).filter(RentalDetails.rental_id == rental_id).first()
        

    def update_rental_details(self ,rental_id , rental_details_data):
        rental_details = self.get_rental_details(rental_id)
        if rental_details:
            for key , value in rental_details_data.items():
                setattr(rental_details , key , value)
            self.db.commit()
            return rental_details
            
        
    def delete_rental_details(self , rental_id):
        rental_details = self.get_rental_details(rental_id)
        if RentalDetails :
            self.db.delete(rental_details)
            self.db.commit()
            return rental_details
            

