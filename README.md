# Statistical Auditing Animations

This repository contains mathematical animations illustrating concepts in statistical auditing made using [manim](https://github.com/ManimCommunity/manim), which is an animation engine for explanatory math videos. We also use [manim voiceover](https://voiceover.manim.community/en/stable/index.html) for adding AI generated voiceovers, so make sure to install that as well.

### Rendering an individual scene

To render the videos on your own computer, make sure that you have a working version of `manim`. See [this page](https://docs.manim.community/en/stable/installation.html) for install instructions.

If you have a working setup, open a terminal in the project folder and type the following command. It will prompt you to choose which scene you want to render. Once specified, this will render the scene using low quality (`-ql`) and will preview it when it is done (`-p`). You should remove the `-ql` flag when rednering the final version of the video.

```
python3 -m manim -ql -p scene.py --disable_caching
```

### Rendering a full video

Open a terminal in the project folder and type the following command.

```
python3 concat.py
```
