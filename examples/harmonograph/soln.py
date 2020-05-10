import tkinter
import time
import math

"""
Parameters for the canvas and its update
"""
CANVAS_WIDTH = 600      # Width of drawing canvas in pixels
CANVAS_HEIGHT = 600     # Height of drawing canvas in pixels
PAUSE = 1/100.0         # Pause between canvas update (seconds)

"""
Parameters for the harmonograph. Feel free
to change them to get your own beautiful graph!
"""
AMPLITUDE_X = (CANVAS_WIDTH - 1) // 2
AMPLITUDE_Y = (CANVAS_HEIGHT - 1) // 2
FREQUENCY_X = 0.0014509
FREQUENCY_Y = 0.0014401
PHASE_X = 0.0
PHASE_Y = 0.5
DAMP_X = 0.0000097
DAMP_Y = 0.000011

DRAWING_SPEED = 10  # Controls the apparent speed of drawing

"""
Parameters to control an evolving color during
the drawing. The current code supports two color 
schemes: 'hsv' and 'twilight'. Feel free to include
your favorite palette.
"""
COLORMAP = 'twilight'
COLOR_CHANGE_SPEED = DRAWING_SPEED * 1E-3 # Controls how fast color evolves


def main():
    """
    Draw a harmonograph on a Tkinter canvas by 
    drawing successive line segments. 
    """
    canvas = make_canvas(CANVAS_WIDTH, CANVAS_HEIGHT, 'Harmonograph')

    # Coordinates of the center
    xc = CANVAS_WIDTH // 2
    yc = CANVAS_HEIGHT // 2

    counter = 0
    while True:
        # Calculate current coordinates
        t = counter * DRAWING_SPEED
        x = xc + sinusoid(t, AMPLITUDE_X, FREQUENCY_X, PHASE_X, DAMP_X)
        y = yc + sinusoid(t, AMPLITUDE_Y, FREQUENCY_Y, PHASE_Y, DAMP_Y)
        
        # Draw a line segment if we have at least two points
        # Use color = 'red', for example, for a fixed color
        if counter > 0:
            color = get_color(counter, COLORMAP)            
            canvas.create_line(x_prev, y_prev, x, y, fill=color)

        # Coordinates of the previous point
        x_prev = x
        y_prev = y

        counter += 1
        canvas.update()
        time.sleep(PAUSE)


def sinusoid(time, amplitude, frequency, phase, damp):
    """
    Returns the result of a damped sinusoidal function
    for a given time
    """
    return amplitude * math.sin(2 * math.pi * frequency * time + phase) \
           * math.exp(-time * damp) 


########################################
##### The following functions are  #####
##### provided. Do not modify them #####
########################################

def make_canvas(width, height, title):
    """
    Creates and returns a drawing canvas
    of the given int size with a blue border,
    ready for drawing.
    """
    top = tkinter.Tk()
    top.minsize(width=width, height=height)
    top.title(title)
    canvas = tkinter.Canvas(top, width=width + 1, height=height + 1)
    canvas.pack()
    return canvas


def get_color(index, colormap):
    """
    Returns a string in the hex format #rrggbb (8 bits per color)
    that corresponds to the color at index position. colormap is 
    a string that contains the name of the colormap to be used.
    Currently only supports 'hsv' and 'twilight'.
    """
    index = round(index * COLOR_CHANGE_SPEED)
    colormap = colormap.lower()
    if colormap == 'twilight':
        return TWILIGHT[index % 256]
    elif colormap == 'hsv':
        return HSV[index % 256]
    raise ValueError("Invalid colormap! Only supports 'hsv' and 'twilight'.")


