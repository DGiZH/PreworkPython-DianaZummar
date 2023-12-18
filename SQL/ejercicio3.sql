/*1. Crea una tabla llamada "Productos" con las columnas: "id" (entero, clave primaria), "nombre" (texto) y "precio" (numérico).*/
 CREATE TABLE IF NOT EXISTS productos(
 	id SERIAL PRIMARY KEY,
	nombre VARCHAR(255),
	precio INT
 )

/*2. Inserta al menos cinco registros en la tabla "Productos".*/

INSERT INTO public.productos(nombre,precio)
VALUES 
('camisa',5),
('pantalon',10),
('zapato',3),
('calcetin',1),
('gorra',4)

/*3. Actualiza el precio de un producto en la tabla "Productos".*/
UPDATE public.productos
SET precio = 3
WHERE nombre = 'gorra'

/*4. Elimina un producto de la tabla "Productos".*/
DELETE FROM public.Productos
WHERE id=3

/*5. Realiza una consulta que muestre los nombres de los usuarios junto con los nombres de los productos que han comprado (utiliza un INNER JOIN con la
tabla "Productos").*/
SELECT 
a.nombre AS nombre,
p.nombre AS producto

FROM public.productos p
INNER JOIN public.usuarios a
ON p.id = a.product_id
GROUP BY a.nombre,p.nombre