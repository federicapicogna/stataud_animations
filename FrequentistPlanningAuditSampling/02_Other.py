from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.coqui import CoquiService

import numpy as np
import scipy.stats as stats

class Other(VoiceoverScene):
	def construct(self):
		self.set_speech_service(CoquiService(transcription_model = 'base', model_name = "tts_models/multilingual/multi-dataset/xtts_v2"))

		# Title
		title = Text("Other Distributions", font_size = 40)
		title.to_edge(UP)
		
		with self.voiceover("As I mentioned at the beginning, the choice of distribution is a matter of preference. Let's explore two other distributions that can be used in addition to the binomial distribution.") as tracker:
			self.play(Write(title))

		bar_values_binom = [round(stats.binom.pmf(i, 59, 0.05), 3) for i in range(5)]
		plot_binom = BarChart(values = [0, 0, 0, 0, 0], y_range = [0, 0.4, 0.1], bar_names = [str(i) for i in range(5)], bar_colors = [BLUE])
		plot_binom.to_edge(LEFT)
		plot_binom.shift(LEFT * 0.9)
		plot_binom.scale(0.6)
		xlab_binom = plot_binom.get_x_axis_label(Tex("Misstatements ($k$)", color = RED).scale(0.75), edge = DOWN, direction = DOWN, buff = 0.2)
		ylab_binom = plot_binom.get_y_axis_label(Tex("Probability ($p$)", color = BLUE).scale(0.75).rotate(90 * DEGREES), edge = LEFT, direction = LEFT, buff = 0.3)
		title_binom = Tex("Binomial ($n$ = 59)", font_size = 25)
		title_binom.next_to(plot_binom, UP)

		with self.voiceover("For comparison, the barplot on the left visualizes the binomial probabilities for a sample of 59 items assuming a true misstatement rate of 5 percent.") as tracker:
			self.play(
				Write(title_binom),
				Create(plot_binom),
				Write(xlab_binom),
				Write(ylab_binom)
			)
			self.play(plot_binom.animate.change_bar_values(bar_values_binom))
			bar_labels_binom = plot_binom.get_bar_labels(color = WHITE, font_size = 19)
			self.play(Write(bar_labels_binom))
			
		new_plot_binom = BarChart(values = bar_values_binom, y_range = [0, 0.4, 0.1], bar_names = [str(i) for i in range(5)], bar_colors = [RED, BLUE, BLUE, BLUE, BLUE])
		new_plot_binom.move_to(plot_binom)
		new_plot_binom.scale(0.6)

		with self.voiceover("The probability of 0 misstatements is lower than the sampling risk of 5 percent, which means that this sample size is sufficient.") as tracker:
			self.play(Transform(plot_binom, new_plot_binom))

		bar_values_pois = [round(stats.poisson.pmf(i, 59 * 0.05), 3) for i in range(5)]
		plot_pois = BarChart(values = [0, 0, 0, 0, 0], y_range = [0, 0.4, 0.1], bar_names = [str(i) for i in range(5)], bar_colors = [BLUE])
		plot_pois.shift(RIGHT * 0.5)
		plot_pois.scale(0.6)
		xlab_pois = plot_pois.get_x_axis_label(Tex("Misstatements ($k$)", color = RED).scale(0.75), edge = DOWN, direction = DOWN, buff = 0.2)
		ylab_pois = plot_pois.get_y_axis_label(Tex("Probability ($p$)", color = BLUE).scale(0.75).rotate(90 * DEGREES), edge = LEFT, direction = LEFT, buff = 0.2)
		title_pois = Tex("Poisson ($n$ = 59)", font_size = 25)
		title_pois.next_to(plot_pois, UP)

		with self.voiceover("Next, we consider the Poisson distribution. The middle barplot displays the probabilities for the same data. The Poisson distribution is often used when we have large sample sizes and small misstatement rates.") as tracker:
			self.play(
				Write(title_pois),
				Create(plot_pois),
				Write(xlab_pois),
				Write(ylab_pois)
			)
			self.play(plot_pois.animate.change_bar_values(bar_values_pois))

		bar_labels_pois = plot_pois.get_bar_labels(color = WHITE, font_size = 19)
		
		new_plot_pois = BarChart(values = [round(stats.poisson.pmf(i, 59 * 0.05), 3) for i in range(5)], y_range = [0, 0.4, 0.1], bar_names = [str(i) for i in range(5)], bar_colors = [RED, BLUE, BLUE, BLUE, BLUE])
		new_plot_pois.move_to(plot_pois)
		new_plot_pois.scale(0.6)

		with self.voiceover("If we look at the probabilities on the bars, we see that the probability of <bookmark mark='A'/>0 misstatements is higher than under the binomial distribution.") as tracker:
			self.play(Write(bar_labels_pois))
			self.wait_until_bookmark("A")
			self.play(ReplacementTransform(plot_pois, new_plot_pois))

		with self.voiceover("This means that the Poisson distribution requires a slightly larger sample size to reduce this probability below 5 percent. <bookmark mark='A'/>In this case, the sample size is 60 items.") as tracker:
			self.wait_until_bookmark("A")
			for i in range(60, 61):
				bar_values_pois = [round(stats.poisson.pmf(j, i * 0.05), 3) for j in range(5)]
				new_title_pois = Tex("Poisson ($n$ = " + str(i) + ")", font_size = 25)
				new_title_pois.move_to(title_pois)
				self.play(
					Transform(title_pois, new_title_pois),
					new_plot_pois.animate.change_bar_values(bar_values_pois),
					run_time = 0.25
				)
				new_bar_labels_pois = new_plot_pois.get_bar_labels(color = WHITE, font_size = 19)
				self.play(Transform(bar_labels_pois, new_bar_labels_pois), run_time = 0.25)

		bar_values_hyper = [round(stats.hypergeom.pmf(i, 500, 25, 59), 3) for i in range(5)]
		plot_hyper = BarChart(values = [0, 0, 0, 0, 0], y_range = [0, 0.4, 0.1], bar_names = [str(i) for i in range(5)], bar_colors = [BLUE])
		plot_hyper.to_edge(RIGHT)
		plot_hyper.shift(RIGHT)
		plot_hyper.scale(0.6)
		xlab_hyper = plot_hyper.get_x_axis_label(Tex("Misstatements ($k$)", color = RED).scale(0.75), edge = DOWN, direction = DOWN, buff = 0.2)
		ylab_hyper = plot_hyper.get_y_axis_label(Tex("Probability ($p$)", color = BLUE).scale(0.75).rotate(90 * DEGREES), edge = LEFT, direction = LEFT, buff = 0.2)
		title_hyper = Tex("Hypergeometric ($n$ = 59, $N$ = 400)", font_size = 25)
		title_hyper.next_to(plot_hyper, UP)

		with self.voiceover("Lastly, we examine the hypergeometric distribution. The right barplot illustrates the probabilities for this distribution, which is used to take into account the population size. In this case, the population consists of 400 items.") as tracker:
			self.play(
				Write(title_hyper),
				Create(plot_hyper),
				Write(xlab_hyper),
				Write(ylab_hyper)
			)
			self.play(plot_hyper.animate.change_bar_values(bar_values_hyper))

		bar_labels_hyper = plot_hyper.get_bar_labels(color = WHITE, font_size = 19)

		new_plot_hyper = BarChart(values = [round(stats.hypergeom.pmf(i, 500, 25, 59), 3) for i in range(5)], y_range = [0, 0.4, 0.1], bar_names = [str(i) for i in range(5)], bar_colors = [RED, BLUE, BLUE, BLUE, BLUE])
		new_plot_hyper.move_to(plot_hyper)
		new_plot_hyper.scale(0.6)
		
		with self.voiceover("By looking at the probabilities on the bars, we see that the probability of <bookmark mark='A'/>0 misstatements is lower than under the binomial distribution.") as tracker:
			self.play(Write(bar_labels_hyper))
			self.wait_until_bookmark("A")
			self.play(ReplacementTransform(plot_hyper, new_plot_hyper))

		with self.voiceover("This means that the hypergeometric distribution requires a slightly smaller sample size than the binomial distribution. <bookmark mark='A'/>In this case, the sample size is 55 items, a reduction of 4 items. However, this reduction in sample size gets smaller when the population size grows.") as tracker:
			self.wait_until_bookmark("A")
			for i in range(59, 54, -1):
				bar_values_hyper = [round(stats.hypergeom.pmf(j, 500, 25, i), 3) for j in range(5)]
				new_title_hyper = Tex("Hypergeometric ($n$ = " + str(i) + ", $N$ = 400)", font_size = 25)
				new_title_hyper.move_to(title_hyper)
				self.play(
					Transform(title_hyper, new_title_hyper),
					new_plot_hyper.animate.change_bar_values(bar_values_hyper),
					run_time = 0.25
				)
				new_bar_labels_hyper = new_plot_hyper.get_bar_labels(color = WHITE, font_size = 19)
				self.play(Transform(bar_labels_hyper, new_bar_labels_hyper), run_time = 0.25)

		self.play(
			FadeOut(title),
			FadeOut(title_binom),
			FadeOut(plot_binom),
			FadeOut(xlab_binom),
			FadeOut(ylab_binom),
			FadeOut(bar_labels_binom),
			FadeOut(title_pois),
			FadeOut(new_plot_pois),
			FadeOut(xlab_pois),
			FadeOut(ylab_pois),
			FadeOut(bar_labels_pois),
			FadeOut(title_hyper),
			FadeOut(new_plot_hyper),
			FadeOut(xlab_hyper),
			FadeOut(ylab_hyper),
			FadeOut(bar_labels_hyper)
		)
		self.wait()
