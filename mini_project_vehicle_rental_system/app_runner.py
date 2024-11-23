import subprocess

def run_user_service():
    subprocess.Popen([r"C:\Users\deepa\OneDrive\Desktop\DBMS Practical\vehicle_rental_system_project\venv\Scripts\python.exe","user_app/app.py"])

def run_car_service():
    subprocess.Popen([r"C:\Users\deepa\OneDrive\Desktop\DBMS Practical\vehicle_rental_system_project\venv\Scripts\python.exe","car_app/app.py"])

def run_rental_service():
    subprocess.Popen([r"C:\Users\deepa\OneDrive\Desktop\DBMS Practical\vehicle_rental_system_project\venv\Scripts\python.exe","rental_app/app.py"])

def run_payment_service():
    subprocess.Popen([r"C:\Users\deepa\OneDrive\Desktop\DBMS Practical\vehicle_rental_system_project\venv\Scripts\python.exe","payment_app/app.py"])

def run_driver_service():
    subprocess.Popen([r"C:\Users\deepa\OneDrive\Desktop\DBMS Practical\vehicle_rental_system_project\venv\Scripts\python.exe","driver_app/app.py"])

def run_customer_service():
    subprocess.Popen([r"C:\Users\deepa\OneDrive\Desktop\DBMS Practical\vehicle_rental_system_project\venv\Scripts\python.exe","customer_app/app.py"])

def run_city_service():
    subprocess.Popen([r"C:\Users\deepa\OneDrive\Desktop\DBMS Practical\vehicle_rental_system_project\venv\Scripts\python.exe","city_app/app.py"])

def run_feedback_service():
    subprocess.Popen([r"C:\Users\deepa\OneDrive\Desktop\DBMS Practical\vehicle_rental_system_project\venv\Scripts\python.exe","feedback_app/app.py"])



    
if __name__ == '__main__':
    run_user_service()
    run_car_service()
    run_rental_service()
    run_payment_service()
    run_city_service()
    run_driver_service()
    run_customer_service()
    run_feedback_service()
    


    # Graceful Termination of the two subprocesses
    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("\nTerminating all the processes. Alvida!")





# Run the service corresponding to the user_app
def run_user_service():
    subprocess.Popen([r"C:\Users\khush\OneDrive\Desktop\online_exam\venv\Scripts\python.exe", "user/app.py"])

# Run the service corresponding to the question_paper_app
def run_question_paper_service():
    subprocess.Popen([r"C:\Users\khush\OneDrive\Desktop\online_exam\venv\Scripts\python.exe", "question_paper/app.py"])

def run_examination_service():
    subprocess.Popen([r"C:\Users\khush\OneDrive\Desktop\online_exam\venv\Scripts\python.exe","examination/app.py"])
    
def run_evaluation_service():
    subprocess.Popen([r"C:\Users\khush\OneDrive\Desktop\online_exam\venv\Scripts\python.exe","Evaluation/app.py"])
    
def run_Live_session_app_service():
     subprocess.Popen([r"C:\Users\khush\OneDrive\Desktop\online_exam\venv\Scripts\python.exe","Live_session_app/app.py"])
        

