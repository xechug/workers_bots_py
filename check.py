#script simple que acota a 8 caracters una numeración de facturas para enviarle parametros de busqueda a un ERP a través de cron o otra funcion de analisis y comprobación

with open("checkfras.txt", "r", encoding="utf8") as fichero:
    content = fichero.readlines()

content = [x.strip() for x in content]
# print(content)
for i in content:
    x = i[-8:]
    print(x)