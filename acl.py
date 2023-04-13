acl = int(input("Introduzca el numero de la ACL IPV4:"))
if acl >= 1 and acl <= 99:
    print("Es una ACL Estandar")
elif acl >= 100 and acl <= 199:
    print("Es una ACL Extendida")
else:
    print("Esta ACL no pertenece a una Estandar o una Extendida")
