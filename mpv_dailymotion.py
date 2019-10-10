# /bin/python3
"""
This script will play a video from dailymotion,
using mpv player. It gets around a problem
with ffmpeg and mpv.

The first argument
it expects is a link, the rest will be
forwarded to mpv.
"""
import os
import requests
import subprocess
import sys

args = sys.argv[1:]
if len(args) == 0:
  print("Provide a link.")
  exit(-1)

link = args[0]
"""
The first call will fail, providing url which it attempted to
access.
Failed to open .....
We capture that url.
"""
result = subprocess.run(["mpv", link], stdout=subprocess.PIPE)
filtered = list(filter(lambda x: "Failed to open" in x,
                       str(result.stdout).split("\\n")))
if len(filtered) != 1:
  print("Something went wrong")
  exit(-1)
id_ = filtered[0].find("http")
link = filtered[0][id_:-1]

"""
We get the header of the request of the captured url,
and extract the appropriate location, and modify it,
so that it works with mpv.
"""
true_link = requests.head(link).headers["Location"]
del_from = true_link.find("#cell=")
true_link = true_link[0:del_from]

os.system(" ".join(["mpv", '"' + true_link + '"'] + args[1:]))
