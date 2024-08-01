from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.coqui import CoquiService

import numpy as np
import scipy.stats as stats

def create_formula(n, k, theta):
	formula = MathTex("p(X = " + str(k) + ") = \\binom{" + str(n) + "}{" + str(k) + "} " + str(theta) + "^{" + str(k) + "} (1 - " + str(theta) + ")^{" + str(n) + " - " + str(k) + "}", font_size = 40)
	formula.scale(0.75)
	formula.to_edge(RIGHT)
	formula[0][0].set_color(BLUE)
	formula[0][4].set_color(RED)
	formula[0][10].set_color(RED)
	formula[0][16].set_color(RED)
	formula[0][28].set_color(RED)
	formula[0][8:10].set_color(GREEN)
	formula[0][25:27].set_color(GREEN)
	formula[0][12:16].set_color(YELLOW)
	formula[0][20:24].set_color(YELLOW)
	return formula

def create_cumulative_formula(n, k, theta):
	formula = MathTex("p(X \\leq " + str(k) + ") = \\sum_{i = 0}^{" + str(k) + "} \\binom{" + str(n) + "}{i} " + str(theta) + "^{i} (1 - " + str(theta) + ")^{" + str(n) + " - i}", font_size = 40)
	formula.scale(0.75)
	formula.to_edge(RIGHT)
	formula.shift(LEFT)
	formula[0][0].set_color(BLUE)
	formula[0][4].set_color(RED)
	formula[0][7].set_color(RED)
	formula[0][13:15].set_color(GREEN)
	formula[0][30:32].set_color(GREEN)
	formula[0][17:21].set_color(YELLOW)
	formula[0][25:29].set_color(YELLOW)
	return formula

def create_cumulative_formula_three(n, k, theta):
	formula = MathTex("p(X \\leq " + str(k) + ") = \\sum_{i = 0}^{" + str(k) + "} \\binom{" + str(n) + "}{i} " + str(theta) + "^{i} (1 - " + str(theta) + ")^{" + str(n) + " - i}", font_size = 40)
	formula.scale(0.75)
	formula.to_edge(RIGHT)
	formula.shift(LEFT)
	formula[0][0].set_color(BLUE)
	formula[0][4].set_color(RED)
	formula[0][7].set_color(RED)
	formula[0][13:16].set_color(GREEN)
	formula[0][31:34].set_color(GREEN)
	formula[0][18:22].set_color(YELLOW)
	formula[0][26:30].set_color(YELLOW)
	return formula

def create_cumulative_formula_three_two(n, k, theta):
	formula = MathTex("p(X \\leq " + str(k) + ") = \\sum_{i = 0}^{" + str(k) + "} \\binom{" + str(n) + "}{i} " + str(theta) + "^{i} (1 - " + str(theta) + ")^{" + str(n) + " - i}", font_size = 40)
	formula.scale(0.75)
	formula.to_edge(RIGHT)
	formula.shift(LEFT)
	formula[0][0].set_color(BLUE)
	formula[0][4].set_color(RED)
	formula[0][7].set_color(RED)
	formula[0][13:16].set_color(GREEN)
	formula[0][33:36].set_color(GREEN)
	formula[0][18:23].set_color(YELLOW)
	formula[0][27:32].set_color(YELLOW)
	return formula

