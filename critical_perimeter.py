import csv
import math
import ezdxf
import pdb

drawing = ezdxf.new(dxfversion='AC1024')
modelspace = drawing.modelspace()
#modelspace.add_line((0, 0), (10, 0), dxfattribs={'color': 3})


def dim12_arrow(u1, u2, u3, u4, l1, l2, l3, l4, c1, c2, c3, c4):
    modelspace.add_line((c1, c2), (c3, c4))
    modelspace.add_line((u1, u2), (u3, u4))
    modelspace.add_line((l1, l2), (l3, l4))

def dim4_arrow(l11, l12, l13, l14):
    modelspace.add_line((l11, l12), (l13, l14))

def atrace(t1, t2, t3, t4, t5, t6):
    points_atrace = [(t1, t2), (t3, t4), (t5, t6), (t1, t2)]
    #modelspace.add_lwpolyline(points_atrace)
    hatch = modelspace.add_hatch(color=2)  # by default a solid fill hatch with fill color 7 (white/black)
    with hatch.edit_boundary() as boundary:  # edit boundary path (context manager)
    # every boundary path is always a 2D element
    # vertex format for the polyline path is: (x, y[, bulge])
    # there are no bulge values in this example
        boundary.add_polyline_path(points_atrace)




scl = 1
text_size = 2.5

# input file
f=open('Critical perimeter.csv')
lst={'A':'','a':'','d':''}
data=[row for row in csv.reader(f)]
for i in lst.keys():
    for j in range(len(data)):
            if(i==data[j][0]):
                    ans=data[j][1]
                    break;
    lst[i]=int(ans)

"""points_list =[(0,lst['A']), (0,0), (lst['A'],0), (lst['A'],lst['A']), (0,lst['A']),(((lst['A'] - lst['a']) / 2), ((lst['A'] + lst['a']) / 2)),
                            (((lst['A'] - lst['a']) / 2), ((lst['A'] - lst['a']) / 2)), (((lst['A'] + lst['a']) / 2), ((lst['A'] -lst['a']) / 2)),
                            (((lst['A'] + lst['a']) / 2), ((lst['A'] + lst['a']) / 2)), (((lst['A'] - lst['a']) / 2), ((lst['A'] + lst['a']) / 2)),
                            (((lst['A'] - lst['a'] - lst['d']) / 2), ((lst['A'] + lst['a'] + lst['d']) / 2)),
                            (((lst['A'] - lst['a'] - lst['d']) / 2), ((lst['A'] - lst['a'] - lst['d'] ) / 2)),
                            (((lst['A'] + lst['a'] + lst['d']) / 2), ((lst['A'] - lst['a'] - lst['d']) / 2)),
                            (((lst['A'] + lst['a'] + lst['d']) / 2), ((lst['A'] + lst['a'] + lst['d']) / 2)),
                            (((lst['A'] - lst['a'] - lst['d']) / 2), ((lst['A'] + lst['a'] + lst['d']) / 2))]
"""


points_list =[(0,scl*lst['A']), (0,0), (scl*lst['A'],0), (scl*lst['A'],scl*lst['A']), (0,scl*lst['A']),(scl*((lst['A'] - lst['a']) / 2), scl*((lst['A'] + lst['a']) / 2)),
                            (scl*((lst['A'] - lst['a']) / 2), scl*((lst['A'] - lst['a']) / 2)), (scl*((lst['A'] + lst['a']) / 2), scl*((lst['A'] -lst['a']) / 2)),
                            (scl*((lst['A'] + lst['a']) / 2), scl*((lst['A'] + lst['a']) / 2)), (scl*((lst['A'] - lst['a']) / 2), scl*((lst['A'] + lst['a']) / 2)),
                            (scl*((lst['A'] - lst['a'] - lst['d']) / 2), scl*((lst['A'] + lst['a'] + lst['d']) / 2)),
                            (scl*((lst['A'] - lst['a'] - lst['d']) / 2), scl*((lst['A'] - lst['a'] - lst['d'] ) / 2)),
                            (scl*((lst['A'] + lst['a'] + lst['d']) / 2), scl*((lst['A'] - lst['a'] - lst['d']) / 2)),
                            (scl*((lst['A'] + lst['a'] + lst['d']) / 2), scl*((lst['A'] + lst['a'] + lst['d']) / 2)),
                            (scl*((lst['A'] - lst['a'] - lst['d']) / 2), scl*((lst['A'] + lst['a'] + lst['d']) / 2))]


