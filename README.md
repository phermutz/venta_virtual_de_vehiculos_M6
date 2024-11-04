# venta_virtual_de_vehiculos_M6

## comandos:

*** python manage.py runserver ***

PARTE 1. CREAR EL AMBIENTE DE DESARROLLO VIRTUAL PARA EL PROYECTO 
## Requisitos:
- Django versión 4.0.5.
- django-bootstrap-v5 versión 1.0.11.
- django-crispy-forms version 1.14.0.
- crispy-bootstrap5 versión 0.6.

### Crear una aplicación vehículo, la cual contiene las siguientes características: 
- Marca: Fiat, Chevrolet, Ford y Toyota. 
 20 caracteres como máximo, y por defecto Ford. 
- Modelo: 
100 caracteres como máximo.
- Serial Carrocería: 
50 caracteres como máximo. 
- Serial Motor: 
50 caracteres como máximo. 
- Categoría: Particular, transporte y carga. 
20 caracteres como máximo, y por defecto Particular. 
- Precio.  
- Fecha de creación. 
- Fecha de modificación.

### Crear un usuario super administrador del framework Django con username: admin y password:admin.


PARTE 2
● Crear una página de inicio (index.html), que indique un texto simple en HTML “Catalogo de 
Vehículos”,  y que apunte a http://localhost:8000 
 
 
● Crear un formulario de ingreso de vehículos, con los datos de cada uno de los campos:  marca, 
modelo, serial carrocería, serial motor, categoría y precio, en el siguiente enlace: 
http://localhost:8000/vehiculo/add  

PARTE 3. AGREGANDO MENÚ CON BOOTSTRAP 
3.1  Instalar  la  Bootstrap  para  Django,  y  construir  una  barra  de  navegación  (navbar)  que  contenga  el 
siguiente aspecto:  
 
 
 
 
Tomando como base: https://getbootstrap.esdocu.com/docs/5.1/components/navbar/  
 
En el  menú inicio  debe  redireccionar  a la página index,  y  el botón en el  menú Agregar a  la página de 
agregar vehículos: 
 
PARTE 4. 
4.1 Crear un permiso con el nombre de visualizar_catalogo, que al momento de registrar un nuevo 
usuario, se asigna automáticamente, puede visualizar Catálogo de Vehículos.  
 
4.2  Listar  los  vehículos,  y  agregar  el  listado  de  los  mismos  al  menú  de  Listar.  Asignar  tres  tipos  de 
condición  de  precios:  bajo,  entre  0  y  10000;  Medio,  para  mayores  de  10000  y  30000;  y  alto,  para 
mayores  de  30000.  Solo se  puede  visualizar  para  usuarios  autenticados.  Los  usuarios  registrados  y 
con  el  permiso  de    “Can  add  vehiculo  model”  pueden  agregar  los  vehículos  tanto  por  la  interfaz  del 
administrador, como por el enlace vehiculo/add o por el menú de Agregar. 
 
 
Usuario Registrado con permisos de visualizar_catalogo. 
 
Usuario Registrado, y con permisos de visualizar_catalogo y de add_vehiculomodel agregado por 
medio de la interfaz del administrador con la opción de Staff. 