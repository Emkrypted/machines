import pymysql
import logging
logging.basicConfig(filename='log/Log.txt', level=logging.DEBUG, format='%(asctime)s -  %(levelname)s -  %(message)s')

class DataBase:
    def __init__(self):
        self.connection = pymysql.connect(
            host = 'localhost',
            user = 'root',
            password = 'Jis2022.',
            db = 'electronic_ticket_system'
        )

        self.cursor = self.connection.cursor(pymysql.cursors.DictCursor)

    def select(self, table, field = '', value = ''):
        if field != '':
            sql = 'SELECT * FROM '+ table + ' WHERE ' + field +' = "'+ str(value) + '"'
        else:
            sql = 'SELECT * FROM '+ table
    
        try:
            logging.info('*****************Desde Sql')
            logging.info('la consulta SQL es: '+ sql)
            self.cursor.execute(sql)
            data = self.cursor.fetchone()
            return data
        except Exception as e:
            raise

    def select_count(self, table, field = '', value = ''):
        if field != '':
            sql = 'SELECT COUNT(*) as quantity FROM '+ table + ' WHERE ' + field +' = "'+ str(value) + '"'
        else:
            sql = 'SELECT COUNT(*) as quantity FROM '+ table
    
        try:
            logging.info('*****************Desde Sql')
            logging.info('la consulta SQL es: '+ sql)
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
            return data[0]['quantity']
        except Exception as e:
            raise

    def select_all(self, table, field = '', value = ''):
        if field != '':
            sql = 'SELECT * FROM '+ table + ' WHERE ' + field +' = '+ str(value)
        else:
            sql = 'SELECT * FROM '+ table

        try:
            logging.info('*****************Desde Sql')
            logging.info('la consulta SQL es: '+ sql)
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
            return data
        except Exception as e:
            raise

    def describe(self, database, table, fields):
        sql = "SELECT "+ fields +" FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = '"+ database +"' AND TABLE_NAME = '"+ table +"'"

        try:
            logging.info('*****************Desde Sql')
            logging.info('la consulta SQL es: '+ sql)
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
            return data
        except Exception as e:
            raise

    def update(self, table, field_to_update, value_to_update, field, value):
        sql = 'UPDATE '+ table + ' SET ' +  field_to_update + ' = "' + str(value_to_update) +'" WHERE ' + field + ' = ' + str(value)
    
        try:
            logging.info('*****************Desde Sql')
            logging.info('la consulta SQL es: '+ sql)
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            raise

    def insert(self, table, fields, values):
        sql = 'INSERT INTO '+ table + ' ('+ fields +') VALUES ('+ values +')'

        try:
            logging.info('*****************Desde Sql')
            logging.info('la consulta SQL es: '+ sql)
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            raise

    def delete(self, table, field, value):
        if field != '':
            sql = 'DELETE FROM '+ table + ' WHERE '+ field +' = '+ str(value)

        try:
            logging.info('*****************Desde Sql')
            logging.info('la consulta SQL es: '+ sql)
            self.cursor.execute(sql)
            if self.connection.commit():
                return 1
            else:
                return 0
        except Exception as e:
            raise

    def execute(self, sentence):
        sql = sentence

        try:
            logging.info('*****************Desde Sql')
            logging.info('la consulta SQL es: '+ sql)
            self.cursor.execute(sentence)
            if self.connection.commit():
                return 1
            else:
                return 0
        except Exception as e:
            raise

    def executeScriptsFromFile(self, filename):
        fd = open(filename, 'r')
        sqlFile = fd.read()
        fd.close()
        sqlCommands = sqlFile.split(';')

        for command in sqlCommands:
            try:
                if command.strip() != '':
                    self.cursor.execute(command)
            except Exception as e:
                raise
