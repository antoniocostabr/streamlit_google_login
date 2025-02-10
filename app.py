import streamlit as st
import time
import os
import dotenv


# load the env variables / reading environment variables
dotenv.load_dotenv()
ALLOWED_DOMAIN = os.getenv('ALLOWED_DOMAIN')

st.title("App title")

if not st.experimental_user.is_logged_in:
    if st.sidebar.button("Sign in with Google", icon=":material/mail:"):
        st.login(provider="google")
else:
    if 'email' in st.experimental_user:
        
        # domain validation
        if ALLOWED_DOMAIN != "any" and (not st.experimental_user.email.endswith(ALLOWED_DOMAIN)):
            with st.spinner():
                st.write(f'User email must be from {ALLOWED_DOMAIN}')
                st.write(f'Logging out...')
                time.sleep(3)
            st.logout()
        else:
            with st.sidebar:
                st.image(st.experimental_user.get('picture'))
                st.write(f"Hello, {st.experimental_user.name}")
                st.write(f"email, {st.experimental_user.email}")
                st.write('You are logged in!')
                
                if st.button("Log out"):
                    st.logout()

            # this is where your app logic goes
            st.subheader("Main logic goes here")
            