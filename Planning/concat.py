from moviepy.editor import VideoFileClip, concatenate_videoclips

# Load your video clips
scene1 = VideoFileClip("./media/videos/scene/480p15/Title.mp4")
scene2 = VideoFileClip("./media/videos/scene/480p15/Contents.mp4")
scene3 = VideoFileClip("./media/videos/scene/480p15/BayesianUpdatingCycle.mp4")
scene4 = VideoFileClip("./media/videos/scene/480p15/UniformPrior.mp4")
scene5 = VideoFileClip("./media/videos/scene/480p15/EffectOfPrior.mp4")
scene6 = VideoFileClip("./media/videos/scene/480p15/TakeHomePoints.mp4")

# Concatenate the clips
final_clip = concatenate_videoclips([scene1, scene2, scene3, scene4, scene5, scene6], method="compose")

# Write the result to a file
final_clip.write_videofile("Video.mp4", audio_codec='aac')