"""
Color map for twilight and hsv, exported from the colormap in matplotlib
using the following snippet. You can create your own by selecting other
palettes available in matplotlib, or using the matplotlib module directly.

.. code-block:: python
    
    from pylab import *

    cmap = cm.get_cmap('hsv', 256)
    for i in range(cmap.N):
        rgb = cmap(i)[:3]
        print(matplotlib.colors.rgb2hex(rgb))
"""
TWILIGHT = ["#e2d9e2", "#e1d9e2", "#e0d9e2", "#ded9e1", "#ddd9e0", "#dcd9df", 
            "#dad8df", "#d8d8de", "#d6d7dd", "#d4d6dc", "#d2d5db", "#d0d4d9", 
            "#cdd3d8", "#cbd2d7", "#c8d0d6", "#c5cfd5", "#c2ced4", "#bfccd3", 
            "#bccbd1", "#b9c9d0", "#b6c8cf", "#b3c6ce", "#b0c5cd", "#adc3cd", 
            "#aac2cc", "#a7c0cb", "#a4beca", "#a1bdc9", "#9ebbc9", "#9cb9c8", 
            "#99b8c8", "#96b6c7", "#93b4c6", "#92b3c6", "#8eb1c5", "#8cafc5", 
            "#89adc5", "#88acc4", "#85a9c4", "#82a7c3", "#80a5c3", "#7fa5c3", 
            "#7ca2c2", "#7aa0c2", "#789ec2", "#779dc2", "#759ac1", "#7398c1", 
            "#7196c1", "#7195c0", "#6e92c0", "#6d90c0", "#6c8ebf", "#6b8dbf", 
            "#698abf", "#6888be", "#6786be", "#6785be", "#6682bd", "#657fbd", 
            "#647dbc", "#647cbc", "#6379bb", "#6277bb", "#6275ba", "#6172ba", 
            "#6171b9", "#606eb8", "#606cb8", "#6069b7", "#6067b6", "#5f65b5", 
            "#5f62b4", "#5f60b4", "#5f5fb3", "#5f5bb2", "#5f59b1", "#5f57b0", 
            "#5e54ae", "#5e52ad", "#5e4fac", "#5e4dab", "#5e4caa", "#5e48a8", 
            "#5e46a6", "#5e43a5", "#5d41a3", "#5d3ea1", "#5d3ca0", "#5d3a9e", 
            "#5c389d", "#5c359a", "#5b3298", "#5b3095", "#5a2e93", "#5a2b90", 
            "#59298e", "#58278b", "#58268a", "#572385", "#562182", "#551f7f", 
            "#531e7c", "#521c79", "#511a75", "#4f1972", "#4f1970", "#4c176b", 
            "#4b1668", "#491564", "#471461", "#46145e", "#44135a", "#421257", 
            "#411256", "#3f1251", "#3d114e", "#3c114b", "#3a1149", "#391146", 
            "#371144", "#361142", "#361141", "#34113e", "#33113c", "#32123a", 
            "#311339", "#301437", "#301437", "#311337", "#331237", "#341238", 
            "#341238", "#361139", "#381139", "#3a113a", "#3b113b", "#3d113c", 
            "#3f123d", "#41123d", "#43123e", "#461240", "#481341", "#4a1342", 
            "#4d1443", "#4f1444", "#521545", "#541546", "#561546", "#591648", 
            "#5c1749", "#5f174a", "#61184b", "#64194b", "#67194c", "#691a4d", 
            "#6c1b4e", "#6f1c4e", "#711d4f", "#741e4f", "#761f4f", "#792050", 
            "#7b2150", "#7e2250", "#7f2350", "#832550", "#852650", "#872750", 
            "#8a2950", "#8c2a50", "#8e2c50", "#902e50", "#922f50", "#943150", 
            "#963350", "#983550", "#9a3750", "#9c3950", "#9e3b50", "#a03d50", 
            "#a03e50", "#a34150", "#a54350", "#a64550", "#a84750", "#a94950", 
            "#ab4b50", "#ac4d51", "#ae5051", "#af5251", "#b15452", "#b25652", 
            "#b35953", "#b55b53", "#b65d54", "#b75f55", "#b86155", "#b96456", 
            "#ba6657", "#bb6958", "#bc6b59", "#bd6e5a", "#be705b", "#bf725d", 
            "#c0755e", "#c1775f", "#c27a61", "#c27c63", "#c37f64", "#c48166", 
            "#c58468", "#c5866a", "#c6876b", "#c68b6e", "#c78e71", "#c89073", 
            "#c89275", "#c99578", "#c9977b", "#ca9a7d", "#ca9c80", "#cb9f83", 
            "#cca186", "#cca389", "#cda68c", "#cda88f", "#ceab92", "#cfad96", 
            "#cfae97", "#d0b29c", "#d1b4a0", "#d1b6a3", "#d2b8a7", "#d3baaa", 
            "#d4bdad", "#d5bfb1", "#d6c1b4", "#d7c3b8", "#d8c5bb", "#d8c7be", 
            "#d9c9c2", "#dacbc5", "#dbccc8", "#dccecb", "#dccfcd", "#ddd1d1", 
            "#ded3d3", "#dfd4d6", "#dfd5d8", "#e0d6da", "#e0d7db", "#e1d8dd", 
            "#e1d8df", "#e2d9e0", "#e2d9e1", "#e2d9e2"]

