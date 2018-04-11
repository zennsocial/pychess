import os
import unittest

from pychess.Players.engineNest import discoverer
from pychess.System import uistuff
from pychess.widgets import gamewidget
from pychess.perspectives.games import Games
from pychess.perspectives.learn import Learn
from pychess.perspectives.learn.EndgamesPanel import start_endgame_from, ENDGAMES
from pychess.perspectives.learn.LecturesPanel import start_lecture_from, LECTURES
from pychess.perspectives.learn.LessonsPanel import start_lesson_from, LESSONS
from pychess.perspectives.learn.PuzzlesPanel import start_puzzle_from, PUZZLES
from pychess.perspectives import perspective_manager

# fix PATH on travis
if "/usr/games" not in os.environ["PATH"]:
    os.environ["PATH"] = "/usr/games:%s" % os.environ["PATH"]

discoverer.pre_discover()


class LearnTests(unittest.TestCase):
    def setUp(self):
        widgets = uistuff.GladeWidgets("PyChess.glade")
        gamewidget.setWidgets(widgets)
        perspective_manager.set_widgets(widgets)

        self.games_persp = Games()
        perspective_manager.add_perspective(self.games_persp)

        self.learn_persp = Learn()
        perspective_manager.add_perspective(self.learn_persp)

    def test1(self):
        """ Start next endgame """
        pieces = ENDGAMES[0][0].lower()
        start_endgame_from(pieces)

    def test2(self):
        """ Start next lecture """
        filename = LECTURES[0][0]
        start_lecture_from(filename)

    def test3(self):
        """ Start next lesson """
        filename = LESSONS[0][0]
        start_lesson_from(filename)

    def test4(self):
        """ Start next puzzle """
        filename = PUZZLES[0][0]
        start_puzzle_from(filename)


if __name__ == '__main__':
    unittest.main()
