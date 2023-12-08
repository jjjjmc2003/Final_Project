import streamlit as st

def welcome_page():
    st.title("Welcome page 🎈")
    st.image('https://media4.giphy.com/media/fvA1ieS8rEV8Y/giphy.gif?cid=ecf05e47qaufxlgp66ki233fhoxpwp28phos9aj3rvk4vj2m&ep=v1_gifs_search&rid=giphy.gif&ct=g',width=600)
    st.markdown(':blue[To customize your game settings please refer to the Settings Tab, Enjoy]')
    st.markdown('\n'':red[To see some dope ping pong shots please refer to the tab labeled Cool Ping Pong Shots]')


def settings():
    st.title("Settings")
    st.write("Adjust your slider's, opponent's slider, or ball color here")
    player_color = st.color_picker('Player Color', '#ff5733')
    configurations = {
        "player_color": player_color
    }




def ping_pong():
    st.title('Cool Ping Pong Shots🔥🔥🔥')
    st.video("https://www.youtube.com/watch?v=CABqlL02I28")


# Sidebar navigation
page = st.sidebar.selectbox("Go to", ("Welcome Page", "Settings", "Cool Ping Pong Shots"))

if page == "Welcome Page":
    welcome_page()
elif page == "Settings":
    settings()
elif page == "Cool Ping Pong Shots":
    ping_pong()
