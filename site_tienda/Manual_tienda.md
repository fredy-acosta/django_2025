# Manual de Usuario  
**Sistema de Gestión de Tienda – Base de datos `tienda_pro`**

Este manual explica el uso del sistema de gestión de la tienda basado en la base de datos `tienda_pro`.  
Incluye la administración de productos, inventario, clientes, órdenes de venta, pagos y descuentos.

El objetivo es que el personal pueda utilizar el sistema de forma rápida y segura en las diferentes sucursales.

---

## 1. Introducción

El sistema permite controlar toda la operación diaria de la tienda:

- Catálogo de **productos** (por ejemplo, `Pro Laptop 101`).
- **Categorías** de producto (por ejemplo, `Computación 1`).
- **Impuestos** (`IVA 5.00%`, `IVA 19.00%`, etc.).
- **Sucursales** (`Sucursal Sur #1`, `Sucursal Norte #2`, etc.).
- **Inventario** por sucursal (existencias, precios y ubicación en estantes).
- **Clientes** (como `María López Morales`, documento `97569018`).
- **Órdenes de venta** (por ejemplo `ORD-202500001`).
- **Pagos** (efectivo, tarjeta, transferencia).
- **Descuentos** (`Promo 1`, `Promo 2`, etc.).
- **Auditoría de cambios** sobre datos importantes.

Todo se organiza desde un menú principal con acceso a cada módulo.

---

## 2. Módulos del Sistema

A continuación se describen los módulos principales según las tablas de la base de datos.

### 2.1 Productos

Corresponde a la tabla `product`.

Aquí se administra el catálogo de productos que vende la tienda.  
Ejemplo de producto (ID 1):

- **SKU:** `SKU-20250001`  
- **Nombre:** `Pro Laptop 101`  
- **Marca:** `Globex`  
- **Categoría:** `Computación 1`  
- **Impuesto asociado:** `IVA 5.00%`  
- **Estado:** `active`  

### 2.2 Categorías

Tabla: `category`.

Agrupa los productos por tipo.  
Ejemplo de categoría (ID 1):

- **Nombre:** `Computación 1`
- **Descripción:** `Productos de Computación`
- **Estado:** `active`

### 2.3 Impuestos

Tabla: `tax`.

Define los impuestos disponibles en el sistema.  
Ejemplo:

- **Nombre:** `IVA 5.00%`
- **Porcentaje:** `5.00`
- **Descripción:** `Impuesto al valor agregado 5.00%`
- **Estado:** `active`

También existen otros como `IVA 0.00%`, `IVA 19.00%`, etc.

### 2.4 Sucursales (Branches)

Tabla: `branch`.

Cada registro representa una tienda física.  
Ejemplo de sucursal (ID 1):

- **Nombre:** `Sucursal Sur #1`  
- **Dirección:** `Calle 10 #96-51, Medellín`  
- **Teléfono:** `+57 337440980`  
- **Estado:** `active`

### 2.5 Inventario

Tabla: `inventory`.

Controla existencias y precio de venta por sucursal y producto.

Ejemplo de inventario (ID 1):

- **Producto:** `Pro Laptop 101` (ID producto = 1)
- **Sucursal:** `Sucursal Sur #1` (ID sucursal = 1)
- **Cantidad disponible:** `133`
- **Cantidad mínima:** `22`
- **Precio de venta:** `2222.98`
- **Ubicación:** `Estante B-3`

### 2.6 Clientes

Tabla: `customer`.

Administra los clientes de la tienda.

Ejemplo de cliente (ID 1):

- **Tipo de documento:** `tax_id`
- **Número de documento:** `97569018`
- **Nombres:** `María`
- **Apellidos:** `López Morales`
- **Estado:** `active`

### 2.7 Órdenes de Venta

Tabla: `orders`.

Representa las ventas realizadas.  
Ejemplo de orden (ID 1):

