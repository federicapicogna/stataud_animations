from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.coqui import CoquiService

class Binomial(VoiceoverScene):
	def construct(self):
		self.set_speech_service(CoquiService(transcription_model = 'base'))

		# Title
		title = Text("Statistical Auditing", font_size = 75)
		title.to_edge(UP)
		
		with self.voiceover(text="First, we will compute the sample size using the binomial distribution.") as tracker:
			self.play(Write(title), run_time = tracker.duration)

		formula = Tex("p(X = k) = \\choose{n}{k}\\theta^k(1-\\theta)^{n-k})")
		formula.to_edge(RIGHT)

