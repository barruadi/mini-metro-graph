from manim import *

class Intro(Scene):
    def construct(self):
        title = Text("Mini Metro", font_size=100)
        self.play(
            Write(title, run_time=3)   
        )

class Strategy(Scene):
    def construct(self):
        # TITLE
        title = Text("Strategy", font_size=90)
        self.play(Write(title, run_time=3))
        self.wait(3)


        #  FIRST STRATEGY
        strat_1 = Text("1. Avoid Duplicates", font_size=40)
        self.play(Unwrite(title))
        self.play(Write(strat_1))
        self.play(strat_1.animate.shift(UP * 3))

        square_1 = Square(0.8, fill_opacity=1)
        square_2 = Square(0.8, fill_opacity=1)
        square_3 = Square(0.8, fill_opacity=1)
        
        g = VGroup(square_1, square_2, square_3)
        g.set_color_by_gradient(RED, ORANGE, YELLOW)
        self.play(Write(g))
        self.play(g.animate.arrange(buff=1.5))
        line = Line(start=square_1.get_center(), end=square_3.get_center(), buff=0.5)
        self.play(Create(line))

        circle = Circle()
        circle.set_width(0.8)
        circle.set_fill(RED, opacity=1)
        triangle = Triangle()
        triangle.set_width(0.8)
        triangle.set_fill(YELLOW, opacity=1)
        circle.move_to(square_1.get_center())
        triangle.move_to(square_3.get_center())
        self.play(Transform(square_1, circle), Transform(square_3, triangle))
        self.play(Uncreate(line))
        self.play(Unwrite(g))
        self.play(Unwrite(strat_1))


        # SECOND STRATEGY
        strat_2 = Text("2. Prefer loops", font_size=40)
        square_4 = Square(0.8, fill_opacity=1)
        g2 = VGroup(circle, square_4, triangle)
        g2.set_color_by_gradient(RED, ORANGE, YELLOW)
        self.play(Write(strat_2))
        self.play(strat_2.animate.shift(UP * 3))
        self.play(Write(g2))
        self.play(g2.animate.arrange(buff=1.5))
        line_2 = Line(start=circle.get_center(), end=triangle.get_center())
        self.play(Create(line_2))
        line_loop = Line(path_arc=2, start=circle.get_center(), end=triangle.get_center())
        self.play(Create(line_loop))
        self.play(Unwrite(strat_2))
        self.play(Uncreate(g2))
        self.play(Uncreate(line_2))
        self.play(Uncreate(line_loop))


        # THIRD STRATEGY
        strat_3 = Text("3. Use unique station as connection", font_size=40)
        self.play(Write(strat_3))
        self.play(strat_3.animate.shift(UP * 3))

        loop1_circle_2 = Circle().set_width(0.8).shift(LEFT * 4)
        loop1_circle_2.set_fill(RED, opacity=1)
        loop1_triangle_2 = Triangle().set_width(0.8).shift(LEFT * 2).shift(DOWN * 2)
        loop1_triangle_2.set_fill(YELLOW, opacity=1)
        loop1_rectangle = Square(0.8, fill_opacity=1).shift(LEFT * 2).shift(UP * 2).set_fill(ORANGE, opacity=1)
        loop1_g = VGroup(loop1_circle_2, loop1_triangle_2, loop1_rectangle)

        loop2_circle_2 = Circle().set_width(0.8).shift(RIGHT * 4)
        loop2_circle_2.set_fill(GREEN, opacity=1)
        loop2_triangle_2 = Triangle().set_width(0.8).shift(RIGHT * 2).shift(DOWN * 2)
        loop2_triangle_2.set_fill(BLUE, opacity=1)
        loop2_rectangle = Square(0.8, fill_opacity=1).shift(RIGHT * 2).shift(UP * 2).set_fill(PURPLE, opacity=1)
        loop2_g = VGroup(loop2_circle_2, loop2_triangle_2, loop2_rectangle)
        line_2 = Circle().set_width(4).shift(LEFT * 2)
        line_3 = Circle().set_width(4).shift(RIGHT * 2)
        middle = Square(0.8, fill_opacity=1).set_fill(WHITE, opacity=1)
        middle_transform = Star().set_width(0.8).set_fill(WHITE, opacity=1)
        self.play(Write(loop1_g), Write(loop2_g), Write(line_2), Write(line_3))
        self.play(Write(middle))
        self.play(Transform(middle, middle_transform))

        self.play(Unwrite(strat_3))
        self.play(Unwrite(loop1_g), Unwrite(loop2_g), Unwrite(line_2), Unwrite(line_3), Unwrite(middle))
        

        # FOURTH STRATEGY
        strat_4 = Text("4. Use express railway", font_size=40)
        self.play(Write(strat_4))
        self.play(strat_4.animate.shift(UP * 3))
        loop1_circle_2 = RegularPolygon(n=5).set_width(0.8).shift(LEFT * 6)
        loop1_circle_2.set_fill(RED, opacity=1)
        loop1_triangle_2 = Triangle().set_width(0.8).shift(LEFT * 4).shift(DOWN * 2)
        loop1_triangle_2.set_fill(YELLOW, opacity=1)
        loop1_rectangle = Square(0.8, fill_opacity=1).shift(LEFT * 4).shift(UP * 2).set_fill(ORANGE, opacity=1)
        loop1_circle_3 = Circle().set_width(0.8).shift(LEFT * 2)
        loop1_circle_3.set_fill(RED, opacity=1)
        loop1_g = VGroup(loop1_circle_2, loop1_triangle_2, loop1_rectangle, loop1_circle_3)

        loop2_circle_2 = Star().set_width(0.8).shift(RIGHT * 6)
        loop2_circle_2.set_fill(GREEN, opacity=1)
        loop2_triangle_2 = Triangle().set_width(0.8).shift(RIGHT * 4).shift(DOWN * 2)
        loop2_triangle_2.set_fill(BLUE, opacity=1)
        loop2_rectangle = Square(0.8, fill_opacity=1).shift(RIGHT * 4).shift(UP * 2).set_fill(PURPLE, opacity=1)
        loop2_circle_3 = Circle().set_width(0.8).shift(RIGHT * 2)
        loop2_circle_3.set_fill(RED, opacity=1)
        loop2_g = VGroup(loop2_circle_2, loop2_triangle_2, loop2_rectangle, loop2_circle_3)

        line_2 = Circle().set_width(4).shift(LEFT * 4)
        line_3 = Circle().set_width(4).shift(RIGHT * 4)
        express_line = Line(start=loop1_circle_2.get_center(), end=loop2_circle_2.get_center())
        express_line.set_color(YELLOW)
        self.play(Write(loop1_g), Write(loop2_g), Write(line_2), Write(line_3))
        self.play(Write(express_line))
        self.play(Unwrite(strat_4))
        self.play(Unwrite(loop1_g), Unwrite(loop2_g), Unwrite(line_2), Unwrite(line_3), Unwrite(express_line))


class SoundSimple(Scene):
    def construct(self):
        text = Text("Sound Simple, Right?", font_size=90)
        self.add(text)

class Plan(Scene):
    def construct(self):
        title = Text("Plan", font_size=90)
        self.play(Write(title, run_time=3))
        plan_1 = Text("1. Create replica using Python", font_size=40)
        self.play(Write(plan_1))
        plan_2 = Text("2. Make the algorithm", font_size=40)
        self.play(Write(plan_2))
        plan_3 = Text("3. Take the conclusion", font_size=40)
        self.play(Write(plan_3))

class RandomList(Scene):
    def construct(self):
        Title = Text("Random List", font_size=90)
        self.play(Write(Title, run_time=3))
        random_1 = Text("1. Random station spawn and shape", font_size=40)
        self.play(Write(random_1))
        random_2 = Text("2. Random passenger spawn and shape", font_size=40)
        self.play(Write(random_2))
        random_3 = Text("3. Random reward", font_size=40)
        self.play(Write(random_3))

        self.wait(3)
        self.play(Unwrite(random_1), Unwrite(random_3))