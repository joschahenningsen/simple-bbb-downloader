import os
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET
import shutil


def download(bbb):
    # extract bbb domain including protocol
    rex = re.search(r"https://([a-z,.]*)/", bbb)
    baseurl = rex[0]

    # extract meeting id
    rex = re.search(r"\?meetingId=(.*)", bbb)
    meetingId = rex[0][11:]

    # extract metadata for filename
    m_url = baseurl + "presentation/" + meetingId + "/metadata.xml"
    m_data = urllib.request.urlopen(m_url).read()
    root = ET.fromstring(m_data)
    m_name = root.find("meta").find("meetingName").text + ".mp4"
    print("Downloading to " + m_name + ".mp4")
    m_name = str.replace(m_name, " ", "\\ ")

    # extract video and audio source
    v_url = baseurl + "presentation/" + meetingId + "/deskshare/deskshare.mp4"
    a_url = baseurl + "presentation/" + meetingId + "/video/webcams.mp4"

    # download presentation and webcam
    os.system("wget " + v_url + " -O v.mp4")
    os.system("wget " + a_url + " -O a.mp4")

    # merge presentations video and webcams audio
    os.system("ffmpeg -i v.mp4 -i a.mp4 -c:v copy -c:a aac -map 0:v:0 -map 1:a:0 " + m_name)

    # remove auxiliary files
    os.remove("v.mp4")
    os.remove("a.mp4")

if __name__ == "__main__":
    # check for dependencies:
    if not shutil.which("wget"):
        print("wget not installed. Exiting")
    elif not shutil.which("ffmpeg"):
        print("ffmpeg not installed. Exiting")
    elif len(sys.argv) != 2:
        print("usage: python3 bbb.py"
              "https://mybbb.example.com/playback/presentation/2.0/playback.html?meetingId=XXX123YYY")
    else:
        download(sys.argv[1])
