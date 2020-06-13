from manimlib.imports import *
import math

class Graphing(GraphScene):
    CONFIG = {
        "x_min": -5,
        "x_max": 5,
        "y_min": -5,
        "y_max": 5,
        "graph_origin": ORIGIN,
        "function_color": WHITE,
        "axes_color": '#0000FF'
    }

    def func_to_graph(self, x):
        return (x**2)

    def func_to_graph2(self, x):
        # if x in range(-5, -2):
        #     return 4
        # if x in range(2, 5):
        #     return 4
        # if x in range(-2, 2):
        #     return (x**2)
        if x<=-2 or x>=2:
            return 4
        else: 
            return (x**2)



    def construct(self):
        text=TextMobject("Convex Function")
        text.to_corner(UL)
        text1=TextMobject("Non-Convex Function")
        text1.to_corner(UL)
        #Make the graph
        self.setup_axes(animate=True)
        func_graph=self.get_graph(self.func_to_graph, color=WHITE)
        graph_lab = self.get_graph_label(func_graph)
        func_graph2 = self.get_graph(self.func_to_graph2, color=WHITE)
        graph_lab2 = self.get_graph_label(func_graph)
        #horizontal rule
        x = self.coords_to_point(1, self.func_to_graph(1))
        y = self.coords_to_point(-1, self.func_to_graph(-1))
        horz_line = Line(x,y, color='#FFFF00')
        point1 = Dot(self.coords_to_point(1,self.func_to_graph(1)))
        point2 = Dot(self.coords_to_point(-1,self.func_to_graph(-1)))
        #tilted rule
        x = self.coords_to_point(-1, self.func_to_graph(-1))
        y = self.coords_to_point(3, self.func_to_graph2(3))
        tilt_line = Line(x,y, color='#FFFF00')
        point3 = Dot(self.coords_to_point(-1 ,self.func_to_graph(-1)))
        point4 = Dot(self.coords_to_point(3,self.func_to_graph2(3)))

        self.play(FadeIn(text))
        self.wait(2)
        self.play(ShowCreation(func_graph), Write(graph_lab))
        self.wait(2)
        self.play(ShowCreation(horz_line))
        self.add(point1, point2)
        self.wait(2)
        self.remove(text, graph_lab, horz_line, point1, point2, func_graph)
        self.wait(1.5)
        self.play(FadeIn(text1))
        self.wait(2)
        self.play(ShowCreation(func_graph2), Write(graph_lab2))
        self.wait(2)
        self.play(ShowCreation(tilt_line))
        self.add(point3, point4)
        self.wait(2)



