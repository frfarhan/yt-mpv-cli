import query
import subprocess
query.chosen = int(input("What to play:")) - 1
query.to_play = query.results[query.chosen]["url"]
print("Now playing:", query.results[query.chosen]["title"])
if query.mode == 1:
    direct_url = subprocess.check_output(["yt-dlp", "-f", aformat, "-g", query.to_play], text = True).strip()
    if query.aqual == 1:
        aformat = "bestaudio"
    elif query.aqual == 2:
        aformat = "bestaudio[abr<=128]"
    else:
        pass
elif query.mode == 2:
    direct_url = query.to_play
    if query.bitrate == 1:
        mpv_flag = "--ytdl-format=bestvideo[height<=1080]+bestaudio"
    elif query.bitrate == 2:
        mpv_flag = "--ytdl-format=bestvideo[height<=720]+bestaudio"
    elif query.bitrate == 3:
        mpv_flag = "--ytdl-format=bestvideo[height<=360]+bestaudio"
    else:
        mpv_flag= "--ytdl-format=bestvideo+bestaudio"
        
subprocess.run(["mpv", mpv_flag, direct_url])
