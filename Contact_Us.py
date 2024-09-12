import streamlit as st


from send_email import send_email

st.header("COntact me")

with st.form(key='email_forms'):
    user_email=st.text_input("your email address")
    massage=st.text_area("your message")
    massage=user_email+"\n"+massage
    button=st.form_submit_button(label='Submit')
    if button:
        send_email(massage)