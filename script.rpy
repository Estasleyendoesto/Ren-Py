init python:
    def screens():
        # Según las condiciones mostrarás un screen u otro

        renpy.show_screen('personajes')
        renpy.show_screen('dinamicos')
        renpy.show_screen('desplazamientos')
        renpy.show_screen('estancias')
        renpy.call_screen('info')


default mensaje = ''

label start:
    jump juego

    return


label juego:
    scene expression 'images/lounge.png'
    $ screens()
    


screen info:
    text mensaje xalign 0.5 yalign 0.1 color '#fc3903' size 48


screen desplazamientos:
    imagemap:
        alpha True

        auto 'images/lounge_%s.png'

        hotspot (9, 333, 88, 64) clicked SetVariable('mensaje', 'Te diriges hacia la cocina')
        hotspot (605, 630, 64, 81) clicked SetVariable('mensaje', 'Te diriges hacia el lavado')


screen estancias:
    imagemap:
        alpha True

        auto 'images/pasillo_%s.png'

        hotspot (962, 160, 104, 191) clicked SetVariable('mensaje', 'Te has ido por la ventana')

    

screen personajes:
    imagemap:
        alpha True

        auto 'images/characters_%s.png'

        hotspot (419, 296, 180, 241) clicked SetVariable('mensaje', 'Intentas hablar con Gura pero te ignora')


screen dinamicos:
    imagemap:
        alpha True

        # Dentro de este screen con condicionales puedes hacer aparecer objetos para tu historia
        # Tan solo deberías modificar los hotspot con coordenadas en variables mediante bucle for() por ejemplo
        # Eso es todo

        auto 'images/objetos_%s.png'

        hotspot (109, 306, 107, 232) clicked SetVariable('mensaje', 'Esta zanahoria tiene muy buena pinta')
        hotspot (710, 492, 114, 73) clicked SetVariable('mensaje', 'Mejor no lo toco o Gura se enfadará, Shaark')
        hotspot (716, 272, 119, 70) clicked SetVariable('mensaje', 'Esa pistola se ve muy peligrosa')