import streamlit as st

# st.markdown('# Main Page') # Queda como un titulo para todo

# Logica de logueo
# if "logged_in" not in st.session_state:
#     st.session_state.logged_in = False

# def login():
#     if st.button("Log in"):
#         st.session_state.logged_in = True
#         st.rerun()

# def logout():
#     if st.button("Log out"):
#         st.session_state.logged_in = False
#         st.rerun()

# login_page = st.Page(login, title="Log in", icon=":material/login:")
# logout_page = st.Page(logout, title="Log out", icon=":material/logout:")


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

pg.run()