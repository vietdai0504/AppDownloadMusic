from cx_Freeze import setup, Executable

executables = [Executable("gui_download.py", base="gui", icon="icon.ico")]

setup(
    name="Download video and audio",
    version="0.1",
    description="App can download video and music from youtube, tiktok, facebook",
    executables=executables,
    includes=["tkinter", "pytube", "yt_dlp", "pydub"],
    options={"build_exe": {"packages": ["tkinter", "pytube", "yt_dlp", "pydub"], 
                           "include_files": ["icon.ico"]}}  
)