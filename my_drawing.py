"""
File: 
Name:
----------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GRect, GLabel,GPolygon,GArc,GLine
from campy.graphics.gwindow import GWindow


def main():
    """
    TODO:
    """
def main():
    window = GWindow(width=800,height=500,title='kevin')
    # face=GOval(200,250,x=350,y=200)
    # face.filled=True
    # face.fill_color='green'
    # window.add(face)
    # l_eye=GOval(90,50,x=290,y=200)
    # l_eye.filled=True
    # l_eye.fill_color='brown'
    # window.add(l_eye)
    # r_eye=GOval(30,30,x=290,y=230)
    # r_eye.filled=True
    # r_eye.fill_color='olive'
    # window.add(r_eye)
    mouth=GRect(100,220,x=290,y=100)
    mouth.filled=True
    mouth.fill_color='yellow'
    window.add(mouth)
    label=GLabel('minions!')
    label.font='-50'
    label.color='brown'
    window.add(label,x=100,y=200)

    mouth=GRect(40,40.5,x=350,y=320)
    mouth.filled=True
    # mouth.fill_color='brown'
    window.add(mouth)

    mouth=GRect(40,40.5,x=290,y=320)
    mouth.filled=True
    # mouth.fill_color='brown'
    window.add(mouth)

    triangle=GPolygon()
    triangle.add_vertex((390,250))
    triangle.add_vertex((290,250))
    triangle.add_vertex((340,300))
    triangle.filled=True
    triangle.fill_color='blue'
    window.add(triangle)

    r_eye=GOval(50,50,x=290,y=120)
    r_eye.filled=True
    r_eye.fill_color='white'
    window.add(r_eye)

    l_eye=GOval(50,50,x=340,y=120)
    l_eye.filled=True
    l_eye.fill_color='white'
    window.add(l_eye)

    arc= GArc(300,200,40,50)
    arc.filled =True
    window.add(arc,x=300,y=50)


    # line=GLine(0,0,100,100)
    # window.add(line)



if __name__ == '__main__':
    main()
