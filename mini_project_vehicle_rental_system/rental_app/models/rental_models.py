from sqlalchemy.ext.automap import automap_base 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# database configuration
DATABASE_URL = 'mysql+pymysql://root:Dtalreja%4002@localhost/vehicle_rental_system'

# create SQLALCHEMY engine
engine = create_engine(DATABASE_URL)


#reflect the existing tables 
Base = automap_base()
Base.prepare(engine , reflect = True)


Rentals = Base.classes.rental


RentalDetails = Base.classes.rentaldetails 


SessionLocal = sessionmaker(autocommit = False , autoflush = False , bind = engine)



