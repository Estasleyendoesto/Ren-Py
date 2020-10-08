init python:
  # Extensión de Character()
  # -----------------------------------
  class CustomChar(ADVCharacter):
        def __init__(
            self, 
            name, 
            kind = None, 
            age = None, 
            height = None, 
            weight = None, 
            description = None, 
            **properties
            ):
            super(CustomChar, self).__init__(name, kind=None, **properties)
            self.age = age
            self.height = height
            self.weight = weight  
            self.description = description
        
        # Tus propios métodos de personaje...
        
  # Clase dedicada al jugador
  # ---------------------------------------       
  class Player(ADVCharacter):
        def __init__(
            self, 
            name, 
            kind = None, 
            age = None, 
            height = None, 
            weight = None, 
            description = None, 
            experience = None,
            **properties
            ):
            super(Player, self).__init__(name, kind=None, **properties)
            self.age = age
            self.height = height
            self.weight = weight
            self.description = description
            self.experience = experience
            
        # Tus propios métodos de jugador...
    
          
