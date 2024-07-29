from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.coqui import CoquiService

import numpy as np
import scipy.stats as stats

# SCENE 1: TITLE CARD ##########################################################
class Title(VoiceoverScene):
	def construct(self):
		self.set_speech_service(CoquiService(transcription_model='base'))

		# Title
		title = Text("Statistical Auditing", font_size = 75)
		
		with self.voiceover(text="Hi there.") as tracker:
			self.play(Write(title), run_time = tracker.duration)

		# Subtitle
		subtitle = Text("Bayesian Learning in Audit Sampling", font_size = 40)
		subtitle.next_to(title, DOWN)

		with self.voiceover("In this clip I will explain how to plan and evaluate a statistical audit sample using Bayesian statistics.") as tracker:
			self.play(Write(subtitle))

		# Clear the scene
		self.play(
			FadeOut(title),
			FadeOut(subtitle)
		)

# SCENE 2: CONTENTS ############################################################
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

# SCENE 3: BAYESIAN LEARNING CYCLE #############################################
class BayesianUpdatingCycle(VoiceoverScene):
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

# SCENE 3: PLANNING WITH A UNIFORM PRIOR #######################################
class UniformPrior(VoiceoverScene):
	def construct(self):
		self.set_speech_service(CoquiService(transcription_model='base'))

		# Axes
		axes = Axes(x_range = [0, 1, 0.1], y_range = [0, 4, 1], axis_config = {"color": YELLOW, "include_ticks": True, "include_numbers": True}, tips = False)
		axes.scale(0.9)
		xlab = axes.get_x_axis_label(Tex("Population misstatement $\\theta$").scale(0.75), edge = DOWN, direction = DOWN, buff = 0.5)
		ylab = axes.get_y_axis_label(Text("Density").scale(0.55).rotate(90 * DEGREES), edge = LEFT, direction = LEFT, buff = 0.3)
		title = Text("The uniform prior distribution", font_size = 40)
		title.to_edge(UP)

		with self.voiceover("To illustrate, I will show you a common prior distribution: the uniform prior distribution.") as tracker:
			self.play(Write(title))
			self.play(AnimationGroup(Create(axes.x_axis), Create(axes.y_axis), lag_ratio = 0))
			self.play(Write(xlab))
			self.play(Write(ylab))

		# Prior distribution
		prior_a, prior_b = 1, 1
		distribution = axes.plot(lambda x: stats.beta.pdf(x, prior_a, prior_b), x_range = (0, 1, 0.001), color = WHITE)

		with self.voiceover("Here you can see the uniform prior distribution as a solid line. Because it has equal density at all values, it represents the prior information that every value of the misstatement is equally plausible before seeing any data.") as tracker:
			self.play(Create(distribution))

		# Label
		label = Tex("beta($\\alpha$ = 1, $\\beta$ = 1)", font_size = 35)
		label.next_to(distribution, UP)

		with self.voiceover("Specifically, this prior distribution is a beta distribution with shape parameters 1 and 1.") as tracker:
			self.play(Write(label))

		# Subtitle (probability)
		subtitle = Tex("Probability is represented by area under the curve ($p$)", font_size = 40, color = BLUE)
		subtitle.next_to(title, DOWN)

		with self.voiceover("The area under the prior distribution represents the probability of a range of values of the misstatement occurring.") as tracker:
			self.play(Write(subtitle))

		# Shaded area
		area = axes.get_area(distribution, x_range = (0, 1), color = BLUE, opacity = 0.25)

		# Shaded area text
		area_text = Tex("$p$ = 1", font_size = 40)
		area_text.move_to(area)

		with self.voiceover("For example, the total probability of observing any value of the misstatement is equal to 1.") as tracker:
			self.play(Create(area))
			self.play(Write(area_text))

		# Update shaded area text
		ub = stats.beta.ppf(0.95, prior_a, prior_b)
		new_area = axes.get_area(distribution, x_range = (0, ub), color = BLUE, opacity = 0.25)

		# Update the area text
		new_area_text = Tex("$p$ = 0.95", font_size = 40)
		new_area_text.move_to(area_text)

		with self.voiceover("By looking at a smaller range of values for the misstatement, the probability of observing these values is adjusted accordingly. For instance, the probability under the area you see now is 95 percent.") as tracker:
			self.play(Transform(area_text, new_area_text), Transform(area, new_area))
			self.wait(0.5)
			self.play(FadeOut(subtitle))

		# Subtitle (upper bound)
		subtitle = Tex("95 percent upper bound ($\\theta_{95}$)", font_size = 40, color = BLUE)
		subtitle.next_to(title, DOWN)

		with self.voiceover("The value of the misstatement below which the probability of occurrance is 95 percent can be seen as an upper bound for the misstatement.") as tracker:
			self.play(Write(subtitle))

		# Line (upper bound)
		point_ub = axes.coords_to_point(ub, 3)
		line_ub = axes.get_vertical_line(point_ub, line_config = {"dashed_ratio": 0.85}, color = BLUE)

		# Upper bound text
		text_ub = Tex("$\\theta_{95}$ = " + str(round(ub, 3)), font_size = 35, color = BLUE)
		text_ub.next_to(line_ub, RIGHT)

		with self.voiceover("I will indicate this 95 percent upper bound with <bookmark mark='A'/>this blue line.") as tracker:
			self.wait_until_bookmark("A")
			self.play(
				Create(line_ub),
				Write(text_ub)
			)

		self.play(
			FadeOut(area_text),
			FadeOut(subtitle)
		)

		# Extend the y-axis
		new_axes = Axes(x_range = [0, 1, 0.1], y_range = [0, 40, 10], axis_config = {"color": YELLOW, "include_ticks": True, "include_numbers": True}, tips = False)
		new_axes.scale(0.9)
		new_distribution = new_axes.plot(lambda x: stats.beta.pdf(x, prior_a, prior_b), x_range = (0, 1, 0.001), color = WHITE)
		new_label = Tex("beta($\\alpha$ = 1, $\\beta$ = 1)", font_size = 35)
		new_label.next_to(new_distribution, UP)
		new_area = new_axes.get_area(new_distribution, x_range = (0, ub), color = BLUE, opacity = 0.25)

		with self.voiceover("To see how the prior distribution is updated to a posterior distribution, we need to zoom out by extending the <bookmark mark='A'/>vertical axis.") as tracker:
			self.wait_until_bookmark("A")
			self.play(
				ReplacementTransform(axes, new_axes),
				Transform(distribution, new_distribution),
				Transform(label, new_label),
				Transform(area, new_area)
			)
		axes = new_axes

		# Subtitle (performance materiality)
		subtitle = Tex("Performance materiality ($\\theta_{max}$)", font_size = 40, color = RED)
		subtitle.next_to(title, DOWN)

		with self.voiceover("Typically, you want to obtain evidence that the misstatement is lower than a certain threshold. This threshold is called the performance materiality.") as tracker:
			self.play(Write(subtitle))

		# Line (performance materiality)
		point_mat = axes.coords_to_point(0.05, 35)
		line_mat = axes.get_vertical_line(point_mat, line_config = {"dashed_ratio": 0.85}, color = RED)

		# Text (performance materiality)
		text_mat = Tex("$\\theta_{max}$ = 0.05", font_size = 35, color = RED)
		text_mat.next_to(line_mat, RIGHT)

		with self.voiceover("Suppose the performance materiality is set to 5 percent, which I will mark with <bookmark mark='A'/>this red line.") as tracker:
			self.wait_until_bookmark("A")
			self.play(
				Create(line_mat),
				Write(text_mat)
			)

		self.play(FadeOut(subtitle))

		# Change the title
		new_title = Text("Posterior distribution", font_size = 50)
		new_title.move_to(title)

		with self.voiceover("Now, let's see how the uniform prior distribution is updated to a posterior distribution after seeing data.") as tracker:
			self.play(Transform(title, new_title))

		subtitle = Tex("Sample size ($n$) = 0\\hspace{0.35cm}Misstatements ($k$) = 0", font_size = 40)
		subtitle.next_to(title, DOWN)

		with self.voiceover("The typical data from an audit sample consist of the sample size and the number of misstatements.") as tracker:
			self.play(Write(subtitle))

		# Update the prior
		n, k = 0, 0
		for i in range(10):
			n = n + 1
			if i == 9:
				k = k + 1
			post_a = prior_a + k
			post_b = prior_b + n - k
			new_distribution = axes.plot(lambda x: stats.beta.pdf(x, post_a, post_b), x_range = (0, 1, 0.001), color = WHITE)
			ub = stats.beta.ppf(0.95, post_a, post_b)
			point_ub = axes.coords_to_point(ub, 30)
			new_line_ub = axes.get_vertical_line(point_ub, line_config = {"dashed_ratio": 0.85}, color = BLUE)
			new_text_ub = Tex("$\\theta_{95}$ = " + str(round(ub, 3)), font_size = 35, color = BLUE)
			new_text_ub.next_to(new_line_ub, RIGHT)
			new_area = axes.get_area(new_distribution, x_range = (0, ub), color = BLUE, opacity = 0.25)
			new_subtitle = Tex("Sample size ($n$) = " + str(n) + "\\hspace{0.35cm}Misstatements ($k$) = " + str(k), font_size = 40)
			new_subtitle.move_to(subtitle)
			new_label = Tex("beta($\\alpha$ = " + str(post_a) + ", $\\beta$ = " + str(post_b) + ")", font_size = 35)
			new_label.move_to(label)

			self.play(
				Transform(subtitle, new_subtitle),
				Transform(distribution, new_distribution),
				Transform(line_ub, new_line_ub),
				Transform(text_ub, new_text_ub),
				Transform(area, new_area),
				Transform(label, new_label),
				run_time = 0.25
			)

			self.wait(0.5)

		self.wait(2)

		# More updates to the prior
		sub_run_time = 0.25
		for i in range(82):
			n = n + 1
			post_a = prior_a + k
			post_b = prior_b + n - k
			new_distribution = axes.plot(lambda x: stats.beta.pdf(x, post_a, post_b), x_range = (0, 1, 0.001), color = WHITE)
			ub = stats.beta.ppf(0.95, post_a, post_b)
			point_ub = axes.coords_to_point(ub, 30)
			new_line_ub = axes.get_vertical_line(point_ub, line_config = {"dashed_ratio": 0.85}, color = BLUE)
			new_text_ub = Tex("$\\theta_{95}$ = " + str(round(ub, 3)), font_size = 35, color = BLUE)
			new_text_ub.next_to(new_line_ub, RIGHT)
			new_area = axes.get_area(new_distribution, x_range = (0, ub), color = BLUE, opacity = 0.25)
			new_subtitle = Tex("Sample size ($n$) = " + str(n) + "\\hspace{0.25cm}Misstatements ($k$) = " + str(k), font_size = 40)
			new_subtitle.move_to(subtitle)
			new_label = Tex("beta($\\alpha$ = " + str(post_a) + ", $\\beta$ = " + str(post_b) + ")", font_size = 35)
			new_label.move_to(label)

			self.play(
				Transform(subtitle, new_subtitle),
				Transform(distribution, new_distribution),
				Transform(line_ub, new_line_ub),
				Transform(text_ub, new_text_ub),
				Transform(area, new_area),
				Transform(label, new_label),
				run_time = sub_run_time
			)

			sub_run_time = sub_run_time / 2

		self.wait(2)
		self.play(FadeOut(label))

		# Zoom in on the posterior distribution
		new_axes = Axes(x_range = [0, 0.1, 0.01], y_range = [0, 40, 10], axis_config = {"color": YELLOW, "include_ticks": True, "include_numbers": True}, tips = False)
		new_axes.scale(0.9)
		new_distribution = new_axes.plot(lambda x: stats.beta.pdf(x, post_a, post_b), x_range = (0, 0.1, 0.001), color = WHITE)
		new_area = new_axes.get_area(new_distribution, x_range = (0, ub), color = BLUE, opacity = 0.25)
		new_point_ub = new_axes.coords_to_point(ub, 30)
		new_line_ub = new_axes.get_vertical_line(new_point_ub, line_config = {"dashed_ratio": 0.85}, color = BLUE)
		new_text_ub = Tex("$\\theta_{95}$ = " + str(round(ub, 3)), font_size = 35, color = BLUE)
		new_text_ub.next_to(new_line_ub, RIGHT)
		new_point_mat = new_axes.coords_to_point(0.05, 35)
		new_line_mat = new_axes.get_vertical_line(new_point_mat, line_config = {"dashed_ratio": 0.85}, color = RED)
		new_text_mat = Tex("$\\theta_{max}$ = 0.05", font_size = 35, color = RED)
		new_text_mat.next_to(new_line_mat, RIGHT)

		self.play(
			ReplacementTransform(axes, new_axes),
			Transform(distribution, new_distribution),
			Transform(area, new_area),
			Transform(line_ub, new_line_ub),
			Transform(text_ub, new_text_ub),
			Transform(line_mat, new_line_mat),
			Transform(text_mat, new_text_mat)
		)
		axes = new_axes
		self.wait()

		# Morph upper bound and materiality labels
		new_text_ub = Tex("$\\theta_{95}$", font_size = 35, color = BLUE)
		new_text_ub.next_to(line_mat, RIGHT)
		text_other = Tex("$<$", font_size = 35, color = WHITE)
		text_other.next_to(new_text_ub, RIGHT)
		new_text_mat = Tex("$\\theta_{max}$", font_size = 35, color = RED)
		new_text_mat.next_to(text_other, RIGHT)

		self.play(Transform(text_ub, new_text_ub), Write(text_other), Transform(text_mat, new_text_mat))
		self.wait()

		# Add rectangle around minimum saple size
		rectangle = SurroundingRectangle(subtitle[0][0:16], color = YELLOW, buff = 0.1)

		self.play(Create(rectangle))
		self.wait(2)

		# Clear the scene
		self.play(
			FadeOut(title),
			FadeOut(subtitle),
			FadeOut(axes),
			FadeOut(xlab),
			FadeOut(ylab),
			FadeOut(distribution),
			FadeOut(line_ub),
			FadeOut(text_ub),
			FadeOut(text_mat),
			FadeOut(line_mat),
			FadeOut(text_other),
			FadeOut(rectangle),
			FadeOut(area)
		)