HSV =      ["#ff0000", "#ff0600", "#ff0c00", "#ff1200", "#ff1800", "#ff1e00", 
            "#ff2300", "#ff2900", "#ff2f00", "#ff3500", "#ff3b00", "#ff4100", 
            "#ff4700", "#ff4d00", "#ff5300", "#ff5900", "#ff5f00", "#ff6400", 
            "#ff6a00", "#ff7000", "#ff7600", "#ff7c00", "#ff8200", "#ff8800", 
            "#ff8e00", "#ff9400", "#ff9a00", "#ff9f00", "#ffa500", "#ffab00", 
            "#ffb100", "#ffb700", "#ffbd00", "#ffc300", "#ffc900", "#ffcf00", 
            "#ffd500", "#ffdb00", "#ffe000", "#ffe600", "#ffec00", "#fef100", 
            "#fcf500", "#faf900", "#f8fd00", "#f4ff00", "#eeff00", "#e8ff00", 
            "#e2ff00", "#ddff00", "#d7ff00", "#d1ff00", "#cbff00", "#c5ff00", 
            "#bfff00", "#b9ff00", "#b3ff00", "#adff00", "#a7ff00", "#a2ff00", 
            "#9cff00", "#96ff00", "#90ff00", "#8aff00", "#84ff00", "#7eff00", 
            "#78ff00", "#72ff00", "#6cff00", "#66ff00", "#61ff00", "#5bff00", 
            "#55ff00", "#4fff00", "#49ff00", "#43ff00", "#3dff00", "#37ff00", 
            "#31ff00", "#2bff00", "#25ff00", "#20ff00", "#1aff00", "#14ff00", 
            "#0eff00", "#08ff00", "#06ff04", "#04ff08", "#02ff0c", "#00ff10", 
            "#00ff16", "#00ff1b", "#00ff21", "#00ff27", "#00ff2d", "#00ff33", 
            "#00ff39", "#00ff3f", "#00ff45", "#00ff4b", "#00ff51", "#00ff57", 
            "#00ff5c", "#00ff62", "#00ff68", "#00ff6e", "#00ff74", "#00ff7a", 
            "#00ff80", "#00ff86", "#00ff8c", "#00ff92", "#00ff97", "#00ff9d", 
            "#00ffa3", "#00ffa9", "#00ffaf", "#00ffb5", "#00ffbb", "#00ffc1", 
            "#00ffc7", "#00ffcd", "#00ffd3", "#00ffd8", "#00ffde", "#00ffe4", 
            "#00ffea", "#00fff0", "#00fff6", "#00fffc", "#00fcff", "#00f6ff", 
            "#00f0ff", "#00eaff", "#00e5ff", "#00dfff", "#00d9ff", "#00d3ff", 
            "#00cdff", "#00c7ff", "#00c1ff", "#00bbff", "#00b5ff", "#00afff", 
            "#00aaff", "#00a4ff", "#009eff", "#0098ff", "#0092ff", "#008cff", 
            "#0086ff", "#0080ff", "#007aff", "#0074ff", "#006eff", "#0069ff", 
            "#0063ff", "#005dff", "#0057ff", "#0051ff", "#004bff", "#0045ff", 
            "#003fff", "#0039ff", "#0033ff", "#002dff", "#0028ff", "#0022ff", 
            "#001cff", "#0016ff", "#0010ff", "#020cff", "#0408ff", "#0604ff", 
            "#0800ff", "#0e00ff", "#1300ff", "#1900ff", "#1f00ff", "#2500ff", 
            "#2b00ff", "#3100ff", "#3700ff", "#3d00ff", "#4300ff", "#4900ff", 
            "#4f00ff", "#5400ff", "#5a00ff", "#6000ff", "#6600ff", "#6c00ff", 
            "#7200ff", "#7800ff", "#7e00ff", "#8400ff", "#8a00ff", "#9000ff", 
            "#9500ff", "#9b00ff", "#a100ff", "#a700ff", "#ad00ff", "#b300ff", 
            "#b900ff", "#bf00ff", "#c500ff", "#cb00ff", "#d000ff", "#d600ff", 
            "#dc00ff", "#e200ff", "#e800ff", "#ee00ff", "#f400ff", "#f800fd", 
            "#fa00f9", "#fc00f5", "#fe00f1", "#ff00ed", "#ff00e7", "#ff00e1", 
            "#ff00db", "#ff00d5", "#ff00cf", "#ff00c9", "#ff00c3", "#ff00bd", 
            "#ff00b7", "#ff00b1", "#ff00ac", "#ff00a6", "#ff00a0", "#ff009a", 
            "#ff0094", "#ff008e", "#ff0088", "#ff0082", "#ff007c", "#ff0076", 
            "#ff0071", "#ff006b", "#ff0065", "#ff005f", "#ff0059", "#ff0053", 
            "#ff004d", "#ff0047", "#ff0041", "#ff003b", "#ff0035", "#ff0030", 
            "#ff002a", "#ff0024", "#ff001e", "#ff0018"]

if __name__ == '__main__':
    main()