#pdb.set_trace()

"""string_for_csv = str()
for i in xrange(len(points_list)):

    string_for_csv = string_for_csv + str(points_list[i][0]) + "," + str(points_list[i][1]) + "\n"


# csv file
inp = raw_input("Enter the name of csv file you want to generate: ")
fw = open(inp+".csv", "w")
fw.write(string_for_csv)

# dxf drawing
drawing_name = raw_input("Enter a drawing name to be created without the extension dxf: ")
drawing = dxf.drawing(drawing_name+".dxf")
"""

#modelspace.add_lwpolyline(points_list, dxfattribs={'layer': 'box', 'color':2})
print points_list

# Squares:
#big square
points_big = [points_list[0], points_list[1], points_list[2], points_list[3], points_list[0]]

print "big rectangle "
print points_big
modelspace.add_lwpolyline(points_big)
#pdb.set_trace()

#modelspace.add_line(points_list[0],points_list[1], dxfattribs={'color': 3})
#modelspace.add_line(points_list[1],points_list[2], dxfattribs={'color': 3})
#modelspace.add_line(points_list[2],points_list[3], dxfattribs={'color': 3})
#modelspace.add_line(points_list[3],points_list[4], dxfattribs={'color': 3})
#modelspace.add_line(points_list[4],points_list[5], dxfattribs={'color': 3})

#small square
#modelspace.add_line(points_list[5],points_list[6], dxfattribs={'color': 3})
#modelspace.add_line(points_list[6],points_list[7], dxfattribs={'color': 3})
#modelspace.add_line(points_list[7],points_list[8], dxfattribs={'color': 3})
#modelspace.add_line(points_list[8],points_list[9], dxfattribs={'color': 2})
#modelspace.add_line(points_list[9],points_list[10], dxfattribs={'color': 2, 'linetype': 'DASHED'})

#middle square
points_middle = [points_list[10],points_list[11], points_list[12], points_list[13], points_list[10]]

print "points_middle"
print points_middle
modelspace.add_lwpolyline(points_middle, dxfattribs={'color': 3, 'linetype': 'DASHED'})

#modelspace.add_line(points_list[10],points_list[11], dxfattribs={'color': 3, 'linetype': 'DASHED'})
#modelspace.add_line(points_list[11],points_list[12], dxfattribs={'color': 3, 'linetype': 'DASHED'})
#modelspace.add_line(points_list[12],points_list[13], dxfattribs={'color': 3, 'linetype': 'DASHED'})
#modelspace.add_line(points_list[13],points_list[14], dxfattribs={'color': 3, 'linetype': 'DASHED'})

points_small = [points_list[5], points_list[6], points_list[7], points_list[8], points_list[9]]
print "points_small"
print points_small

hatch = modelspace.add_hatch(color=2)  # by default a solid fill hatch with fill color 7 (white/black)
with hatch.edit_boundary() as boundary:  # edit boundary path (context manager)
    # every boundary path is always a 2D element
    # vertex format for the polyline path is: (x, y[, bulge])
    # there are no bulge values in this example
    boundary.add_polyline_path(points_small)


# Diagonal lines:
modelspace.add_line(points_list[0],points_list[5], dxfattribs={'color': 4})
modelspace.add_line(points_list[1],points_list[6], dxfattribs={'color': 4})
modelspace.add_line(points_list[2],points_list[7], dxfattribs={'color': 4})
modelspace.add_line(points_list[3],points_list[8], dxfattribs={'color': 4})