- **Número de orden:** `ORD-202500001`
- **Cliente:** `María López Morales` (ID cliente = 1)
- **Sucursal:** `Sucursal Sur #1` (ID sucursal = 1)
- **Fecha:** `2025-10-02 05:35:09`
- **Subtotal:** `3814.58`
- **Impuestos:** `190.73`
- **Descuento total:** `0.00`
- **Total final:** `4005.31`
- **Vendedor:** `Luis González`
- **Estado:** por ejemplo, `completed` o similar (según configuración real).

### 2.8 Detalle de Órdenes

Tabla: `order_detail`.

Contiene las líneas de cada orden.

Ejemplo de detalle para la orden `ORD-202500001` (order_id = 1, order_detail_id = 1):

- **Producto:** `Pro Laptop 101` (product_id = 1)
- **Cantidad:** `2`
- **Precio unitario:** `1907.29`
- **Subtotal línea:** `3814.58`
- **Impuesto línea:** `190.73`
- **Descuento línea:** `0.00`
- **Total línea:** `4005.31`

### 2.9 Pagos

Tabla: `payment`.

Define cómo se pagó cada orden.

Ejemplo de pago (ID 1) para la orden `ORD-202500001`:

- **order_id:** `1`
- **Método principal:** `credit_card`
- **Efectivo:** `0.00`
- **Tarjeta:** `4005.31`
- **Transferencia:** `0.00`
- **Total pagado:** `4005.31`
- **Cambio:** `0.00`
- **Código de autorización:** `AUTH-20250000…`
- **Fecha de pago:** `2025-10-02 05:35:09`
- **Estado:** `processed`
- **Nota:** `Pago registrado automáticamente.`

### 2.10 Descuentos

Tabla: `discount`.

Administra las campañas de descuento.

Ejemplo de descuento (ID 1):

- **Nombre:** `Promo 1`
- **Tipo:** `fixed_amount` (monto fijo)
- **Valor del descuento:** `15.39`
- **Fecha inicio:** `2023-11-19`
- **Fecha fin:** `2024-03-25`
- **Monto mínimo:** `41.89`
- **Estado:** `active`

### 2.11 Auditoría

Tabla: `audit_log`.

Registra cambios importantes:

- **Tabla afectada** (`table_name`)
- **Clave primaria** (`pk_value`)
- **Operación** (`INSERT`, `UPDATE`, `DELETE`)
- **Fecha y hora** (`changed_at`)
- **Usuario que realizó el cambio** (`changed_by`)
- **Datos antes y después** (`before_data`, `after_data` en formato JSON)

---

## 3. Flujo de Trabajo: Ejemplo de Venta Real

Para entender el uso del sistema, veamos un flujo completo usando los datos reales del ejemplo.

> **Caso:**  
> La cliente **María López Morales** compra **2 unidades de `Pro Laptop 101`** en la **Sucursal Sur #1**, pagando con tarjeta de crédito.

### Paso 1: Verificar el producto en el catálogo

1. Ir al módulo **Productos**.
2. Buscar el SKU `SKU-20250001` o el nombre `Pro Laptop 101`.
3. Confirmar:
   - Categoría: `Computación 1`.
   - Impuesto: `IVA 5.00%`.
   - Estado: `active`.

### Paso 2: Verificar inventario en la sucursal

1. Ir a **Inventario**.
2. Seleccionar la sucursal **Sucursal Sur #1**.
3. Buscar el producto `Pro Laptop 101`.
4. Verificar que hay stock suficiente:
   - Disponible: `133`
   - Mínimo: `22`
   - Ubicación: `Estante B-3`

### Paso 3: Crear la orden de venta

1. Ir a **Ventas / Órdenes** → **Nueva Orden**.
2. Seleccionar al cliente **María López Morales** (documento `97569018`).
3. Seleccionar la sucursal **Sucursal Sur #1`.
4. Añadir al detalle:
   - Producto: `Pro Laptop 101`
   - Cantidad: `2`
   - Precio unitario: `1907.29`
