from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix - 
	    takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
	 ident: set the transform matrix to the identity matrix - 
	 scale: create a scale matrix, 
	    then multiply the transform matrix by the scale matrix - 
	    takes 3 arguments (sx, sy, sz)
	 move: create a translation matrix, 
	    then multiply the transform matrix by the translation matrix - 
	    takes 3 arguments (tx, ty, tz)
	 rotate: create a rotation matrix,
	    then multiply the transform matrix by the rotation matrix -
	    takes 2 arguments (axis, theta) axis should be x, y or z
	 apply: apply the current transformation matrix to the 
	    edge matrix
	 display: draw the lines of the edge matrix to the screen
	    display the screen
	 save: draw the lines of the edge matrix to the screen
	    save the screen to a file -
	    takes 1 argument (file name)
	 quit: end parsing

See the file script for an example of the file format
"""
def parse_file( fname, points, transform, screen, color ):
    fo = open(fname, "r")
    lines = fo.read()
    lines = lines.split("\n")
    ima = 0
    while (ima < len(lines)):
        if (lines[ima].find('line') > -1):
            args = lines[ima+1]
            args = args.split(" ")
            add_edge(points, int(args[0]), int(args[1]), int(args[2]), int(args[3]), int(args[4]), int(args[5]))
            ima += 1
        elif (lines[ima].find('ident') > -1):
            ident(transform)
        elif (lines[ima].find('scale') > -1):
            args = lines[ima+1]
            args = args.split(" ")
            matrix_mult(make_scale(int(args[0]), int(args[1]), int(args[2])), transform)
            ima += 1
        elif (lines[ima].find('move') > -1):
            args = lines[ima+1]
            args = args.split(" ")
            matrix_mult(make_translate(int(args[0]), int(args[1]), int(args[2])), transform)
            ima += 1
        elif (lines[ima].find('rotate') > -1):
            args = lines[ima+1]
            args = args.split(" ")
            if (args[0].find('x') > -1):
                rot = make_rotX(int(args[1]))
            elif (args[0].find('y') > -1):
                rot = make_rotY(int(args[1]))
            elif (args[0].find('z') > -1):
                rot = make_rotZ(int(args[1]))
            matrix_mult(rot, transform)
            ima += 1
        elif (lines[ima].find('apply') > -1):
            print points
            matrix_mult(transform, points)
            print points
        elif (lines[ima].find('display') > -1):
            draw_lines(points, screen, color)
            display(screen)
        elif (lines[ima].find('save') > -1):
            draw_lines(points, screen, color)
            args = lines[ima+1]
            save_extension(screen, args)
            ima += 1
        ima += 1
    return
