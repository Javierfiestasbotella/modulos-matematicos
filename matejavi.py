


def factorial(x):
  '''
    La función impar(n) devuelve:
    -  True: si número es impar
    - False: si número no es impar
    >>> factorial(0)
    1
    >>> factorial(1)
    1
    >>> factorial(3)
    6
    >>> factorial(-4)
    1

  '''


  factorial=1
  for i in range (1,x+1):
    factorial=factorial*i
  return factorial



def potencia(a,b):
  '''
  La potencia eleva a a la potencia b
  >>> potencia(2,3)
  8
  >>> potencia(6,0)
  1
  >>> potencia(0,4)
  0
  '''
  potencia=a**b
  print(potencia)



def sumatoria(a,b):
  
  '''
  >>> sumatoria(1,100)
  5050
  >>> sumatoria(-100,100)
  0
  
  '''
  suma=0
  '''
  >>> suma(3,7)
  10
  >>> suma(-4,-6)
  -10
  >>> suma(-34,4)
  -30
  '''
  for i in range (a,b+1):
    suma=suma+i
  print(suma)


def pitagoras(a,b,c): #coloca 0 el elemento para hallar
  if a==0:
    a=a**2
    a=b**2+c**2
    print(f"la hipotenusa es igual a la raiz cuadrada de: {a}",end=" = ")
    print(a**.5)

  elif b==0:
    b=b**2
    b=a**2-c**2-c
    print("el cateto es igual a la raiz cuadrada de: " + str(b),end=" = ")
    print(b**.5)

  else:
    c=c**2
    c=a**2-b**2
    print("el cateto es igual a la raiz cuadrada de: " + str(c),end=" = ")
    print(c**.5)


def mcd(a,b):# halla el mcd de dos numeros
  '''
  >>> mcd(3,12)
  el mcd de los números  3 y 12= 3
  >>> mcd (34,56)
  el mcd de los números  34 y 56= 2
  >>> mcd(27,144)
  el mcd de los números  27 y 144= 9


  
  '''
  listaA=[]
  listaB=[]
  for i in range(1,a+1):
      if a%i==0:
          listaA.append(i)
  for j in range(1,b+1):
      if b%j==0:
          listaB.append(j)
  lista_divisores=[]
  for x in listaA:
    for y in listaB:
      if x==y:
        lista_divisores.append(x)
    #for maximo in lista_divisores:
    maximo= max(lista_divisores, key=int)
  print("el mcd de los números  " + str(a) +" y " + str(b) +"= "+ str(maximo))


def tablas(numero):#crea la tabla de multiplicar de cualquier número
  for i in range(1, 11):
    print(str(numero) + " x " + str(i) + " = " + str(numero * i))




def porcentaje(a,b):#halla el tanto % de un numero. a=%, y b= al numero.
  

  '''
  >>> porcentaje(30,10)
  el 30% de 10 = 3.0
  >>> porcentaje(97,345)
  el 97% de 345 = 334.65
  >>> porcentaje(15,-100)
  el 15% de -100 = -15.0


  '''
  x=(b*a)/100
  print ("el " + str(a) + "% de " + str(b) +" = " + str(x))

def listado():
  lista=("factorial(x), \npotencia(a,b), \nsumatoria(a,b), \npitagoras(a,b,c), \ntablas(numero), \nporcentaje(a,b), \nmcd(a,b),\nmcm(a,b),\necuacion(a,b),  \necuacion2_grado(a,b,c), \nperfecto(a),  \nsumafraccion(a,b,c,d), \ndescomponer(x),\nfibonachi(m), \nmulti_rusa(x,y), \nsuma_angulos(g1,m1,s1,g2,m2,s2), \nresta_angulos(g1,m1,s1,g2,m2,s2)")
  print(lista)


def mcm(a,b):#funcion halla el mcm de dos numeros
  '''
  >>> mcm(4,12)
  12
  >>> mcm(3,4)
  12
  
  '''
  divide2=0
  divide3=0
  divide5=0
  divide7=0
  divide11=0
  divide2b=0
  divide3b=0
  divide5b=0
  divide7b=0
  divide11b=0
  lista_a=[]
  lista_b=[]
  
  while a>0:
    if a%2==0:
      a=a/2
      divide2=divide2+1
    elif a%3==0:
      a=a/3
      divide3=divide3+1
    elif a%5==0:
      a=a/5
      divide5=divide5+1
    elif a%7==0:
      a=a/7
      divide7=divide7+1
    elif a%11==0:
      a=a/11
      divide11=divide11+1
    else:
      #print(a)
      break
  x=2**divide2
  y=3**divide3
  z=5**divide5
  l=7**divide7
  m=11**divide11
  lista_a.append(x)
  lista_a.append(y)
  lista_a.append(z)
  lista_a.append(l)
  lista_a.append(m)

  #print(lista_a
    
    
  while b>0:
    if b%2==0:
      b=b/2
      divide2b=divide2b+1
    elif b%3==0:
      b=b/3
      divide3b=divide3b+1
    elif b%5==0:
      b=b/5
      divide5b=divide5b+1
    elif b%7==0:
      b=b/7
      divide7b=divide7b+1
    elif b%11==0:
      b=b/11
      divide11b=divide11b+1
    else:
      #print(b)
      break
  w=2**divide2b
  k=3**divide3b
  p=5**divide5b
  h=7**divide7b
  g=11**divide11b
  lista_b.append(w)
  lista_b.append(k)
  lista_b.append(p)
  lista_b.append(h)
  lista_b.append(g)

  #print(lista_b)
  resultado=1
  if lista_a[0]>lista_b[0]:
    resultado=resultado*lista_a[0]
  else:
    resultado=resultado*lista_b[0]
  
  if lista_a[1]>lista_b[1]:
    resultado=resultado*lista_a[1]
  else:
    resultado=resultado*lista_b[1]
  
  if lista_a[2]>lista_b[2]:
    resultado=resultado*lista_a[2]
  else:
    resultado=resultado*lista_b[2]
  
  if lista_a[3]>lista_b[3]:
    resultado=resultado*lista_a[3]
  else:
    resultado=resultado*lista_b[3]
  
  if lista_a[4]>lista_b[4]:
    resultado=resultado*lista_a[4]
  else:
    resultado=resultado*lista_b[4]

  return resultado
  #print("el mcm = "+str(resultado))


