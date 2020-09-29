# Simple BBB Downloader

This file automates downloads from Big Blue Button.

_Note: This was made to download one particular video. 
It has not yet been tested anywhere else, nor does it work on videos 
without webcam **and** presentation enabled._ 

## Prerequisites 
This code-snippet depends on:
```
python3 
wget
ffmpeg
```

On debian run
```
sudo apt update && sudo apt install python3 wget ffmpeg -y 
```

## Usage
Download repository:
```
git clone https://github.com/joschahenningsen/simple-bbb-downloader.git ~/bbb-dl
cd ~/bbb-dl
python3 bbbdl.py https://my.bbb.node/playback/presentation/2.0/playback.html?meetingId=ABC123DEF
```

If you feel fancy add an alias to `~/.bashrc` or `~/.zshrc`:

```
alias bbbdl='python3 ~/bbb-dl/bbbdl.py'
```

Now you can simply run 

```
bbbdl https://my.bbb.node/playback/presentation/2.0/playback.html?meetingId=ABC123DEF
```

## Outlook
I might be able to extend features to other kinds of videos like group conferences,
videos without webcam and so on as soon as my exams are done.