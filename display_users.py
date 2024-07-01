from db_connections import connect_db, Error

def display_users():
    conn = connect_db()

    if conn is not None:
        try:
            cursor = conn.cursor()
            
            query = 'SELECT * FROM users;'

            cursor.execute(query)

            for id, user_name, email, phone in cursor.fetchall():
                print(f'{id}. Name: {user_name} Email: {email} Phone: {phone}')
                
        
        except Error as e:
            print(f"Error: {e}")
        
        finally:
            cursor.close()
            conn.close()