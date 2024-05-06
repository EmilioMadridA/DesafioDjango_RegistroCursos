# Desafío Django - Registro de Cursos

## Descripción

El propósito de este desafío es desarrollar un sistema de administración de cursos para una institución educativa. El sistema permitirá gestionar cursos, estudiantes y profesores. Además de modelar el sistema basado en un diagrama de entidad-relación, permitirá realizar un análisis del sistema y agregar funcionalidades adicionales para operar sobre los datos ingresados.

Este ejercicio permitirá acercarse a un entorno de desarrollo iterativo donde se va agregando más funcionalidad y complejidad al sistema.

## Objetivos

- **Implementar un Proyecto Django:** Crear un proyecto denominado `course_management` y dentro de él, una aplicación llamada `education`.

- **Modelado de Datos:** Configurar cuatro modelos principales: `Student`, `Teacher`, `Course` y `Address`. Cada modelo tiene los siguientes campos:
  - **Student:** `rut`, `name`, `last_name`, `birth_date`, `active`, `created_at`, `updated_at`, `created_by`
  - **Teacher:** `rut`, `name`, `last_name`, `active`, `created_at`, `updated_at`, `created_by`
  - **Course:** `code`, `name`, `version`, `teacher`, `students`
  - **Address:** `street`, `number`, `apt`, `district`, `city`, `region`, `student`

- **Configuración de Base de Datos:** Permitir la conexión a través de PostgreSQL.

- **Servicios de Aplicación:** Crear un archivo `services.py` que contendrá las siguientes funciones:
  - **crear_curso:** Crea un nuevo curso.
  - **crear_profesor:** Crea un nuevo profesor.
  - **crear_estudiante:** Crea un nuevo estudiante.
  - **crear_direccion:** Crea una nueva dirección para un estudiante.
  - **obtiene_estudiante:** Recupera la información de un estudiante por su `rut`.
  - **obtiene_profesor:** Recupera la información de un profesor por su `rut`.
  - **obtiene_curso:** Recupera la información de un curso por su `code`.
  - **agrega_profesor_a_curso:** Asigna un profesor a un curso.
  - **agrega_cursos_a_estudiante:** Asigna cursos a un estudiante.
  - **imprime_estudiante_cursos:** Imprime los cursos a los que está inscrito un estudiante.

## Empezando 🚀

Para realizar este desafío, necesitas tener Python 3 instalado en tu sistema. Se recomienda usar un navegador web moderno como Google Chrome para acceder a la documentación en inglés y permitir la traducción automática del contenido.

### Pre-requisitos 📋

- Python 3.
- PostgreSQL.
- Conocimientos básicos de programación en Python.
- Conocimientos básicos de uso de la terminal o consola de comandos.
- Acceso a Internet para consultar la documentación oficial de Django y tutoriales complementarios.

## Autores ✒️

- **Emilio Madrid** - [EmilioMadridA](https://github.com/EmilioMadridA)

## Agradecimientos 🎁

- A todo el equipo de Desafio Latam y Talento Digital por la oportunidad de aprender y crecer en el campo del desarrollo web con Python y Django.
- A Brayan y Gustavo, por todo lo enseñado.
