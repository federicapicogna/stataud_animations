from manim import *
import numpy as np
from scipy.stats import beta

class Planning(Scene):
	def construct(self):

		# SCENE 1: VIDEO TITLE #################################################

		title = Text("Statistical Auditing", font_size = 75)
		subtitle = Text("Bayesian Sample Sizes for Testing", font_size = 40)
		subtitle.next_to(title, DOWN)

		self.play(FadeIn(title))
		self.play(FadeIn(subtitle))
		self.wait(1)

		# Clear the scene
		self.clear()
		self.next_section(skip_animations = False)

		# SCENE 2: BAYESIAN UPDATING CYCLE #####################################

		title = Text("The Bayesian updating cycle", color = WHITE, font_size = 40)
		title.shift(UP * 3)

		self.wait(1)
		self.play(Write(title), run_time = 1)
		self.wait(1)

		circle_prior = Circle(color = BLUE, radius = 1.35)
		circle_prior.next_to(title, DOWN)
		circle_prior.set_fill(BLUE, opacity = 0.25)

		circle_prior_text = Text("Prior")
		circle_prior_text.move_to(circle_prior)

		self.play(Create(circle_prior), Write(circle_prior_text))

		circle_data = Circle(color=BLUE, radius = 1.35)
		circle_data.set_fill(BLUE, opacity = 0.25)
		circle_data.next_to(circle_prior, DR * 2)

		circle_data_text = Text("Data")
		circle_data_text.move_to(circle_data)

		self.play(Create(circle_data), Write(circle_data_text))

		circle_post = Circle(color = BLUE, radius = 1.35)
		circle_post.set_fill(BLUE, opacity = 0.25)
		circle_post.next_to(circle_prior, DL * 2)

		circle_post_text = Text("Posterior")
		circle_post_text.move_to(circle_post)

		self.play(Create(circle_post), Write(circle_post_text))

		arrow_prior_data = Arrow(start = circle_prior.get_center(), end = circle_data.get_center(), buff = 1.5, color = YELLOW)
		arrow_data_post = Arrow(start = circle_data.get_center(), end = circle_post.get_center(), buff = 1.5, color = YELLOW)
		arrow_post_prior = Arrow(start = circle_post.get_center(), end = circle_prior.get_center(), buff = 1.5, color = YELLOW)
	
		for i in range(3):
			if i == 0:
				self.play(Create(arrow_prior_data))
			else:
				self.play(
					Create(arrow_prior_data),
					FadeOut(arrow_post_prior)
				)
			self.play(
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
		self.clear()
		self.next_section(skip_animations = False)
		
		# SCENE 3: PLANNING WITH A UNIFORM PRIOR ###############################

		# Create the axes and title
		axes = Axes(x_range = [0, 1, 0.1], y_range = [0, 4, 1], axis_config = {"color": YELLOW, "include_ticks": True, "include_numbers": True}, tips = False)
		axes.scale(0.9)
		xlab = axes.get_x_axis_label(Tex("Population misstatement $\\theta$").scale(0.75), edge = DOWN, direction = DOWN, buff = 0.5)
		ylab = axes.get_y_axis_label(Text("Density").scale(0.55).rotate(90 * DEGREES), edge = LEFT, direction = LEFT, buff = 0.3)
		title = Text("Uniform prior distribution", font_size = 40)
		title.next_to(axes, UP)

		self.wait(1)
		self.play(Write(title))
		self.wait(1)
		self.play(AnimationGroup(Create(axes.x_axis), Create(axes.y_axis), lag_ratio = 0), run_time = 1.5)
		self.play(Write(xlab), run_time = 1)
		self.play(Write(ylab), run_time = 1)
		self.wait(0.5)

		# Add the prior distribution
		prior_a, prior_b = 1, 1
		distribution = axes.plot(lambda x: beta.pdf(x, prior_a, prior_b), x_range = (0, 1, 0.001), color = WHITE)

		self.play(Create(distribution), run_time = 2)

		# Add the functional form of the prior distribution
		label = Tex("beta($\\alpha$ = 1, $\\beta$ = 1)", font_size = 35)
		label.next_to(distribution, UP)

		self.play(Write(label))
		self.wait(2)

		# Subtitle for the probability area
		subtitle = Tex("Probability is represented by area under the curve ($p$)", font_size = 40, color = BLUE)
		subtitle.next_to(title, DOWN)

		self.play(Write(subtitle), run_time = 1)

		# Shade the 100 percent probability area
		area = axes.get_area(distribution, x_range = (0, 1), color = BLUE, opacity = 0.25)

		self.play(Create(area), run_time = 1.5)

		# Create the probability text
		area_text = Tex("$p$ = 1", font_size = 40)
		area_text.move_to(area)

		self.play(Write(area_text))
		self.wait(1)

		# Change into 0.95 percent probablity area
		ub = beta.ppf(0.95, prior_a, prior_b)
		new_area = axes.get_area(distribution, x_range = (0, ub), color = BLUE, opacity = 0.25)
		new_area_text = Tex("$p$ = 0.95", font_size = 40)
		new_area_text.move_to(area_text)

		self.play(Transform(area_text, new_area_text), Transform(area, new_area))
		self.wait(0.5)
		self.play(FadeOut(subtitle))

		# Subtitle for the upper bound
		subtitle = Tex("95 percent upper bound ($\\theta_{95}$)", font_size = 40, color = BLUE)
		subtitle.next_to(title, DOWN)

		self.play(Write(subtitle))

		# Show the upper bound as a line with text
		point_ub = axes.coords_to_point(ub, 3)
		line_ub = axes.get_vertical_line(point_ub, line_config = {"dashed_ratio": 0.85}, color = BLUE)

		self.play(Create(line_ub))

		text_ub = Tex("$\\theta_{95}$ = " + str(round(ub, 3)), font_size = 35, color = BLUE)
		text_ub.next_to(line_ub, RIGHT)

		self.play(Write(text_ub))
		self.wait(1.5)
		self.play(FadeOut(area_text), FadeOut(subtitle))

		# Extend the y-axis, adjust the position of the prior and the label
		new_axes = Axes(x_range = [0, 1, 0.1], y_range = [0, 40, 10], axis_config = {"color": YELLOW, "include_ticks": True, "include_numbers": True}, tips = False)
		new_axes.scale(0.9)
		new_distribution = new_axes.plot(lambda x: beta.pdf(x, prior_a, prior_b), x_range = (0, 1, 0.001), color = WHITE)
		new_label = Tex("beta($\\alpha$ = 1, $\\beta$ = 1)", font_size = 35)
		new_label.next_to(new_distribution, UP)
		new_area = new_axes.get_area(new_distribution, x_range = (0, ub), color = BLUE, opacity = 0.25)

		self.play(
			ReplacementTransform(axes, new_axes),
			Transform(distribution, new_distribution),
			Transform(label, new_label),
			Transform(area, new_area)
		)
		axes = new_axes
		self.wait(1)

		# Caption for the performance materiality
		subtitle = Tex("Performance materiality ($\\theta_{max}$)", font_size = 40, color = RED)
		subtitle.next_to(title, DOWN)

		self.play(Write(subtitle))

		# Show the materiality as a line with text
		point_mat = axes.coords_to_point(0.05, 35)
		line_mat = axes.get_vertical_line(point_mat, line_config = {"dashed_ratio": 0.85}, color = RED)

		self.play(Create(line_mat))

		text_mat = Tex("$\\theta_{max}$ = 0.05", font_size = 35, color = RED)
		text_mat.next_to(line_mat, RIGHT)

		self.play(Write(text_mat))
		self.wait(2)
		self.play(FadeOut(subtitle))

		# Change the title above the graph
		new_title = Text("Posterior distribution", font_size = 50)
		new_title.move_to(title)
		subtitle = Tex("Sample size ($n$) = 0\\hspace{0.35cm}Misstatements ($k$) = 0", font_size = 40)
		subtitle.next_to(title, DOWN)

		self.play(Transform(title, new_title), Write(subtitle))
		self.wait(1)

		# Slowly update the prior into the posterior until n = 9
		n, k = 0, 0
		for i in range(10):
			n = n + 1
			if i == 9:
				k = k + 1
			post_a = prior_a + k
			post_b = prior_b + n - k
			new_distribution = axes.plot(lambda x: beta.pdf(x, post_a, post_b), x_range = (0, 1, 0.001), color = WHITE)
			ub = beta.ppf(0.95, post_a, post_b)
			point_ub = axes.coords_to_point(ub, 30)
			new_line_ub = axes.get_vertical_line(point_ub, line_config = {"dashed_ratio": 0.85}, color = BLUE)
			new_text_ub = Tex("$\\theta_{95}$ = " + str(round(ub, 3)), font_size = 35, color = BLUE)
			new_text_ub.next_to(new_line_ub, RIGHT)
			new_area = axes.get_area(new_distribution, x_range = (0, ub), color = BLUE, opacity = 0.25)
			new_subtitle = Tex("Sample size ($n$) = " + str(n) + "\\hspace{0.35cm}Misstatements ($k$) = " + str(k), font_size = 40)
			new_subtitle.move_to(subtitle)
			new_label = Tex("beta($\\alpha$ = " + str(post_a) + ", $\\beta$ = " + str(post_b) + ")", font_size = 35)
			new_label.move_to(label)

			self.play(Transform(subtitle, new_subtitle), run_time = 0.25)
			self.play(
				Transform(distribution, new_distribution),
				Transform(line_ub, new_line_ub),
				Transform(text_ub, new_text_ub),
				Transform(area, new_area),
				Transform(label, new_label),
				run_time = 0.25
			)

			self.wait(0.5)

		self.wait(2)

		# Update the prior now much faster until n = 92, k = 1
		sub_run_time = 0.25
		for i in range(82):
			n = n + 1
			post_a = prior_a + k
			post_b = prior_b + n - k
			new_distribution = axes.plot(lambda x: beta.pdf(x, post_a, post_b), x_range = (0, 1, 0.001), color = WHITE)
			ub = beta.ppf(0.95, post_a, post_b)
			point_ub = axes.coords_to_point(ub, 30)
			new_line_ub = axes.get_vertical_line(point_ub, line_config = {"dashed_ratio": 0.85}, color = BLUE)
			new_text_ub = Tex("$\\theta_{95}$ = " + str(round(ub, 3)), font_size = 35, color = BLUE)
			new_text_ub.next_to(new_line_ub, RIGHT)
			new_area = axes.get_area(new_distribution, x_range = (0, ub), color = BLUE, opacity = 0.25)
			new_subtitle = Tex("Sample size ($n$) = " + str(n) + "\\hspace{0.25cm}Misstatements ($k$) = " + str(k), font_size = 40)
			new_subtitle.move_to(subtitle)
			new_label = Tex("beta($\\alpha$ = " + str(post_a) + ", $\\beta$ = " + str(post_b) + ")", font_size = 35)
			new_label.move_to(label)

			self.play(Transform(subtitle, new_subtitle), run_time = sub_run_time)
			self.play(
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

		# Zoom into the posterior distribution
		new_axes = Axes(x_range = [0, 0.1, 0.01], y_range = [0, 40, 10], axis_config = {"color": YELLOW, "include_ticks": True, "include_numbers": True}, tips = False)
		new_axes.scale(0.9)
		new_distribution = new_axes.plot(lambda x: beta.pdf(x, post_a, post_b), x_range = (0, 0.1, 0.001), color = WHITE)
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
		self.wait(1)

		# Put the texts beside each other
		new_text_ub = Tex("$\\theta_{95}$", font_size = 35, color = BLUE)
		new_text_ub.next_to(line_mat, RIGHT)
		text_other = Tex("$<$", font_size = 35, color = WHITE)
		text_other.next_to(new_text_ub, RIGHT)
		new_text_mat = Tex("$\\theta_{max}$", font_size = 35, color = RED)
		new_text_mat.next_to(text_other, RIGHT)

		self.play(Transform(text_ub, new_text_ub), Write(text_other), Transform(text_mat, new_text_mat))
		self.wait(1)

		# Add a rectangle around the minimum saple size
		rectangle = SurroundingRectangle(subtitle[0][0:16], color = YELLOW, buff = 0.1)
		self.play(Create(rectangle))
		self.wait(2)
