import streamlit as st

introduction = st.Page('pages/introduction.py',
                       title='Introduccion', default=True)
commands = st.Page(
    "pages/commands.py", title="Comandos", icon="🔥"
)
resources = st.Page("pages/resources.py", title="Recursos",
                    icon=":material/favorite:")

howToSave = st.Page("pages/howToSave.py", title="Como guardar los cambios",
                    icon=":material/favorite:")

# Funciona como router, desde aca se renderizan las paginas

# Con esto configuro a mano las paginas pudiendo customizar el titulo e icono
pg = st.navigation(
    {
        "": [introduction],
        # "Account": [logout_page],
        "Recursos": [resources, howToSave],
        "Commands": [commands]
    }
)