mkdir -p ~/.streamlit/

echo "\
[general]\n\
email = \"jordan.lee.harrs@icloud.com\"\n\
" > ~/.streamlit/credentials.toml

echo "\
[server]\n\
headless = fasle\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/credentials.toml

echo "\
[theme]\n\
headless = fasle\n\
enableCORS=false\n\
port = $PORT\n\
" > ~/.streamlit/credentials.tomls3
