from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.coqui import CoquiService

# SCENE 00: TITLE CARD ##########################################################
class Title(VoiceoverScene):
	def construct(self):
		self.set_speech_service(CoquiService(transcription_model='base'))

		# Title
		title = Text("Statistical Auditing", font_size = 75)
		
		with self.voiceover(text="Hi there.") as tracker:
			self.play(Write(title), run_time = tracker.duration)

		# Subtitle
		subtitle = Text("Bayesian Learning in Audit Sampling", font_size = 40)
		subtitle.next_to(title, DOWN)

		with self.voiceover("In this clip I will explain how to plan and evaluate a statistical audit sample using Bayesian statistics.") as tracker:
			self.play(Write(subtitle))

		# Clear the scene
		self.play(
			FadeOut(title),
			FadeOut(subtitle)
		)