from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.coqui import CoquiService

import numpy as np
import scipy.stats as stats

def prior_to_posterior(self, n, k, prior_a, prior_b, axes, subtitle, distribution, line_ub, text_ub, area, label, run_time = 0.25):
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
		run_time = run_time
	)

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

		with self.voiceover("I will show you an example of a prior that is commonly used in practice: the uniform prior distribution.") as tracker:
			self.play(Write(title))
			self.play(AnimationGroup(Create(axes.x_axis), Create(axes.y_axis), lag_ratio = 0))
			self.play(Write(xlab))
			self.play(Write(ylab))

		# Prior distribution
		prior_a, prior_b = 1, 1
		distribution = axes.plot(lambda x: stats.beta.pdf(x, prior_a, prior_b), x_range = (0, 1, 0.001), color = WHITE)

		with self.voiceover("Here you can see the uniform prior as a solid line. Since it has equal density at all values, it represents the prior information that every value of the misstatement is equally plausible before seeing any data.") as tracker:
			self.play(Create(distribution))

		# Label
		label = Tex("beta($\\alpha$ = 1, $\\beta$ = 1)", font_size = 35)
		label.next_to(distribution, UP)

		with self.voiceover("Specifically, this prior distribution is a beta distribution with both shape parameters set to one.") as tracker:
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

		with self.voiceover("For example, the total probability of observing any value of the misstatement is equal to one.") as tracker:
			self.play(Create(area))
			self.play(Write(area_text))

		# Update shaded area text
		ub = stats.beta.ppf(0.95, prior_a, prior_b)
		new_area = axes.get_area(distribution, x_range = (0, ub), color = BLUE, opacity = 0.25)

		# Update the area text
		new_area_text = Tex("$p$ = 0.95", font_size = 40)
		new_area_text.move_to(area_text)

		with self.voiceover("By looking at a smaller range of values, the probability of observing these values is adjusted accordingly. For instance, the probability under the area you see here is 95 percent.") as tracker:
			self.play(Transform(area_text, new_area_text), Transform(area, new_area))
			self.wait(0.5)
			self.play(FadeOut(subtitle))

		# Subtitle (upper bound)
		subtitle = Tex("95 percent upper bound ($\\theta_{95}$)", font_size = 40, color = BLUE)
		subtitle.next_to(title, DOWN)

		with self.voiceover("The value of the misstatement below which the probability of occurrance is 95 percent can be seen as a 95 percent upper bound for the misstatement.") as tracker:
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

		with self.voiceover("Now, I will visualize how the uniform prior is updated to a posterior.") as tracker:
			self.play(Transform(title, new_title))

		subtitle = Tex("Sample size ($n$) = 0\\hspace{0.35cm}Misstatements ($k$) = 0", font_size = 40)
		subtitle.next_to(title, DOWN)

		with self.voiceover("For this, we need some data in the form of the sample size and the number of misstatements.") as tracker:
			self.play(Write(subtitle))

		# Update the prior to a posterior
		n, k = 1, 0

		with self.voiceover("We first observe a single correct item<bookmark mark='A'/>. You can see that this shifts the upper bound to the left, relative to the prior.") as tracker:
			self.wait_until_bookmark("A")
			prior_to_posterior(self, n, k, prior_a, prior_b, axes, subtitle, distribution, line_ub, text_ub, area, label)

		with self.voiceover("I will show you what happends to the upper bound if you observe 8 more correct items in the sample<bookmark mark='A'/>. As you can see, it gets increasingly lower.") as tracker:
			self.wait_until_bookmark("A")
			for i in range(8):
				n = n + 1
				prior_to_posterior(self, n, k, prior_a, prior_b, axes, subtitle, distribution, line_ub, text_ub, area, label)	
		
		k = k + 1
		with self.voiceover("However, watch what happends if you observe a misstatement. <bookmark mark='A'/>Now the upper bound moves to the right.") as tracker:
			self.wait_until_bookmark("A")
			prior_to_posterior(self, n, k, prior_a, prior_b, axes, subtitle, distribution, line_ub, text_ub, area, label)
	
		with self.voiceover("You might be wondering how many correct items should you see before the upper bound is below the performance materiality? I will increase the sample size all the way up <bookmark mark='A'/>until this happends.") as tracker:
			self.wait_until_bookmark("A")
			for i in range(83):
				n = n + 1
				prior_to_posterior(self, n, k, prior_a, prior_b, axes, subtitle, distribution, line_ub, text_ub, area, label, run_time = 0.05)

		rectangle = SurroundingRectangle(label, color = YELLOW, buff = 0.1)
		
		with self.voiceover("Based on these data, the posterior distribution<bookmark mark='A'/> is a beta distribution with parameters 2 and 92.") as tracker:
			self.wait_until_bookmark("A")
			self.play(Create(rectangle))
		
		self.play(FadeOut(rectangle))
		self.play(FadeOut(label))

		# Zoom in on the posterior distribution
		post_a = prior_a + k
		post_b = prior_b + n - k
		ub = stats.beta.ppf(0.95, post_a, post_b)
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

		with self.voiceover("By zooming in on the lower part of the graph, you can see that the upper bound is close to the performance materiality.") as tracker:
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

		# Morph upper bound and materiality labels
		new_text_ub = Tex("$\\theta_{95}$", font_size = 35, color = BLUE)
		new_text_ub.next_to(line_mat, RIGHT)
		text_other = Tex("$<$", font_size = 35, color = WHITE)
		text_other.next_to(new_text_ub, RIGHT)
		new_text_mat = Tex("$\\theta_{max}$", font_size = 35, color = RED)
		new_text_mat.next_to(text_other, RIGHT)

		with self.voiceover("In fact, the upper bound is now slightly lower than the performance materiality.") as tracker:
			self.play(
				Transform(text_ub, new_text_ub),
				Write(text_other),
				Transform(text_mat, new_text_mat)
			)

		# Add rectangle around minimum saple size
		rectangle = SurroundingRectangle(subtitle[0][0:16], color = YELLOW, buff = 0.1)

		with self.voiceover("This means that a sample of 92 items with one misstatement provides sufficient evidence to conclude that the misstatement is lower than the performance materiality of 5 percent.") as tracker:
			self.play(Create(rectangle))

		self.play(
			FadeOut(rectangle),
			FadeOut(subtitle),
			FadeOut(line_ub),
			FadeOut(line_mat),
			FadeOut(text_ub),
			FadeOut(text_mat),
			FadeOut(text_other)
		)

		# Add a line on the mode
		point_mle = axes.coords_to_point(k / n, stats.beta.pdf(k / n, post_a, post_b))
		dot_mle = Dot(point_mle, color = YELLOW)

		# Add text besides the line
		text_mle = Tex("$\\theta_{mle} = \\frac{1}{92} = 0.011$", font_size = 35, color = YELLOW)
		text_mle.next_to(dot_mle, RIGHT)

		with self.voiceover("The most likely misstatement is the value of the misstatement with the highest probability<bookmark mark='A'/>. In this case this is equal to one divided by 92, or one point one percent.") as tracker:
			self.wait_until_bookmark("A")
			self.play(
				Create(dot_mle),
				Create(text_mle)
			)

		# Clear the scene
		self.play(
			FadeOut(title),
			FadeOut(axes),
			FadeOut(xlab),
			FadeOut(ylab),
			FadeOut(distribution),
			FadeOut(area),
			FadeOut(dot_mle),
			FadeOut(text_mle)
		)
