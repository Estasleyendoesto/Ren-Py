# Ren'Py

> Custom Scripts

## Guardar las variables que Ren'Py no hace
> `Save_variables.rpy`

Ren'Py solo guarda aquellas variables cuyos valores han sido actualizados dentro de **label**. Pero cuando cambiamos el valor de una variable dentro de un screen, Ren'Py no los toma en cuenta y se queda con el último valor que almacenó dentro de un label.

Esta es una solución que resulta bastante eficaz, y consiste tratar un screen como si fuera un label mediante una función de python que llamaremos cada vez que un screen actualice algún valor de su variable.

Es irrelevante el lugar en donde coloquemos la variable, pues screen por detrás es un bucle que muestra la pantalla y con cada iteración e independientemente del número de cambios que podamos hacer dentro de este screen, los datos quedarán guardados.

``` python

# Usarlo cada vez que un screen actualice variables
# - Deshabilita salto de pantalla
# - Guarda todas las variables declaradas para que el usuario pueda volver atrás (save)
# - Prohíbe que el usuario vuelva atrás
# - Conserva los valores de las variables después de load (evita que se borre el save)
init python:
  def update():     
      config.skipping = None  
      renpy.checkpoint()
      renpy.block_rollback()   
      renpy.retain_after_load()
      
# Dentro de su screen
 $ update()
```

## Extender la clase Character()
próximamente...
