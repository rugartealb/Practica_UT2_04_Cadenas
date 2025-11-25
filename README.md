# Práctica 02 · Cadenas en Python (funciones + tests)

Esta práctica transforma ejercicios de **cadenas** en funciones testeables con `pytest`.

## ¿Qué debes hacer?

- En `src/` tienes **11 ejercicios**, cada uno con una función **sin implementar**.
- En `test/test_cadenas.py` tienes **todas las pruebas unitarias**.
- Tu objetivo es hacer que **TODOS los tests pasen**.

## Pasos recomendados

### 1) Crear entorno (opcional)

python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate

### 2) Instalar dependencias

pip install -r requirements.txt

### 3) Ejecutar los tests

python -m pytest

Verás muchos fallos al principio porque las funciones aún no están implementadas.

### 4) Implementar un ejercicio

Escoge un archivo dentro de src/, por ejemplo:

src/ex03_name_length.py

Lee el docstring, implementa la función y elimina el raise NotImplementedError.

### 5) Volver a probar

python -m pytest

Cuando todos los tests pasen → práctica completada ✔️
