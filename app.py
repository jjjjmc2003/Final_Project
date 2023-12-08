import streamlit as st
import json

def welcome_page():
    st.title("🎈🎈Welcome page🎈🎈")
    st.image('https://media4.giphy.com/media/fvA1ieS8rEV8Y/giphy.gif?cid=ecf05e47qaufxlgp66ki233fhoxpwp28phos9aj3rvk4vj2m&ep=v1_gifs_search&rid=giphy.gif&ct=g',width=600)
    st.write('TABS LOCATED AT TOP LEFT OF SCREEN: LABELED GO TO')
    st.markdown(':blue[To customize your game settings please refer to the Settings Tab, Enjoy]')
    st.markdown('\n'':red[To see some dope ping pong shots please refer to the tab labeled Cool Ping Pong Shots]')



def settings():
    st.title("Settings")

    st.write("Adjust your slider's, opponent's slider, or ball color here:")

    player_color = st.color_picker('Player Color', '#ff5733')
    ball_color = st.color_picker('Ball Color', '#ff5733')
    opponent_color = st.color_picker('Opponent Color', '#ff5733')

    st.write('\n')

    st.write(':red[To Increase Difficulty...]')

    player_speed = st.slider("Add Weight to Your Slider", min_value=0, max_value=5, value=0)
    st.write(':blue[Note: adding weight to slider drags your slider down. The more weight you add the harder it pulls your slider. So by adding weight you have to fight your chosen weight as you play the game]')

    opponent_speed = st.slider("Increase Opponent's Speed", min_value=1, max_value=20, value=7)
    st.write(":blue[Note: Opponent's Natural Speed is 7 so if you go lower it will be slower, higher than 7 it will be faster]")

    opponent_score = st.slider("Increase Opponent's Score", min_value=0, max_value=2, value = 0)
    st.write(":blue[Note: Winner is first to 3 so if you make start your opponent at 2 you better be good]")

    configurations = {
        "player_color": player_color,
        "ball_color": ball_color,
        "opponent_color": opponent_color,
        "player_speed": player_speed,
        "opponent_speed": opponent_speed,
        "opponent_score": opponent_score
    }

    with open("configurations.json", "w") as json_file:
        json.dump(configurations, json_file)


def ping_pong():
    st.title('Cool Ping Pong Shots🔥🔥🔥')
    st.video("https://www.youtube.com/watch?v=CABqlL02I28")


page = st.sidebar.selectbox("Go to", ("Welcome Page", "Settings", "Cool Ping Pong Shots"))

if page == "Welcome Page":
    welcome_page()
elif page == "Settings":
    settings()
elif page == "Cool Ping Pong Shots":
    ping_pong()

