# Vehicle_Rental_System
MINI PROJECT - VEHICLE RENTAL SYSTEM 

This is the backend application for the Vehicle Rental System, developed using Flask. The app provides APIs to manage vehicle rentals, users, bookings, and other related operations.


Features
User Management: API endpoints for user registration, login, and profile management.
Vehicle Management: Manage vehicle details, including availability and pricing.
Booking System: Book, modify, and cancel vehicle rentals.
Authentication: Secure authentication using JWT (or other methods used)
Database Integration: Stores data in a relational database ( MySQL).
Error Handling: Comprehensive error handling for APIs.
Scalable Structure: Modular codebase for easy scaling and maintenance.

INSTRUCTIONS-

1.to create virtual environmein run the command python -m venv venv
2.now to activate venv we will run the command venv\Scripts\activate
3.now we will install requirements by running command pip install -r requirements.txt
4.intialize the database first change the directory using command:cd shared then use commands:flask db init
                                                                                              flask db migrate
                                                                                              flask db upgrade

5.then we will rollback to main directory by using command :cd..
6.then we will run our application using command python app_runner.py
