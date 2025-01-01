import streamlit as st
import pandas as pd
import time

def divider():
    return st.markdown('---')

def H3(text):
    return st.markdown(f"### {text}")

st.title("Titulo")
st.header("Encabezado")
st.subheader('Sub Encabezado')
st.text("Texto")

divider()

st.markdown("# Titulo en markdown")

divider()

json={"a":{"1":1}, "b": [1,2,3]}
st.text("Codigo JSON")
st.json(json)

divider()
st.text("Bloque de codigo")
code="""
print("Hello World")

def func():
    return "foo"
"""
st.code(code, language="python")

st.markdown('---')
st.subheader("Tabla")

H3("Data")

tableData={"Column 1": ["A","B","C","D"], "Column 2": [1,2,3,4]}

st.json(tableData)
table=pd.DataFrame(tableData)
st.code("st.table(table)")
st.table(table)
st.code("st.dataFrame(table)")
st.dataframe(table)

divider()

H3('Audio')
st.code('st.audio(<path>)')
H3('Video')
st.code('st.video(<path>)')
H3('Image')
st.code('st.image(<path>)')

divider()
H3("Checkbox")


def handleCheckChange():
    print(st.session_state.check)

st.checkbox("Check", value=False,key="check", on_change=handleCheckChange)

st.text(st.session_state.check)

divider()
H3("Radio Button")
st.code('st.radio("Country", options=["US","Spain","Argentina"])')
radio_selection=st.radio('Country', options=['US',"Spain","Argentina"])
st.text(f'Selected: {radio_selection}')

divider()
H3("Select box")
st.code('st.selectbox("Country", options=["US","Spain","Argentina"])')
list_selection=st.selectbox('Country', options=['US',"Spain","Argentina"])
st.text(f'Selected: {list_selection}')

divider()
H3("Multi Select")
st.code('st.multiselect("Country", options=["US","Spain","Argentina"])')
multi_selection=st.multiselect('Country', options=['US',"Spain","Argentina"])
st.text(f'Selected: {multi_selection}')

divider()
H3("Upload File")
st.code("st.file_uploader('Upload an image', type=['png','jpg'])")
image_file=st.file_uploader('Upload an image', type=['png','jpg'])
if image_file is not None:
    st.image(image_file)

divider()
H3("Upload Multiple Files")
st.code("st.file_uploader('Upload an image', type=['png','jpg'], accept_multiple_files=True)")
images=st.file_uploader('Upload an image', type=['png','jpg'], accept_multiple_files=True)
if image_file is not None:
    for image in images:
        st.image(image_file)

divider()
H3("Slider")
st.code('st.slider("Slider", min_value=12, max_value=78,value=54)')
slider_value=st.slider('Slider', min_value=12, max_value=78,value=54)
st.text(f'Selected: {slider_value}')

divider()
H3('Text Input')
st.code('st.text_input("Escriba algo")')
input_text_value=st.text_input('Escriba algo')
st.text(f'Selected: {input_text_value}')

divider()
H3('Date Input')
st.code('st.date_input("Selecciona una fecha")')
input_date_value=st.date_input('Selecciona una fecha')
st.text(f'Selected: {input_date_value}')

divider()
H3('Time Input')
st.code('st.time_input("Selecciona una fecha")')
input_time_value=st.time_input('Selecciona un valor')
st.text(f'Selected: {input_time_value}')

divider()
H3('Progress bar')
st.code('''progress_bar=st.progress(0)
i=0
while i < 11:
    if i==10:
        i=0
    i+=1
    progress_bar.progress((i)*10)
    time.sleep(1)
''')
progress_bar=st.progress(0)
i=0
while i < 11:
    if i==10:
        i=0
    i+=1
    progress_bar.progress((i)*10)
    time.sleep(1)
