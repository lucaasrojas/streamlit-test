import streamlit as st

st.markdown('# Introduccion')

st.text("Streamlit is an open-source Python framework for data scientists and AI/ML engineers to deliver dynamic data apps with only a few lines of code. Build and deploy powerful data apps in minutes. Let's get started!")

st.markdown('''
Primero instalar [VSCode](https://code.visualstudio.com/) y [Python](https://www.python.org/downloads/).
Abrir VSCode, en la barra superior clickear `Terminal` y en el menu seleccionar `Nueva Terminal`. Se va abrir un bloque en la parte inferior
''')

st.image('images/open_terminal_step.png')

st.markdown('''
En la terminal escribir `pip install streamlit` y apretar enter. Esto instalara la libreria de Streamlit

Una vez terminado el proceso de instalacion, crear un nuevo archivo, por ejemplo `main.py`
            
Todo script de Streamlit debe importar la libreria de la siguiente forma en la parte superior
            
`import streamlit as st`

(La parte de `as st` es para asignarle un alias y no tener que escribir todo el tiempo streamlit, se puede poner otro nombre)
            
Luego agregar el comando `st.text("Hello World")`. 
''')
st.image('images/first_code_lines.png')
st.markdown('''
Guardar el archivo y en la terminal de VSCode ejecutar `streamlit run main.py` en lugar de main.py usar el nombre del archivo.
Esto creara el host e iniciara una instancia de la app local para poder probarlo en la direccion http://localhost:8501
''')
st.image('images/local_test.png')