from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import PCMYKColor



black1 = PCMYKColor(0,0,0,100)
gray0 = PCMYKColor(0,0,0,30)
gray1 = PCMYKColor(0,0,0,80)
gray2 = PCMYKColor(0,0,0,60)
red1 = PCMYKColor(0,100,100,0)

a4_width, a4_height = A4
a5_page_width =  a4_height / 2 
a5_page_height = a4_width 

print("a5_page_width = ", a5_page_width)
print("a5_page_height = ", a5_page_height)

my_canvas = canvas.Canvas("writingpad.pdf")
#my_canvas.setFont("Helvetica", 12)#default

my_canvas.setStrokeColor(gray1)
my_canvas.line(0, a4_height/2, a4_width, a4_height/2)
#my_canvas.drawString(100,150,"Welcome to Reportlab!")

# my_canvas.saveState()
# my_canvas.rotate(90)
# my_canvas.drawString(a4_height/4,-10,"writng pad")
# my_canvas.drawString(a4_height*3/4,-10,"writng pad")
# my_canvas.restoreState()

#calendar general
#spacing
calendar_small_line_pos_horizontal = 0.7*a4_height/2 
calendar_small_line_pos_vertical = 0.15*a4_width
#calendar- for first half
time_start = 7
time_end = 21

for page_num in range(2):
    my_canvas.setFont("Helvetica", 12)
    offset = page_num * a5_page_width
    my_canvas.setStrokeColor(gray1)
    my_canvas.line(0, offset + calendar_small_line_pos_horizontal, a4_width, offset + calendar_small_line_pos_horizontal)#vertical full line for a5
    my_canvas.line(calendar_small_line_pos_vertical, offset + calendar_small_line_pos_horizontal, calendar_small_line_pos_vertical, offset + a4_height/2)#horizontal small line

    my_canvas.setFillColor(gray2)
    my_canvas.saveState()
    my_canvas.rotate(90)
    calendar_text_pos_x = offset + calendar_small_line_pos_horizontal  + 0.1*a4_height/2
    calendar_text_pos_y = -1*calendar_small_line_pos_vertical + 1
    my_canvas.drawString(calendar_text_pos_x,calendar_text_pos_y ,"Calendar")
    #my_canvas.drawString(a4_height*3/4,-10,"writng pad")
    my_canvas.restoreState()

    #grid
    space_hori = 15
    space_vert = 15
    num_lines_hori = int( a5_page_height / space_vert)
    num_lines_vert = int( calendar_small_line_pos_horizontal / space_hori)

    my_canvas.setStrokeColor(gray0)
    for i in range(num_lines_hori):
        line_pos_x = i * space_vert
        line_pos_start_y = offset 
        line_pos_end_y = offset + calendar_small_line_pos_horizontal
        my_canvas.line(line_pos_x, line_pos_start_y, line_pos_x, line_pos_end_y)
    for i in range(num_lines_vert):
        line_pos_y = i * space_hori + offset
        line_pos_start_x = 0 
        line_pos_end_x = a5_page_height
        my_canvas.line(line_pos_start_x, line_pos_y, line_pos_end_x, line_pos_y)

    my_canvas.setFillColor(black1)
    #time text
    my_canvas.setFont("Times-Roman", 6)
    time_hours = time_end - time_start
    space_per_hour = (a4_width - calendar_small_line_pos_vertical)/time_hours
    for i in range(int(time_hours)):
        line_pos_vert = calendar_small_line_pos_vertical + i* space_per_hour
        line_pos_hor = offset + calendar_small_line_pos_horizontal + 0.5
        my_canvas.line(line_pos_vert, line_pos_hor, line_pos_vert, offset + a4_height/2)
        temp_string = str(int(time_start)+i) + '.00-' + str(int(time_start)+i+1) +'.00'
        my_canvas.drawString(line_pos_vert+1,line_pos_hor ,temp_string)

my_canvas.save()