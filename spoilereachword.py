import streamlit as st

def spoilerit(anan):
    inp = list(anan)
    endinp = ""
    for inpnum in inp:
        endinp = "{}||{}||".format(endinp, inpnum)
    return endinp

text = st.text_input("Text:")

if st.button('Spoiler it!'):
    st.write(spoilerit(text))