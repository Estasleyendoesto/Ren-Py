init python:
    class Item:
        def __init__(self, name, ud):
            self.name = name
            self.ud = ud

        def set(self, value):
            self.ud += value

        def get(self, value):
            self.ud -= value


    class Inventario:
        def __init__(self):
            self.items = []

        def add(self, item):
            self.items.append(item)

        def remove(self, item):
            self.items.remove(item)

    
    # Usarlo cada vez que un screen actualice variables
    # - Deshabilita salto de pantalla
    # - Guarda todas las variables declaradas para que el usuario pueda volver atrás (save)
    # - Prohíbe que el usuario vuelva atrás xD
    # - Conserva los valores de las variables después de load (evita que se borre el save)
    def update():     
        config.skipping = None  
        renpy.checkpoint()
        renpy.block_rollback()   
        renpy.retain_after_load()


label start:
    # Declaramos variables para el juego
    $ e = Character("Eileen")
    $ bolsa = Inventario()
    $ banana = Item('banana', 0)
    $ bolsa.add(banana)

    jump juego

    return

        
label juego:
    scene bg room
    show eileen happy

    e 'Yo soy [e] y voy a recoger objetos'

    show screen info
    call screen play


screen info:
    $ b = bolsa.items[0]
    text '[e] tiene [b.ud] [b.name]s' xalign 0.5 yalign 0.1 color '#fc3903' size 48

screen play:
    $ update() # Actualiza y guarda variables
    $ b = bolsa.items[0]

    frame:
        xalign 0.5
        yalign 0.5

        vbox:
            textbutton 'Añadir 1 banana' action Function(b.set, 1)
            textbutton 'Comer 1 banana' action Function(b.get, 1)
