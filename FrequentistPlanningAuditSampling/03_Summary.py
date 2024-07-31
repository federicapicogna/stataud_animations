from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.coqui import CoquiService

class TakeHomePoints(VoiceoverScene):
	def construct(self):
		self.set_speech_service(CoquiService(transcription_model = 'base', model_name = "tts_models/multilingual/multi-dataset/xtts_v2"))

		# Title
		title = Text("Summary", font_size = 40)
		title.to_edge(UP)

		with self.voiceover("So, what have you learned in this clip?") as tracker:
			self.play(Write(title))

		# Take home points
		takehome1 = Tex("1. A sufficient sample size implies $p(X \\leq k) < \\alpha$", font_size = 40)
		takehome1.to_edge(LEFT)
		takehome1.shift(UP * 2)

		with self.voiceover("First, a sufficient sample size implies that the cumulative probability of observing the misstatements in the sample is below the sampling risk.") as tracker:
			self.play(Write(takehome1))

		takehome2 = Tex("2. Depends on sample size and true misstatement rate", font_size = 40)
		takehome2.next_to(takehome1, DOWN)
		takehome2.to_edge(LEFT)

		with self.voiceover("Second, these probabilities depend on the sample size and the true misstatement rate.") as tracker:
			self.play(Write(takehome2))

		takehome3 = Tex("3. Same principles apply to other distributions", font_size = 40)
		takehome3.next_to(takehome2, DOWN)
		takehome3.to_edge(LEFT)

		with self.voiceover("And finally, the same principles apply when using other distributions to calculate the sample size, such as the Poisson distribution and the hypergeometric distribution.") as tracker:
			self.play(Write(takehome3))

		self.play(
			FadeOut(title),
			FadeOut(takehome1),
			FadeOut(takehome2),
			FadeOut(takehome3)
		)
		self.wait()
