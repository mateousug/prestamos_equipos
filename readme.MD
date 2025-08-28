Explicacion: 

(equipos): Cada equipo esta en una biblioteca, y para saber si esta disponible estos tienen sus propios identificadores llamado disponible, con un valor bolleano, ademas, el valor de los prestamos va a guardar los datos de el usuario que contiene el prestamo solo si un nuevo prestamo ha sido agregado, sino, no contendra informacion.

(mostrar equipos): En este, primero se verifica si si hay equipos usando la palabra reservada not, pero, si hay, entonces primero va a ver el nombre y los datos en los items de los equipos (items siendo su contenido), luego, hace una condicion para revisar si el estado de los datos es true, si es true lo pone disponible, sino, lo muestra como prestado, y por ultimo muestra el nombre y el estado que ya definimos.

(registrar prestamo): Lo primero que hace es llamar a la funcion para mostrar equipos, luego de eso, continuamos con pedir el ingreso de un equipo para , luego, revisa si ese equipo esta en equipos, y luego revisa el valor de equipo_a_prestar