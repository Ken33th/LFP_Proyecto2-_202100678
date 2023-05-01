# LFP_Proyecto2-_202100678

| 202100678 | Kenneth Isaí Aquino Ortíz|
| ----- | ---- |
| Diego Andres Obin Rosales | Seccion B+|


## ------------------------- MANUAL DE USO (USUARIO) -------------------------
A continuación se le dara una serie de instrucciones para poder ejecutar el sitio web de manera correcta
- Primeramente necesitamos tener los archivos para poder utilizar el proyecto, estos estan en un repositorio privado de GitHub, si desea acceso a ellos pongase en contacto con el creador de este repositorio. 
  - Url del repositorio: https://github.com/Ken33th/LFP_Proyecto2-_202100678
- Luego de obtener el archivo comprimido (*.rar*) con los archivos dentro, debemos de descomprimir y este nos generará una carpeta con el siguiente nombre "LFP_Proyecto2-_202100678-master" 

![image](https://user-images.githubusercontent.com/109756579/235397017-1533ab2d-a282-445b-a261-6adede6fb6d2.png)



- Luego iniciamos Visual Studio Code y arrastramos la carpeta que descargamos hacia los archivos para abrirla (o tambien puede abrirla agregando al area de trabajo).

- Si no quiere abrir Visual Studio Code, de igual forma puede abrirlo normal desde los archivos que se descargaron antenriormente, solamtene debe seleccionar y hacer doble click sobre "interfaz" 

![image](https://user-images.githubusercontent.com/109756579/235398542-7ab4020d-9aba-45ee-8751-a78848760e4d.png)

y a partir de ahi puede interactuar con la aplicación en la cual puede:

- Abrir un archivo y cargarlo en el area de texto:

![image](https://user-images.githubusercontent.com/109756579/235399007-53b0a909-0178-4950-a6cb-d4f640fe97e9.png)

![image](https://user-images.githubusercontent.com/109756579/235399436-c3572005-a043-4da8-b217-61549bd1a58e.png)


- Luego analizar y generar las sentencias MongoDB:

![image](https://user-images.githubusercontent.com/109756579/235399488-2517462b-bfbf-4dfd-b947-a1d99afe385c.png)

Al seleccionar la opcion de "Generar sentencias MongoDB" se expande la ventana y se muestra el lenguaje traducido

![image](https://user-images.githubusercontent.com/109756579/235399533-f2ca93da-1c34-49cf-a8db-7480895101d1.png)


- Para guardar, entonces tiene 2 opciones, si desea guardar el codigo modificado o guardarlo como un nombre nuevo y encima de otro tipo si desea:

![image](https://user-images.githubusercontent.com/109756579/235400416-b3054115-252b-4706-b495-db903067750f.png)

y si desea abrir un nuevo archivo le preguntara si desea guardar los cambios realizados previamente y 2 opciones: si y no

![image](https://user-images.githubusercontent.com/109756579/235400667-7f642d56-f8b4-45bc-8d2d-8e6757852007.png)



## ------------------------- Manual Técnico -------------------------
A continuación se describe el proceso de desarrollo de manera resumida.
Primero que nada se sebe mencionar que se trabajo con Python en la version 3.11.2 y el IDE que se utilizú fue Visual Studio Code

Ahora, para crear la interfaz gráfica se hizo uso de la libreria Tkinter por lo tanto se descargo la libreria en el sistema y luego se importo dentro del programa:

![image](https://user-images.githubusercontent.com/109756579/235402758-a7a93fbf-5fc7-4304-9c9a-a1c99800db23.png)

Ahora ya la ventana esta creada de la siguiente manera:

![image](https://user-images.githubusercontent.com/109756579/235403218-e842a680-f17c-4199-9279-c9e31d12d423.png)

![image](https://user-images.githubusercontent.com/109756579/235403255-3aaf66f8-b949-4b8f-93f2-0719467e9095.png)

para mostrar la posición del cursor se creo la suguiente función 

![image](https://user-images.githubusercontent.com/109756579/235403329-aed8b4b3-a718-4e68-a6d6-9bb6ab59158c.png)

Como cada una de las opciones debe hacer algo entonces se crearon distintas funciones para cada una y se manda a llamar la función cuando es seleccionada una cierta opción, entonces aqui se tiene lo que es:

- Abrir:

![abrir](https://user-images.githubusercontent.com/109756579/235403584-1962832e-ef0b-453e-a386-abe74aafb512.png)

- Nuevo

![nuevo](https://user-images.githubusercontent.com/109756579/235403635-eaac6bb1-3eb8-4dfe-92cb-249d6e0d87de.png)

- Guardar:

![guardar](https://user-images.githubusercontent.com/109756579/235403700-9628eeac-de45-4b8d-83b1-f804865bb746.png)

- Guardar Como:

![guardarcomo](https://user-images.githubusercontent.com/109756579/235403747-313f11c7-933a-4e9b-99d2-ba657fac7886.png)

- Salir:

![salir](https://user-images.githubusercontent.com/109756579/235403912-0fee209b-b478-49b7-b39a-37ac9286d9af.png)

y en las demas opciones seran de una sola elección la cual hará lo que se le indica como tal, por ejemplo que se genere la sentencia, o que muestre los tokens cargados y también que muestre los errores que hay en el archivo cargado.

Aqui la que es para hacer la traducción:

![generarSentencias](https://user-images.githubusercontent.com/109756579/235404433-c6cdff49-b7c6-4253-88c1-d6da73443055.png)


Gramatica Libre de Contexto:

LEXICO:
    CrearDB
    EliminarDB
    CrearColeccion
    EliminarColeccion
    InsertarUnico
    ActualizarUnico
    EliminarUnico
    BuscarTodo
    BuscarUnico
    nueva
    (
    )
    ;
    =
    ID -> [a-z_A-Z_][a-z_A-Z_0-9]*
    NUMERO -> [0-9]+
    STRING -> "[^"]*"
    IGNORE -> \t\r
    COMENTARIOS -> //.*
                | /\*([^*]|\*+[^*/])*\*+/
    "

SINTACTICO:
    init : instrucciones

    instrucciones : instruccion instrucciones
                | instruccion

    instruccion : crearDB ;
                | eliminarDB ; 
                | crearColeccion ;
                | eliminarColeccion ;
                | insertarUnico ;
                | actualizarUnico ;
                | eliminarUnico ;
                | buscarTodo ;
                | buscarUnico ;

    crearDB : CrearDB ID = nueva CrearDB ( )

    eliminarDB : EliminarDB ID = nueva EliminarDB ( )

    crearColeccion : CrearColeccion ID = nueva CrearColeccion ( STRING )

    eliminarColeccion : EliminarColeccion ID = nueva EliminarColeccion ( STRING )

    insertarUnico : InsertarUnico ID = nueva InsertarUnico ( STRING , STRING )

    actualizarUnico : ActualizarUnico ID = nueva ActualizarUnico ( STRING , STRING )

    eliminarUnico : EliminarUnico ID = nueva EliminarUnico ( STRING )

    buscarTodo : BuscarTodo ID = nueva BuscarTodo ( STRING )

    buscarUnico : BuscarUnico ID = nueva BuscarUnico ( STRING )

