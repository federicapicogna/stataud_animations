import os
import subprocess
from moviepy.editor import VideoFileClip, concatenate_videoclips

# Get the name of the current script
current_script = os.path.basename(__file__)

# Collect all Python filenames except the current script
filenames = [filename for filename in os.listdir('.') if filename.endswith('.py') and filename != current_script]

# Sort the filenames alphabetically (1_ is first, 2_ is second, etc.)
filenames.sort()

# Initialize the scenelist
scenelist = []

# Iterate over the sorted filenames
for filename in filenames:
    # Construct the command
    cmd = f"manim {filename} --disable_caching"
    # Run the command
    subprocess.run(cmd, shell=True)
    # Add the scene to the scenelist
    file_root, _ = os.path.splitext(filename)
    clip_name = file_root.split('_', 1)[-1]
    scenelist.append(VideoFileClip(f"./media/videos/{file_root}/1080p60/{clip_name}.mp4"))

# Concatenate the clips in the list
final_clip = concatenate_videoclips(scenelist, method = "chain")

# Write the result to a file
final_clip.write_videofile("Video.mp4", codec = "mpeg4", audio_codec = 'libfdk_aac')
