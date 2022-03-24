#script que conecta con Oracle y realiza una comprobación de datos (en este caso facturas) para revisar su contabilidad y asientos contables correctos y si la factyura se ha pagado correctamente

import cx_Oracle
import config
import sys

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

print("Revisar facturas, antes de empezar pon las facturas linea por linea en el checkfras.txt para empezar")
menu= input("Escribe 1 para empezar a consultar estado en centro integral de pago: ")
if menu == '1':
    with open("checkfras.txt","r", encoding="utf8") as fichero:
        content = fichero.readlines()

    content = [x.strip() for x in content]
    print("Se van a analizar las siguientes facturas : ")
    #print(content)
    cur = connection.cursor()
    for i in content:
        x = i[-8:]
        cur.execute("select row1,row2,row3 from table1,table2 where row1=row2 and row5 =:mybv", mybv=x)
        while True:
            row = cur.fetchone()
            if row is None:
                print("Factura: "+x+" no pagada")
                break
            else:
                print("Factura: "+x+" con Situación : "+str(row[0])+" en Centro integral de Pago y con fecha contable: "+str(row[1])+" su estado de visado en tabla de visado es "+str(row[2]))
                break
        #length = len(i)
        #print(i[length - 8:])
        #print(x)

menu= input("Escribe 2 para empezar a consultar estado en su extracto: ")
if menu == '2':
        with open("checkfras.txt", "r", encoding="utf8") as fichero:
                content = fichero.readlines()

        content = [x.strip() for x in content]
        print("Se van a analizar las siguientes facturas en su extracto : ")
        # print(content)
        cur = connection.cursor()
        for i in content:
            x = i[-8:]
            cur.execute("select * from table1 WHERE row100 LIKE '%"+x+"%'")
            while True:
                row = cur.fetchone()
                if row is None:
                    print("Factura: " + x + " no encontrada en extracto")
                    break
                else:
                    print("Factura: " + x + " en extracto : ")
                    break

        # c = connection.cursor()
        # c.execute('') #script sql
else:
    sys.exit(1)
