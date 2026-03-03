# 📋 Documento de Requerimientos: cammseb

## 1. Introducción
Este documento detalla los requerimientos para el desarrollo de una aplicación orientada a la gestión integral de un centro de estética y cosmetología. El software busca optimizar la atención al cliente, el diagnóstico personalizado y el control financiero de los servicios.

---

## 2. Stack Tecnológico Sugerido
Para el desarrollo de esta aplicación se han seleccionado las siguientes herramientas, considerando la eficiencia y la facilidad de implementación:
* **Lenguaje de Programación:** Python (Lenguaje principal para la lógica de negocio).
* **Framework de Interfaz:** NiceGUI (Permite crear una interfaz web interactiva y moderna directamente desde Python).
* **Base de Datos:** SQLite (Base de datos local y segura para el almacenamiento persistente de la información de clientes y servicios).

---

## 3. Requerimientos Funcionales (RF)
Son las funciones específicas que el software debe realizar para ser útil en el área de estética:

* **RF1 - Gestión de Citas:** El sistema debe permitir el registro de clientas, almacenando su nombre, el servicio solicitado y la fecha de la cita.
* **RF2 - Asistente de Diagnóstico:** Módulo interactivo que, según el tipo de piel (seca, grasa, mixta) o estado del cabello, recomiende el tratamiento cosmetológico adecuado.
* **RF3 - Calculadora de Costos e Insumos:** Herramienta para calcular el precio final de los servicios basándose en el costo de los materiales utilizados y el tiempo invertido, asegurando un margen de ganancia.
* **RF4 - Visualización de Base de Datos:** Una tabla dinámica que muestre en tiempo real todos los registros guardados en la base de datos SQLite.

---

## 4. Funcionalidades Futuras
Capacidades que podrían agregarse en versiones posteriores para mejorar el software:
* **Generación de Fichas Clínicas en PDF:** Capacidad para descargar el historial de tratamientos de una clienta.
* **Recordatorios Automáticos:** Sistema que notifique a las clientas sobre su próxima cita.
* **Galería de Resultados:** Módulo para cargar fotos de "antes y después" de los tratamientos realizados.

---

## 5. Requerimientos No Funcionales (RNF)
Atributos de calidad del sistema:
* **RNF1 - Interfaz Amigable:** El diseño debe ser intuitivo y con una paleta de colores acorde a un entorno de spa o clínica estética.
* **RNF2 - Integridad de Datos:** La información almacenada en SQLite no debe perderse al cerrar la aplicación.