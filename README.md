# Statistical Auditing Animations

This repository contains mathematical animations illustrating concepts in statistical auditing made using [manim](https://github.com/ManimCommunity/manim), which is an animation engine for explanatory math videos.

### Rendering an individual scene

To render the videos on your own computer, make sure that you have a working version of `manim` for Python 3.12. See [this page](https://docs.manim.community/en/stable/installation.html) for install instructions. We also use [manim voiceover](https://voiceover.manim.community/en/stable/index.html) (with [coqui-tts](https://github.com/idiap/coqui-ai-TTS/tree/dev#installation) for Python 3.12) for adding AI generated voiceovers, so make sure to install that as well.

If you have a working setup, open a terminal in the project folder and type the following command. It will prompt you to choose which scene you want to render. Once specified, this will render the scene using low quality (`-ql`) and will preview it when it is done (`-p`).

```
manim -ql -p NameOfTheSceneFile.py --disable_caching
```

You should remove the `-ql` flag when rednering the final version of the video to render in high quality.

### Rendering a full video

Concatenating the scenes into a full movie can be done using [moviepy](https://www.google.com/search?client=safari&rls=en&q=moviepy&ie=UTF-8&oe=UTF-8). To do so, open a terminal in the project folder and type the following command.

```
python3 _montage_.py
```
