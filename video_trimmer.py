import streamlit as st
# from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.editor import VideoFileClip
import tempfile
import os

def cut_video(input_path, output_path, start_time, end_time):
    """Trim video segment using MoviePy"""
    with VideoFileClip(input_path) as video:
        clip = video.subclip(start_time, end_time)
        clip.write_videofile(output_path)

# Set page metadata
st.set_page_config(
    page_title="Video Trimmer App ✂️",  # Updated title
    page_icon="✂️",  # Optional: Add an icon
    layout="centered",  # Optional: Set layout
    initial_sidebar_state="auto"  # Optional: Control sidebar state
)

st.title("Video Trimmer App ✂️")

# File uploader with supported formats
uploaded_file = st.file_uploader("Select a video file", 
                               type=["mp4", "avi", "mov", "mkv", "mpeg", "webm"])

if uploaded_file is not None:
    # Create temporary files
    with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(uploaded_file.name)[1]) as input_temp:
        input_temp.write(uploaded_file.getbuffer())
        input_path = input_temp.name

    try:
        with VideoFileClip(input_path) as video:
            duration = int(video.duration)
            st.success(f"Loaded: {uploaded_file.name} ({duration}s)")

            # Time selection
            col1, col2 = st.columns(2)
            with col1:
                start_time = st.number_input("Start time (seconds)", 
                                           value=0, 
                                           min_value=0, 
                                           max_value=duration-1)
            with col2:
                end_time = st.number_input("End time (seconds)", 
                                         value=min(10, duration), 
                                         min_value=1, 
                                         max_value=duration)

            st.write(f"Trim duration: {end_time - start_time}s")

            # Output filename
            output_filename = st.text_input("Save as", 
                                          value=f"trimmed_{uploaded_file.name}")

            if st.button("Trim Video"):
                with tempfile.NamedTemporaryFile(delete=False, suffix=os.path.splitext(output_filename)[1]) as output_temp:
                    output_path = output_temp.name

                with st.spinner("Trimming..."):
                    cut_video(input_path, output_path, start_time, end_time)

                # Show download button
                with open(output_path, "rb") as f:
                    st.download_button(
                        "Download Trimmed Video",
                        f.read(),
                        file_name=output_filename,
                        mime="video/mp4"
                    )
                
                # Cleanup temporary files
                os.unlink(output_path)
                
    except Exception as e:
        st.error(f"Error: {str(e)}")
    finally:
        os.unlink(input_path)