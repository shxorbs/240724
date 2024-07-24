import streamlit as st
st.title('나의 첫 웹 서비스!!!')
name = st.text_input("이름을 입력하세요: ")
menu = st.selectbox("좋아하는 음식을 선택하세요: ",['빙수','과일','밥'])
if st.button('dls사말 생성'):
  st.write(f'안녕하세요, {}님! 당신이 좋아하는 음식은 {} 입니다.'.format(name,menu))
