import pymysql

connection = pymysql.connect(
            host = 'localhost',
            user = 'root',
            password = 'Jis2022.'
        )

cursor = connection.cursor(pymysql.cursors.DictCursor)

sqlStatement = "DROP DATABASE IF EXISTS `electronic_ticket_system`"

cursor.execute(sqlStatement)

sqlStatement = "CREATE DATABASE electronic_ticket_system"

cursor.execute(sqlStatement)