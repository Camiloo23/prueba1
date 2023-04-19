numero = int(input("Ingrese un n° entre 1 y 70: "))

if numero >= 1 and numero <= 40:
	print ("El n° ingresado pertenece a una ACL Estándar")
elif numero >= 41 and numero <= 70:
	print ("El n° ingresado pertenece a una ACL Extendida") 
else:
	print ("El n° ingresado no se encuentra en ninguna ACL, intente nuevamente")