def ecuacion(a,b):#ecuaciones de 1º grado ax+b=0
  '''
  >>> ecuacion(7,21)
  -3.0
  >>> ecuacion(6,3)
  -0.5
  
  
  '''
  
  if a==a and b==b:
    return -b/a
  elif a==-a and b==b:
    return b/a
  elif a==a and b==-b:
    return b/a
  elif a==-a and b==-b:
    return -b/a
  else:
    print("no se puede dividir entre 0")

def ecuacion_2grado(a,b,c):#halla los dos resultados + y - de ecuacion de 2ºgrado
  '''
  >>> ecuacion_2grado(1,3,2)
  (-1.0, -2.0)
  >>> ecuacion_2grado(1,-25,144)
  (16.0, 9.0)
  >>> ecuacion_2grado(1,-2,-80)
  (10.0, -8.0)
  
  
  '''
  raiz=float((b**2-4*a*c))
  raiz=raiz**0.5
  x1=(-(b)+raiz)/2*a
  x2=(-(b)-raiz)/2*a
  return x1,x2

def perfecto(a):#te dice si a es un numero perfecto o no.

  '''
  >>> perfecto (6)
  True
  >>> perfecto (46)
  False
  
  '''
  perfect=[]
  for i in range (1,a):
    if a%i==0:
      perfect.append(i)
  suma=0
  for j in perfect:
    suma=suma+j
  if suma==a:
    return True
  else:
    return False
 


def sumafraccion(a,b,c,d):#suma dos fracciones a/b + c/d
  '''
  >>> sumafraccion(5,3,5,4)
  2.92
  >>> sumafraccion(56,6,4,7)
  34.67
  '''
  
  while b!=0 or d!=0:
    
    denominador=mcm(b,d)
    resultado=(a*(denominador/b)+(c*(denominador/d)))/12
    return float("{0:.2f}".format(resultado))
  


def descomponer(x):# descopone cualquier numero en base 10
  '''
  >>> descomponer(3011)
  3 x 1000
  0 x 100
  1 x 10
  1 x 1
  '''
  y=str(x)
  base=len(y)
  for numero in y:
    if numero!="0":
      print (numero+" x",10**(base-1))
      base-=1
    else:
      print (numero+" x",10**(base-1))
      base-=1
      
def fibonachi(m):#el atributo 'm' indica los primeros m numeros de la secuencia de fibonachi
  '''
  >>> fibonachi(7)
  0
  1
  1
  2
  3
  5
  8
   '''
  f0=0 
  f1=1
  lista_fibo=[0,1]
  for k in range (2, m):
    f=f0+f1
    f0=f1
    f1=f
    lista_fibo.append(f)
  for i in lista_fibo:
    print(i)


def multi_rusa(x,y):#multiplicacion rusa
  '''
  >>> multi_rusa(25,6)
  150
  >>> multi_rusa(0,23)
  0
  '''
  cont1=0
  cont2=0
  resultado=0
  while y!=1:
    y=y//2
    cont1+=1
  while cont2!=cont1:
    x=x*2
    resultado+=x
    cont2+=1
  return resultado

def suma_angulos(g1,m1,s1,g2,m2,s2):
  '''
  >>> suma_angulos(24,35,48,12,27,36)
  "37° 3' 24''"
 
  '''
  segundos=s1+s2
  minutos=0
  grados=0
  if segundos>60:
    minutos+=1
    segundos-=60
  minutos=minutos+m1+m2
  if minutos>60:
    grados+=1
    minutos-=60
  grados=grados+g1+g2
  #return str(grados)+'°'+str(minutos)+"'"+str(segundos)+"''"
  return ("{}° {}' {}''").format(grados,minutos,segundos)




def resta_angulos(g1,m1,s1,g2,m2,s2):
  '''
  >>> resta_angulos(24,35,48,12,27,36)
  "12° 8' 12''"
 
  '''
  
  segundos=s1-s2
  minutos=0
  grados=0
  if g1<g2:
    minutos-=1
    segundos=segundos+60
  minutos=m1-m2+minutos
  if m1<m2:
    grados-=1
    minutos=minutos+60
  grados=g1-g2+grados
  #return (str(grados)+"°"+str(minutos)+"'"+str(segundos)+"''")
  return ("{}° {}' {}''").format(grados,minutos,segundos)

 








listado ()  
    
if __name__=="__main__":
  import doctest
  doctest.testmod()
