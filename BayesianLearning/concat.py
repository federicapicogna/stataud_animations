from moviepy.editor import VideoFileClip, concatenate_videoclips

quality = "low"

# Set 
if quality == "low":
	res = "480p15"
else:
	res = "1080p60"

# Load your video clips
scene1 = VideoFileClip("./media/videos/Title/" + res + "/Title.mp4")
scene2 = VideoFileClip("./media/videos/Contents/" + res + "/Contents.mp4")
scene3 = VideoFileClip("./media/videos/BayesianLearningCycle/" + res + "/BayesianLearningCycle.mp4")
scene4 = VideoFileClip("./media/videos/UniformPrior/" + res + "/UniformPrior.mp4")
scene5 = VideoFileClip("./media/videos/EffectOfPrior/" + res + "/EffectOfPrior.mp4")
scene6 = VideoFileClip("./media/videos/TakeHomePoints/" + res + "/TakeHomePoints.mp4")

# Concatenate the clips
final_clip = concatenate_videoclips([scene1, scene2, scene3, scene4, scene5, scene6], method="compose")

# Write the result to a file
final_clip.write_videofile("Video.mp4", audio_codec='aac')
