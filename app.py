import streamlit as st
from rembg import remove
from PIL import Image
from io import BytesIO
import base64

st.set_page_config(layout="wide", page_title="Removedor de Fondo")

st.write("## Remueve el fondo de tus fotos")
st.write(
    ":dog: Intente cargar una imagen para ver cómo se elimina el fondo mágicamente. Se pueden descargar imágenes de calidad completa desde la barra lateral. :grin:"
)
st.sidebar.write("## Subir y descargar :gear:")

MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB

# Descargar la imagen corregida
def convert_image(img):
    buf = BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()
    return byte_im


def fix_image(upload):
    image = Image.open(upload)
    col1.write("Imagen Original :camera:")
    col1.image(image)

    fixed = remove(image)
    col2.write("Imagen fija :wrench:")
    col2.image(fixed)
    st.sidebar.markdown("\n")
    st.sidebar.download_button("Descargar imagen corregida", convert_image(fixed), "fixed.png", "image/png")


col1, col2 = st.columns(2)
my_upload = st.sidebar.file_uploader("Subir una imagen", type=["png", "jpg", "jpeg"])

if my_upload is not None:
    if my_upload.size > MAX_FILE_SIZE:
        st.error("El archivo cargado es demasiado grande. Cargue una imagen de menos de 5 MB..")
    else:
        fix_image(upload=my_upload)
else:
    fix_image("./mariposa.jpg")