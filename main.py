from display import *
from draw import *
from parser import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()

#matrix_mult(make_rotZ(90), transform)
#print_matrix(transform)

parse_file( 'script', edges, transform, screen, color )
