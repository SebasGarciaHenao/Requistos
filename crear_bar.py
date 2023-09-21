from crear_usuario import Crear_Usuario
class Bar(Crear_Usuario):
    def __init__(self,):
        self.bebida = None
        self.precio = None
        self.enlistado = []
        
       
    def enlistar(self,bebida,precio):
       
       usuario = Crear_Usuario
       self.enlistado.append(bebida)
       self.enlistado.append(precio)
       self.total=self.enlistado
       

       if usuario.Usuario_Crear is not usuario.Usuario_creado:
           print("El usuario no puede pedir bebidas por no estar registrado")
        
       else:print(self.total)

 
     
      
      
usuario = Crear_Usuario("Jorge","Garcia",12)
usuario.Usuario_Crear()
usuario.Usuario_creado()
usuario = Bar()
usuario.enlistar("Guaro",25000)

       
print("--------")

      
usuario = Crear_Usuario("Sebas","Garcia",20)
usuario.Usuario_Crear()
usuario.Usuario_creado()
usuario = Bar()
usuario.enlistar("Guaro",25000)
usuario.enlistar("Cerveza",1500)   
       
