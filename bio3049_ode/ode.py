from manimlib import *

class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()                   # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        #self.play(Create(circle))     # show the circle on screen
        self.add(circle)

class IntroScreens(Scene):
    def construct(self):
        maintitle = Text("BIO3049 Biological Modelling",
                font="Consolas", font_size=40)
        subtitle = Text(
            """
            What are Ordinary Differential Equations (ODEs)?\n
            Why are they useful for biologists?
            """,
            font="Arial", font_size=24,
            t2c={"Text": BLUE, "TexText": BLUE, "LaTeX": ORANGE}
        )
        VGroup(maintitle, subtitle).arrange(DOWN, buff=1)
        self.play(Write(maintitle))
        self.play(FadeIn(subtitle, UP))
        self.wait(2)

        keypoints1 = Text(
            "ODEs focus on rates of change rather than current values",
            font="Arial", font_size=24,
            t2c={"rates": GREEN}
        )
        keypoints2 = Text(
            "e.g. changes in populations of plants, animals, microbes over time",
            font="Consolas", font_size=24,
            t2c={"changes": ORANGE}
        )
        VGroup(keypoints1, keypoints2).arrange(DOWN, buff=0.8)
        self.play(FadeOut(maintitle), FadeOut(subtitle, shift=DOWN))
        self.play(Write(keypoints1))
        self.wait()
        self.play(Write(keypoints2))
        self.wait()
