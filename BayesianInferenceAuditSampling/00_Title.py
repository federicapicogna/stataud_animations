from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.coqui import CoquiService

class Title(VoiceoverScene):
	def construct(self):
		self.set_speech_service(CoquiService(transcription_model = 'base', model_name = "tts_models/multilingual/multi-dataset/xtts_v2"))

		# Title
		title = Text("Statistical Auditing", font_size = 75)
		
		with self.voiceover("Welcome.") as tracker:
			self.play(Write(title), run_time = tracker.duration)

		# Subtitle
		subtitle = Text("Bayesian Inference for Audit Sampling", font_size = 40)
		subtitle.next_to(title, DOWN)

		with self.voiceover("In this clip I will explain how to plan and evaluate a statistical audit sample using Bayesian statistics.") as tracker:
			self.play(Write(subtitle))

		# Clear the scene
		self.play(
			FadeOut(title),
			FadeOut(subtitle)
		)
		self.wait()
