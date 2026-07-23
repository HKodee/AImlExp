import numpy as np
import pandas as pd
from yt_dlp import YoutubeDL
import time
import csv

df=pd.read_csv("MLCampusX.csv")
# print(df["Video url"][])
video_list=np.array(df["Video url"])
pdf=pd.DataFrame(video_list)
pdf.to_csv('output.csv',index=False)

# ydl_opts = {
#     "format": "bestvideo+bestaudio/best",
#     "merge_output_format": "mp4",
#     "continuedl": True,
#     "download_archive": "downloaded.txt",
#     "overwrites": False,
# }

