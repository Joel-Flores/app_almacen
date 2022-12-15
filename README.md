# app_almacen
una aplicación para un almacén de instalaciones de internet

el blueprint de autenticacion es para que ingrese el tecnico o el de almacen
el blueprint de technical es la perte de el tecnico pueda registar sus codigos ejecutados
    todas las intalaciones estan puestas con los materiales que debe ingresar
    hay materiales que tiene como ejemplo el tecnico para que empieze a usar la aplicacon
    la parte de reclamos donde se retira un equipo esta separada del reto de la aplicacion para no causar conficto
    el primer usuario ingresado es joe con contraseña joe
    la parte de retiros ingresas los codigos ejecutados y las series de equipos que recojiste,
    asi mismo la parte del material se sumara a tu material que tienes asignado

el blueprint de store es para el manejador de el almacen en general, el usuario de almacen registra los equipos,
    los asigna al tecnico, descarga el material, crear nuevos usuarios para tecnicos, el administrador en si

para iniciar la aplicacion debes aceder a la app con la siguiente configuracion

-inicias las dependencias de la aplicacion 
    esta corre con python 3.8 y pip3
    instalas las dependencias con
    - pip install -r requierement.txt
    
-configuramos flask para un buen inicio
    export FLASK_APP='main.py' es el archivo principal de la app
    export FLASK_SECRET_KEY='' -> ingresas una llave maestra
    export FLASK_DATABASE_HOST='' -> el puerto de ingreso a la base de datos: localhost en caso de que se ejecute en tu computadora
    export FLASK_DATABASE_PASSWORD='' el password de el usuario de mysql
    export FLASK_DATABASE_USER='' el usuario de mysql
    export FLASK_DATABASE='app_store' nombre de la base de datos, esta esta por defecto app_store

para iniciar la base de datos con los datos de prueba
    flask init-db

una vez iniciado la base de datos inicias la aplicacion
    flask run