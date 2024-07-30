from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.coqui import CoquiService

import numpy as np
import scipy.stats as stats

class Binomial(VoiceoverScene):
	def construct(self):
		self.set_speech_service(CoquiService(transcription_model = 'base'))

		# Title
		title = Text("The binomial distribution", font_size = 40)
		title.to_edge(UP)
		
		with self.voiceover("First, we will compute the sample size using the binomial distribution.") as tracker:
			self.play(Write(title))

		formula = MathTex(r"p(k) = \binom{n}{k} \theta^{k} (1 - \theta)^{n - k}", font_size = 40)

		with self.voiceover("The formula for the binomial probability is shown here.") as tracker:
			self.play(Write(formula))

		with self.voiceover("This formula simply states that the probability of observing a <bookmark mark='A'/>number of misstatements in a sample, shown in red, can be computed as a function of the <bookmark mark='B'/>sample size, shown in green, and the <bookmark mark='C'/>assumed misstatement rate, shown in yellow.") as tracker:
			self.wait_until_bookmark("A")
			self.play(
				formula[0][2].animate.set_color(RED),
				formula[0][7].animate.set_color(RED),
				formula[0][10].animate.set_color(RED),
				formula[0][18].animate.set_color(RED)
			)
			self.wait_until_bookmark("B")
			self.play(
				formula[0][6].animate.set_color(GREEN),
				formula[0][16].animate.set_color(GREEN)
			)
			self.wait_until_bookmark("C")
			self.play(
				formula[0][9].animate.set_color(YELLOW),
				formula[0][14].animate.set_color(YELLOW)
			)

		prob = stats.binom.pmf(0, 60, 0.03)
		new_formula = MathTex(r"p(0) = \binom{60}{0} 0.03^{0} (1 - 0.03)^{10 - 0} = " + str(round(prob, 3)), font_size = 40)
		new_formula[0][2].set_color(RED)
		new_formula[0][8].set_color(RED)
		new_formula[0][14].set_color(RED)
		new_formula[0][26].set_color(RED)
		new_formula[0][6:8].set_color(GREEN)
		new_formula[0][23:25].set_color(GREEN)
		new_formula[0][18:22].set_color(YELLOW)
		new_formula[0][10:14].set_color(YELLOW)

		with self.voiceover("For example, the probability of finding no misstatements in a sample of 60 items, assuming a misstatement rate of three percent is around " + str(round(prob * 100, 1)) + " percent.") as tracker:
			self.play(Transform(formula, new_formula))

		new_formula.scale(0.75)
		new_formula.to_edge(RIGHT)

		plot = BarChart(values = [0, 0, 0, 0, 0], y_range = [0, 1, 0.2], bar_names = ["0", "1", "2", "3", "4"], bar_colors = [BLUE])
		plot.to_edge(LEFT)
		plot.shift(RIGHT)
		xlab = plot.get_x_axis_label(Tex("$k$").scale(0.75), edge = DOWN, direction = DOWN, buff = 0.2)
		ylab = plot.get_y_axis_label(Text("Probability").scale(0.55).rotate(90 * DEGREES), edge = LEFT, direction = LEFT, buff = 0.4)

		with self.voiceover("Let's visualize the result of this calculation in a graph.") as tracker:
			self.play(
				Create(plot),
				Transform(formula, new_formula),
				Write(xlab),
				Write(ylab)
			)

		new_formula = MathTex(r"p(0) = \binom{60}{0} 0.03^{0} (1 - 0.03)^{10 - 0}", font_size = 40)
		new_formula.scale(0.75)
		new_formula.to_edge(RIGHT)
		new_formula[0][2].set_color(RED)
		new_formula[0][8].set_color(RED)
		new_formula[0][14].set_color(RED)
		new_formula[0][26].set_color(RED)
		new_formula[0][6:8].set_color(GREEN)
		new_formula[0][23:25].set_color(GREEN)
		new_formula[0][18:22].set_color(YELLOW)
		new_formula[0][10:14].set_color(YELLOW)

		with self.voiceover("First, I will draw the probability of no misstatements into the graph.") as tracker:
			self.play(plot.animate.change_bar_values([round(stats.binom.pmf(0, 60, 0.03), 3), 0, 0, 0, 0]))
			bar_labels = plot.get_bar_labels(color = WHITE)
			self.play(
				Transform(formula, new_formula),
				Write(bar_labels)
			)

		with self.voiceover("We can also draw the probabilities for the other number of misstatements.") as tracker:
			self.play(plot.animate.change_bar_values([round(stats.binom.pmf(0, 60, 0.03), 3), round(stats.binom.pmf(1, 60, 0.03), 3), 0, 0, 0]))
			new_bar_labels = plot.get_bar_labels(color = WHITE)
			self.play(Transform(bar_labels, new_bar_labels))
			self.play(plot.animate.change_bar_values([round(stats.binom.pmf(0, 60, 0.03), 3), round(stats.binom.pmf(1, 60, 0.03), 3), round(stats.binom.pmf(2, 60, 0.03), 3), 0, 0]))
			new_bar_labels = plot.get_bar_labels(color = WHITE)
			self.play(Transform(bar_labels, new_bar_labels))
			self.play(plot.animate.change_bar_values([round(stats.binom.pmf(0, 60, 0.03), 3), round(stats.binom.pmf(1, 60, 0.03), 3), round(stats.binom.pmf(2, 60, 0.03), 3), round(stats.binom.pmf(3, 60, 0.03), 3), 0]))
			new_bar_labels = plot.get_bar_labels(color = WHITE)
			self.play(Transform(bar_labels, new_bar_labels))
			self.play(plot.animate.change_bar_values([round(stats.binom.pmf(0, 60, 0.03), 3), round(stats.binom.pmf(1, 60, 0.03), 3), round(stats.binom.pmf(2, 60, 0.03), 3), round(stats.binom.pmf(3, 60, 0.03), 3), round(stats.binom.pmf(4, 60, 0.03), 3)]))
			new_bar_labels = plot.get_bar_labels(color = WHITE)
			self.play(Transform(bar_labels, new_bar_labels))
