import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from glob import glob
import os
import openpyxl
import qrcode
from PIL import Image, ImageDraw, ImageFont

st.title('qrcode生成')
url = st.text_input('QRコードを生成したいURL:')
if st.button('QRコード生成'):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    def add_margin(pil_img, top, right, bottom, left, color):
        width, height = pil_img.size
        new_width = width + right + left
        new_height = height + top + bottom
        result = Image.new(pil_img.mode, (new_width, new_height), color)
        result.paste(pil_img, (left, top))
        return result
    top = 0
    right = 0
    left = 0
    bottom = 40
    img_new = add_margin(img, top, right, bottom, left, '#ffffff')
    new_w,new_h = img_new.size
    img_new.save('qrcode.png')
    img1 = Image.open(img_new)

    draw = ImageDraw.Draw(img_new) 
    font = ImageFont.truetype('./ipaexm.ttf',35)
    ceter_w,bottom_h = new_w/2,(new_h - 45)
    draw.text((ceter_w,bottom_h), 'ダイエットの秘密', font=font,anchor='mm', fill='#000000') 
    st.image(img1)
