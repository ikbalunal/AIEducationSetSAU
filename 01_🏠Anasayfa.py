# -*- coding:utf-8 -*-
# @Filename:    01_🏠Anasayfa.py
# @Author:      Ikbal Unal
# @Time:        12/27/2023 10:12 PM
# @GitHub:      https://github.com/ikbalunal
# @Email:       eikbalunal@gmail.com

import streamlit as st
from PIL import Image
import requests
from io import BytesIO


st.set_page_config(
    page_title="SAU AI Education",
    page_icon="🧊",
    layout="centered",
    menu_items={"Get Help": "https://github.com/ikbalunal", "Report a bug": None, "About": None},
)

hide_img_fs = '''
    <style>
    button[title="View fullscreen"]{
        visibility: hidden;}
    </style>
    '''

st.markdown(hide_img_fs, unsafe_allow_html=True)

# Sakarya Üniversitesi logosunu çekme
url = "https://www.sakarya.edu.tr/assets/img/sau-logo-dikey.jpg"
response = requests.get(url)
img = Image.open(BytesIO(response.content))

# Streamlit sütunu oluşturma
col = st.columns(1)

# Resmi HTML ile ortalamak için
with col[0]:
    st.markdown(f"<div style='text-align: center;'><img src='{url}' width='200'></div>", unsafe_allow_html=True)



st.markdown("""
#
# :blue[Yapay Zekaya Giriş Dersi İnteraktif Eğitim Portalı]
\n\n
""")

st.markdown("""
## 
### :arrow_forward: Proje Amaç ve Kapsamı

 - Bu eğitim portalı, Sakarya Üniversitesi Bilişim Sistemleri Mühendisliği Bölümü tarafından düzenlenen "Yapay Zekaya Giriş" dersi temelinde interaktif öğrenme içeriklerini sunmak için hazırlanmıştır.
 - Proje, **ISE401 Bilişim Sistemleri Mühendisliği Tasarımı** kapsamında; \n\n Sayın ``` Prof. Dr. İsmail Hakkı Cedimoğlu ``` Danışmanlığında, Bilişim Sistemleri Mühendisliği 4. Sınıf öğrencisi ``` A.F. İkbal Ünal ``` tarafından hazırlanmıştır.
 - Sakarya Üniversitesi Resmi sitesi için [tıklayınız](https://www.sakarya.edu.tr/).
 - Bu eğitim içeriği, [Streamlit](https://streamlit.io) ile oluşturulmuştur.

""")



