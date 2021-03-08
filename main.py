from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()
add_edge(matrix, 50, 450, 0, 100, 450, 0)
add_edge(matrix, 50, 450, 0, 50, 400, 0)
add_edge(matrix, 100, 450, 0, 100, 400, 0)
add_edge(matrix, 100, 400, 0, 50, 400, 0)


draw_lines( matrix, screen, color )
display(screen)
