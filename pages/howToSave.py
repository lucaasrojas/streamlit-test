import streamlit as st
image_prefix="images/howToSave/"

st.markdown('''

# Como guardar los cambios?
Cuando hayamos hecho un cambio vamos a poder ver en la barra lateral izquierda el siguiente icono. El numero que tenga va variar en base a la cantidad de archivos que hayamos cambiado.
 ''')
st.image(f"{image_prefix}changes_icon.png")

st.markdown('''
Al hacer click, se va a abrir el controlador de cambios 
''')

st.image(f"{image_prefix}changes_list.png")
st.text("Al posicion el raton a la altura del texto Changes va aparecer una serie de iconos, al hacer click en le icono de mas '+' va a seleccionar todos los archivos para poder generar un 'commit' ")
st.image(f"{image_prefix}changes_list_plus_sign.png")
st.text("Una vez hecho esto, colocamos un mensaje corto explicando los cambios que se hicieron en el campo de texto que esta arriba y confirmamos haciendo click en el boton que dice 'Commit' ")
st.image(f"{image_prefix}staged_changes_message.png")
st.text("Generado el commit, vamos a ver que la lista desaparece y el boton cambia a 'Sync Changes'")
st.image(f"{image_prefix}changes_ready_push.png")
st.text('Al clickearlo va a enviar los cambios al repositorio. Luedo de unos minutos el sitio va estar actualizado')