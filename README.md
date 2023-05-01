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



## ------------------------- BACKEND (PROGRAMADORES) -------------------------
A continuación se describe el proceso de desarrollo de manera resumida.

Los cambios referentes a HTML o CSS no se mencionan ya que el foco está en el funcionamiento de la aplicación y el entendimiento de Node.

También se incluyen para mayor claridad las fuentes de datos que normalmente no estarían presentes en el repositorio.

### Configuración de Express y vistas iniciales
1. Creamos nuestra carpeta de vistas src/views con un archivo index.ejs que servirá de página principal.
2. Configuramos Express para que utilice EJS como motor de plantillas y para que tome nuestra carpeta src/views como fuente de plantillas.
3. Creamos una ruta que carge nuestra página principal con el método render().

Verificamos que el servidor levante las vistas de EJS correctamente.

### Estructura MVC, rutas y controladores

1. Creamos nuestra carpeta de rutas src/routes y un archivo static.js, que servirá para todas las páginas estáticas
2. Creamos nuestra carpeta de controladores src/controllers y un archivo staticController.js que implementará la funcionalidad de las rutas anteriores.
3. Creamos el método index en nuestro controllador que renderizará la plantilla de la página principal.
4. Creamos la ruta que responda a la raiz de nuestro sitio / e implementamos el método anterior

Reemplazamos la ruta de nuestro archivo app.js por nuestro nuevo archivo de rutas.

### Parciales y vistas adicionales

1. Creamos la carpeta de vistas parciales views/partials que utilizaremos para los componentes de las vistas.
2. Separamos el header y el footer en archivos parciales.
3. Los implementamos en nuestra vista con la directiva include de EJS
4. Creamos vistas adicionales e implementamos la misma estructura.
-
  - Rutas
  - Métodos del Controlador
  - Parciales de EJS
  
Verificamos que el servidor responda a las nuevas rutas.

### Recursos estáticos

1. Creamos la carpeta public donde pondremos nuestros recursos estáticos.
2. Creamos la carpeta public/css y un archivo main.css donde escribiremos algunos estilos básicos para nuestro sitio.
3. Configuramos Express para que tome la carpeta public como fuente de contenido estático.
4. Implementamos la hoja de estilo en nuestro parcial head.ejs

Verificamos que el servidor haya tomado los estilos correctamente.

### Agregamos la entidad de pokemons

Repetimos los pasos anteriores para los pokemons
1. Archivo de rutas routes/pokemons.js, de momento solo la ruta del listado /.
-
  - Archivo de controllador controllers/pokemonsController.js, de momento sólo el método index.
  - Carpeta de vistas views/products con la vista del listado index.ejs.
  - Estilos básicos para la vista
  - app.use() en src/app.js con las rutas de productos.

Colecciones de pokemons en formato JSON

1. Creamos la carpeta src/data donde pondremos nuestras colecciones en formato JSON.
2. Creamos el archivo products.json en la carpeta anterior, de momento con algunos productos agregados manualmente.
3. Creamos la carpeta models que guardará nuestros modelos, ellos interactuarán con las colecciones.
4. Creamos el modelo genérico para JSON models/jsonModel.js, en él tendremos dos métodos iniciales:
-
  - Lectura del archivo JSON
  - Traer todos los elementos

5. Actualizamos el controlador de productos para que utilize nuestro nuevo modelo y envíe los productos a la vista.
6. Actualizamos la vista para que muestre los productos de manera dinámica.

### Detalle de productos

1. Detalle de producto:
- 
  - Modelo: método find()
  - Ruta: /pokemon/:id (GET)
  - Controlador: método show()
  - Vista: pokemon/detail.ejs
  - Error: pokemon/404.ejs

### Entidad de usuarios
1. Implementamos la entidad de usuarios replicando la de pokemons
- 
  - Rutas: src/routes/user.js
  - Controlador: src/controllers/userController.js
  - Vistas: src/views/users/
  - Coleccion: src/data/users.json

### Login y perfil
1. Implementamos las vistas de registro (usamos el create que ya teníamos) y login
2. Implementamos las rutas correspondientes
- 
  - /usuarios/login (GET y POST)
  - /usuarios/logout (GET)
3. Implementamos en el modelo, el método que nos permitirá buscar usuarios por email (o cualquier otro campo)
4. Implementamos la encriptación de contraseñas
- 
  - npm i bcrypt
  - Lo requerimos en el controlador de usuarios
  - Lo implementamos en el método create, bcrypt.hashSync(...)
  - Lo implementamos en el método login, bcrypt.compareSync(...)
5. Implementamos el uso de sesiones
- 
  - npm i express-session
  - Lo requerimos en src/app.js
  - Lo inicializamos con la configuración mínima sugerida { secret..., resave..., saveUninitialized...}
  - Creamos la sesión al hacer el login y guardamos los datos del usuario en ella.
  - Destruimos la sesión al hacer logout

### Middlewares de autenticación, rutas de huésped y rutas de usuario

1. Implementamos un middleware de autenticación El middleware se encargará de verificar si existe un usuario en sesión y en ese caso hará disponible su información para las vistas.
- 
  - Creamos la carpeta src/middlewares
  - Creamos el middleware src/middlewares/auth
  - Lo implementamos en src/app.js
  - Modificamos la barra de navegación para que muestre los enlaces que correspondan según el usuario esté logeado o no.
2. Implementamos dos middlewares para tener rutas de
- 
  - Creamos el middleware src/middlewares/guestRoute
    
    ♠ Si un usuario accede a esta ruta, lo redirigimos
  - Creamos el middleware src/middlewares/userRoute
    
    ♠ Si un huésped (alquien no logeado) accede a esta ruta, lo redirigimos
    
  - Los implementamos en src/routes/users.js

### Implementamos la funcionalidad de recordar al usuario

1. Implementamos el módulo de manejo de cookies
- 
  -   npm i cookie-parser
  -   Lo requerimos en src/app.js
  -   Lo inicializamos con app.use(...)
2. Implementamos la funcionalidad para recordar al usuario
- 
  - Modelo

    ♠ Implementamos el método para traer todos los registros por campo

  - Controlador
  - 
    ♠ Utilizamos el modulo crypto para generar un token seguro
    
    ♠ Creamos la cookie con el token si llega el campo remember durante el login

    ♠ Destruimos la cookie y el documento durante el logout

  - Coleccion: src/data/userTokens.json
3. Modificamos nuestro middleware de autenticación para que detecte la cookie y loguee al usuario
