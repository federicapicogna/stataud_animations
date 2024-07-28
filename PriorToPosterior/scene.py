from manim import *
import numpy as np
from scipy.stats import beta

class TransformBetaDistributionGraph(Scene):
	def construct(self):
		
		# Add the axes
		axes_short = Axes(
			x_range=[0, 1, 0.1],
			y_range=[0, 5, 1],
			axis_config={
				"color": YELLOW,
				"include_ticks": True,
				"include_numbers": True
			},
			tips = False
		).scale(0.9)
		self.play(Create(axes_short), run_time=1)
		self.wait(0.5)

		# Add the x-label
		xlabel = axes_short.get_x_axis_label(
			Tex("Population misstatement ($\\theta$)").scale(0.75), edge=DOWN, direction=DOWN, buff=0.5
		)
		self.play(Write(xlabel), run_time = 0.5)
		self.wait(0.5)

		# Add the y-label
		ylabel = axes_short.get_y_axis_label(
			Text("Probability density").scale(0.55).rotate(90 * DEGREES), edge=LEFT, direction=LEFT, buff=0.2
		)
		self.play(Write(ylabel), run_time = 0.5)
		self.wait(0.5)

		# Add the prior distribution
		x = np.linspace(0, 1, 100)
		a, b = 1, 1
		y1 = beta.pdf(x, a, b)
		short_prior = axes_short.plot_line_graph(x, y1, line_color=WHITE, add_vertex_dots=False)
		self.play(Create(short_prior), run_time=2)
		self.wait(0.5)

		# Add the title above the graph
		title = Text("Prior Distribution", font_size=40)
		title.next_to(axes_short, UP)  # Position the text above the axes
		self.play(Write(title), run_time = 0.5)
		self.wait(2)

		# Extend the y-axis
		axes_long = Axes(
			x_range=[0, 1, 0.1],
			y_range=[0, 30, 5],
			axis_config={
				"color": YELLOW,
				"include_ticks": True,
				"include_numbers": True
			},
			tips = False
		).scale(0.9)
		prior = axes_long.plot_line_graph(x, y1, line_color=WHITE, add_vertex_dots=False)
		self.play(Transform(axes_short, axes_long), ReplacementTransform(short_prior, prior))

		# Change the title above the graph
		title_post = Text("Posterior Distribution", font_size=50)
		title_post.next_to(axes_long, UP)
		self.play(Transform(title, title_post))

		n = 0
		caption = Tex("$n$ = " + str(n) + ", $k$ = 0", font_size=40)
		caption.next_to(title_post, DOWN)
		self.play(Create(caption))

		# Update the prior into the posterior
		for i in range(20):
			n = n + 1
			b = b + 1
			y2 = beta.pdf(x, a, b)
			posterior = axes_long.plot_line_graph(x, y2, line_color=WHITE, add_vertex_dots=False)
			new_caption = Tex("$n$ = " + str(n) + ", $k$ = 0", font_size=40)
			new_caption.next_to(title_post, DOWN)
			self.play(ReplacementTransform(prior, posterior), ReplacementTransform(caption, new_caption), run_time=0.5)
			prior = posterior
			caption = new_caption
			self.wait(0.5)

		# Hold the final frame for a few seconds
		self.wait(2)
