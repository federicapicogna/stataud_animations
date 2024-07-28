from manim import *
import numpy as np
from scipy.stats import beta

class Planning(Scene):
	def construct(self):

		# SCENE 1: VIDEO TITLE #################################################

		title = Text("Statistical Auditing", font_size = 75)
		subtitle = Text("Planning a Minimum Sample Size for Testing", font_size=40)
		subtitle.next_to(title, DOWN)

		self.play(AnimationGroup(Write(title), Write(subtitle), lag_ratio = 1))
		self.wait(1)

		# Clear the scene
		self.play(
			FadeOut(title),
			FadeOut(subtitle)
		)
		self.next_section(skip_animations=False)

		# SCENE 2: BAYESIAN UPDATING CYCLE #####################################

		title = Text("Bayesian statistics: From prior to posterior", color=WHITE, font_size=40)
		title.shift(UP*3)

		self.play(Write(title))

		circle_prior = Circle(color=BLUE, radius=1.35)
		circle_prior.next_to(title, DOWN)
		circle_prior.set_fill(BLUE, opacity=0.25)

		circle_prior_text = Text("Prior")
		circle_prior_text.move_to(circle_prior)

		self.play(
			Create(circle_prior),
			Write(circle_prior_text)
		)

		circle_data = Circle(color=BLUE, radius = 1.35)
		circle_data.set_fill(BLUE, opacity=0.25)
		circle_data.next_to(circle_prior, DR * 2)

		circle_data_text = Text("Data")
		circle_data_text.move_to(circle_data)

		self.play(
			Create(circle_data),
			Write(circle_data_text)
		)

		circle_post = Circle(color=BLUE, radius=1.35)
		circle_post.set_fill(BLUE, opacity=0.25)
		circle_post.next_to(circle_prior, DL * 2)

		circle_post_text = Text("Posterior")
		circle_post_text.move_to(circle_post)

		self.play(
			Create(circle_post),
			Write(circle_post_text)
		)

		arrow_prior_to_data = Arrow(start=circle_prior.get_center(), end=circle_data.get_center(), buff=1.5, color=YELLOW)
		arrow_data_to_post = Arrow(start=circle_data.get_center(), end=circle_post.get_center(), buff=1.5, color=YELLOW)
		arrow_post_to_prior = Arrow(start=circle_post.get_center(), end=circle_prior.get_center(), buff=1.5, color=YELLOW)
	
		for i in range(3):
			if i == 0:
				self.play(Create(arrow_prior_to_data))
			else:
				self.play(
					Create(arrow_prior_to_data),
					FadeOut(arrow_post_to_prior)
				)
			self.play(
				Create(arrow_data_to_post),
				FadeOut(arrow_prior_to_data)
			)
			if i < 2:
				self.play(
					Create(arrow_post_to_prior),
					FadeOut(arrow_data_to_post)
				)
			else:
				self.play(FadeOut(arrow_data_to_post))

		# Clear the scene
		self.play(
			FadeOut(title),
			FadeOut(circle_prior),
			FadeOut(circle_prior_text),
			FadeOut(circle_data),
			FadeOut(circle_data_text),
			FadeOut(circle_post),
			FadeOut(circle_post_text)
		)
		self.next_section(skip_animations=False)
		
		# SCENE 3: PLANNING WITH A UNIFORM PRIOR ###############################

		axes_short = Axes(
			x_range=[0, 1, 0.1],
			y_range=[0, 4, 1],
			axis_config={
				"color": YELLOW,
				"include_ticks": True,
				"include_numbers": True
			},
			tips = False
		).scale(0.9)
		xlab = axes_short.get_x_axis_label(Tex("Population misstatement $\\theta$").scale(0.75), edge=DOWN, direction=DOWN, buff=0.5)
		ylab = axes_short.get_y_axis_label(Text("Density").scale(0.55).rotate(90 * DEGREES), edge=LEFT, direction=LEFT, buff=0.3)

		self.play(AnimationGroup(Create(axes_short.x_axis), Create(axes_short.y_axis), lag_ratio=0), run_time = 1.5)
		self.play(Write(xlab))
		self.play(Write(ylab))
		self.wait(0.5)

		# Add the title
		title = Text("Uniform prior distribution", font_size=40)
		title.next_to(axes_short, UP)

		self.play(Create(title))
		self.wait(1)

		# Add the prior distribution
		prior_a, prior_b = 1, 1
		short_prior = axes_short.plot(lambda x: beta.pdf(x, prior_a, prior_b), x_range=(0, 1, 0.001), color=WHITE)

		self.play(Create(short_prior), run_time=2)

		# Add the functional form of the prior distribution
		short_prior_label = Tex("beta($\\alpha$ = 1, $\\beta$ = 1)", font_size = 35)
		short_prior_label.next_to(short_prior, UP)

		self.play(Write(short_prior_label), run_time = 0.5)
		self.wait(2)

		# Caption for the probability area
		caption = Tex("Probability is represented by area under the curve ($p$)", font_size=40, color=BLUE)
		caption.next_to(title, DOWN)

		self.play(Write(caption))

		# Shade the 100 percent probability area
		initial_short_prior_area = axes_short.get_area(short_prior, x_range=(0, 1), color=BLUE, opacity =0.25)

		self.play(Create(initial_short_prior_area), run_time=1.5)

		# Create the probability text
		initial_area_text = Tex("$p$ = 1", font_size =40)
		initial_area_text.move_to(initial_short_prior_area)

		self.play(Write(initial_area_text))
		self.wait(1)

		# Change into 0.95 percent probablity area
		prior_ub = beta.ppf(0.95, prior_a, prior_b)
		short_prior_area = axes_short.get_area(short_prior, x_range=(0, prior_ub), color=BLUE, opacity =0.25)
		area_text = Tex("$p$ = 0.95", font_size =40)
		area_text.move_to(initial_area_text)

		self.play(
			ReplacementTransform(initial_area_text, area_text),
			ReplacementTransform(initial_short_prior_area, short_prior_area)
		)
		self.wait(0.5)
		self.play(FadeOut(caption))

		# Caption for the upper bound
		caption = Tex("95 percent upper bound ($\\theta_{95}$)", font_size=40, color=BLUE)
		caption.next_to(title, DOWN)

		self.play(Write(caption))

		# Show the upper bound as a line with text
		point_ub = axes_short.coords_to_point(prior_ub, 3)
		line_ub = axes_short.get_vertical_line(point_ub, line_config={"dashed_ratio": 0.85}, color=BLUE)

		self.play(Create(line_ub))

		ub_text = Tex("$\\theta_{95}$ = " + str(round(prior_ub, 3)), font_size=35, color=BLUE)
		ub_text.next_to(line_ub, RIGHT)

		self.play(Write(ub_text))
		self.wait(1.5)
		self.play(FadeOut(area_text), FadeOut(caption))

		# Extend the y-axis, adjust the position of the prior and the label
		axes_long = Axes(
			x_range=[0, 1, 0.1],
			y_range=[0, 40, 10],
			axis_config={
				"color": YELLOW,
				"include_ticks": True,
				"include_numbers": True
			},
			tips = False
		).scale(0.9)
		prior = axes_long.plot(lambda x: beta.pdf(x, prior_a, prior_b), x_range=(0, 1, 0.001), color=WHITE)
		prior_label = Tex("beta($\\alpha$ = 1, $\\beta$ = 1)", font_size = 35)
		prior_label.next_to(prior, UP)
		prior_area = axes_short.get_area(prior, x_range=(0, prior_ub), color=BLUE, opacity = 0.25)

		self.play(
			ReplacementTransform(axes_short, axes_long),
			ReplacementTransform(short_prior, prior),
			ReplacementTransform(short_prior_label, prior_label),
			ReplacementTransform(short_prior_area, prior_area)
		)
		self.wait(1)

		# Caption for the performance materiality
		caption = Tex("Performance materiality ($\\theta_{max}$)", font_size=40, color=RED)
		caption.next_to(title, DOWN)

		self.play(Write(caption))

		# Show the materiality as a line with text
		point_mat = axes_long.coords_to_point(0.05, 35)
		line_mat = axes_long.get_vertical_line(point_mat, line_config={"dashed_ratio": 0.85}, color=RED)

		self.play(Create(line_mat))

		mat_text = Tex("$\\theta_{max}$ = 0.05", font_size=35, color=RED)
		mat_text.next_to(line_mat, RIGHT)

		self.play(Write(mat_text))
		self.wait(2)
		self.play(FadeOut(caption))

		# Change the title above the graph
		new_title = Text("Posterior distribution", font_size=50)
		new_title.move_to(title)
		caption = Tex("Sample size ($n$) = 0\\hspace{0.35cm}Misstatements ($k$) = 0", font_size=40)
		caption.next_to(title, DOWN)

		self.play(
			Transform(title, new_title),
			Create(caption)
		)
		self.wait(1)

		# Slowly update the prior into the posterior until n = 9
		n, k = 0, 0
		for i in range(10):
			n = n + 1
			if i == 8:
				k = k + 1
			post_a = prior_a + k
			post_b = prior_b + n - k
			posterior = axes_long.plot(lambda x: beta.pdf(x, post_a, post_b), x_range=(0, 1, 0.001), color=WHITE)
			post_ub = beta.ppf(0.95, post_a, post_b)
			point_ub = axes_long.coords_to_point(post_ub, 30)
			post_line_ub = axes_long.get_vertical_line(point_ub, line_config={"dashed_ratio": 0.85}, color=BLUE)
			post_ub_text = Tex("$\\theta_{95}$ = " + str(round(post_ub, 3)), font_size=35, color=BLUE)
			post_ub_text.next_to(post_line_ub, RIGHT)
			post_area = axes_long.get_area(posterior, x_range=(0, post_ub), color=BLUE, opacity = 0.25)
			new_caption = Tex("Sample size ($n$) = " + str(n) + "\\hspace{0.35cm}Misstatements ($k$) = " + str(k), font_size=40)
			new_caption.move_to(caption)
			post_label = Tex("beta($\\alpha$ = " + str(post_a) + ", $\\beta$ = " + str(post_b) + ")", font_size = 35)
			post_label.move_to(prior_label)

			self.play(
				ReplacementTransform(prior, posterior), 
				Transform(caption, new_caption), 
				ReplacementTransform(prior_label, post_label), 
				ReplacementTransform(prior_area, post_area),
				ReplacementTransform(line_ub, post_line_ub),
				ReplacementTransform(ub_text, post_ub_text),
				run_time=0.25
			)

			prior = posterior
			prior_label = post_label
			prior_area = post_area
			line_ub = post_line_ub
			ub_text = post_ub_text

			self.wait(0.5)

		self.wait(2)

		# Update the prior now much faster until n = 92, k = 1
		sub_run_time = 0.25
		for i in range(82):
			n = n + 1
			post_a = prior_a + k
			post_b = prior_b + n - k
			posterior = axes_long.plot(lambda x: beta.pdf(x, post_a, post_b), x_range=(0, 1, 0.001), color=WHITE)
			post_ub = beta.ppf(0.95, post_a, post_b)
			point_ub = axes_long.coords_to_point(post_ub, 30)
			post_line_ub = axes_long.get_vertical_line(point_ub, line_config={"dashed_ratio": 0.85}, color=BLUE)
			post_ub_text = Tex("$\\theta_{95}$ = " + str(round(post_ub, 3)), font_size=35, color=BLUE)
			post_ub_text.next_to(post_line_ub, RIGHT)
			post_area = axes_short.get_area(posterior, x_range=(0, post_ub), color=BLUE, opacity = 0.25)
			new_caption = Tex("Sample size ($n$) = " + str(n) + "\\hspace{0.25cm}Misstatements ($k$) = " + str(k), font_size=40)
			new_caption.move_to(caption)
			post_label = Tex("beta($\\alpha$ = " + str(post_a) + ", $\\beta$ = " + str(post_b) + ")", font_size = 35)
			post_label.move_to(prior_label)

			self.play(
				ReplacementTransform(prior, posterior), 
				Transform(caption, new_caption), 
				ReplacementTransform(prior_label, post_label), 
				ReplacementTransform(prior_area, post_area),
				ReplacementTransform(line_ub, post_line_ub),
				ReplacementTransform(ub_text, post_ub_text),
				run_time=sub_run_time
			)

			prior = posterior
			prior_label = post_label
			prior_area = post_area
			line_ub = post_line_ub
			ub_text = post_ub_text
			sub_run_time = sub_run_time / 2

		self.wait(2)
		self.play(FadeOut(post_label))

		# Zoom into the posterior distribution
		axes_zoom = Axes(
			x_range=[0, 0.1, 0.01],
			y_range=[0, 40, 10],
			axis_config={
				"color": YELLOW,
				"include_ticks": True,
				"include_numbers": True
			},
			tips = False
		).scale(0.9)
		posterior_zoom = axes_zoom.plot(lambda x: beta.pdf(x, post_a, post_b), x_range=(0, 0.1, 0.001), color=WHITE)
		post_area_zoom = axes_zoom.get_area(posterior_zoom, x_range=(0, post_ub), color=BLUE, opacity = 0.25)
		point_ub_zoom = axes_zoom.coords_to_point(post_ub, 30)
		line_ub_zoom = axes_zoom.get_vertical_line(point_ub_zoom, line_config={"dashed_ratio": 0.85}, color=BLUE)
		ub_text_zoom = Tex("$\\theta_{95}$ = " + str(round(post_ub, 3)), font_size=35, color=BLUE)
		ub_text_zoom.next_to(line_ub_zoom, RIGHT)
		point_mat_zoom = axes_zoom.coords_to_point(0.05, 35)
		line_mat_zoom = axes_zoom.get_vertical_line(point_mat_zoom, line_config={"dashed_ratio": 0.85}, color=RED)
		mat_text_zoom = Tex("$\\theta_{max}$ = 0.05", font_size=35, color=RED)
		mat_text_zoom.next_to(line_mat_zoom, RIGHT)

		self.play(
			ReplacementTransform(posterior, posterior_zoom),
			ReplacementTransform(post_area, post_area_zoom),
			ReplacementTransform(axes_long, axes_zoom),
			ReplacementTransform(line_mat, line_mat_zoom),
			ReplacementTransform(mat_text, mat_text_zoom),
			ReplacementTransform(ub_text, ub_text_zoom),
			ReplacementTransform(line_ub, line_ub_zoom)
		)
		self.wait(1)

		# Put the texts beside each other
		ub_text_zoom_conc = Tex("$\\theta_{95}$", font_size=35, color=BLUE)
		ub_text_zoom_conc.next_to(line_mat_zoom, RIGHT)
		oth_text_zoom_conc = Tex("$<$", font_size=35, color=WHITE)
		oth_text_zoom_conc.next_to(ub_text_zoom_conc, RIGHT)
		mat_text_zoom_conc = Tex("$\\theta_{max}$", font_size=35, color=RED)
		mat_text_zoom_conc.next_to(oth_text_zoom_conc, RIGHT)

		self.play(
			ReplacementTransform(ub_text_zoom, ub_text_zoom_conc),
			Write(oth_text_zoom_conc),
			ReplacementTransform(mat_text_zoom, mat_text_zoom_conc),
		)
		self.wait(1)

		# Add a rectangle around the minimum saple size
		sample_size_rect = SurroundingRectangle(caption[0][0:16], color=YELLOW, buff=0.1)
		self.play(Create(sample_size_rect))
		self.wait(2)

		# Clear the scene
		self.play(FadeOut(VGroup(axes_zoom, sample_size_rect, title, caption, posterior_zoom, post_area_zoom, axes_zoom, line_mat_zoom, mat_text_zoom_conc, oth_text_zoom_conc, ub_text_zoom_conc, line_ub_zoom)))
		self.next_section(skip_animations=False)

		# SCENE 4: PLANNING WITH AN IMPARTIAL PRIOR ############################

		axes_long = Axes(
			x_range=[0, 1, 0.1],
			y_range=[0, 50, 10],
			axis_config={
				"color": YELLOW,
				"include_ticks": True,
				"include_numbers": True
			},
			tips = False
		).scale(0.9)

		self.play(AnimationGroup(Create(axes_long.x_axis), Create(axes_long.y_axis), lag_ratio=0), run_time = 1.5)

		title = Text("Impartial prior distribution", font_size=40).next_to(axes_long, UP)

		self.play(Create(title))
		self.wait(1)
