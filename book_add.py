from db_connections import connect_db, Error

def add_book():
    conn = connect_db()
    if conn is not None:
        try:
            cursor = conn.cursor()

            title = input("What is the title of the book you would like to add?").title()
            author = input("Who is the author of the book you would like to add?").title()

            new_book = (title, author)

            query = "INSERT INTO books (book_title, book_author) VALUES (%s, %s)"

            cursor.execute(query, new_book)
            conn.commit()
            print(f"New book: {title} by {author} has been successfully added to the Library!")

        except Error as e:
            print(f"Error: {e}")
        
        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()