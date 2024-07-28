from manim import *
import numpy as np
from scipy.stats import beta

class TransformBetaDistributionGraph(Scene):
	def construct(self):
		
		# Add the axes
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
		xlabel = axes_short.get_x_axis_label(
			Tex("Population misstatement ($\\theta$)").scale(0.75), edge=DOWN, direction=DOWN, buff=0.5
		)
		ylabel = axes_short.get_y_axis_label(
			Text("Density").scale(0.55).rotate(90 * DEGREES), edge=LEFT, direction=LEFT, buff=0.3
		)
		title = Text("Prior distribution", font_size=40)
		title.next_to(axes_short, UP)  # Position the text above the axes
		self.add(axes_short, xlabel, ylabel, title)
		self.wait(0.5)

		# Add the prior distribution
		theta = np.linspace(0, 1, 1000)
		prior_a, prior_b = 1, 1
		short_prior = axes_short.plot(lambda x: beta.pdf(x, prior_a, prior_b), x_range=(0, 1, 0.001), color=WHITE)
		self.play(Create(short_prior), run_time=2)

		# Add the functional form of the prior distribution
		short_prior_label = Tex("beta($\\alpha$ = 1, $\\beta$ = 1)", font_size = 35)
		short_prior_label.next_to(short_prior, UP)
		self.play(Write(short_prior_label), run_time = 0.5)
		self.wait(2)

		# Shade the 95 percent probability area
		prior_ub = beta.ppf(0.95, prior_a, prior_b)
		short_prior_area = axes_short.get_area(short_prior, x_range=(0, prior_ub), color=BLUE, opacity =0.25)
		self.play(Create(short_prior_area), run_time=1.5)

		# Create the probability text
		area_text = Tex("$p$ = 0.95", font_size =40)
		area_text.move_to(short_prior_area)
		self.play(Write(area_text))
		self.wait(1.5)
		self.play(FadeOut(area_text))

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
		self.wait(2)

		# Change the title above the graph
		title_post = Text("Posterior distribution", font_size=50)
		title_post.next_to(axes_short, UP)
		caption = Tex("Sample size ($n$) = 0\\hspace{0.25cm}Misstatements ($k$) = 0", font_size=40)
		caption.next_to(title_post, DOWN)
		self.play(Transform(title, title_post), Create(caption))
		self.wait(1)

		# Slowly update the prior into the posterior until n = 9
		n, k = 0, 0
		for i in range(9):
			n = n + 1
			if i == 8:
				k = k + 1
			post_a = prior_a + k
			post_b = prior_b + n - k
			posterior = axes_long.plot(lambda x: beta.pdf(x, post_a, post_b), x_range=(0, 1, 0.001), color=WHITE)
			post_ub = beta.ppf(0.95, post_a, post_b)
			post_area = axes_short.get_area(posterior, x_range=(0, post_ub), color=BLUE, opacity = 0.25)
			new_caption = Tex("Sample size ($n$) = " + str(n) + "\\hspace{0.25cm}Misstatements ($k$) = " + str(k), font_size=40)
			new_caption.next_to(title_post, DOWN)
			post_label = Tex("beta($\\alpha$ = " + str(post_a) + ", $\\beta$ = " + str(post_b) + ")", font_size = 35)
			post_label.move_to(prior_label)
			self.play(
				ReplacementTransform(prior, posterior), 
				ReplacementTransform(caption, new_caption), 
				ReplacementTransform(prior_label, post_label), 
				ReplacementTransform(prior_area, post_area),
				run_time=0.25
			)
			prior = posterior
			caption = new_caption
			prior_label = post_label
			prior_area = post_area
			self.wait(0.5)

		# Show the materiality as a line with text
		point = axes_long.coords_to_point(0.05, 10)
		dot = Dot(point)
		line = axes_long.get_vertical_line(point, line_config={"dashed_ratio": 0.85})
		self.play(Create(dot), Create(line))

		materiality_text = Tex("$\\theta_{max}$ = 0.05", font_size=25)
		materiality_text.next_to(dot, RIGHT)
		self.play(Write(materiality_text))

		self.wait(2)

		# Update the prior now much faster until n = 92, k = 1
		sub_run_time = 0.25
		for i in range(83):
			n = n + 1
			post_a = prior_a + k
			post_b = prior_b + n - k
			posterior = axes_long.plot(lambda x: beta.pdf(x, post_a, post_b), x_range=(0, 1, 0.001), color=WHITE)
			post_ub = beta.ppf(0.95, post_a, post_b)
			post_area = axes_short.get_area(posterior, x_range=(0, post_ub), color=BLUE, opacity = 0.25)
			new_caption = Tex("Sample size ($n$) = " + str(n) + "\\hspace{0.25cm}Misstatements ($k$) = " + str(k), font_size=40)
			new_caption.next_to(title_post, DOWN)
			post_label = Tex("beta($\\alpha$ = " + str(post_a) + ", $\\beta$ = " + str(post_b) + ")", font_size = 35)
			post_label.move_to(prior_label)
			self.play(
				ReplacementTransform(prior, posterior), 
				ReplacementTransform(caption, new_caption), 
				ReplacementTransform(prior_label, post_label), 
				ReplacementTransform(prior_area, post_area),
				run_time=sub_run_time
			)
			prior = posterior
			caption = new_caption
			prior_label = post_label
			prior_area = post_area
			sub_run_time = sub_run_time / 2

		# Hold the final frame for a few seconds
		self.wait(2)
