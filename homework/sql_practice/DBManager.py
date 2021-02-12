import psycopg2
from loguru import logger

logger.add('db_logger.log', format='{time} {message} {level}', level='DEBUG', rotation='10 MB', compression='zip')


class CustomError(Exception):
    pass


class DBManager:

    def __init__(self):
        try:
            self.connection = psycopg2.connect(dbname="dmytro", user="dmytro", password="pass", host="0.0.0.0",
                                               port="5432")
            self.cursor = self.connection.cursor()
        except ConnectionError:
            logger.debug("Problem with connection")
            raise CustomError("Connection problem, check inputed data!")
        else:
            logger.info("Database opened successfully")

    def create_user(self, user_info: dict):
        try:
            self.cursor.execute(
                "INSERT INTO users (name, email, registration_time) VALUES (%(name)s, %(email)s, %(registration_time)s);",
                user_info)
        except Exception:
            logger.debug("Insert new user wffas failed!")
            raise CustomError("User didn`t add to the shop database, data was inputed incorrectly!")
        else:
            logger.info('Insert new user was successfully')

    def read_user_info(self, _id: int):
        try:
            self.cursor.execute("SELECT * From users WHERE id=%s;", (_id,))
        except Exception:
            logger.debug("Read user from database was failed")
            raise CustomError("Couldn`t get user from shop database, check inputed data and try again!")
        else:
            logger.info("Read user from database was successfully")
            for row in self.cursor:
                print(row)

    def update_user(self, new_info: dict, _id: int):
        try:
            self.cursor.execute(f"UPDATE users SET name = (%(name)s), email = (%(email)s) WHERE id = {_id};", new_info)
        except Exception:
            logger.debug("Update user in database was failed!")
            raise CustomError("Couldn`t update user in shop database, check inputed data!")
        else:
            logger.info("Update user in database was successfully")

    def delete_user(self, _id: int):
        try:
            self.cursor.execute("DELETE FROM users WHERE id=%s;", (_id,))
        except Exception as err:
            logger.debug(f"Delete user from database was failed! {err}")
            raise CustomError("Couldn`t delete user from shop database.")
        else:
            logger.info("Delete user from database was successfully")

    def create_cart(self, cart: dict):
        try:
            self.cursor.execute("INSERT INTO cart (creation_time, user_id) VALUES (%(creation_time)s, %(user_id)s);",
                                cart)
        except Exception:
            logger.debug("Insert new cart was failed!")
            raise CustomError("Cart didn`t add to the shop database, data was inputed incorrectly!")
        else:
            logger.info('Insert new cart was successfully')

    def read_cart(self, _id: int):
        try:
            self.cursor.execute("SELECT * From cart WHERE id=%s;", (_id,))
        except Exception:
            logger.debug("Read cart from shop database was failed")
            raise CustomError("Couldn`t get cart from shop database, check inputed data and try again!")
        else:
            logger.info("Read cart from shop database was successfully")
            for row in self.cursor:
                print(row)

    def update_cart(self, cart: dict):
        try:
            self.cursor.execute(
                "UPDATE cart SET creation_time = (%(creation_time)s), user_id = (%(user_id)s) WHERE user_id = (%(user_id)s);",
                cart)
        except Exception:
            logger.debug("Update cart in shop database was failed!")
            raise CustomError("Couldn`t update cart in shop database, check inputed data!")
        else:
            logger.info("Update cart in shop database was successfully")

    def delete_cart(self, _id: int):
        try:
            self.cursor.execute("DELETE FROM cart_details WHERE cart_id = %s;", (_id,))
            self.cursor.execute("DELETE FROM cart WHERE id=%s;", (_id,))
        except Exception as err:
            logger.debug(f"Delete cart from shop database was failed! {err}")
            raise CustomError("Couldn`t delete cart from shop database.")
        else:
            logger.info("Delete cart from shop database was successfully")

    def commit_db(self):
        try:
            self.connection.commit()
        except Exception:
            logger.debug("Database commit was failed!")
            raise CustomError("Problem with commit database!")
        else:
            logger.info("Database commit successfuly")

    def close_cursor(self):
        try:
            self.cursor.close()
        except Exception:
            logger.debug("Cursor stoping was failed!")
            raise CustomError("Problem with closing cursor in database!")
        else:
            logger.info("Cursor was stop successfuly")

    def connection_close(self):
        try:
            self.connection.close()
        except Exception:
            logger.debug("Connection close was failed")
            raise CustomError("Problem with closing connection database!")
        else:
            logger.info("Connection to database stop successfuly")


if __name__ == '__main__':
    dbmanager = DBManager()
    dbmanager.create_user(
        {'name': 'Romko', 'email': 'vitalik@gmail.com', 'registration_time': '2021-02-04 17:40:59'})
    dbmanager.read_user_info(6)
    dbmanager.update_user({'name': 'Roman', 'email': 'roman@gmail.com'}, 8)
    dbmanager.read_user_info(1)
    dbmanager.delete_user(8)
    dbmanager.create_cart({'creation_time': '2021-02-04 17:40:59', 'user_id': '3'})
    dbmanager.read_cart(3)
    dbmanager.update_cart({'creation_time': '2021-02-05 18:59:59', 'user_id': '2'})
    dbmanager.read_cart(2)
    dbmanager.delete_cart(6)
    dbmanager.delete_cart(5)
    dbmanager.delete_cart(7)
    dbmanager.commit_db()
    dbmanager.close_cursor()
    dbmanager.connection_close()
