# Softesting
Robot automatizado con Selenium que llena el [formulario de registro](https://qa-practice.netlify.app/bugs-form) con los datos del aspirante y lo envía.

## Información del aspirante
- **Nombre:** Juliana Alarcón

## Herramientas
- **Lenguaje:** Python 3
- **IDE:** PyCharm
- **Navegador:** Google Chrome

## ¿Qué hace el robot?
El archivo `main.py`:
1. Abre Chrome en la página del formulario.
2. Llena nombre, apellido, teléfono, país, correo y contraseña.
3. Hace clic en **Register** para enviar el formulario.
4. Verifica que aparezca el mensaje *"Successfully registered the following information"* y cierra el navegador.

## Instalación
```bash
git clone https://github.com/julianagala/Softesting.git
cd Softesting
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
En Windows, el entorno se activa con `.venv\Scripts\activate`.

## Ejecución
pytest:
```bash
pytest
```
