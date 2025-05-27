from manim import *

class helloworld(Scene):
    def construct(self):
        circle1 = Circle(radius=1, color=BLUE)
        circle2 = Circle(radius=0.5, color=RED)
        circle2.next_to(circle1, RIGHT, buff=0.5)
        self.play(Create(circle1), Create(circle2))