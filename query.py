import subprocess
query = input("What do you want to listen:")
mode = int(input("Mode?:\n1) audio\n2) video\n"))
if mode == 2:
    bitrate = int(input("select video quality:\n1)1080p\n2)720p\n3)480p\n"))
elif mode == 1:
    aqual = int(input("select audio quality:\n1)high\n2)low\n"))
else:
    pass
stream = subprocess.check_output(["yt-dlp", "--print", "%(title)s | %(webpage_url)s",  "ytsearch5:"+query], text = True)
results = []
for index, trm in enumerate(stream.splitlines()):
    title, url = trm.rsplit(" | ", 1)
    print(index + 1, title)
    results.append({"title":title, "url":url})

