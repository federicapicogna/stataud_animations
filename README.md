# Statistical Auditing Animations

This repository contains mathematical animations illustrating concepts in statistical auditing made using [manim](https://github.com/ManimCommunity/manim), which is an animation engine for explanatory math videos.

To render the videos on your own computer, make sure that you have a working version of `manim` for Python 3.12. See [this page](https://docs.manim.community/en/stable/installation.html) for install instructions. We also use [manim voiceover](https://voiceover.manim.community/en/stable/index.html) (with [coqui-tts](https://github.com/idiap/coqui-ai-TTS/tree/dev#installation) for Python 3.12) for adding AI generated voiceovers, so make sure to install that as well.

### Developing a scene

If you have a working setup and a Python file containing a scene named `NameOfScene.py`, open a terminal in the project folder and type the following command. Once executed, this will render the scene in low quality (`-ql`) and will preview it in the default video player when it is finished (`-p`).

```
manim -ql -p NameOfScene.py --disable_caching
```

### Rendering a full video in high quality

Concatenating all high quality scenes into a full movie can be done using [moviepy](https://www.google.com/search?client=safari&rls=en&q=moviepy&ie=UTF-8&oe=UTF-8). To do so, open a terminal in the project folder and simply type the following command.

```
python3 _montage.py
```

The script will take care of everyting and produce an `.mp4` file called `Video.mp4`. Note that it is important that your files start with `[scene number]_SceneName` so that the script can place them in the right order. For example, the title card is typically named `00_Title.py` and the next scene `01_SceneName.py`.
