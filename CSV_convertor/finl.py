import numpy as np
import pandas as pd
from yt_dlp import YoutubeDL


df=pd.read_csv("MLCampusX.csv")
# print(df["Video url"][])
video_list=np.array(df["Video url"])
pdf=pd.DataFrame(video_list)
pdf.to_csv('output.csv',index=False)


