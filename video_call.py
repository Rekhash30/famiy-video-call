import streamlit as st
from streamlit_webrtc import webrtc_streamer, RTCConfiguration

st.set_page_config(page_title="Family Video Call", page_icon="📹")
st.title("📹 Family Video Call")

# WebRTC configuration (STUN server)
RTC_CONFIGURATION = RTCConfiguration(
    {
        "iceServers": [
            {"urls": ["stun:stun.l.google.com:19302"]}
        ]
    }
)

# Allowed family members (optional but recommended)
ALLOWED_USERS = ["Rekha", "Brother", "Mom", "Dad"]

username = st.text_input("Enter your name")

ROOM_NAME = "rekha_family_private_room"  # keep this secret

if username:
    if username not in ALLOWED_USERS:
        st.error("❌ Access denied. Family members only.")
        st.stop()

    st.success(f"Welcome {username} 👋")

    webrtc_streamer(
        key=ROOM_NAME,
        rtc_configuration=RTC_CONFIGURATION,
        media_stream_constraints={
            "video": True,
            "audio": True,
        },
        async_processing=True,
    )
else:
    st.info("Please enter your name to start the video call")
