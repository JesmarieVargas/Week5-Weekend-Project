from db_connections import connect_db, Error 

def book_search():
    conn = connect_db()

    if conn is not None:
        try:
            title = input("Please enter the title of the book you would like to find: ").title()

            cursor = conn.cursor()

            query = 'SELECT * FROM books WHERE book_title = %s;'

            cursor.execute(query, (title,))

            id, title, author, availability = cursor.fetchall()[0]
            print(f'{id}. {title} by {author}')
        
        except Error as e:
            print(f"Error: {e}")
        
        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()