"""
# text
drawing.add(dxf.text('A', height=text_size, halign=CENTER, alignpoint=(115, 50)))
drawing.add(dxf.text('A', height=text_size, halign=CENTER, alignpoint=(50, -8)))
drawing.add(dxf.text('a', height=text_size, halign=CENTER, alignpoint=(85, 52)))
drawing.add(dxf.text('d/2', height=text_size, halign=CENTER, alignpoint=(85, 65)))
drawing.add(dxf.text('a', height=text_size, halign=CENTER, alignpoint=(48, 21)))
drawing.add(dxf.text('d/2', height=text_size, halign=CENTER, alignpoint=(35, 21)))
drawing.add(dxf.text('d/2', height=text_size, halign=CENTER, alignpoint=(64, 21)))
drawing.add(dxf.text('d/2', height=text_size, halign=CENTER, alignpoint=(85, 34)))
drawing.add(dxf.text('1', height=text_size, halign=CENTER, alignpoint=(30, 73)))
drawing.add(dxf.text('1\'', height=text_size, halign=CENTER, alignpoint=(70,73 )))
drawing.add(dxf.text('1', height=text_size, halign=CENTER, alignpoint=(30, 17)))
drawing.add(dxf.text('1\'', height=text_size, halign=CENTER, alignpoint=(70, 17)))
"""

# A upperright
u1 = (points_big[2][0]+(points_big[2][0]/10))-(0.02*(points_big[2][0]+(points_big[2][0]/10)))
u2 = points_big[2][0]
u3 = (points_big[2][0]+(points_big[2][0]/10))+(0.02*(points_big[2][0]+(points_big[2][0]/10)))
u4 = points_big[2][0]

l1 =  points_big[2][0]+points_big[2][0]/10
l2 =  points_big[3][1]
l3 =  points_big[2][0]+points_big[2][0]/10
l4 = 0

c1 = (points_big[2][0]+(points_big[2][0]/10))-(0.02*(points_big[2][0]+(points_big[2][0]/10)))
c2 = 0
c3 = (points_big[2][0]+(points_big[2][0]/10))+(0.02*(points_big[2][0]+(points_big[2][0]/10)))
c4 = 0

dim12_arrow(u1, u2, u3, u4, l1, l2, l3, l4, c1, c2, c3, c4)
atrace(scl*109.5, scl*97, scl*110.5, scl*97, scl*110, scl*100)
atrace(scl*109.5, scl*3, scl*110.5, scl*3, scl*110, 0)
#pdb.set_trace()

# A
# def dim12_arrow(u1, u2, u3, u4, l1, l2, l3, l4, c1, c2, c3, c4):
#u1 = points_list[3][0]
#u2 = points_list[0][1] - 10 * scl
#u4 = u2 + (4 * scl)
#c1 = points_list[-1][0]
#l2 = (u2 + u4) / 2
#dim12_arrow(u1, u2, u1, u4, u1, l2, c1, l2, c1, u2, c1, u4)
#atrace(3, -19.5, 3, -20.5, 0, -20)
#atrace(97, -19.5, 97, -20.5, 100, -20)
#drawing.add(dxf.text('A', height=textsize, halign=CENTER,
#                     alignpoint=((u1 + c1) / 2, u4)))



# A bottom
u1 = 0
u2 = -(points_big[2][0]/10) + (0.02*(points_big[2][0]+(points_big[2][0]/10)))
u3 = 0
u4 = -(points_big[2][0]/10) - (0.02*(points_big[2][0]+(points_big[2][0]/10)))

l1 = 0
l2 = -(points_big[2][0]/10)
l3 = points_big[2][0]
l4 = -(points_big[2][0]/10)

c1 = points_big[2][0]
c2 = -(points_big[2][0]/10) + (0.02*(points_big[2][0]+(points_big[2][0]/10)))
c3 = points_big[2][0]
c4 = -(points_big[2][0]/10) - (0.02*(points_big[2][0]+(points_big[2][0]/10)))

print l1, l2, l3, l4

dim12_arrow(u1, u2, u3, u4,    l1, l2, l3, l4,       c1, c2, c3, c4)

