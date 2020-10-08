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
    
# Puede que los colores estén mal :/    
default eileen = CustomChar('Eileen', color='#f2435b', age=21, height=1.68, description='Vivía bajo un puente hasta que se aburrió')
default player = Player('Euclides', color='#c3235d', age=99, height=3.40, description='Se perdió de regreso a casa y conoció a Eileen')

label start:
  
  eileen 'Tú te llamas [player.name] y tienes [player.age] años de edad'
  player 'Bebe este elixir'
  
  $ eileen.age = 23
  
  eileen 'Me has hecho envejecer dos años, ahora tengo [eileen.age] años. Noooo!'
  
  return