5. El sistema calcula:
   - Subtotal: `3814.58`
   - Impuesto (5%): `190.73`
   - Descuento: `0.00`
   - **Total de la orden:** `4005.31`
6. Guardar la orden → se genera el número `ORD-202500001`.

### Paso 4: Registrar el pago

1. Desde el detalle de la orden `ORD-202500001`, pulsar **Registrar Pago**.
2. Seleccionar método **Tarjeta de crédito**.
3. Ingresar:
   - Efectivo: `0.00`
   - Tarjeta: `4005.31`
   - Transferencia: `0.00`
4. Verificar:
   - **Total pagado:** `4005.31`
   - **Cambio:** `0.00`
5. Guardar el pago.
6. El sistema crea un registro en `payment` con:
   - método = `credit_card`
   - estado = `processed`
   - nota = `Pago registrado automáticamente.`

### Paso 5: Actualización de inventario

Tras confirmar la venta, el sistema descuenta la cantidad vendida del inventario de la sucursal:

- Antes: `133` unidades de `Pro Laptop 101` en **Sucursal Sur #1**.
- Después de vender 2 unidades: `131` unidades.

---

## 4. CRUD de los Módulos Principales

A continuación se explica cómo crear, listar, editar y eliminar registros.  
La lógica es similar en casi todos los módulos.

> Las imágenes (`![](...)`) son solo marcadores para que insertes tus capturas de pantalla reales.

### 4.1 Gestión de Productos

#### Crear Producto

1. Menú **Productos** → botón **Nuevo Producto**.
2. Completa los campos, por ejemplo:
   - SKU: `SKU-20250001`
   - Nombre: `Pro Laptop 101`
   - Marca: `Globex`
   - Categoría: `Computación 1`
   - Impuesto: `IVA 5.00%`
   - Estado: `active`
3. Haz clic en **Guardar**.

![Crear producto](/ruta/a/captura_crear_producto.png)

#### Listar / Editar / Eliminar Productos

- Desde el listado de productos puedes:
  - Buscar por nombre, SKU o categoría.
  - Pulsar **Editar** para modificar datos.
  - Pulsar **Eliminar** o **Desactivar** para dejar de usar el producto.

![Listado de productos](/ruta/a/captura_listado_productos.png)

---

### 4.2 Gestión de Clientes

#### Crear Cliente

1. Menú **Clientes** → **Nuevo Cliente**.
2. Completar, por ejemplo:
   - Tipo doc.: `tax_id`
   - Número doc.: `97569018`
   - Nombres: `María`
   - Apellidos: `López Morales`
   - Estado: `active`
3. Guardar el registro.

![Crear cliente](/ruta/a/captura_crear_cliente.png)

#### Listar / Editar / Eliminar Clientes

- Buscar por documento o nombre.
- Editar datos (teléfono, dirección, correo).
- Eliminar o marcar como inactivo según las políticas de tu empresa.

![Listado de clientes](/ruta/a/captura_listado_clientes.png)

---

### 4.3 Gestión de Órdenes

#### Crear Orden

1. Menú **Ventas / Órdenes** → **Nueva Orden**.
2. Seleccionar cliente y sucursal.
3. Agregar productos al detalle (cantidad y precio).
4. Aplicar descuento (por ejemplo `Promo 1`) si corresponde.
5. Verificar totales.
6. Guardar para obtener un número de orden similar a `ORD-202500001`.

![Crear orden](/ruta/a/captura_crear_orden.png)

#### Consultar / Editar Órdenes

- Buscar por número (`ORD-202500001`), cliente o fecha.
- Ver el detalle completo (líneas de productos, pagos).
- Según permisos, se puede:
  - editar antes de facturar/pagar;
  - anular una orden.

![Listado de órdenes](/ruta/a/captura_listado_ordenes.png)

---

### 4.4 Gestión de Pagos

#### Registrar Pago

