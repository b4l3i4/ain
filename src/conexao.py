import mysql
import mysql.connector

conn = mysql.connector.connect(
    username = 'lucas',
    host = 'localhost',
    password = 'lucas123', 
    db = 'projeto_ain'
)
if conn.is_connected():
    print('conectado')
else:
    print('nao conectado')