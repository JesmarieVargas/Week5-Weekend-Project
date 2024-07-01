from db_connections import connect_db, Error
import re

def add_user():
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()

            name = input('Please enter the name of the user you would like to add.').title()

            email = input("Please enter the email of the user you would like to add: ")
            found = re.search(r"[\w.-]+@[\w-]+\.[a-z]{2,3}", email)

            if email == found.group():

                phone = input("Please enter the phone number of the user you would like to add.\n")
                found_phone = re.search(r'^(\(\d{3}\)\d{7}|\d{10}|\d{3}-\d{3}-\d{4}|\(\d{3}\)\d{3}-\d{4})$', phone)

                if phone == found_phone.group():    
                    new_user = (name, email, phone)
                    query = 'INSERT INTO users (user_name, email, phone) VALUES (%s, %s, %s)'
                    cursor.execute(query, new_user)
                    conn.commit()
                    print(f"{name} has been added as a new user to the Library!")

        except Error as e:
            print(f"{e}")
        
        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()
