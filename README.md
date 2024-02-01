# Prueba Técnica - Desarrollo de CRUD para Autores y Libros

## Descripción del Proyecto:

Desarrollar un sistema CRUD (Crear, Leer, Actualizar, Eliminar) para gestionar autores y libros utilizando Django en el backend y React en el frontend. La API RESTful de Django ya ha sido proporcionada, y su objetivo es construir interfaces de usuario para interactuar con dicha API.

## Requerimientos:

### Backend (Django):

1. **Configuración del Entorno:**
   - Antes de comenzar, asegúrate de tener Django y Django Rest Framework instalados en tu entorno de desarrollo. Puedes instalar las dependencias utilizando el siguiente comando:

     ```bash
     pip install -r requirements.txt
     ```

   Asegúrate de ejecutar este comando en el mismo directorio que el archivo `requirements.txt`.

2. **Modelos:**
   - Familiarízate con los modelos `Autor` y `Libro` que se encuentran en la carpeta `autores` de la API. Estos modelos definen la estructura de datos para autores y libros.

3. **Vistas y Serializadores:**
   - Verifica que las vistas y serializadores estén configurados correctamente para realizar operaciones CRUD en autores y libros. Puedes encontrar estas configuraciones en los archivos de vistas y serializadores en la carpeta `autores`.

### Inicialización y Ejecución del API:

Antes de ejecutar la API, sigue estos pasos:

1. **Migración de la Base de Datos:**
   - Accede a la carpeta `autores` que contiene la API Django.
   - Ejecuta el siguiente comando para aplicar las migraciones y crear la base de datos:

     ```bash
     python manage.py migrate
     ```

2. **Crear Superusuario:**
   - Crea un superusuario para acceder al panel de administración y gestionar los datos. Ejecuta el siguiente comando y sigue las instrucciones:

     ```bash
     python manage.py createsuperuser
     ```

3. **Ejecutar la API:**
   - Inicia el servidor de desarrollo de Django con el siguiente comando:

     ```bash
     python manage.py runserver
     ```

   - La API estará disponible en [http://localhost:8000/api/](http://localhost:8000/api/).

4. **Acceder al Panel de Administración:**
   - Visita [http://localhost:8000/admin/](http://localhost:8000/admin/) e ingresa con las credenciales del superusuario que creaste.

Ahora, la API estará lista para recibir solicitudes. Puedes utilizar la documentación mencionada anteriormente para interactuar con los modelos de autores y libros.

### Frontend (React):

1. **Estructura del Proyecto:**
   - Crear una estructura de proyecto en React.

2. **Listado de Autores y Libros:**
   - Implementar vistas para listar autores y libros.

3. **Formularios de Registro:**
   - Crear formularios para registrar nuevos autores y libros.

4. **Estilo y Diseño:**
   - Aplicar un diseño limpio utilizando CSS-in-JS (por ejemplo, Styled Components).

5. **Gestión de Estados y Validación:**
   - Utilizar estados locales con `useState` para componentes sencillos y bibliotecas como Formik o React Hook Form para la gestión y validación de formularios.

6. **Navegación:**
   - Utilizar React Router para manejar la navegación entre las vistas de listar autores y libros, y para la creación de nuevos registros.