class Binomial(VoiceoverScene):
	def construct(self):
		self.set_speech_service(CoquiService(transcription_model = 'base', model_name = "tts_models/multilingual/multi-dataset/xtts_v2"))

		# Title
		title = Text("The Binomial Distribution", font_size = 40)
		title.to_edge(UP)
		
		with self.voiceover("We will compute the sample size using the binomial distribution, but this is a matter of preference.") as tracker:
			self.play(Write(title))

		formula = MathTex(r"p(X = k) = \binom{n}{k} \theta^{k} (1 - \theta)^{n - k}", font_size = 40)

		with self.voiceover("Let me show you the formula to compute a binomial probability.") as tracker:
			self.play(Write(formula))

		text_p = Tex("$p$ = Probability", font_size = 30)
		text_p[0][0].set_color(BLUE)
		text_p.to_edge(LEFT)
		text_p.shift(UP * 2)

		text_k = Tex("$k$ = Misstatements", font_size = 30)
		text_k[0][0].set_color(RED)
		text_k.to_edge(LEFT)
		text_k.shift(UP * 1.5)

		text_n = Tex("$n$ = Sample size", font_size = 30)
		text_n[0][0].set_color(GREEN)
		text_n.to_edge(LEFT)
		text_n.shift(UP * 1)

		text_theta = Tex("$\\theta$ = True misstatement rate", font_size = 30)
		text_theta[0][0].set_color(YELLOW)
		text_theta.to_edge(LEFT)
		text_theta.shift(UP * 0.5)

		with self.voiceover("Although this formula may seem complicated, it simply states that the <bookmark mark='A'/>probability of discovering a certain <bookmark mark='B'/>number of misstatements in the sample can be computed using the <bookmark mark='C'/>sample size and the <bookmark mark='D'/>true misstatement rate.") as tracker:
			self.wait_until_bookmark("A")
			self.play(
				formula[0][0].animate.set_color(BLUE),
				Write(text_p)
			)
			self.wait_until_bookmark("B")
			self.play(
				*[formula[0][i].animate.set_color(RED) for i in [4, 9, 12, 20]],
				Write(text_k)
			)
			self.wait_until_bookmark("C")
			self.play(
				*[formula[0][i].animate.set_color(GREEN) for i in [8, 18]],
				Write(text_n)
			)
			self.wait_until_bookmark("D")
			self.play(
				*[formula[0][i].animate.set_color(YELLOW) for i in [11, 16]],
				Write(text_theta)
			)

		self.wait(0.5)

		self.play(
			FadeOut(text_p),
			FadeOut(text_k),
			FadeOut(text_n),
			FadeOut(text_theta)
		)

		prob = stats.binom.pmf(0, 60, 0.03)
		new_formula = MathTex(r"p(X = 0) = \binom{60}{0} 0.03^{0} (1 - 0.03)^{60 - 0} = " + str(round(prob, 3)), font_size = 40)
		new_formula[0][0].set_color(BLUE)
		new_formula[0][4].set_color(RED)
		new_formula[0][10].set_color(RED)
		new_formula[0][16].set_color(RED)
		new_formula[0][28].set_color(RED)
		new_formula[0][8:10].set_color(GREEN)
		new_formula[0][25:27].set_color(GREEN)
		new_formula[0][20:24].set_color(YELLOW)
		new_formula[0][12:16].set_color(YELLOW)

		with self.voiceover("For example, the probability of discovering 0 misstatements in a sample of 60 items, assuming a true misstatement rate of 3 percent, is around " + str(round(prob * 100, 1)) + " percent.") as tracker:
			self.play(Transform(formula, new_formula))

		new_formula = new_formula = create_formula(60, 0, 0.03)

		bar_values = [round(stats.binom.pmf(0, 60, 0.03), 3), 0, 0, 0, 0]
		plot = BarChart(values = [0, 0, 0, 0, 0], y_range = [0, 0.4, 0.1], bar_names = [str(i) for i in range(5)], bar_colors = [BLUE])
		plot.to_edge(LEFT)
		plot.shift(RIGHT * 0.5)

		xlab_text = Tex("Misstatements $k$").scale(0.75)
		xlab_text[0][13].set_color(RED)
		xlab = plot.get_x_axis_label(xlab_text, edge = DOWN, direction = DOWN, buff = 0.2)

		ylab_text = Tex("Probability $p$").scale(0.75).rotate(90 * DEGREES)
		ylab_text[0][11].set_color(BLUE)
		ylab = plot.get_y_axis_label(ylab_text, edge = LEFT, direction = LEFT, buff = 0.4)

		with self.voiceover("It is intuitive to visualize the result of this calculation in this barplot.") as tracker:
			self.play(
				Create(plot),
				Transform(formula, new_formula),
				Write(xlab),
				Write(ylab)
			)
			self.play(plot.animate.change_bar_values(bar_values))

		with self.voiceover("Next to the probability of 0 misstatements, we can also visualize the probability of discovering <bookmark mark='A'/>1 misstatement, <bookmark mark='B'/>2 misstatements, <bookmark mark='C'/>3 misstatements, and <bookmark mark='D'/>4 misstatements.") as tracker:
			self.wait_until_bookmark("A")
			bar_values[1] = round(stats.binom.pmf(1, 60, 0.03), 3)
			self.play(
				Transform(formula, create_formula(60, 1, 0.03)),
				plot.animate.change_bar_values(bar_values)
			)
			self.wait_until_bookmark("B")
			bar_values[2] = round(stats.binom.pmf(2, 60, 0.03), 3)
			self.play(
				Transform(formula, create_formula(60, 2, 0.03)),
				plot.animate.change_bar_values(bar_values)
			)
			self.wait_until_bookmark("C")
			bar_values[3] = round(stats.binom.pmf(3, 60, 0.03), 3)
			self.play(
				Transform(formula, create_formula(60, 3, 0.03)),
				plot.animate.change_bar_values(bar_values)
			)
			self.wait_until_bookmark("D")
			bar_values[4] = round(stats.binom.pmf(4, 60, 0.03), 3)
			self.play(
				Transform(formula, create_formula(60, 4, 0.03)),
				plot.animate.change_bar_values(bar_values)
			)
		
		new_plot = BarChart(values = [stats.binom.pmf(i, 60, 0.03) for i in range(61)], y_range = [0, 0.4, 0.1], bar_colors = [BLUE])
		new_plot.to_edge(RIGHT)

		with self.voiceover("As you might have noticed, these probabilities do not sum to 1. That is because I have hidden many of the probabilities, either because they are too small or simply not relevant for this explanation. <bookmark mark='A'/>Here you can see the full barplot.") as tracker:
			self.play(Transform(formula, create_formula(60, "k", 0.03)))
			self.wait_until_bookmark("A")
			self.play(ReplacementTransform(plot, new_plot))

		self.wait()

		plot = BarChart(values = [round(stats.binom.pmf(i, 60, 0.03), 3) for i in range(5)], y_range = [0, 0.4, 0.1], bar_names = [str(i) for i in range(5)], bar_colors = [BLUE])
		plot.to_edge(LEFT)
		plot.shift(RIGHT * 0.5)

		with self.voiceover("However, to keep it simple we zoom back in on the <bookmark mark='A'/>lower part of the barplot.") as tracker:
			self.wait_until_bookmark("A")
			self.play(ReplacementTransform(new_plot, plot))

		bar_labels = plot.get_bar_labels(color = WHITE)

		with self.voiceover("For clarity, I will show the relevant probabilities on top of the bars.") as tracker:
			self.play(Write(bar_labels), run_time = 1)

		with self.voiceover("You have seen earlier that these probabilities depend on the sample size. To illustrate this dependency, I will <bookmark mark='A'/>increase the sample size from 60 to 99.") as tracker:
			self.wait_until_bookmark("A")
			for i in range(61, 100):
				bar_values = [round(stats.binom.pmf(j, i, 0.03), 3) for j in range(5)]
				self.play(
					Transform(formula, create_formula(i, "k", 0.03)),
					plot.animate.change_bar_values(bar_values),
					run_time = 0.025
				)
				new_bar_labels = plot.get_bar_labels(color = WHITE)
				self.play(Transform(bar_labels, new_bar_labels), run_time = 0.025)

		new_plot = BarChart(values = bar_values, y_range = [0, 0.4, 0.1], bar_names = [str(i) for i in range(5)], bar_colors = [RED, BLUE, BLUE, BLUE, BLUE])
		new_plot.move_to(plot)

		with self.voiceover("You can see that if the true misstatement rate is 3 percent, the probability of discovering <bookmark mark='A'/>0 misstatements in a sample of 99 items is equal to " + str(round(stats.binom.pmf(0, i, 0.03) * 100, 1)) + " percent.") as tracker:
			self.wait_until_bookmark("A")
			self.play(
				Transform(plot, new_plot),
				Transform(formula, create_formula(99, 0, 0.03))
			)

		self.wait()

		new_formula = create_cumulative_formula(99, 0, 0.03)
		
		risk_text = MathTex(r"< \alpha", font_size = 30)
		risk_text.next_to(new_formula, RIGHT)

		with self.voiceover("Typically, you want the probability of the number of misstatements in the sample or less to be lower than the sampling risk, which is denoted by alpha.") as tracker:
			self.play(
				Transform(formula, new_formula),
				Write(risk_text)
			)

		new_risk_text = MathTex("< 0.05", font_size = 30)
		new_risk_text.move_to(risk_text)

		with self.voiceover("For example, planning a sample with 95 percent confidence means that the sampling risk is 5 percent. Since the probability of observing no misstatements is lower than this sampling risk, a sample size of 99 is sufficient, but only if you tolerate no misstatements in the sample.") as tracker:
			self.play(Transform(risk_text, new_risk_text))

		new_risk_text = MathTex("> 0.05", font_size = 30)
		new_risk_text.move_to(risk_text)

		new_plot = BarChart(values = bar_values, y_range = [0, 0.4, 0.1], bar_names = ["0", "1", "2", "3", "4"], bar_colors = [RED, RED, BLUE, BLUE, BLUE])
		new_plot.move_to(plot)

		with self.voiceover("However, when you tolerate <bookmark mark='A'/>1 misstatement in the sample you need to consider the probability of finding 0 misstatements, or <bookmark mark='B'/>1 misstatement. This cumulative probability is higher than the sampling risk of 5 percent, which means that a sample size of 99 is insufficient.") as tracker:
			self.wait_until_bookmark("A")
			self.play(Transform(formula, create_cumulative_formula(99, 1, 0.03)),)
			self.wait_until_bookmark("B")
			self.play(
				ReplacementTransform(plot, new_plot),
				Transform(risk_text, new_risk_text)
			)

		with self.voiceover("To bring this cumulative probability below 5 percent, we will need to increase the sample size further. Let's do that <bookmark mark='A'/>now. Pay attention to what effect this has on the probabilities.") as tracker:
			self.wait_until_bookmark("A")
			for i in range(100, 158):
				bar_values = [round(stats.binom.pmf(0, i, 0.03), 3), round(stats.binom.pmf(1, i, 0.03), 3), round(stats.binom.pmf(2, i, 0.03), 3), round(stats.binom.pmf(3, i, 0.03), 3), round(stats.binom.pmf(4, i, 0.03), 3)]
				self.play(
					Transform(formula, create_cumulative_formula_three(i, 1, 0.03)),
					new_plot.animate.change_bar_values(bar_values),
					run_time = 0.025
				)
				new_bar_labels = new_plot.get_bar_labels(color = WHITE)
				self.play(Transform(bar_labels, new_bar_labels), run_time = 0.025)

		new_risk_text = MathTex(" < 0.05", font_size = 30)
		new_risk_text.move_to(risk_text)

		with self.voiceover("Only at a sample size of 157 the cumulative probability is 4.9 percent, which is lower than the sampling risk. This means that a sample size of 157 is sufficient when tolerating 1 misstatement in the sample and assuming a true misstatement rate of 3 percent.") as tracker:
			self.play(Transform(risk_text, new_risk_text))

		plot = BarChart(values = bar_values, y_range = [0, 0.4, 0.1], bar_names = ["0", "1", "2", "3", "4"], bar_colors = [RED, BLUE, BLUE, BLUE, BLUE])
		plot.move_to(new_plot)

		with self.voiceover("Besides depending on the sample size, the binomial probabilities also depend on the true misstatement rate. To illustrate this, we will go back to the situation where we do not tolerate any misstatements in the <bookmark mark='A'/>sample.") as tracker:
			self.wait_until_bookmark("A")
			self.play(
				ReplacementTransform(new_plot, plot),
				Transform(formula, create_cumulative_formula_three(157, 0, 0.03))
			)

		with self.voiceover("Watch what happends to the probabilities if I gradually lower the value of the true misstatement <bookmark mark='A'/>rate from 3 percent to 1 percent.") as tracker:
			self.wait_until_bookmark("A")
			for i in np.arange(0.03, 0.009, -0.001):
				bar_values = [round(stats.binom.pmf(0, 157, i), 3), round(stats.binom.pmf(1, 157, i), 3), round(stats.binom.pmf(2, 157, i), 3), round(stats.binom.pmf(3, 157, i), 3), round(stats.binom.pmf(4, 157, i), 3)]
				self.play(
					Transform(formula, create_cumulative_formula_three_two(157, 0, "{:.3f}".format(i))),
					plot.animate.change_bar_values(bar_values),
					run_time = 0.15
				)
				new_bar_labels = plot.get_bar_labels(color = WHITE)
				self.play(Transform(bar_labels, new_bar_labels), run_time = 0.025)

		new_risk_text = MathTex("> 0.05", font_size = 30)
		new_risk_text.move_to(risk_text)

		with self.voiceover("As you can see, the probability of 0 misstatements in a sample of 157 items assuming a true misstatement rate of 1 percent is once again <bookmark mark='A'/>higher than the sampling risk.") as tracker:
			self.wait_until_bookmark("A")
			self.play(Transform(risk_text, new_risk_text))

		with self.voiceover("To bring this probability below 5 percent, <bookmark mark='A'/>we will once more need to increase the sample size.") as tracker:
			self.wait_until_bookmark("A")
			for i in range(157, 300):
				bar_values = [round(stats.binom.pmf(0, i, 0.01), 3), round(stats.binom.pmf(1, i, 0.01), 3), round(stats.binom.pmf(2, i, 0.01), 3), round(stats.binom.pmf(3, i, 0.01), 3), round(stats.binom.pmf(4, i, 0.01), 3)]
				self.play(
					Transform(formula, create_cumulative_formula_three_two(i, 1, "{:.3f}".format(0.01))),
					plot.animate.change_bar_values(bar_values),
					run_time = 0.005
				)
				new_bar_labels = plot.get_bar_labels(color = WHITE)
				self.play(Transform(bar_labels, new_bar_labels), run_time = 0.025)

		new_risk_text = MathTex(" < 0.05", font_size = 30)
		new_risk_text.move_to(risk_text)

		with self.voiceover("Now you see that you need a sample size of 299 to bring the probability of 0 misstatements below the sampling risk. This means that a sample size of 299 is sufficient when tolerating 0 misstatements in the sample and assuming a true misstatement rate of 1 percent.") as tracker:
			self.play(Transform(risk_text, new_risk_text))

		self.play(
			FadeOut(title),
			FadeOut(risk_text),
			FadeOut(formula),
			FadeOut(plot),
			FadeOut(xlab),
			FadeOut(ylab),
			FadeOut(bar_labels)
		)
		self.wait()
