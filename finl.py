import numpy as np
import pandas as pd
from yt_dlp import YoutubeDL
import time
import csv

df=pd.read_csv("DBMS.csv")
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

# i=103
# with YoutubeDL(ydl_opts) as ydl:
    
#     i=i+1

#     while True:
#         try:
#             print(f"Downloading {i}")
#             ydl.download([video_list[i]])
#             break

#         except Exception as e:

#             print(e)
#             print("Retrying in 30 seconds...")
#             time.sleep(30)