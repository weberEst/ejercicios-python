def agregar_usuario (id,nombre,lista_usuarios):  
    for elementos in lista_usuarios:
        for buscandoid in elementos:     
                
          if id!=buscandoid: 
             validation = True
             break   
                      
          elif id==buscandoid:            
             validation = False
             break

    if validation == True: 
        lista_usuarios.append([id, nombre])
     
    elif validation == False:
         print("El id ingresado ya existe, porfavor ingresa otro numero id para el nuevo usuario") 



def listar_usuarios(nombre_lista): # ya funciona
    for x in nombre_lista:

            print (x)



def actualizar_usuario():
    print("actualizando data del usuario....")


def eliminar_usuario():
    print("eliminando usuario...")