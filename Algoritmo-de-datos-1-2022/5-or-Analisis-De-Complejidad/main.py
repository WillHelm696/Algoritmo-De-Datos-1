import time
#import math

# Algoritmo inútil que resta billetes de 100,10 y 1 a un monto dado.
def entrega_billetes_2(monto):
	billete=100
	inc=0	
	billete_actual=billete/(10**inc)
	while monto>0:
		if monto >= billete_actual:
			monto=monto-billete_actual
		else:
			inc=inc+1
			billete_actual=billete/(10**inc)

def Tiempo(a,b,paso):
	print("Intervalo de [",a,",",b,"] Con Paso ",paso)
	start = time.time()
	
	for n in range (a,b+paso,paso):
		monto=n
		entrega_billetes_2(monto)
		end=time.time()


		print("(",n,",",end="")
		print(round(end-start,5),")")
	return end-start

numero = 15.85489498987
redondeado = round(numero, 4)

print("round(1.5): {}".format(redondeado))

Tim=0
Tim+=Tiempo(0,100,10)
print()
Tim+=Tiempo(100,1000,100)
print()
Tim+=Tiempo(1000,10000,1000)
print()
Tim+=Tiempo(10000,100000,10000)
print()
Tim+=Tiempo(100000,1000000,100000)
print()
print("Total",Tim)

