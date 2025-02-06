import streamlit as st

st.markdown('''

# Como guardar los cambios?
Cuando hayamos hecho un cambio vamos a poder ver en la barra lateral izquierda el siguiente icono. El numero que tenga va variar en base a la cantidad de archivos que hayamos cambiado.
 ''')
st.image("images/Screenshot 2025-02-06 195109.png")

st.markdown('''
Al hacer click, se va a abrir el controlador de cambios 
''')

st.image("images/Screenshot 2025-02-06 195355.png")
st.text("Al posicion el raton a la altura del texto Changes va aparecer una serie de iconos, al hacer click en le icono de mas '+' va a seleccionar todos los archivos para poder generar un 'commit' ")
st.image("images/Screenshot 2025-02-06 195436.png")
st.text("Una vez hecho esto, colocamos un mensaje corto explicando los cambios que se hicieron en el campo de texto que esta arriba y confirmamos haciendo click en el boton que dice 'Commit' ")
st.image("images/Screenshot 2025-02-06 195824.png")
st.text("Generado el commit, vamos a ver que la lista desaparece y el boton cambia a 'Sync Changes'")
st.image('images/Screenshot 2025-02-06 200131.png')
st.text('Al clickearlo va a enviar los cambios al repositorio')