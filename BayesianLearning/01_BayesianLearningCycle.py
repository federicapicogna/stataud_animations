from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.coqui import CoquiService

class BayesianLearningCycle(VoiceoverScene):
	def construct(self):
		self.set_speech_service(CoquiService())

		# Title
		title = Text("The Bayesian learning cycle", color = WHITE, font_size = 40)
		title.to_edge(UP)

		with self.voiceover("I will first give you a short introduction into the philosophy of Bayesian statistics.") as tracker:
			self.play(Write(title), run_time = 1)

		# Top circle
		circle_prior = Circle(color = BLUE, radius = 1.35)
		circle_prior.next_to(title, DOWN * 2)
		circle_prior.set_fill(BLUE, opacity = 0.25)
		circle_prior_text = Text("Prior")
		circle_prior_text.move_to(circle_prior)

		# Sample size text
		label = Tex("$n$ = 0", font_size = 60)
		label.next_to(circle_prior, RIGHT * 6)

		with self.voiceover("The idea of this type of statistics is that you formulate your pre-existing information about the misstatement as a prior distribution.") as tracker:
			self.play(
				Create(circle_prior),
				Write(circle_prior_text),
				Write(label)
			)

		# Bottom right circle
		circle_data = Circle(color=BLUE, radius = 1.35)
		circle_data.set_fill(BLUE, opacity = 0.25)
		circle_data.next_to(circle_prior, DR * 2)
		circle_data_text = Text("Data")
		circle_data_text.move_to(circle_data)

		# Update label
		new_label = Tex("$n$ = 1", font_size = 60)
		new_label.move_to(label)
		
		with self.voiceover("Next, suppose that you observe some data from an audit sample.") as tracker:
			self.play(
				Create(circle_data),
				Write(circle_data_text),
				Transform(label, new_label)
			)

		# Bottom left circle
		circle_post = Circle(color = BLUE, radius = 1.35)
		circle_post.set_fill(BLUE, opacity = 0.25)
		circle_post.next_to(circle_prior, DL * 2)
		circle_post_text = Text("Posterior")
		circle_post_text.move_to(circle_post)

		with self.voiceover("Using the data, you can update your prior to a posterior distribution. The posterior represents your updated knowledge about the misstatement and acts as your prior distribution for the next observation.") as tracker:
			self.play(
				Create(circle_post),
				Write(circle_post_text)
			)

		# Arrows
		arrow_prior_data = Arrow(start = circle_prior.get_center(), end = circle_data.get_center(), buff = 1.5, color = YELLOW)
		arrow_data_post = Arrow(start = circle_data.get_center(), end = circle_post.get_center(), buff = 1.5, color = YELLOW)
		arrow_post_prior = Arrow(start = circle_post.get_center(), end = circle_prior.get_center(), buff = 1.5, color = YELLOW)

		with self.voiceover("When you observe more data, the process of updating the prior to a posterior is repeated. This is called the Bayesian learning cycle.") as tracker:
			n = 1
			for i in range(3):
				n = n + 1
				new_label = Tex("$n$ = " + str(n), font_size = 60)
				new_label.move_to(label)

				if i == 0:
					self.play(Create(arrow_prior_data))
				else:
					self.play(
						Create(arrow_prior_data),
						FadeOut(arrow_post_prior)
					)
				self.play(
					Transform(label, new_label),
					Create(arrow_data_post),
					FadeOut(arrow_prior_data)
				)
				if i < 2:
					self.play(
						Create(arrow_post_prior),
						FadeOut(arrow_data_post)
					)
				else:
					self.play(FadeOut(arrow_data_post))

		# Clear the scene
		self.play(
			FadeOut(title),
			FadeOut(label),
			FadeOut(circle_prior),
			FadeOut(circle_prior_text),
			FadeOut(circle_data),
			FadeOut(circle_data_text),
			FadeOut(circle_post),
			FadeOut(circle_post_text)
		)
