# streamlit_google_login
Example of login using google account

This is a simple Streamlit app for login using google account with the 
login / logout components introduced in streamlit 1.42.0 / feb 2025


## requirements

- `streamlit==1.42.0`
- `Authlib>=1.3.2`
- `python-dotenv==1.0.1`
- `Python 3.11.11`


## secrets.toml
```toml
[auth]
redirect_uri = "http://localhost:8501/oauth2callback"
cookie_secret = "jkldhalskjgdasf7o39274jkbdjashvudasjk237898929387dkljahljkgh"

[auth.google]
client_id = "YOUR GOOGLE CLOUD AUTHENTICATION ID"
client_secret = "YOUR GOOGLE CLOUD AUTHENTICATION SECRET"
server_metadata_url = "https://accounts.google.com/.well-known/openid-configuration"
```

## enviroment variables

```sh
# list the domain allowed for login. If anyone with a google login account, specify "any"
ALLOWED_DOMAIN=YOUR_ALLOWED_DOMAIN
```

## Usage

```sh
streamlit run app.py
```