# SCENE 4: THE EFFECT OF THE PRIOR #############################################
class EffectOfPrior(VoiceoverScene):
	def construct(self):
		self.set_speech_service(CoquiService(transcription_model='base'))

		# Data
		n, k = 0, 0

		# Title
		title = Text("The effect of the prior", color = WHITE, font_size = 40)
		title.to_edge(UP)

		with self.voiceover("Finally, I will demonstrate the effect of the prior distribution.") as tracker:
			self.play(Write(title))

		# Subtitle
		subtitle = Tex("Sample size ($n$) = " + str(n) + "\\hspace{0.35cm}Misstatements ($k$) = " + str(k), color = WHITE, font_size = 40)
		subtitle.next_to(title, DOWN)

		self.play(Write(subtitle))

		# Axes (top left, top right, bottom left, bottom right)
		axes_ul = Axes(x_range = [0, 1, 0.1], y_range = [0, 50, 10], axis_config = {"color": YELLOW, "include_ticks": True, "include_numbers": True}, tips = False)
		axes_ul.scale(0.4)
		axes_ul.next_to(subtitle, DOWN)
		axes_ul.shift(LEFT * 3.5)

		axes_ur = Axes(x_range = [0, 1, 0.1], y_range = [0, 50, 10], axis_config = {"color": YELLOW, "include_ticks": True, "include_numbers": True}, tips = False)
		axes_ur.scale(0.4)
		axes_ur.next_to(subtitle, DOWN)
		axes_ur.shift(RIGHT * 3.5)

		axes_dl = Axes(x_range = [0, 1, 0.1], y_range = [0, 50, 10], axis_config = {"color": YELLOW, "include_ticks": True, "include_numbers": True}, tips = False)
		axes_dl.scale(0.4)
		axes_dl.next_to(axes_ul, DOWN)

		axes_dr = Axes(x_range = [0, 1, 0.1], y_range = [0, 50, 10], axis_config = {"color": YELLOW, "include_ticks": True, "include_numbers": True}, tips = False)
		axes_dr.scale(0.4)
		axes_dr.next_to(axes_ur, DOWN)

		self.play(
			AnimationGroup(Create(axes_ul.x_axis), Create(axes_ul.y_axis), lag_ratio = 0),
			AnimationGroup(Create(axes_ur.x_axis), Create(axes_ur.y_axis), lag_ratio = 0),
			AnimationGroup(Create(axes_dl.x_axis), Create(axes_dl.y_axis), lag_ratio = 0),
			AnimationGroup(Create(axes_dr.x_axis), Create(axes_dr.y_axis), lag_ratio = 0)
		)

		# Distribution top left
		dist_ul = axes_ul.plot(lambda x: stats.beta.pdf(x, 1, 1), x_range = (0, 1, 0.001), color = WHITE)

		self.play(Create(dist_ul))

		# Label top left
		label_ul = Tex("beta($\\alpha$ = 1, $\\beta$ = 1)", color = WHITE, font_size = 20)
		label_ul.next_to(dist_ul, DOWN)
		label_ul.shift(UP * 0.6)

		self.play(Write(label_ul))

		# Distribution top right
		dist_ur = axes_ur.plot(lambda x: stats.beta.pdf(x, 1, 20), x_range = (0, 1, 0.001), color = WHITE)

		self.play(Create(dist_ur))

		# Label top right
		label_ur = Tex("beta($\\alpha$ = 1, $\\beta$ = 20)", color = WHITE, font_size = 20)
		label_ur.next_to(dist_ur, DOWN)
		label_ur.shift(UP * 0.6)

		self.play(Write(label_ur))

		# Distribution bottom left
		dist_dl = axes_dl.plot(lambda x: stats.beta.pdf(x, 2, 20), x_range = (0, 1, 0.001), color = WHITE)

		self.play(Create(dist_dl))

		# Label bottom left
		label_dl = Tex("beta($\\alpha$ = 2, $\\beta$ = 20)", color = WHITE, font_size = 20)
		label_dl.next_to(dist_dl, DOWN)
		label_dl.shift(UP * 0.6)

		self.play(Write(label_dl))

		# Distribution bottom right
		dist_dr = axes_dr.plot(lambda x: stats.beta.pdf(x, 2, 35), x_range = (0, 1, 0.001), color = WHITE)
		
		self.play(Create(dist_dr))

		# Label bottom right
		label_dr = Tex("beta($\\alpha$ = 2, $\\beta$ = 35)", color = WHITE, font_size = 20)
		label_dr.next_to(dist_dr, DOWN)
		label_dr.shift(UP * 0.6)

		self.play(Write(label_dr))
		self.wait()
		self.play(
			FadeOut(label_ul),
			FadeOut(label_ur),
			FadeOut(label_dl),
			FadeOut(label_dr)
		)

		# Lines for materiality and upper bounds (top left, top right, bottom left, bottom right)
		point_mat_ul = axes_ul.coords_to_point(0.05, 50)
		line_mat_ul = axes_ul.get_vertical_line(point_mat_ul, line_config = {"dashed_ratio": 0.85}, color = RED)

		point_ub_ul = axes_ul.coords_to_point(stats.beta.ppf(0.95, 1, 1), 50)
		line_ub_ul = axes_ul.get_vertical_line(point_ub_ul, line_config = {"dashed_ratio": 0.85}, color = BLUE)

		point_mat_ur = axes_ur.coords_to_point(0.05, 50)
		line_mat_ur = axes_ur.get_vertical_line(point_mat_ur, line_config = {"dashed_ratio": 0.85}, color = RED)

		point_ub_ur = axes_ur.coords_to_point(stats.beta.ppf(0.95, 1, 20), 50)
		line_ub_ur = axes_ur.get_vertical_line(point_ub_ur, line_config = {"dashed_ratio": 0.85}, color = BLUE)

		point_mat_dl = axes_dl.coords_to_point(0.05, 50)
		line_mat_dl = axes_dl.get_vertical_line(point_mat_dl, line_config = {"dashed_ratio": 0.85}, color = RED)

		point_ub_dl = axes_dl.coords_to_point(stats.beta.ppf(0.95, 2, 20), 50)
		line_ub_dl = axes_dl.get_vertical_line(point_ub_dl, line_config = {"dashed_ratio": 0.85}, color = BLUE)

		point_mat_dr = axes_dr.coords_to_point(0.05, 50)
		line_mat_dr = axes_dr.get_vertical_line(point_mat_dr, line_config = {"dashed_ratio": 0.85}, color = RED)

		point_ub_dr = axes_dr.coords_to_point(stats.beta.ppf(0.95, 2, 35), 50)
		line_ub_dr = axes_dr.get_vertical_line(point_ub_dr, line_config = {"dashed_ratio": 0.85}, color = BLUE)

		self.play(
			Create(line_mat_ul),
			Create(line_mat_ur),
			Create(line_mat_dl),
			Create(line_mat_dr),
			Create(line_ub_ul),
			Create(line_ub_ur),
			Create(line_ub_dl),
			Create(line_ub_dr)
		)
		self.wait()

		for i in range(30):
			n = n + 1

			new_subtitle = Tex("Sample size ($n$) = " + str(n) + "\\hspace{0.35cm}Misstatements ($k$) = " + str(k), color = WHITE, font_size = 40)
			new_subtitle.move_to(subtitle)

			new_dist_ul = axes_ul.plot(lambda x: stats.beta.pdf(x, 1, 1 + n), x_range = (0, 1, 0.001), color = WHITE)

			point_ub_ul = axes_ul.coords_to_point(stats.beta.ppf(0.95, 1, 1 + n), 50)
			new_line_ub_ul = axes_ul.get_vertical_line(point_ub_ul, line_config = {"dashed_ratio": 0.85}, color = BLUE)

			new_dist_ur = axes_ur.plot(lambda x: stats.beta.pdf(x, 1, 20 + n), x_range = (0, 1, 0.001), color = WHITE)

			point_ub_ur = axes_ur.coords_to_point(stats.beta.ppf(0.95, 1, 20 + n), 50)
			new_line_ub_ur = axes_ur.get_vertical_line(point_ub_ur, line_config = {"dashed_ratio": 0.85}, color = BLUE)

			point_ub_dl = axes_dl.coords_to_point(stats.beta.ppf(0.95, 2, 20 + n), 50)
			new_line_ub_dl = axes_dl.get_vertical_line(point_ub_dl, line_config = {"dashed_ratio": 0.85}, color = BLUE)

			new_dist_dl = axes_dl.plot(lambda x: stats.beta.pdf(x, 2, 20 + n), x_range = (0, 1, 0.001), color = WHITE)

			point_ub_dr = axes_dr.coords_to_point(stats.beta.ppf(0.95, 2, 35 + n), 50)
			new_line_ub_dr = axes_dr.get_vertical_line(point_ub_dr, line_config = {"dashed_ratio": 0.85}, color = BLUE)

			new_dist_dr = axes_dr.plot(lambda x: stats.beta.pdf(x, 2, 35 + n), x_range = (0, 1, 0.001), color = WHITE)

			self.play(
				Transform(subtitle, new_subtitle),
				Transform(dist_ul, new_dist_ul),
				Transform(dist_ur, new_dist_ur),
				Transform(dist_dl, new_dist_dl),
				Transform(dist_dr, new_dist_dr),
				Transform(line_ub_ul, new_line_ub_ul),
				Transform(line_ub_ur, new_line_ub_ur),
				Transform(line_ub_dl, new_line_ub_dl),
				Transform(line_ub_dr, new_line_ub_dr),
				run_time = 0.25
			)

		self.wait(2)

		# Clear the scene
		self.play(
			FadeOut(title),
			FadeOut(subtitle),
			FadeOut(axes_ul),
			FadeOut(axes_ur),
			FadeOut(axes_dl),
			FadeOut(axes_dr),
			FadeOut(dist_ul),
			FadeOut(dist_ur),
			FadeOut(dist_dl),
			FadeOut(dist_dr),
			FadeOut(line_ub_ul),
			FadeOut(line_ub_ur),
			FadeOut(line_ub_dl),
			FadeOut(line_ub_dr),
			FadeOut(line_mat_ul),
			FadeOut(line_mat_ur),
			FadeOut(line_mat_dl),
			FadeOut(line_mat_dr)
		)

