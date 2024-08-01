from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.coqui import CoquiService

import numpy as np
import scipy.stats as stats

class Other(VoiceoverScene):
	def construct(self):
		self.set_speech_service(CoquiService(transcription_model = 'base', model_name = "tts_models/multilingual/multi-dataset/xtts_v2"))

		# scene title
		title = Text("Exploring Other Distributions", font_size = 40)
		title.to_edge(UP)
		
		with self.voiceover("As I mentioned at the beginning, the choice of distribution is a matter of preference. Let's explore two other distributions that can be used in addition to the binomial distribution.") as tracker:
			self.play(Write(title))

		# binomial distribution
		bar_values_binom = [round(stats.binom.pmf(i, 59, 0.05), 3) for i in range(5)]
		plot_binom = BarChart(values = [0, 0, 0, 0, 0], y_range = [0, 0.4, 0.1], bar_names = [str(i) for i in range(5)], bar_colors = [BLUE])
		plot_binom.to_edge(LEFT)
		plot_binom.shift(UP * 0.5)
		plot_binom.shift(LEFT * 0.9)
		plot_binom.scale(0.6)

		xlab_text_binom = Tex("Misstatements $k$").scale(0.65)
		xlab_text_binom[0][13].set_color(RED)
		xlab_binom = plot_binom.get_x_axis_label(xlab_text_binom, edge = DOWN, direction = DOWN, buff = 0.2)

		ylab_text_binom = Tex("Probability $p$").scale(0.65).rotate(90 * DEGREES)
		ylab_text_binom[0][11].set_color(BLUE)
		ylab_binom = plot_binom.get_y_axis_label(ylab_text_binom, edge = LEFT, direction = LEFT, buff = 0.3)
		
		title_binom = Tex("Binomial ($n$ = 59)", font_size = 25)
		title_binom.next_to(plot_binom, UP)
		title_binom[0][9].set_color(GREEN)
		
		formula_binom = MathTex("p(X = k) = \\binom{n}{k} \\theta^{k} (1 - \\theta)^{n - k}", font_size = 25)
		formula_binom.next_to(xlab_binom, DOWN)
		formula_binom.shift(DOWN * 0.5)
		formula_binom[0][0].set_color(BLUE)
		formula_binom[0][4].set_color(RED)
		formula_binom[0][9].set_color(RED)
		formula_binom[0][12].set_color(RED)
		formula_binom[0][20].set_color(RED)
		formula_binom[0][8].set_color(GREEN)
		formula_binom[0][18].set_color(GREEN)
		formula_binom[0][11].set_color(YELLOW)
		formula_binom[0][16].set_color(YELLOW)

		with self.voiceover("For comparison, the barplot on the left visualizes the binomial probabilities for a sample of 59 items assuming a true misstatement rate of 5 percent.") as tracker:
			self.play(
				Write(title_binom),
				Create(plot_binom),
				Write(xlab_binom),
				Write(ylab_binom),
				Write(formula_binom)
			)
			self.play(plot_binom.animate.change_bar_values(bar_values_binom))
			bar_labels_binom = plot_binom.get_bar_labels(color = WHITE, font_size = 19)
			self.play(Write(bar_labels_binom))
			
		new_plot_binom = BarChart(values = bar_values_binom, y_range = [0, 0.4, 0.1], bar_names = [str(i) for i in range(5)], bar_colors = [RED, BLUE, BLUE, BLUE, BLUE])
		new_plot_binom.move_to(plot_binom)
		new_plot_binom.scale(0.6)

		with self.voiceover("The probability of 0 misstatements is lower than the sampling risk of 5 percent, which means that this sample size is sufficient.") as tracker:
			self.play(Transform(plot_binom, new_plot_binom))

		# poisson distribution
		bar_values_pois = [round(stats.poisson.pmf(i, 59 * 0.05), 3) for i in range(5)]
		plot_pois = BarChart(values = [0, 0, 0, 0, 0], y_range = [0, 0.4, 0.1], bar_names = [str(i) for i in range(5)], bar_colors = [BLUE])
		plot_pois.shift(RIGHT * 0.5)
		plot_pois.shift(UP * 0.5)
		plot_pois.scale(0.6)

		xlab_text_pois = Tex("Misstatements $k$").scale(0.65)
		xlab_text_pois[0][13].set_color(RED)
		xlab_pois = plot_pois.get_x_axis_label(xlab_text_pois, edge = DOWN, direction = DOWN, buff = 0.2)

		ylab_text_pois = Tex("Probability $p$").scale(0.65).rotate(90 * DEGREES)
		ylab_text_pois[0][11].set_color(BLUE)
		ylab_pois = plot_pois.get_y_axis_label(ylab_text_pois, edge = LEFT, direction = LEFT, buff = 0.2)

		title_pois = Tex("Poisson ($n$ = 59)", font_size = 25)
		title_pois.next_to(plot_pois, UP)
		title_pois[0][8].set_color(GREEN)

		formula_pois = MathTex("p(X = k) = \\frac{(\\theta n)^k e^{-\\theta n}}{k!}", font_size = 25)
		formula_pois.next_to(xlab_pois, DOWN)
		formula_pois.shift(DOWN * 0.5)
		formula_pois[0][0].set_color(BLUE)
		formula_pois[0][4].set_color(RED)
		formula_pois[0][11].set_color(RED)
		formula_pois[0][17].set_color(RED)
		formula_pois[0][9].set_color(GREEN)
		formula_pois[0][15].set_color(GREEN)
		formula_pois[0][8].set_color(YELLOW)
		formula_pois[0][14].set_color(YELLOW)

		with self.voiceover("Next, we consider the Poisson distribution. <bookmark mark='A'/>Here you can see the probabilities for the same data.") as tracker:
			self.play(
				Write(title_pois),
				Create(plot_pois),
				Write(xlab_pois),
				Write(ylab_pois),
				Write(formula_pois)
			)
			self.wait_until_bookmark("A")
			self.play(plot_pois.animate.change_bar_values(bar_values_pois))

		bar_labels_pois = plot_pois.get_bar_labels(color = WHITE, font_size = 19)
		
		new_plot_pois = BarChart(values = [round(stats.poisson.pmf(i, 59 * 0.05), 3) for i in range(5)], y_range = [0, 0.4, 0.1], bar_names = [str(i) for i in range(5)], bar_colors = [RED, BLUE, BLUE, BLUE, BLUE])
		new_plot_pois.move_to(plot_pois)
		new_plot_pois.scale(0.6)

		with self.voiceover("If we look at the probabilities on the bars, we see that the probability of <bookmark mark='A'/>0 misstatements is higher than under the binomial distribution.") as tracker:
			self.play(Write(bar_labels_pois))
			self.wait_until_bookmark("A")
			self.play(ReplacementTransform(plot_pois, new_plot_pois))

		with self.voiceover("This means that the Poisson distribution requires a slightly larger sample size to reduce this probability below 5 percent. <bookmark mark='A'/>In this case, a sufficient sample size is 60 items, an increase of 1.") as tracker:
			self.wait_until_bookmark("A")
			for i in range(60, 61):
				bar_values_pois = [round(stats.poisson.pmf(j, i * 0.05), 3) for j in range(5)]
				new_title_pois = Tex("Poisson ($n$ = " + str(i) + ")", font_size = 25)
				new_title_pois[0][8].set_color(GREEN)
				new_title_pois.move_to(title_pois)
				self.play(
					Transform(title_pois, new_title_pois),
					new_plot_pois.animate.change_bar_values(bar_values_pois),
					run_time = 0.25
				)
				new_bar_labels_pois = new_plot_pois.get_bar_labels(color = WHITE, font_size = 19)
				self.play(Transform(bar_labels_pois, new_bar_labels_pois), run_time = 0.25)

		# hypergeometric distribution
		bar_values_hyper = [round(stats.hypergeom.pmf(i, 500, 25, 59), 3) for i in range(5)]
		plot_hyper = BarChart(values = [0, 0, 0, 0, 0], y_range = [0, 0.4, 0.1], bar_names = [str(i) for i in range(5)], bar_colors = [BLUE])
		plot_hyper.to_edge(RIGHT)
		plot_hyper.shift(RIGHT)
		plot_hyper.shift(UP * 0.5)
		plot_hyper.scale(0.6)

		xlab_text_hyper = Tex("Misstatements $k$").scale(0.65)
		xlab_text_hyper[0][13].set_color(RED)
		xlab_hyper = plot_hyper.get_x_axis_label(xlab_text_hyper, edge = DOWN, direction = DOWN, buff = 0.2)

		ylab_text_hyper = Tex("Probability $p$").scale(0.65).rotate(90 * DEGREES)
		ylab_text_hyper[0][11].set_color(BLUE)
		ylab_hyper = plot_hyper.get_y_axis_label(ylab_text_hyper, edge = LEFT, direction = LEFT, buff = 0.2)
		
		title_hyper = Tex("Hypergeometric ($n$ = 59, $N$ = 400)", font_size = 25)
		title_hyper.next_to(plot_hyper, UP)
		title_hyper[0][15].set_color(GREEN)

		formula_hyper = MathTex("p(X = k) = \\frac{\\binom{\\theta N}{k} \\binom{N - \\theta N}{n - k}}{\\binom{N}{n}}", font_size = 25)
		formula_hyper.next_to(xlab_hyper, DOWN)
		formula_hyper.shift(DOWN * 0.5)
		formula_hyper[0][0].set_color(BLUE)
		formula_hyper[0][4].set_color(RED)
		formula_hyper[0][10].set_color(RED)
		formula_hyper[0][19].set_color(RED)
		formula_hyper[0][17].set_color(GREEN)
		formula_hyper[0][24].set_color(GREEN)
		formula_hyper[0][8].set_color(YELLOW)
		formula_hyper[0][15].set_color(YELLOW)

		with self.voiceover("Lastly, we examine the hypergeometric distribution. <bookmark mark='A'/>On the right you see the probabilities for this distribution, which is used to take into account the population size. In this case, the population consists of <bookmark mark='B'/>400 items.") as tracker:
			self.play(
				Write(title_hyper),
				Create(plot_hyper),
				Write(xlab_hyper),
				Write(ylab_hyper),
				Write(formula_hyper)
			)
			self.wait_until_bookmark("A")
			self.play(plot_hyper.animate.change_bar_values(bar_values_hyper))
			self.wait_until_bookmark("B")
			self.play(Indicate(title_hyper[0][20:25]), run_time = tracker.get_remaining_duration())

		bar_labels_hyper = plot_hyper.get_bar_labels(color = WHITE, font_size = 19)

		new_plot_hyper = BarChart(values = [round(stats.hypergeom.pmf(i, 500, 25, 59), 3) for i in range(5)], y_range = [0, 0.4, 0.1], bar_names = [str(i) for i in range(5)], bar_colors = [RED, BLUE, BLUE, BLUE, BLUE])
		new_plot_hyper.move_to(plot_hyper)
		new_plot_hyper.scale(0.6)
		
		with self.voiceover("The probability of <bookmark mark='A'/>0 misstatements under this distribution is smaller than under the binomial distribution.") as tracker:
			self.play(Write(bar_labels_hyper))
			self.wait_until_bookmark("A")
			self.play(ReplacementTransform(plot_hyper, new_plot_hyper))

		with self.voiceover("This means that the hypergeometric distribution requires a slightly smaller sample size. <bookmark mark='A'/>In this case, a sufficient sample size is 55 items, a reduction of 4 items. However, this reduction in sample size gets smaller when the population size increases.") as tracker:
			self.wait_until_bookmark("A")
			for i in range(59, 54, -1):
				bar_values_hyper = [round(stats.hypergeom.pmf(j, 500, 25, i), 3) for j in range(5)]
				new_title_hyper = Tex("Hypergeometric ($n$ = " + str(i) + ", $N$ = 400)", font_size = 25)
				new_title_hyper[0][15].set_color(GREEN)
				new_title_hyper.move_to(title_hyper)
				self.play(
					Transform(title_hyper, new_title_hyper),
					new_plot_hyper.animate.change_bar_values(bar_values_hyper),
					run_time = 0.25
				)
				new_bar_labels_hyper = new_plot_hyper.get_bar_labels(color = WHITE, font_size = 19)
				self.play(Transform(bar_labels_hyper, new_bar_labels_hyper), run_time = 0.25)

		# clear scene
		self.play(
			FadeOut(title),
			FadeOut(title_binom),
			FadeOut(plot_binom),
			FadeOut(xlab_binom),
			FadeOut(ylab_binom),
			FadeOut(bar_labels_binom),
			FadeOut(formula_binom),
			FadeOut(title_pois),
			FadeOut(new_plot_pois),
			FadeOut(xlab_pois),
			FadeOut(ylab_pois),
			FadeOut(bar_labels_pois),
			FadeOut(formula_pois),
			FadeOut(title_hyper),
			FadeOut(new_plot_hyper),
			FadeOut(xlab_hyper),
			FadeOut(ylab_hyper),
			FadeOut(bar_labels_hyper),
			FadeOut(formula_hyper)
		)
		self.wait()
