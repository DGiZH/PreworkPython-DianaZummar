/*1. Crea una base de datos llamada "MiBaseDeDatos".*/
CREATE DATABASE "MiBaseDeDatos"
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'C'
    LC_CTYPE = 'C'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;

/*2. Crea una tabla llamada "Usuarios" con las columnas: "id" (entero, clave
primaria), "nombre" (texto) y "edad" (entero).*/
CREATE TABLE IF NOT EXISTS Usuarios(
	id SERIAL Primary key,
	nombre varchar(255) NOT NULL,
	edad INT NOT NULL
	
)
/*3. Inserta dos registros en la tabla "Usuarios".*/
INSERT INTO public.usuarios(nombre,edad)
VALUES
('Diana', 29),
('Juan',34)
/*4. Actualiza la edad de un usuario en la tabla "Usuarios".*/
UPDATE public.usuarios
SET edad = 35 
WHERE nombre = 'Juan'

/*5. Elimina un usuario de la tabla "Usuarios".*/
DELETE FROM public.usuarios
WHERE nombre = 'Juan'

/*Nivel de dificultad: Moderado*/

/*1. Crea una tabla llamada "Ciudades" con las columnas: "id" (entero, clave
primaria), "nombre" (texto) y "pais" (texto). */
CREATE TABLE IF NOT EXISTS ciudades(
	id SERIAL Primary key,
	nombre Varchar(255) NOT NULL,
	pais Varchar(255) NOT NULL
	)

/*2. Inserta al menos tres registros en la tabla "Ciudades".*/

INSERT INTO public.ciudades(nombre,pais)
VALUES
('San Pedro Sula', 'Honduras'),
('Bogota','Colombia'),
('Madrid','España')

/*3. Crea una foreign key en la tabla "Usuarios" que se relacione con la columna "id" de la tabla "Ciudades".*/
ALTER TABLE public.usuarios
 ADD CONSTRAINT fk_ciudad FOREIGN KEY (ciudad) REFERENCES ciudades(id)

/*4. Realiza una consulta que muestre los nombres de los usuarios junto con el nombre de su ciudad y país (utiliza un LEFT JOIN).*/
SELECT 
a.nombre,
c.nombre AS ciudad,
c.pais AS pais
FROM public.ciudades c
LEFT JOIN public.usuarios a
ON c.id = a.ciudad
GROUP BY a.nombre, c.nombre, c.pais

/*5. Realiza una consulta que muestre solo los usuarios que tienen una ciudad asociada (utiliza un INNER JOIN).*/
SELECT 
a.nombre,
c.nombre AS ciudad,
c.pais AS pais
FROM public.ciudades c
INNER JOIN public.usuarios a
ON c.id = a.ciudad
GROUP BY a.nombre, c.nombre, c.pais
