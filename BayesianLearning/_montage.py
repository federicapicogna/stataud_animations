import os
import subprocess
from moviepy.editor import VideoFileClip, concatenate_videoclips

# Get the name of the current script
current_script = os.path.basename(__file__)

# Iterate over all files in the current directory
scenelist = [ ]
for filename in os.listdir('.'):
    # Check if the file is a Python file and not the current script
    if filename.endswith('.py') and filename != current_script:
        # Construct the command
        cmd = f"manim {filename} --disable_caching"
        # Run the command
        subprocess.run(cmd, shell = True)
        # Add the scene to the scenelist
        file_root, _ = os.path.splitext(filename)
        scenelist.append(VideoFileClip("./media/videos/" + file_root + "/1080p60/" + file_root + ".mp4"))

# Concatenate the clips in the list
final_clip = concatenate_videoclips(scenelist, method = "compose")

# Write the result to a file
final_clip.write_videofile("Video.mp4", audio_codec = 'aac')
