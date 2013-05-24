#Marcelo Minay
#implementar busqueda binaria recursiva


def BusquedaBinaria(array, numerito):
    if len(array) == 0 :
        return -1
    elif ( len(A) == 1 ):
        if array[0] == numerito :
            return A[0]
        else:
            return -1
    else:
       medio = int(len(array)/2)
       if array[medio] > numerito :
           return BusquedaBinaria(array[0:medio],numerito)   #se envia la primera mitad del arreglo
       else:
           return BusquedaBinaria(array[medio:len(array)],numerito)  #o se envía la segunda.

array = [1,2,3,4,5,6,7,8,9]
num = eval(input("Número a verificar"))
numerito = BusquedaBinaria(array, num)
if numerito == -1:
    print ("número no encontrado")
else:
    print ("número encontrado")