#atrace(scl*3, scl*-9.5 , scl*3, scl*-10.5 , 0, scl*-10)
#atrace(scl*97, scl*-9.5, scl*97, scl*-10.5, scl*100, scl*-10)



# Center lines
modelspace.add_line((points_big[2][0]/2, points_big[2][0]),(points_big[2][0]/2, scl*0), dxfattribs= {'layer': 'TESTLAYER', 'linetype': 'CENTER'})
modelspace.add_line((scl*0, points_big[2][0]/2), (points_big[2][0], points_big[2][0]/2), dxfattribs={'layer': 'TESTLAYER','linetype': 'CENTER'})


# d/2
#pdb.set_trace()

u1 = (points_middle[3][1] + points_middle[3][1]/7) - (0.02*(points_big[2][0]+(points_big[2][0]/10)))
u2 = points_middle[3][1]
u3 = (points_middle[3][1] + points_middle[3][1]/7) + (0.02*(points_big[2][0]+(points_big[2][0]/10)))
u4 = points_middle[3][1]

l1 = points_middle[3][1] + points_middle[3][1]/7
l2 = points_middle[3][1]
l3 = points_middle[3][1] + points_middle[3][1]/7
l4 = points_middle[3][1] - points_middle[3][1]/7
print l1, l2, l3, l4

c1 = points_small[2][0] + points_small[2][0]/6 - (0.025*(points_big[2][0]+(points_big[2][0]/10)))
c2 = points_middle[3][1] - points_small[2][0]/6
c3 = (points_middle[3][1] + points_middle[3][1]/7) + (0.02*(points_big[2][0]+(points_big[2][0]/10)))
c4 = points_middle[3][1] - points_middle[3][1]/7
print c1, c2, c3, c4
dim12_arrow(u1, u2, u3, u4, l1, l2, l3, l4, c1, c2, c3, c4)

#dim12_arrow(scl*77, scl*70, scl*82, scl*70,       scl*80, scl*70, scl*80, scl*60,          scl*68, scl*60, scl*82, scl*60)
#atrace(scl*79.5, scl*67, scl*80.5, scl*67, scl*80, scl*70)
#atrace(scl*79.5, scl*63, scl*80.5, scl*63, scl*80, scl*60)

"""
# a
dim4_arrow(scl*80, scl*60, scl*80, scl*40)
atrace(scl*79.5, scl*57, scl*80.5, scl*57,scl*80, scl*60)
atrace(scl*79.5, scl*43, scl*80.5, scl*43,scl*80, scl*40)

# d/2
dim12_arrow(scl*77, scl*30, scl*82, scl*30, scl*80, scl*40, scl*80, scl*30, scl*68, scl*40, scl*82, scl*40)
atrace(scl*79.5, scl*33, scl*80.5, scl*33, scl*80, scl*30)
atrace(scl*79.5, scl*37, scl*80.5, scl*37, scl*80, scl*40)

# d/2 bottom
dim12_arrow(scl*30, scl*27, scl*30,scl*23, scl*30, scl*25, scl*40, scl*25, scl*40, scl*31, scl*40, scl*23)
atrace(scl*33, scl*24.5, scl*33, scl*25.5, scl*30, scl*25)
atrace(scl*37, scl*24.5, scl*37, scl*25.5, scl*40, scl*25)

# a bottom
dim4_arrow(scl*40, scl*25, scl*60, scl*25)
atrace(scl*43, scl*24.5, scl*43, scl*25.5, scl*40, scl*25)
atrace(scl*57, scl*24.5, scl*57, scl*25.5, scl*60, scl*25)

# d/2 bottom
dim12_arrow(scl*70, scl*23, scl*70, scl*27, scl*60, scl*25, scl*70, scl*25, scl*60, scl*31, scl*60, scl*22)
atrace(scl*63, scl*24.5, scl*63, scl*25.5, scl*60, scl*25)
atrace(scl*67, scl*24.5, scl*67, scl*25.5, scl*70, scl*25)
"""


drawing.saveas("critical_perimeter.dxf")


