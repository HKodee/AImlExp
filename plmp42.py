import yt_dlp

url = "https://www.youtube.com/watch?v=CrLRFn5O_F8&list=PLYwpaL_SFmcArHtWmbs_vXX6soTK3WEJw"

ydl_opts = {
    'format': '136+140/18',
    'merge_output_format': 'mp4',
    'playliststart': 8,
    'ignoreerrors': True,
    'retries': 10,
    'fragment_retries': 10,
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])