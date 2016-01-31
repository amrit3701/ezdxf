import ezdxf
import csv
import math
import pdb 


############ Input values ##############

a = 10
A = 100
D = 20


############# layers #################

drawing = ezdxf.new(dxfversion='AC1027')
drawing.layers.create(name='base', dxfattribs={'color': 240})
drawing.layers.create(name='zigzag', dxfattribs={'color': 140})
drawing.layers.create(name='arrows')

############ functions ################

def arrow(bottom_point,arrow_point, length_arrow = 3):
    modelspace.add_line(bottom_point,arrow_point, dxfattribs={'layer': 'arrows', 'color': 4})
    vertex = arrow_point
    left_pt = (arrow_point[0] - length_arrow / 6.0 , arrow_point[1] - length_arrow )
    right_pt = (arrow_point[0] + length_arrow / 6.0 , arrow_point[1] - length_arrow)
    modelspace.add_trace([vertex, left_pt, right_pt], dxfattribs={'layer': 'arrows', 'color': 20})
    return

pdb.set_trace()
############# point list ################
points_list = [((A-a) / 2, 2*D), ((A-a) / 2, D), (0, D), (0, 0),
               (A, 0), (A, D), ((A + a) / 2, D), ((A + a) / 2, 2*D)]
zigzag = [((A - 2 *a) / 2, 2*D), ((A -  a) / 2, 2*D), ((A - a) / 2 + (a / 3), 2*D),
               ((A / 2), (a / 3) + 2*D),  ((A / 2), 2*D - (a / 3)),
               ((A + a) / 2 - (a / 3), 2*D), ((A + a)/ 2, 2*D), ((A + 2*a) / 2, 2*D)]


############# csv file ##################

string_for_csv = str()
for i in xrange(len(points_list)):
    string_for_csv = string_for_csv + str(points_list[i][0]) + "," + str(points_list[i][1]) + "\n"

inp = raw_input("Enter the name of csv file you want to generate: ")
fw = open(inp+".csv", "w")
fw.write(string_for_csv)


############### text ######################

modelspace = drawing.modelspace()
modelspace.add_text("a").set_pos((50,33), align='CENTER')
#modelspace.add_text('a', (50, 33), 'height': 2.5)
#modelspace.add_lwpolyline(points_list, dxfattribs={'color': 71})
modelspace.add_lwpolyline(points_list, dxfattribs={'layer': 'base'}) 
modelspace.add_lwpolyline(zigzag, dxfattribs={'layer': 'zigzag'}) 


############ arrow/trace #################

dist_of_arrow_from_footing_base = 10
no_of_arrows = 10
list_xcoordinates_for_arrows = [(float(A)/(no_of_arrows - 1))*i 
	for i in xrange(no_of_arrows + 1)]
list_bottom_points = zip(list_xcoordinates_for_arrows,[-dist_of_arrow_from_footing_base] * no_of_arrows)
list_arrow_points = zip(list_xcoordinates_for_arrows,[0] * no_of_arrows)
final_arrow_points = zip(list_bottom_points,list_arrow_points)
for i in xrange(len(final_arrow_points)):
    arrow(final_arrow_points[i][0], final_arrow_points[i][1])


############ base line for arrows ###############

modelspace.add_line(list_bottom_points[0],list_bottom_points[-1], dxfattribs={'layer': 'arrows', 'color': 4, 'linetype': 'DASHED'})

############### dxf drawing ####################
drawing.saveas("lw.dxf")
