﻿# Chanchirata-6

Nombre del alumno

Heizon Baca Guerrero

Curso

Algoritmos y Estructuras de Datos - Semana 6

Descripción general

Este repositorio contiene el desarrollo de dos retos diferentes utilizando estructuras de colas circulares avanzadas, correspondientes al Laboratorio 6 del curso. Ambos retos fueron diseñados con entradas interactivas (input) y validaciones completas, incluyendo casos límite, errores y ejecución normal.

🧪 Reto 1: Round-Robin Scheduler con Prioridades

Descripción

Se implementó un planificador Round-Robin que utiliza tres colas circulares separadas por prioridad (alta, media, baja). Cada proceso tiene un PID, nombre, duración y prioridad.

Se utiliza collections.deque para simular las colas circulares

El tiempo de ejecución se divide por "quantum".

Procesos se reinsertan si no han terminado

Se incluyen mensajes de validación y ejecución

Archivo

Ejercicio1.py

Casos de prueba

Caso 1 – Prioridad inválida

Quantum: 4
Número de procesos: 2
Proceso 1: PID 1, Chrome, duración 5, prioridad 4 ❌
Proceso 2: PID 2, Slack, duración 7, prioridad 2 ✅

Caso 2 – Ejecución normal

Quantum: 3
Número de procesos: 3
PID 10, VSCode, 5s, prioridad 1
PID 11, Slack, 4s, prioridad 2
PID 12, Zoom, 6s, prioridad 3

Caso 3 – Sin procesos

Quantum: 5
Número de procesos: 0 ❌

🔄 Reto 2: Circular Log Buffer

Descripción

Se implementó un buffer circular que mantiene solo los últimos N logs insertados.

Se utiliza una lista de tamaño fijo

Sobrescribe los elementos más antiguos cuando se llena

Informa al usuario cuando sobrescribe

Solo imprime los logs más recientes

Archivo

Ejercicio2.py

Casos de prueba

Caso 1 – Comportamiento normal

Tamaño del buffer: 3
Entradas: Evento A, Evento B, Evento C
Resultado: Muestra los 3 logs

Caso 2 – Buffer lleno y sobreescribir

Tamaño del buffer: 2
Entradas: Entrada 1, Entrada 2, Entrada 3, Entrada 4
Resultado: Muestra advertencia de sobreescritura, imprime Entrada 3 y 4

Caso 3 – Sin logs

Tamaño del buffer: 5
Entrada: fin
Resultado: No se ingresaron logs

👨‍💻 Instrucciones de ejecución

Ambos programas utilizan entrada por teclado. Para ejecutar:

python Ejercicio1.py
python Ejercicio2.py

🗃️ Estructura del repositorio

Chanchirata-6/
├── Ejercicio1.py                 # Reto 1
├── Ejercicio2.py                 # Reto 2
├── informe_lab06.docx           # Informe completo
├── README.md                    # Este archivo

📚 Conclusiones

Este laboratorio permitió aplicar conceptos clave como:

Simulación de sistemas con colas circulares

Control de flujos de entrada

Validación de datos en tiempo real

Diseño modular e interactivo

Manejo de buffers circulares y prioridades de ejecución
