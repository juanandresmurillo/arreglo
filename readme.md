# Bienvenido al Proyecto

Este proyecto tiene como objetivo ofrecer una plataforma para el registro y seguimiento de actividades de los distintos usuarios: campers, trainers y coordinadores. Cada uno de estos roles tiene una función específica dentro del sistema y sus interacciones están claramente definidas en los módulos correspondientes. A través de esta documentación, proporcionamos información esencial para la correcta comprensión y uso de la plataforma, así como detalles técnicos sobre su estructura y funcionamiento.

## Estructura del Proyecto

El código fuente de este proyecto está completamente alojado en el repositorio de Git, lo que permite su fácil acceso y actualización. En él se incluyen todos los archivos necesarios para el funcionamiento del sistema, así como la base de datos que alimenta la plataforma. El programa está dividido en varios módulos, cada uno con una función específica que aborda diferentes necesidades dentro del sistema.

## Módulos y Funciones

El sistema está compuesto por diferentes módulos, lo que facilita la comprensión y el mantenimiento del código. Cada módulo tiene una responsabilidad bien definida, y su propósito es permitir el acceso y la gestión de diferentes aspectos de la plataforma. Entre las funciones clave que realizan estos módulos se encuentran el inicio de sesión, la gestión de notas, y el control de acceso basado en el rol del usuario.

## Inicio del Programa

Cuando un usuario inicia el programa, se le solicita que elija su estudio preferido, lo que lo llevará directamente al módulo principal (main). Este módulo es donde reside el código fuente de este proyecto, y su función es coordinar las interacciones entre los diferentes módulos, redirigiendo a los usuarios a las funcionalidades que les corresponden según su rol.

En el código fuente del módulo principal se encuentran comentarios que guían al usuario a través de las diferentes secciones del programa. Estos comentarios están diseñados para facilitar la navegación y comprensión del código, permitiendo que los desarrolladores, testers o cualquier persona que interactúe con el código tenga una visión clara de cómo y por qué se realiza cada acción.

## Roles de Usuario

Existen tres roles principales dentro de la plataforma: camper, trainer y coordinador. Cada uno tiene acceso a diferentes funcionalidades según sus permisos y necesidades dentro del sistema:

- **Camper:** Este rol tiene acceso a funciones orientadas a la gestión de sus actividades, como el registro de notas o el seguimiento de su progreso dentro de los estudios. Su interacción con la plataforma está centrada en la visualización y actualización de su propio perfil y actividades.
  
- **Trainer:** Los trainers son los encargados de brindar orientación y formación a los campers. Este rol tiene acceso a la información de los campers a los que está asignado, así como la capacidad de gestionar y actualizar las notas relacionadas con su progreso.

- **Coordinador:** Los coordinadores tienen un rol más amplio dentro de la plataforma. Además de gestionar a los trainers y campers, tienen la capacidad de configurar estudios, asignar usuarios a diferentes roles y controlar el flujo general de las actividades dentro de la plataforma.

## Interacción con la Base de Datos

La base de datos está integrada al proyecto para almacenar y gestionar la información de los usuarios, así como sus actividades y progresos. El acceso a la base de datos está controlado de manera eficiente a través de los diferentes módulos, garantizando que cada rol pueda interactuar solo con los datos que le corresponden. Esto se logra a través de sistemas de control de acceso y autenticación, que aseguran la privacidad y seguridad de la información.

## Guía y Documentación

Aunque este proyecto es relativamente sencillo, se ha optado por dejar comentarios en el código que brindan una guía completa sobre su estructura y funcionamiento. Estos comentarios están diseñados para que cualquier desarrollador pueda entender fácilmente cómo interactúan los módulos y qué propósito tiene cada una de sus funciones.

## Conclusión

Este sistema está pensado para ser intuitivo y fácil de usar, pero también es lo suficientemente flexible para permitir una expansión futura si es necesario. Gracias a la división del programa en módulos y la implementación de un sistema de roles claramente definidos, la plataforma es capaz de ofrecer una experiencia personalizada para cada tipo de usuario. Los comentarios en el código permiten una fácil comprensión de cómo se organiza el programa, lo que facilita su mantenimiento y actualización.
