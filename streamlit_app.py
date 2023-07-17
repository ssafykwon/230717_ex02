import streamlit as st
import math

msg = "Hello World!!!"
st.write(msg)

# 터미널(git bash, cmd) : pip install streamlit (ctrl + `)

st.write(math.pi)

# 원주율
pi = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
# 반지름
r = 15

with st.echo():
    st.write('원주율 : ', pi)
    st.write('반지름 : ', r)
    st.write('원의 둘레 : ', 2 * pi * r)
    st.write('원의 넓이 : ', pi * r ** 2)

with st.echo():
    r = st.number_input("반지름 입력:")
    st.write('원주율 : ', pi)
    st.write('반지름 : ', r)
    st.write('원의 둘레 : ', 2 * pi * r)
    st.write('원의 넓이 : ', pi * r ** 2)