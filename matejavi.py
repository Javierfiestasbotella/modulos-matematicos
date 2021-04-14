

def factorial(x):
  '''
  Halla el factorial de un número, ose la multiplicación
  de todos los numeros del 1 hasta ese número
  >>> factorial(3)
  6
  >>> factorial(0)
  1
  >>> factorial(34)
  295232799039604140847618609643520000000
  >>> factorial(-3)
  1
  '''
  factorial=1
  for i in range (1,x+1):
    factorial=factorial*i
  print( factorial)



def potencia(a,b):
  '''
  Eleva a al número b
  >>> potencia(3,0)
  1
  >>> potencia(2,3)
  8


  '''


  potencia=a**b
  print(potencia)



def sumatoria(a,b):
  '''
    Esta funcion suma todos los elementos que hay entre a y b 
    éstos incluidos
    >>> sumatoria(2,4)
    9
    >>> sumatoria(0,1)
    1
    >>> sumatoria(0,100)
    5050



     ''' 
  suma=0
  for i in range (a,b+1):
    suma=suma+i
  print(suma)


def pitagoras(a,b,c): #coloca 0 el elemento para hallar
  '''
    Esta funcion halla el elemento que falta dentro 
    del triángulo de pitágoras
       
    >>> pitagoras (0,5,3)  
    la hipotenusa es igual a la raiz cuadrada de: 34 = 5.830951894845301



     ''' 
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
    print("el mcd de los nuemeros  " + str(a) +" y " + str(b) +"= "+ str(maximo))


def tablas(numero):#crea la tabla de multiplicar de cualquier número
  '''

 >>> tablas(2)
 2 x 1 = 2
 2 x 2 = 4
 2 x 3 = 6
 2 x 4 = 8
 2 x 5 = 10
 2 x 6 = 12
 2 x 7 = 14
 2 x 8 = 16
 2 x 9 = 18
 2 x 10 = 20


  '''
  for i in range(1, 11):
    print(str(numero) + " x " + str(i) + " = " + str(numero * i))

def porcentaje(a,b):#halla el tanto % de un numero. a=%, y b= al numero.

  '''
  >>> porcentaje(30,10)
  el 30%  de 10 = 3.0

  '''
  x=(b*a)/100
  print ("el " + str(a) + "%  de " + str(b) +" = " + str(x))

def listado():
  lista=("factorial(x), \npotencia(a,b), \nsumatoria(a,b), \npitagoras(a,b,c), \ntablas(numero), \nporcentaje(a,b), \nmcd(a,b),\nmcm(a,b),\necuacion(a,b), \nperfecto(a), \nbase10(a)","\nbinario(a)","\nnumeroabinario(a)")
  print(lista)


def mcm(a,b):#funcion halla el mcm de dos numeros
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

  #print(lista_a)
    
    
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

  print("el mcm = "+str(resultado))


def ecuacion(a,b):#ecuaciones de 1º grado ax+b=0
  
  if a==a and b==b:
    print("x="+str(-b/a))
  elif a==-a and b==b:
    print("x="+str(b/a))
  elif a==a and b==-b:
    print("x="+str(b/a))
  elif a==-a and b==-b:
      print("x="+str(-b/a))
  else:
    print("no se puede dividir entre 0")
 

def perfecto(a):#te dice si a es un numero perfecto o no.
  perfect=[]
  for i in range (1,a):
    if a%i==0:
      perfect.append(i)
  suma=0
  for j in perfect:
    suma=suma+j
  if suma==a:
    print(str(a)+" es un numero perfecto")
  else:
    print("lo siento "+str(a)+" no es un número perfecto")
 


def sumafraccion(x,b,c,d):
  if x== a/b and y==c/d:
    denominador=mcm(b,d) 
    resultado=([a*(denominador/b)]+[c*(denominador/d)])
  print(resultado)


def base10(a):#te descompone cualquier numero en base 10
  x=str(a)
  base=len(x)-1
  for i in x:
    d=10**base
    print(i +"x",end=" ")
    print(d)
    base=base-1
    
def binario(a):# convierte cualquier numero binario a decimal
  x=int(str(a),2)
  print(x)
      
      
def numeroabinario(a):# convierte un número entero a número binario
  binlista=[]
  while a>=1:
    r=int(a%2)
    binlista.append(r)
    division=a/2
    a=division
  print()
  for i in range(len(binlista)-1,-1,-1):
    print(binlista[i],end="")

if __name__=='__main__':
  import doctest
  doctest.testmod() 