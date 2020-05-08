from simpleimage import SimpleImage
import math

# Domain of the plot
X_MIN = -10
X_MAX = 10

# Range of the plot
Y_MIN = -10
Y_MAX = 10

# Size of the plot in pixels
PLOT_WIDTH = 400
PLOT_HEIGHT = 400

# Color of the axes
AXIS_COLOR_R = 200
AXIS_COLOR_G = 0
AXIS_COLOR_B = 0

# Color of the plot
PLOT_COLOR_R = 0
PLOT_COLOR_G = 200
PLOT_COLOR_B = 0

# x and y step sizes
DELTA_X = 0.01
DELTA_Y = 0.01


def main():
	"""
	Make a blank plot, draw the x and y axis, plot the 
	function defined by plotted_function and show the plot.
	"""
	plot = make_blank_plot()
	plot = draw_axes(plot)
	plot = plot_function(plot)
	plot.show()


def ploted_function(x):
	"""
	Compute the ploted function at point :param:x
	"""
	# return math.cos(x)
	# return math.tanh(x)
	# return x**3
	return x ** 2


def make_blank_plot():
	"""
	Create an image with all pixel colors set to black
	"""
	plot = SimpleImage.blank(PLOT_WIDTH, PLOT_HEIGHT)
	for px in plot:
		px.red = 0
		px.green = 0
		px.blue = 0
	return plot


def x_to_pixel_x(x):
	"""
	Compute the horizontal pixel position for horizontal 
	position :param:x in the plotted coordinate system.

	Test Cases: 

	x = 0 should correspond to middle of the plot
	>>> x_to_pixel_x(0)
	200

	x = -10 should correspond to far left of the plot
	>>> x_to_pixel_x(-10)
	0

	x = 10 should correspond to far right of the plot
	Note: x=10 is outside of the plotting area 
	>>> x_to_pixel_x(10)
	400
	"""
	h_pixel_per_point = PLOT_WIDTH / (X_MAX - X_MIN)
	px = x * h_pixel_per_point + PLOT_WIDTH/2
	return int(px)


def y_to_pixel_y(y):
	"""
	Compute the horizontal pixel position for vertical 
	position :param:y in the plotted coordinate system

	Test Cases:

	y =  0 should correspond to the middle of the plot
	>>> y_to_pixel_y(0)
	200

	y=10 should correspond to the top of the plot.
	>>> y_to_pixel_y(10)
	0

	y=-10 should correspond to the bottom of the plot
	Note y=-10 is actually outside of the plotting area
	>>> y_to_pixel_y(-10)
	400
	"""
	v_pixel_per_point = PLOT_HEIGHT / (Y_MAX - Y_MIN)
	py = PLOT_HEIGHT/2 - y * v_pixel_per_point
	return int(py)


def draw_axes(plot):
	"""
	Draw the horizontal and vertical axes
	"""
	draw_x_axis(plot)
	draw_y_axis(plot)
	return plot


def draw_x_axis(plot):
	"""
	Draw the horizontal axis
	Set of points for which (x, 0) where x in [X_MIN, XMAX[ (x-max not included)
	"""
	x = X_MIN
	while x<X_MAX:
		px = x_to_pixel_x(x)
		py = y_to_pixel_y(0)
		pixel = plot.get_pixel(px, py)
		pixel.red = AXIS_COLOR_R
		pixel.green = AXIS_COLOR_G
		pixel.blue = AXIS_COLOR_B
		x+=DELTA_X
	return plot


def draw_y_axis(plot):
	"""
	Draw the vertical axis
	Set of points for which (0, y) where x in ]Y_MIN, Y_MAX] (Y_MIN not included)
	"""
	y = Y_MIN + DELTA_Y
	while y<Y_MAX:
		px = x_to_pixel_x(0)
		py = y_to_pixel_y(y)
		pixel = plot.get_pixel(px, py)
		pixel.red = AXIS_COLOR_R
		pixel.green = AXIS_COLOR_G
		pixel.blue = AXIS_COLOR_B
		y += DELTA_Y
	return plot


def plot_function(plot):
	"""
	Draw the points of the function defined by plotted_function()
	that are in range
	"""
	x = X_MIN
	while x < X_MAX:
		y = ploted_function(x)
		if y > Y_MIN and y <= Y_MAX:
			px = x_to_pixel_x(x)
			py = y_to_pixel_y(y)
			pixel = plot.get_pixel(px, py)
			pixel.red = PLOT_COLOR_R
			pixel.green = PLOT_COLOR_G
			pixel.blue = PLOT_COLOR_B

		x += DELTA_X
	return plot


if __name__ == '__main__':
	main()