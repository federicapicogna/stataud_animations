from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.coqui import CoquiService

import numpy as np
import scipy.stats as stats

def update_formula(n, k):
	formula = MathTex("p(" + str(k) + ") = \\binom{" + str(n) + "}{" + str(k) + "} 0.03^{" + str(k) + "} (1 - 0.03)^{" + str(n) + " - " + str(k) + "}", font_size = 40)
	formula.scale(0.75)
	formula.to_edge(RIGHT)
	formula[0][0].set_color(BLUE)
	formula[0][2].set_color(RED)
	formula[0][8].set_color(RED)
	formula[0][14].set_color(RED)
	formula[0][26].set_color(RED)
	formula[0][6:8].set_color(GREEN)
	formula[0][23:25].set_color(GREEN)
	formula[0][18:22].set_color(YELLOW)
	formula[0][10:14].set_color(YELLOW)
	return formula

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
			self.play(formula[0][0].animate.set_color(BLUE))
			self.wait_until_bookmark("A")
			self.play(*[formula[0][i].animate.set_color(RED) for i in [2, 7, 10, 18]])
			self.wait_until_bookmark("B")
			self.play(*[formula[0][i].animate.set_color(GREEN) for i in [6, 16]])
			self.wait_until_bookmark("C")
			self.play(*[formula[0][i].animate.set_color(YELLOW) for i in [9, 14]])

		prob = stats.binom.pmf(0, 60, 0.03)
		new_formula = MathTex(r"p(0) = \binom{60}{0} 0.03^{0} (1 - 0.03)^{60 - 0} = " + str(round(prob, 3)), font_size = 40)
		new_formula[0][0].set_color(BLUE)
		new_formula[0][2].set_color(RED)
		new_formula[0][8].set_color(RED)
		new_formula[0][14].set_color(RED)
		new_formula[0][26].set_color(RED)
		new_formula[0][6:8].set_color(GREEN)
		new_formula[0][23:25].set_color(GREEN)
		new_formula[0][18:22].set_color(YELLOW)
		new_formula[0][10:14].set_color(YELLOW)

		with self.voiceover("For example, the probability of discovering zero misstatements in a sample of 60 items, assuming a misstatement rate of three percent, is around " + str(round(prob * 100, 1)) + " percent.") as tracker:
			self.play(Transform(formula, new_formula))

		new_formula.scale(0.75)
		new_formula.to_edge(RIGHT)

		plot = BarChart(values = [0, 0, 0, 0, 0], y_range = [0, 0.4, 0.1], bar_names = ["0", "1", "2", "3", "4"], bar_colors = [BLUE])
		plot.to_edge(LEFT)
		plot.shift(RIGHT)
		xlab = plot.get_x_axis_label(Tex("Misstatements ($k$)", color = RED).scale(0.75), edge = DOWN, direction = DOWN, buff = 0.2)
		ylab = plot.get_y_axis_label(Tex("Probability ($p$)", color = BLUE).scale(0.75).rotate(90 * DEGREES), edge = LEFT, direction = LEFT, buff = 0.4)

		with self.voiceover("It is intuitive to visualize the result of this calculation in this barplot.") as tracker:
			self.play(
				Create(plot),
				Transform(formula, new_formula),
				Write(xlab),
				Write(ylab)
			)

		new_formula = update_formula(60, 0)
		bar_values = [round(stats.binom.pmf(0, 60, 0.03), 3), 0, 0, 0, 0]

		with self.voiceover("I will first draw the probability of finding no misstatements into the barplot.") as tracker:
			self.play(
				plot.animate.change_bar_values(bar_values),
				Transform(formula, new_formula)
			)

		with self.voiceover("We can also draw the probabilities for <bookmark mark='A'/>one misstatement, <bookmark mark='B'/>two misstatements, <bookmark mark='C'/>three misstatements, and <bookmark mark='D'/>four misstatements. For clarity I will show the probabilities above the bars.") as tracker:
			self.wait_until_bookmark("A")
			bar_values[1] = round(stats.binom.pmf(1, 60, 0.03), 3)
			self.play(
				Transform(formula, update_formula(60, 1)),
				plot.animate.change_bar_values(bar_values)
			)
			self.wait_until_bookmark("B")
			bar_values[2] = round(stats.binom.pmf(2, 60, 0.03), 3)
			self.play(
				Transform(formula, update_formula(60, 2)),
				plot.animate.change_bar_values(bar_values)
			)
			self.wait_until_bookmark("C")
			bar_values[3] = round(stats.binom.pmf(3, 60, 0.03), 3)
			self.play(
				Transform(formula, update_formula(60, 3)),
				plot.animate.change_bar_values(bar_values)
			)
			self.wait_until_bookmark("D")
			bar_values[4] = round(stats.binom.pmf(4, 60, 0.03), 3)
			self.play(
				Transform(formula, update_formula(60, 4)),
				plot.animate.change_bar_values(bar_values)
			)
			bar_labels = plot.get_bar_labels(color = WHITE)
			self.play(Write(bar_labels))

		with self.voiceover("Let's increase the sample size to 99 and see how this affects the probabilities.") as tracker:
			for i in range(61, 100):
				bar_values = [round(stats.binom.pmf(0, i, 0.03), 3), round(stats.binom.pmf(1, i, 0.03), 3), round(stats.binom.pmf(2, i, 0.03), 3), round(stats.binom.pmf(3, i, 0.03), 3), round(stats.binom.pmf(4, i, 0.03), 3)]
				self.play(
					Transform(formula, update_formula(i, "k")),
					plot.animate.change_bar_values(bar_values),
					run_time = 0.025
				)
				new_bar_labels = plot.get_bar_labels(color = WHITE)
				self.play(Transform(bar_labels, new_bar_labels), run_time = 0.025)

		new_plot = BarChart(values = bar_values, y_range = [0, 0.4, 0.1], bar_names = ["0", "1", "2", "3", "4"], bar_colors = [RED, BLUE, BLUE, BLUE, BLUE])
		new_plot.to_edge(LEFT)
		new_plot.shift(RIGHT)

		with self.voiceover("The probability of discovering zero misstatements is now 4.9 percent.") as tracker:
			self.play(Transform(plot, new_plot))
