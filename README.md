# Video Trimmer App ✂️

A Streamlit application that allows you to trim video files with precision timing.

## Features
- Upload any video file (MP4, AVI, MOV, MKV, MPEG, WEBM)
- Set start and end times with decimal precision
- Download trimmed videos
- Cross-platform support

## Installation

### Using Python Virtual Environment
1. Install Python 3.7+ from [python.org](https://python.org)
2. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/video-trimmer.git
   cd video-trimmer
   ```
3. Create virtual environment:
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Run the app:
   ```bash
   streamlit run video_trimmer.py
   ```

## Configuration

To increase upload size limit:

1. Create a `.streamlit/config.toml` file in the project root.
2. Add the following:
   ```toml
   [server]
   maxUploadSize = 1000  # Size in MB
   ```

## Troubleshooting

- **Q: I get "FFmpeg not found" error**
  - **A:** Install FFmpeg:
    - Windows: Download from [ffmpeg.org](https://ffmpeg.org/) and add to PATH
    - macOS: `brew install ffmpeg`
    - Linux: `sudo apt install ffmpeg`

- **Q: App runs but trimming fails**
  - **A:** Try reducing the trim duration or convert the video to MP4 first.

## Directory Structure

Your project should look like this:
```
video-trimmer/
├── .streamlit/           # Config directory
│   └── config.toml       # Streamlit configuration file
├── venv/                 # Virtual environment (ignored by git)
├── app.py                # Main Streamlit application
├── requirements.txt      # Python dependencies
└── README.md             # Usage instructions (this file)
```

## License

MIT License - Free for personal and commercial use

---
