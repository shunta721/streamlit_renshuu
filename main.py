import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time


st.title("python練習")

st.write ("プログレスバーの表示")
'Start!!'

latest_iteration=st.empty()
bar=st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.01)



left_column,right_column=st.columns(2)
if left_column.button("右カラムに文字を表示"):
    right_column.write("ここは右カラム")

expander=st.expander("問い合わせ")
expander.text_input("問い合わせ内容を書いてください")



text=st.text_input("あなたの趣味は何ですか")
"あなたの趣味:",text,"です"

condition=st.slider("あなたの今の調子は?",0,100,0)
'コンディション;',condition,


if st.checkbox("show image"):
    img=Image.open("hana.jpg")
    st.image(img,caption="ハナはかわいい",use_column_width=True)


#option=st.selectbox('好きな数字を教えてください',
#            list(range(1,11)) 
#)

#st.write('あなたの好きな数字は',option,"です")
