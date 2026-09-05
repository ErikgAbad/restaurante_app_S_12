# 🍽️ APLICACIÓN DE RESTAURANTE

---

## 📝 DESCRIPCIÓN
Este proyecto es una aplicación de consola desarrollada en **Python con Programación Orientada a Objetos (POO)**. Sirve para administrar un restaurante: permite registrar productos, registrar usuarios y llevar el control de las ventas. Toda la información se guarda automáticamente en archivos **JSON**, por lo que **no se pierde al cerrar el programa**.

---

## 👤 DATOS DEL ESTUDIANTE
| Campo | Información |
|---|---|
| **Nombre** | ERIKG ABAD|
| **Materia** | Programación Orientada a Objetos |
| **Trabajo** | Semana 12 — Persistencia en Archivos JSON |
| **Fecha** | 05 de septiembre de 2026 |

---

## 📂 ESTRUCTURA DEL PROYECTO

restaurante_app_S_12/

│

├── datos/ ← Aquí se guardan los archivos con información

│ ├── productos.json ← Lista de productos, precios y cantidades

│ ├── usuarios.json ← Lista de clientes registrados

│ └── ventas.json ← Historial de todas las ventas realizadas

│

├── modelos/ ← Las clases que definen cada elemento

│ ├── init.py

│ ├── producto.py ← Qué es un producto y cómo se guarda

│ ├── usuario.py ← Qué es un usuario y cómo se guarda

│ └── venta.py ← Qué es una venta y cómo se guarda

│

├── servicios/ ← La lógica para guardar y leer información

│ ├── init.py

│ ├── archivo_servicio.py ← Cómo se escriben y leen los archivos

│ └── restaurante.py ← Funciones principales del sistema

│

├── main.py ← Archivo que se ejecuta para iniciar

└── README.md ← Explicación del proyecto


---

## ✨ FUNCIONALIDADES DEL PROGRAMA
Al iniciar el programa aparece un menú con estas opciones:

| Opción | Acción que realiza |
|---|---|
| **1** | Registrar un producto nuevo |
| **2** | Registrar un usuario nuevo |
| **3** | Registrar una venta realizada |
| **4** | Buscar un producto por su código |
| **5** | Buscar un usuario por su identificación |
| **6** | Ver todas las ventas de un usuario específico |
| **7** | Mostrar la lista completa de productos |
| **8** | Mostrar la lista completa de usuarios |
| **9** | Mostrar el historial completo de ventas |
| **0** | Salir del programa guardando todo |

---

## 💾 CÓMO SE GUARDA LA INFORMACIÓN
Todo se guarda **automáticamente** en archivos de tipo **JSON** dentro de la carpeta `datos`:

| Archivo | Contiene |
|---|---|
| `productos.json` | Código, nombre, precio y stock de cada producto |
| `usuarios.json` | Identificación, nombre y correo de cada usuario |
| `ventas.json` | Fecha, usuario, producto, cantidad y total de cada venta |

✅ Al abrir el programa de nuevo, **toda la información se carga automáticamente**.

---

## 🚀 PASOS PARA EJECUTAR EL PROGRAMA

| Paso | Acción |
|---|---|
| **1** | Abre la terminal en Visual Studio Code |
| **2** | Escribe: `python main.py` y pulsa **Enter** |
| **3** | Escribe el número de la opción que deseas usar |
| **4** | Sigue las instrucciones que aparecen en pantalla |
| **5** | Para salir escribe: `0` y pulsa **Enter** → se guarda todo automáticamente |

---

## 🛠️ TECNOLOGÍAS UTILIZADAS
| Herramienta | Detalle |
|---|---|
| **Lenguaje** | Python 3 |
| **Paradigma** | Programación Orientada a Objetos (POO) |
| **Almacenamiento** | Archivos formato JSON |
| **Editor** | Visual Studio Code |
| **Sistema Operativo** | Windows |

---

## ✅ ESTADO DEL PROYECTO
| Etapa | Estado |
|---|---|
| Semana 11 — Clases y estructura | ✅ Completada |
| Semana 12 — Guardado y lectura en JSON | ✅ Completada y funcionando |

---

## 📌 RESUMEN
El programa funciona correctamente: registra productos, usuarios y ventas, los guarda en archivos JSON y los carga al iniciar. Todo se actualiza automáticamente y se puede consultar en cualquier momento.
