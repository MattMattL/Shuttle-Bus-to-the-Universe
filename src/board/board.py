import matplotlib.pyplot as plt

from src.board.player import Player
from src.graphics.graphics_object import GraphicsObject
from src.board.land import Land

class Board:

	_players: [Player] = []
	_lands: [Land] = []
	_graphicsObjects: [GraphicsObject] = []

	def __init__(self):
		# set graphics properties
		figure = plt.figure(figsize=(7, 7))

		PLOT_MARGIN = 1
		PLOT_SIZE = 100

		plt.xlim(-PLOT_MARGIN, PLOT_SIZE + PLOT_MARGIN)
		plt.ylim(-PLOT_MARGIN, PLOT_SIZE + PLOT_MARGIN)
		plt.axis("off")

		# draw the basic map
		plt.plot([0, PLOT_SIZE], [0, 0], color='black', linewidth=1)
		plt.plot([PLOT_SIZE, PLOT_SIZE], [0, PLOT_SIZE], color='black', linewidth=1)
		plt.plot([PLOT_SIZE, 0], [PLOT_SIZE, PLOT_SIZE], color='black', linewidth=1)
		plt.plot([0, 0], [PLOT_SIZE, 0], color='black', linewidth=1)

		# test graphic object
		greenRectangle = GraphicsObject()
		greenRectangle \
				.newLineElements().setColor('green').setThickness(3).startFrom(50, 50) \
						.setAngle(absolute=0).moveBy(10) \
						.setAngle(absolute=90).moveBy(10) \
						.setAngle(absolute=180).moveBy(10) \
						.setAngle(absolute=270).moveBy(10).endElements() \
				.newLineElements().setColor('green').setThickness(3).startFrom(30, 30) \
						.setAngle(absolute=0).moveBy(10) \
						.setAngle(absolute=90).moveBy(10) \
						.setAngle(absolute=180).moveBy(10) \
						.setAngle(absolute=270).moveBy(10).endElements() \
				.updateCenter()

		blueRectangle = GraphicsObject()
		blueRectangle \
				.newLineElements().setColor('blue').setThickness(3).startFrom(50, 50) \
						.setAngle(absolute=0).moveBy(10) \
						.setAngle(absolute=90).moveBy(10) \
						.setAngle(absolute=180).moveBy(10) \
						.setAngle(absolute=270).moveBy(10).endElements() \
				.newLineElements().setColor('blue').setThickness(3).startFrom(30, 30) \
						.setAngle(absolute=0).moveBy(10) \
						.setAngle(absolute=90).moveBy(10) \
						.setAngle(absolute=180).moveBy(10) \
						.setAngle(absolute=270).moveBy(10).endElements() \
				.updateCenter() \
				.rotate(60)

		self.addGraphicsObject(greenRectangle)
		self.addGraphicsObject(blueRectangle)

	def addGraphicsObject(self, object: GraphicsObject):
		self._graphicsObjects.append(object)

	def renderGraphicsObjects(self):
		for object in self._graphicsObjects:
			allLineElements = object.getAllLineElements()

			for lineElement in allLineElements:
				plt.plot(lineElement.getXCoordinates(),
						lineElement.getYCoordinates(),
						color=lineElement.getColor(),
						linewidth=lineElement.getThickness())

	def drawBoard(self):
		self.renderGraphicsObjects()
		plt.show()
