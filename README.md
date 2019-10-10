# mpv_dailymotion
Stream videos from dailymotion using mpv

**mpv_dailymotion** solves the problem of *ffmpeg* and *mpv* failing to stream videos from *dailymotion*. 

## Usage

```
mpv_dailymotion.py <link to video> <other> <args> <to forward> <to mpv>
``` 

### Example
Play the *video at the link*, but *flip the image* horizontally and set *playback speed to `0.9`.
```
python mpv_dailymotion.py https://www.dailymotion.com/video/x6anit1 --vf="hflip" -speed 0.9
```
