#script comprobar que comprueba datos recibidos contra datos en oracle en producción y crea un dataset con problemas en la factura

import cx_Oracle
import config
import sys
import csv

connection = None
try:
    cx_Oracle.init_oracle_client(lib_dir=r"c:\oracle\instantclient_19_9")
    connection = cx_Oracle.connect(
        config.username,
        config.password,
        config.dsn,
        encoding=config.encoding)

    # show the version of the Oracle Database
    print(connection.version)
except cx_Oracle.Error as error:
    print(error)
    print("Por favor Comprueba los archivos de configuración de la base de datos config.py")
# finally:
#     # release the connection
#     if connection:
#         connection.close()
cur = connection.cursor()
with open('AUDITORIA-IVA.csv', mode='r', encoding='utf-8') as ivafile:
    reader = csv.reader(ivafile, delimiter=';')
    print("Auditoria para las siguientes facturas y % de IVA : ")
    for i in reader:
        cur.execute("select row from table where row=:mybv and filter >= TO_DATE('2021-01-01', 'YYYY-MM-DD')", mybv=i[0])
        rowy = cur.fetchone()
        if rowy is None:
            print("COMPROBAR")
        else:
            iva= int(rowy[0])
            #print(iva)
            if iva == int(i[1]):
                print("IVA OK EN "+i[0])
            else:
                print ("IVA KO")

