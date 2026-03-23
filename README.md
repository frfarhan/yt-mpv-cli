# 🎧 CLI Music Player (yt-dlp + mpv)

##  Description

A lightweight command-line music player built in Python that fetches songs using **yt-dlp** and plays them using **mpv**
. Currently supports selecting audio/video quality but contains bugs. 

---

## Features

*  Search songs directly from terminal
*  Play audio instantly using `mpv`
*  Select audio/video quality 
*  Fast and minimal — no GUI needed

---

##  Tech Stack

* **Python 3**
* **yt-dlp** (for fetching media links)
* **mpv** (for playback)
* **subprocess module** (to connect everything)

---

## Concepts Used

* Working with **APIs / scraping (yt-dlp)**
* **Subprocess communication**
* **Lists & dictionaries**
* **User input handling**
* Modular structure using multiple files

### Install dependencies

```bash
pip install yt-dlp
sudo apt install mpv   # (Linux)
```

### Select a song

* Enter your query
* Choose from displayed results
* Enjoy playback 


##  Future Improvements

- [ ] Bugs fix
- [ ] TUI using Textual
- [ ] Playlist saving (JSON)
- [ ] Loop / queue system and other functions
