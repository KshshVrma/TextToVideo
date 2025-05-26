from manim import *

class HelloWorld(Scene):
    def construct(self):
        square = Square()
        self.play(Create(square))
        circle = Circle()
        self.play(Transform(square, circle))
        text = Text("Hello, India!")
        self.play(Write(text))
        