1. Desde la orden pendiente, pulsar **Registrar Pago**.
2. Elegir método (`cash`, `credit_card`, `bank_transfer`).
3. Distribuir montos en los campos:
   - `cash_amount`
   - `card_amount`
   - `transfer_amount`
4. Guardar el pago.

![Registrar pago](/ruta/a/captura_registrar_pago.png)

#### Consultar Pagos

- Ver pagos por orden, método, fecha y estado (`processed`, `pending`, etc.).

![Listado de pagos](/ruta/a/captura_listado_pagos.png)

---

### 4.5 Otros Módulos (Resumen)

La lógica de CRUD es similar para:

- **Categorías** (`category`): crear, editar, desactivar categorías como `Computación 1`.
- **Impuestos** (`tax`): configurar impuestos como `IVA 5.00%`.
- **Sucursales** (`branch`): administrar tiendas como `Sucursal Sur #1`.
- **Descuentos** (`discount`): campañas como `Promo 1`.
- **Inventario** (`inventory`): actualizar cantidades y precios.
- **Auditoría** (`audit_log`): revisar quién y cuándo modificó un registro.

---

## 5. Navegación del Sistema

1. **Menú principal**  
   Desde aquí se accede a:
   - Productos
   - Categorías
   - Impuestos
   - Sucursales
   - Inventario
   - Clientes
   - Ventas / Órdenes
   - Pagos
   - Descuentos
   - Auditoría

2. **Buscadores en listados**  
   Campos de búsqueda por:
   - texto (nombre, SKU, documento),
   - filtros (sucursal, estado, fecha).

3. **Paginación**  
   En listados largos, se muestran resultados por página con controles de **Anterior / Siguiente**.

4. **Botones estándar**
   - **Nuevo**: crear registro.
   - **Editar**: modificar registro.
   - **Eliminar / Desactivar**: borrar o inactivar.
   - **Guardar**: confirmar cambios.
   - **Cancelar**: volver al listado.

![Menú principal](/ruta/a/captura_menu_principal.png)

---

## 6. Mensajes de Éxito y Error

### 6.1 Mensajes de Éxito

Ejemplos típicos:

- `Producto creado correctamente.`
- `Cliente guardado exitosamente.`
- `Orden ORD-202500001 registrada.`
- `Pago registrado automáticamente.`  ← texto real que aparece en la tabla `payment`.

### 6.2 Mensajes de Error Comunes

- `Faltan campos obligatorios.`
- `No hay inventario suficiente para el producto seleccionado.`
- `El total pagado es menor que el total de la orden.`
- `Error de conexión a la base de datos. Intente nuevamente.`

Cuando aparezca un mensaje de error:

1. Leer el mensaje con atención.
2. Corregir la información indicada (por ejemplo, cantidad, método de pago, campos vacíos).
3. Volver a pulsar **Guardar**.

---

## 7. Contacto y Soporte

Para dudas, errores o sugerencias sobre el sistema:

- **Correo de soporte:** soporte@tuempresa.com  
- **Teléfono:** +57 XXX XXX XXXX  
- **Horario de atención:** Lunes a Viernes, 8:00 a.m. – 6:00 p.m.

> Ajusta estos datos con la información real de tu organización.

---

_Fin del Manual de Usuario_

---

## Anexo: Capturas de pantalla del sistema

### Módulo de Impuestos
![Módulo de Impuestos](WhatsApp Image 2025-11-20 at 1.29.32 PM (1).jpeg)

### Módulo de Categorías
![Módulo de Categorías](WhatsApp Image 2025-11-20 at 1.29.32 PM.jpeg)

### Módulo de Sucursales
![Módulo de Sucursales](WhatsApp Image 2025-11-20 at 1.29.31 PM (2).jpeg)

### Módulo de Inventario
![Módulo de Inventario](WhatsApp Image 2025-11-20 at 1.29.31 PM (1).jpeg)

### Módulo de Productos
![Módulo de Productos](WhatsApp Image 2025-11-20 at 1.29.31 PM.jpeg)

