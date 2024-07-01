from db_connections import connect_db, Error
import datetime

def borrow_book():
    conn = connect_db()
    if conn is not None:
        try:
            title = input("Please enter the title of the book you are trying to borrow:").title()

            cursor = conn.cursor()

            query = 'SELECT * FROM books WHERE book_title = %s;'

            cursor.execute(query, (title,))

            id, title, author, availability = cursor.fetchall()[0]
            print(f'{id}. {title} by {author} is currently {availability}.')
            
            if availability == "available for rent":
                
                change_to_rented = "rented"
                
                availability_update = (change_to_rented, title)

                query2 = 'UPDATE books SET availability = %s WHERE book_title = %s;'

                cursor.execute(query2, availability_update)

                user_id = input("what is your unique user_id:  ")
                book_id = id
                date_today = datetime.datetime.now()

                add_to_junct = (user_id, book_id, title, date_today) 

                query3 = 'INSERT INTO borrowed_books (user_id, book_id, title, borrow_date) VALUES (%s, %s, %s, %s)'

                cursor.execute(query3, add_to_junct)
                conn.commit()
                print(f'{title} has been rented')

            
        except Error as e:
            print(f"Error: {e}")

        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()