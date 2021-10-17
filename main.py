from mysql.connector import MySQLConnection as MyDB, Error

def obtener_foto(url_foto):
    with open(url_foto, 'rb') as f:
        photo = f.read()
    return photo

def update_image(author_id, url_foto):
    data = obtener_foto(url_foto)

    query = "UPDATE authors " \
            "SET photo = %s " \
            "WHERE id  = %s"

    array_datos = (data, author_id)

    db_config = read_db_config()

    try:
        conn = MyDB(**db_config)
        cursor = conn.cursor()
        cursor.execute(query, array_datos)
        conn.commit()
    except Error as e:
        print(e)
    finally:
        cursor.close()
        conn.close()

def main():
    update_image(144, "pictures\garth_stein.jpg")

#SELECT * FROM authors
#WHERE id = 144;
