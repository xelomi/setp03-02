#Marcelo Minay
#implementar la busqueda binaria de forma iterativa

def BusquedaBinaria(array, numerito):
    if ( len(array) == 0 ):
        return -1
    elif ( len(array) == 1 ):
        if ( array[0] == numerito ):
            return array[0]
        else:
            return -1
    else:
       inicio = 0
       final = len(array)
       while(inicio < final):
            medio = int((inicio+final)/2)
            if(array[medio] > numerito):
                final = medio
            elif(array[medio] == numerito):
                return numerito
            else:

                inicio = medio

array = [1,2,3,4,5,6,7,8,9]
num = eval(input("Número a verificar"))
numerito = BusquedaBinaria(array, num)
if numerito == -1:
    print ("número no encontrado")
else:
    print ("número encontrado")

