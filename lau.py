#Existe k tal que se cumple (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...) = n * k?
#El código del problema se analiza mediante el algoritmo de la división de la siguiente manera
a=input("Digite n:")#Entero positivo conformado por los digitos 0-9
p=int(input("Digite p:"))#Entero positivo
while p<0:#Necesariamente p>0
    print("Oops! No era válido. Intente nuevamente...")
    p=int(input("Digite p:"))
ser=[int(x) for x in str(a)]#Lista de numeros
print("La lista de numeros es"+str(ser))
s=int(len(ser))
print(s)#tamaño de la lista de numeros
sumatoria=0
for i in range(s):#sumatoria (a ^ p + b ^ (p+1) + c ^(p+2) + d ^ (p+3) + ...)
    sumatoria =ser[i]**(p+i)+sumatoria
print(sumatoria)

k=sumatoria % int(a) #Operador modulo in Python
print(k)
#sumatoria=int(a)*k+r, k y r existe por el algoritmo de la division, asi mismo cuando r=0 obtenemos k
if r==0:#Para el caso en que el residuo se anula
  print("k es"+str(sumatoria/int(a)))
else:#en caso contrario
  print("En caso contrario -1")