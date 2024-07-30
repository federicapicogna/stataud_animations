from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.coqui import CoquiService

import numpy as np
import scipy.stats as stats

class EffectOfPrior(VoiceoverScene):
	def construct(self):
		self.set_speech_service(CoquiService(transcription_model = 'base'))

		# Data
		n, k = 0, 0

		# Title
		title = Text("The effect of the prior", color = WHITE, font_size = 40)
		title.to_edge(UP)

		with self.voiceover("Finally, I will show you the effect of the prior distribution on the posterior distribution.") as tracker:
			self.play(Write(title))

		# Subtitle
		subtitle = Tex("Sample size ($n$) = " + str(n) + "\\hspace{0.35cm}Misstatements ($k$) = " + str(k), color = WHITE, font_size = 40)
		subtitle.next_to(title, DOWN)

		with self.voiceover("Let's reset the data.") as tracker:
			self.play(Write(subtitle), run_time = tracker.duration)

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

		with self.voiceover("I will show you four different prior distributions.") as tracker:
			self.play(
				AnimationGroup(Create(axes_ul.x_axis), Create(axes_ul.y_axis), lag_ratio = 0),
				AnimationGroup(Create(axes_ur.x_axis), Create(axes_ur.y_axis), lag_ratio = 0),
				AnimationGroup(Create(axes_dl.x_axis), Create(axes_dl.y_axis), lag_ratio = 0),
				AnimationGroup(Create(axes_dr.x_axis), Create(axes_dr.y_axis), lag_ratio = 0)
			)

		# Distribution top left
		dist_ul = axes_ul.plot(lambda x: stats.beta.pdf(x, 1, 1), x_range = (0, 1, 0.001), color = WHITE)

		# Label top left
		label_ul = Tex("beta($\\alpha$ = 1, $\\beta$ = 1)", color = WHITE, font_size = 20)
		label_ul.next_to(dist_ul, DOWN)
		label_ul.shift(UP * 0.6)

		with self.voiceover("In the top left you see the uniform prior distribution.") as tracker:
			self.play(Create(dist_ul))
			self.play(Write(label_ul))

		# Distribution top right
		dist_ur = axes_ur.plot(lambda x: stats.beta.pdf(x, 1, 20), x_range = (0, 1, 0.001), color = WHITE)

		# Label top right
		label_ur = Tex("beta($\\alpha$ = 1, $\\beta$ = 20)", color = WHITE, font_size = 20)
		label_ur.next_to(dist_ur, DOWN)
		label_ur.shift(UP * 0.6)

		with self.voiceover("In the top right you see the beta distribution with parameters one and twenty.") as tracker:
			self.play(Create(dist_ur))
			self.play(Write(label_ur))

		# Distribution bottom left
		dist_dl = axes_dl.plot(lambda x: stats.beta.pdf(x, 2, 20), x_range = (0, 1, 0.001), color = WHITE)

		# Label bottom left
		label_dl = Tex("beta($\\alpha$ = 2, $\\beta$ = 20)", color = WHITE, font_size = 20)
		label_dl.next_to(dist_dl, DOWN)
		label_dl.shift(UP * 0.6)

		with self.voiceover("In the bottom left you see a third beta distribution. However, this one has parameters two and 20.") as tracker:
			self.play(Create(dist_dl))
			self.play(Write(label_dl))

		# Distribution bottom right
		dist_dr = axes_dr.plot(lambda x: stats.beta.pdf(x, 2, 35), x_range = (0, 1, 0.001), color = WHITE)

		# Label bottom right
		label_dr = Tex("beta($\\alpha$ = 2, $\\beta$ = 35)", color = WHITE, font_size = 20)
		label_dr.next_to(dist_dr, DOWN)
		label_dr.shift(UP * 0.6)

		with self.voiceover("Finally, in the bottom right you see the beta distribution with parameters two and 35.") as tracker:
			self.play(Create(dist_dr))
			self.play(Write(label_dr))

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

		with self.voiceover("I will again indicate the 95 percent upper bound and the performance materiality of 5 percent as lines.") as tracker:
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

		with self.voiceover("Now, I will pretend as if a sample of 30 items is observed sequentially. As you can see, the upper bound for priors that allocate more mass to lower values of the misstatement is lower than that of the uniform prior.") as tracker:
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
