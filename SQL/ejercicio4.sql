/*1. Crea una tabla llamada "Pedidos" con las columnas: "id" (entero, clave
primaria), "id_usuario" (entero, clave foránea de la tabla "Usuarios") y
"id_producto" (entero, clave foránea de la tabla "Productos").*/

CREATE TABLE IF NOT EXISTS pedidos(
	id SERIAL PRIMARY KEY NOT NULL,
	id_usuario INT,
	id_producto INT,
	CONSTRAINT FK_id_usuario FOREIGN KEY (id_usuario) REFERENCES usuarios(id),
	CONSTRAINT FK_id_producto FOREIGN KEY (id_producto) REFERENCES productos(id)
	
)

/*2. Inserta al menos tres registros en la tabla "Pedidos" que relacionen usuarios con productos. */
INSERT INTO public.pedidos(id_usuario,id_producto)
VALUES 
(1,1),
(1,4),
(1,5)

/*3. Realiza una consulta que muestre los nombres de los usuarios y los nombres de los productos que han comprado, incluidos aquellos que no han realizado ningún pedido (utiliza LEFT JOIN y COALESCE).*/
SELECT 
a.nombre,
c.nombre AS producto

FROM public.usuarios a
LEFT JOIN public.pedidos p
ON a.id = p.id_usuario 
LEFT JOIN public.productos c
ON c.id = p.id_producto 
GROUP BY a.nombre, c.nombre


/*4. Realiza una consulta que muestre los nombres de los usuarios que han
realizado un pedido, pero también los que no han realizado ningún pedido
(utiliza LEFT JOIN).*/

SELECT 
a.nombre,
c.nombre AS producto

FROM public.usuarios a
LEFT JOIN public.pedidos p
ON a.id = p.id_usuario 
LEFT JOIN public.productos c
ON c.id = p.id_producto 
GROUP BY a.nombre, c.nombre




/*5. Agrega una nueva columna llamada "cantidad" a la tabla "Pedidos" y actualiza los registros existentes con un valor (utiliza ALTER TABLE y UPDATE)*/

ALTER TABLE public.pedidos
ADD COLUMN cantidad INT

UPDATE public.pedidos
SET cantidad = 3
WHERE cantidad is NULL