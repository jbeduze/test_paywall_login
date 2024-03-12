import streamlit as st

from config import pagesetup as ps

ps.display_background_image()

#Font styling (kode mono= @import url('https://fonts.googleapis.com/css2?family=Kode+Mono:wght@400..700&display=swap'))
with open( "config/style.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)


st.write("hello world")