# SCENE 5: TAKE HOME POINTS ####################################################
class TakeHomePoints(VoiceoverScene):
	def construct(self):
		self.set_speech_service(CoquiService(transcription_model='base'))

		# Title
		title = Text("Take home points", color = WHITE, font_size = 40)
		title.to_edge(UP)

		with self.voiceover("So, what have you learned in this clip?") as tracker:
			self.play(Write(title))

		# Take home points
		th1_sub1 = Tex("1. A sufficient sample size implies ", color = WHITE, font_size = 40)
		th1_sub2 = Tex("$\\theta_{95}$", color = BLUE, font_size = 40)
		th1_sub2.next_to(th1_sub1, RIGHT)
		th1_sub3 = Tex("$<$", color = WHITE, font_size = 40)
		th1_sub3.next_to(th1_sub2, RIGHT)
		th1_sub4 = Tex("$\\theta_{max}$", color = RED, font_size = 40)
		th1_sub4.next_to(th1_sub3, RIGHT)
		takehome1 = VGroup(th1_sub1, th1_sub2, th1_sub3, th1_sub4)
		takehome1.to_edge(LEFT)
		takehome1.shift(UP * 2)

		with self.voiceover("First, a sufficient sample size implies that the upper bound for the misstatement is below the performance materiality.") as tracker:
			self.play(Write(takehome1))

		takehome2 = Tex("2. The uniform prior is conservative", font_size = 40)
		takehome2.next_to(takehome1, DOWN)
		takehome2.to_edge(LEFT)

		with self.voiceover("Second, the uniform prior is conservative.") as tracker:
			self.play(Write(takehome2))

		takehome3 = Tex("3. Risk-reducing priors require a lower sample size", font_size = 40)
		takehome3.next_to(takehome2, DOWN)
		takehome3.to_edge(LEFT)

		with self.voiceover("And finally, risk reducing priors require a lower sample size to come to a similar conclusion as the uniform prior.") as tracker:
			self.play(Write(takehome3))

		self.play(
			FadeOut(title),
			FadeOut(takehome1),
			FadeOut(takehome2),
			FadeOut(takehome3)
		)
