import numpy as np
import streamlit as st
import cv2
from  PIL import Image, ImageEnhance

Output_image = 550

def main():

    imagem = Image.open('/home/rafael/Documentos/Projeto/OpenCv-Projects/Projeto1/Imagens/ef3-placeholder-image.jpg')
    st.title('Seletor de Filtros')
    st.sidebar.title('Barra Lateral')

    menu = ['Filtros','Correções de Imagem', 'Sobre']
    op = st.sidebar.selectbox('Opção', menu)

    if op == 'Filtros':

        img = st.file_uploader('Faça o upload de uma imagem', type=['jpg', 'png', 'jpeg'])

        if img is not None:
            imagem = Image.open(img)
            st.sidebar.text('Imagem Original')
            st.sidebar.image(imagem, width=200)

        filtro = st.sidebar.radio('Filtros', ['Original','Grayscale', 'Sépia', 'Blur', 'Contorno', 'Sketch'])
     
        if filtro == 'Grayscale':
            img_convert = np.array(imagem.convert('RGB'))
            gray_image = cv2.cvtColor(img_convert, cv2.COLOR_RGB2GRAY)
            st.image(gray_image, width=Output_image)
            
        elif filtro == 'Sépia':
            img_convert = np.array(imagem.convert('RGB'))
            img_convert = cv2.cvtColor(img_convert, cv2.COLOR_RGB2BGR)
            kernel = np.array([[0.272, 0.534, 0.131],
                            [0.349, 0.686, 0.168],
                            [0.393, 0.769, 0.189]])
            sepia_image = cv2.filter2D(img_convert, -1, kernel)
            st.image(sepia_image, channels='BGR', width=Output_image)
        
        elif filtro == 'Blur':
            img_convert = np.array(imagem.convert('RGB'))
            slide = st.sidebar.slider('Quantidade de Blur', 3, 81, 9, step=2)
            img_convert = cv2.cvtColor(img_convert, cv2.COLOR_RGB2BGR)
            blur_image = cv2.GaussianBlur(img_convert, (slide,slide), 0, 0)
            st.image(blur_image, channels='BGR', width=Output_image) 
        
        elif filtro == 'Contorno':
            img_convert = np.array(imagem.convert('RGB'))
            img_convert = cv2.cvtColor(img_convert, cv2.COLOR_RGB2BGR)
            blur_image = cv2.GaussianBlur(img_convert, (11,11), 0)
            canny_image = cv2.Canny(blur_image, 100, 150)
            st.image(canny_image, width=Output_image)

        elif filtro == 'Sketch':
            img_convert = np.array(imagem.convert('RGB')) 
            gray_image = cv2.cvtColor(img_convert, cv2.COLOR_RGB2GRAY)
            inv_gray = 255 - gray_image
            blur_image = cv2.GaussianBlur(inv_gray, (25,25), 0, 0)
            sketch_image = cv2.divide(gray_image, 255 - blur_image, scale=256)
            st.image(sketch_image, width=Output_image) 
        else: 
            st.image(imagem, width=Output_image)

    if op == 'Correções de Imagem':

        img = st.file_uploader('Faça o upload de uma imagem', type=['jpg', 'png', 'jpeg'])
        
        if img is not None:
            imagem = Image.open(img)
            st.sidebar.text('Imagem Original')
            st.sidebar.image(imagem, width=200)

        MImage = st.sidebar.radio('Aprimoramento da imagem', ['Original', 'Contraste', 'Brilho', 'Nitidez'])

        if MImage == 'Contraste':
            slide = st.sidebar.slider('Contraste', 0.0, 2.0, 1.0)
            enh = ImageEnhance.Contrast(imagem)
            contrast_image = enh.enhance(slide)
            st.image(contrast_image, width=Output_image)
        
        elif MImage == 'Brilho':
            slide = st.sidebar.slider('Brilho', 0.0, 5.0, 1.0)
            enh = ImageEnhance.Brightness(imagem)
            brightness_image = enh.enhance(slide)
            st.image(brightness_image, width=Output_image)

        elif MImage == 'Nitidez':
            slide = st.sidebar.slider('Nitidez', 0.0, 2.0, 1.0)
            enh = ImageEnhance.Sharpness(imagem)
            sharpness_image = enh.enhance(slide)
            st.image(sharpness_image, width=Output_image)
        else: 
            st.image(imagem, width=Output_image)
    
    elif op == 'Sobre':
        st.subheader('Projeto desenvolvido por Rafael Messias Grecco')

if __name__ == '__main__':
    main()
