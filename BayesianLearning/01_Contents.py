from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.coqui import CoquiService

# SCENE 01: CONTENTS ############################################################
class Contents(VoiceoverScene):
	def construct(self):
		self.set_speech_service(CoquiService(transcription_model='base'))

		# Title
		title = Text("Contents", font_size = 40)
		title.to_edge(UP)

		with self.voiceover("We will touch on the following ideas.") as tracker:
			self.play(Write(title))

		content1 = Text("1. The Bayesian learning cycle", font_size = 35)
		content1.to_edge(LEFT)
		content1.shift(UP * 2)

		with self.voiceover("First, I will discuss the Bayesian learning cycle.") as tracker:
			self.play(Write(content1))

		content2 = Text("2. The uniform prior distribution", font_size = 35)
		content2.next_to(content1, DOWN)
		content2.to_edge(LEFT)

		with self.voiceover("Next, I show you an example of a uniform prior distribution.") as tracker:
			self.play(Write(content2))

		content3 = Text("3. The effect of the prior distribution", font_size = 35)
		content3.next_to(content2, DOWN)
		content3.to_edge(LEFT)

		with self.voiceover("Finally, I demonstrate the effect of the prior distribution on the conclusions.") as tracker:
			self.play(Write(content3))

		# Clear the scene
		self.play(
			FadeOut(title),
			FadeOut(content1),
			FadeOut(content2),
			FadeOut(content3)
		)
