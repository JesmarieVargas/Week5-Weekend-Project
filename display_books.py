from db_connections import connect_db, Error

def display_books():
    conn = connect_db()

    if conn is not None:
        try:
            cursor = conn.cursor()
            
            query = 'SELECT * FROM books;'

            cursor.execute(query)

            for id, title, author, availability in cursor.fetchall():
                print(f"{id}. {title} by {author} is {availability}")
        
        except Error as e:
            print(f"Error: {e}")
        
        finally:
            cursor.close()
            conn.close()