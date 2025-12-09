import streamlit as st
import os

st.title("Video to Audio Converter")

uploaded = st.file_uploader("Upload a video file", type=["mp4", "mov", "avi", "mkv"])

if uploaded:
    st.write("Processing the video file...")
    path = uploaded.name

    base, ext = os.path.splitext(uploaded.name)
    with open(path, "wb") as f:
        f.write(uploaded.read())

    from moviepy import VideoFileClip

    clip = VideoFileClip(path)

    audio = clip.audio

    audio.write_audiofile(base + ".mp3")

    st.write("Audio extracted successfully!")

    with open(base + ".mp3", "rb") as f:
        st.download_button(
            label="Download Extracted Audio",
            data=f,
            file_name=base + ".mp3",
            mime="audio/mpeg",
        )
st.markdown(
    """
    <style>
    .custom-font {
        font-family: 'Courier New', monospace;
        font-size: 24px;
        color: #FF0000;
    }
    </style>
    <p class="custom-font">MADE WITH MOVIEPY</p>
    """,
    unsafe_allow_html=True,
)
