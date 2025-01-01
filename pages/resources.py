import streamlit as st
st.markdown('# Recursos')

st.markdown('[Paginado y navegacion](https://docs.streamlit.io/develop/concepts/multipage-apps/page-and-navigation)')
st.text('Solo se puede un st.navigation por ejecucion de app, es el enrutador general')
st.code ('''
   import streamlit as st

create_page = st.Page("create.py", title="Create entry", icon=":material/add_circle:")
delete_page = st.Page("delete.py", title="Delete entry", icon=":material/delete:")

pg = st.navigation([create_page, delete_page])
st.set_page_config(page_title="Data manager", page_icon=":material/edit:")
pg.run()          
''')

st.markdown('''
- [Multi App Demo](https://docs.streamlit.io/get-started/tutorials/create-a-multipage-app)
- [Biblioteca de componentes externos](https://streamlit.io/components)
- [Logica de Login/Navbar](https://docs.streamlit.io/develop/concepts/multipage-apps/page-and-navigation#dynamically-changing-the-available-pages)
''')

