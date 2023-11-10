import mysql.connector


class Connection:
    def __init__(self, host='localhost', port='3306', database='students_info', username='root',
                 password='',
                 check=0):
        self.host = host
        self.port = port
        self.database = database
        self.username = username
        self.password = password
        self.connection = None
        try:
            self.connection = mysql.connector.connect(host=self.host,
                                                      port=self.port,
                                                      database=self.database,
                                                      user=self.username,
                                                      passwd=self.password, )
            if check == 1:
                print("connection is done")
        except mysql.connector.Error as error:
            # print("Failed to create table in MySQL: {}".format(error))
            pass

    def connector(self):
        return self.connection

    def close_connection(self):
        if self.connection.is_connected():
            self.connection.close()
        else:
            pass


if __name__ == '__main__':
    # con = Connection(host='localhost', port='3306', database='students_info', username='root',
    #                  password='', check=1)
    pass
