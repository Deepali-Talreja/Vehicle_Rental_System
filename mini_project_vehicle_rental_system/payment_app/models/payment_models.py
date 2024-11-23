from sqlalchemy.ext.automap import automap_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = 'mysql+pymysql://root:Dtalreja%4002@localhost/vehicle_rental_system'

engine = create_engine(DATABASE_URL)

Base = automap_base()
Base.prepare(engine , reflect = True)

Payments = Base.classes.payment

SessionLocal = sessionmaker(autocommit = False , autoflush = False , bind = engine)

