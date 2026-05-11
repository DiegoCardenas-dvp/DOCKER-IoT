# Proyecto Docker & Git: Virtualización para Sistemas Embebidos e IoT

Este repositorio contiene el desarrollo y la documentación técnica de la implementación de contenedores Docker para la ejecución de aplicaciones en **C++** y **Python**. El enfoque principal es demostrar la portabilidad de software y la consistencia de entornos de ejecución en el desarrollo de ingeniería.

---

## ¿Qué se hizo en este proyecto?

El objetivo fue encapsular dos flujos de trabajo técnicos dentro de contenedores aislados. La principal ventaja de esta arquitectura es que el software no depende de las librerías instaladas localmente en el sistema operativo, sino de una **Imagen Docker** preconfigurada.

### Puntos Clave de la Implementación:
* **Dockerización de C++:** Se configuró un entorno basado en Ubuntu 22.04 que incluye el compilador `g++` y la herramienta de graficado técnico `gnuplot`.
* **Automatización de Procesos:** El contenedor no solo compila, sino que ejecuta la lógica matemática y procesa la salida gráfica de forma secuencial.
* **Persistencia mediante Volúmenes:** Se utilizó el parámetro de volumen `-v` para mapear la carpeta del host con la del contenedor, permitiendo que archivos generados internamente (como imágenes `.png`) persistan en nuestra máquina física.

---

## Entorno 1: Generación de Conjunto de Julia (C++)

El código fuente implementa el algoritmo del **Conjunto de Julia**, un fractal que requiere cálculos iterativos con números complejos.

### Procedimiento Técnico:
1. **Compilación:** Se utiliza `g++` con el estándar de C++.
2. **Generación de Datos:** El ejecutable crea un archivo `julia_set.txt` con coordenadas (X, Y) y el valor de iteración (Z).
3. **Renderizado:** `gnuplot` lee el archivo de texto y aplica un mapeo de colores `pm3d` para generar la imagen final.

### Evidencias del Proceso

<table style="width:100%">
  <tr>
    <th style="text-align:center">Paso del Proceso</th>
    <th style="text-align:center">Captura de Pantalla</th>
  </tr>
  <tr>
    <td><b>1. Construcción (Build):</b> Creación de la imagen a partir del Dockerfile. Se instalan las dependencias <code>build-essential</code> y <code>gnuplot</code>.</td>
    <td align="center"><img src="contenedor-julia/evidencias/build_julia.png" width="400" alt="Docker Build Julia"></td>
  </tr>
  <tr>
    <td><b>2. Ejecución (Run):</b> El contenedor procesa el código C++. Aquí se observa la salida en terminal confirmando la creación de los datos.</td>
    <td align="center"><img src="contenedor-julia/evidencias/run_julia.png" width="400" alt="Docker Run Julia"></td>
  </tr>
  <tr>
    <td><b>3. Resultado Final:</b> Visualización del fractal generado en formato PNG, guardado automáticamente en la carpeta <code>output/</code>.</td>
    <td align="center"><img src="contenedor-julia/evidencias/resultado_fractal.png" width="300" alt="Fractal Julia PNG"></td>
  </tr>
</table>

---

## Entorno 2: Análisis Estadístico (Python) - Contenedor Adicional

Como propuesta de valor, se añadió un contenedor que utiliza **Python 3.9** para demostrar la facilidad con la que se pueden desplegar herramientas de Ciencia de Datos e IoT.

### Procedimiento Técnico:
1. **Instalación:** El Dockerfile utiliza `pip` para instalar `numpy` y `matplotlib`.
2. **Lógica:** El script `app.py` genera una señal senoidal amortiguada.
3. **Salida:** Se exporta un gráfico de alta resolución directamente a la carpeta de evidencias.

### Evidencias del Segundo Contenedor

<table style="width:100%">
  <tr>
    <th style="text-align:center">Paso del Proceso</th>
    <th style="text-align:center">Captura de Pantalla</th>
  </tr>
  <tr>
    <td><b>Ejecución de Python:</b> El contenedor corre el script y gestiona las librerías necesarias de forma aislada.</td>
    <td align="center"><img src="contenedor-julia/evidencias/ejecucion_python.png" width="400" alt="Ejecución Python"></td>
  </tr>
  <tr>
    <td><b>Gráfica Resultante:</b> Representación visual de los datos procesados en Python.</td>
    <td align="center"><img src="contenedor-julia/evidencias/resultado_python.png" width="300" alt="Gráfica Python PNG"></td>
  </tr>
</table>

---

## Configuración del Repositorio Git

Se aplicaron buenas prácticas de control de versiones:
* **Estructuración:** Separación clara entre entornos de C++ y Python.
* **Limpieza:** Uso de un archivo `.gitignore` para evitar la subida de binarios pesados o archivos temporales innecesarios.

---

### **Autor**
**Diego Aarón Cárdenas Mendoza** Estudiante de Ingeniería en Sistemas Computacionales
**ESCOM - IPN**
