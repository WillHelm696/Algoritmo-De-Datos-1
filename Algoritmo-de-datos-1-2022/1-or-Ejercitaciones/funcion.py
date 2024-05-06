def promedio_media(desde,hasta):
	suma=0
	cantidad=hasta-desde+1
	for n in range (desde,hasta+1):
		suma=suma+n
	return suma/cantidad
def resta_5(Suma):
	print("La suma es mayor a 50 y la resta de 5 en 5 es")
	while Suma>0:
		print(Suma)
		Suma=Suma-5
	return print ("Fin")
	
def resta_2(Suma):
	print("La suma menor o igual 50 tiene resta de 2 en 2 es")
	while Suma>0:
		print(Suma)
		Suma=Suma-2
	return print ("Fin")

def orden(val_1,val_2,val_3):
	if val_1<=val_2 and val_1<=val_3:
		if val_2<=val_3:
			print(val_1,val_2,val_3)
			promedio=(val_1+val_3)/2
		elif val_2>=val_3:
			print(val_1,val_3,val_2)
			promedio=(val_1+val_2)/2
	elif val_2<=val_1 and val_2<=val_3:
		if val_1<=val_3:
			print(val_2,val_1,val_3)
			promedio=(val_2+val_3)/2
		elif val_1>=val_3:
			print(val_2,val_3,val_1)
			promedio=(val_2+val_1)/2
	elif val_3<=val_1 and val_3<=val_2:
		if val_1<=val_2:
			print(val_3,val_1,val_2)
			promedio=(val_2+val_3)/2
		elif val_1>=val_2:
			print(val_3,val_2,val_1)
			promedio=(val_1+val_3)/2
	return promedio