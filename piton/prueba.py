#Escribir un programa que pregunte al usuario por el número de horas trabajadas 
#y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde

horas = int(input("Digite la cantidad de horas: "))
pago= int(input("Valor de la hora de trabajo: "))
total= int(horas*pago)
print(f"Usted a trabajado {horas} horas, a un valor de {pago}, cobrara un total de {total} pesos.")
print(" ")
if total >= 1000:
    print("Usted esta trabando bien ")
elif total >= 1500:
    print("Usted esta trabajando muy bien")
elif total <= 999 and total >= 500:
    print ("Usted no sabe trabajar")    
else:
    print("Usted es muy vago")