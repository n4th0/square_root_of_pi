from manim import *


class sierpinski(Scene):
    def construct(self):

        t1 = Tex(r"Sierpiński relatives").set_color(YELLOW)
        self.play(Create(t1))
        self.wait(3)
        self.play(Uncreate(t1))

        def transform(e:VMobject, n) -> VMobject:
            if n < 4:
                return e.rotate(n*PI/2)
            else:
                return transform(e.scale([-1, 1, 0]), n-4)


        def sierpin(n, size, comb) -> VMobject:
            if n == 0:
                t = Square().scale(size*1/10)
                t.set_color([YELLOW, BLACK])
                # e = [point[0]+size, point[1], 0]
                # f = [point[0], point[1]+size/2, 0]
                # t.set_color_by_gradient(WHITE, BLACK)
                # t = createL(point, size)
                return t
            else:
                g2 = transform(sierpin(n-1, size/2, comb), comb[0])
                g1 = transform(sierpin(n-1, size/2, comb), comb[1])
                g3 = transform(sierpin(n-1, size/2, comb), comb[2])
                g1.next_to(g2, RIGHT, buff=0)
                g3.next_to(g2, UP, buff=0)
                return VGroup(g2, g1, g3)


        def explain(s):
            t1 = Tex(s).scale(1/2).set_color(YELLOW)
            self.play(Create(t1))
            self.wait(3)
            self.play(Uncreate(t1))
            # self.wait(2)


        comb = [0, 0, 1]

        s = r"The Sierpiński gasket can be formed by splitting a square into four equal pieces, each scaled by $\frac{1}{2}$, and then removing the upper right square."
        explain(s)
        self.wait(1)
        s = r"As a variation, however, we can rotate or reflect the scaled squares, thereby changing the orientation. For example, suppose we rotate the upper left square by 90° counterclockwise."
        explain(s)

        a1 = sierpin(2, 30, comb).shift((LEFT+DOWN)*3)
        self.play(Create(a1))
        self.wait(2)
        a2 = sierpin(6, 30, comb).shift((LEFT+DOWN)*3)
        self.play(ReplacementTransform(a1, a2))
        self.wait(2)
        self.play(Uncreate(a2))
        self.wait(1.5)

        s = r"A square has 8 symmetry transformations that preserve the basic shape. These are the identity (leave it alone), counterclockwise rotations by 90°, 180°, and 270°, horizontal and vertical reflections, and reflections across each diagonal, as shown below. These 8 transformations form a finite group, the symmetry group of the square, also known as the dihedral group of order 8."
        explain(s)

        s = r"Examples of these transformations: "
        explain(s)

        mess = Tex(r"Identity in all sides").scale(1/2).shift(UP*2+LEFT*4).set_color(YELLOW)
        self.play(Create(mess))

        self.wait(2)

        def evolve(comb, a):
            a1 = sierpin(1, 10, comb).shift(5*LEFT).shift(2*DOWN)
            a2 = sierpin(3, 20, comb).shift(2.5*LEFT).shift(2.3*DOWN)
            a3 = sierpin(6, 25, comb).shift(4*RIGHT).shift(2*LEFT).shift(2.5*DOWN)

            if a:

                self.play(Create(a1))
                self.play(Create(a2))
                self.play(Create(a3))
                self.wait(2)
                self.play(Uncreate(a1))
                self.play(Uncreate(a2))
                self.play(Uncreate(a3))
                self.wait(1)

            else:
                self.add(a1)
                self.add(a2)
                self.add(a3)
                self.wait(2)
                self.remove(a1)
                self.remove(a2)
                self.remove(a3)
                self.wait(1)


        evolve([0,0,0], True)
        self.play(Uncreate(mess))

        mess = Tex(r"Identity, rotated 270° and rotated 90°").scale(1/2).shift(UP*2+LEFT*4).set_color(YELLOW)
        self.play(Create(mess))

        self.wait(2)
        evolve([0,3,1], True)
        self.play(Uncreate(mess))
        mess = Tex(r"Identity, reflected and rotated 270° and rotated 270°").scale(1/2).shift(UP*2+LEFT*4).set_color(YELLOW)
        self.play(Create(mess))

        self.wait(2)
        evolve([0,7,3], True)
        self.play(Uncreate(mess))

        # self.wait(2)
        # evolve([2,2,2], True)














