import matplotlib.pyplot as plt

from src.board.player import Player
from src.graphics.graphics_object import GraphicsObject

class Board:

	_players: [Player] = []
	_graphicsObjects: [GraphicsObject] = []

	def __init__(self):
		# set graphics properties
		figure = plt.figure(figsize=(8, 7))

		PLOT_MARGIN = 10
		PLOT_SIZE = 1000

		plt.xlim(-PLOT_MARGIN, PLOT_SIZE + PLOT_MARGIN)
		plt.ylim(-PLOT_MARGIN, PLOT_SIZE + PLOT_MARGIN)
		plt.axis("off")

		# draw the basic map
		plt.plot([0, 1000], [0, 0], color='black', linewidth=1)
		plt.plot([1000, 1000], [0, 1000], color='black', linewidth=1)
		plt.plot([1000, 0], [1000, 1000], color='black', linewidth=1)
		plt.plot([0, 0], [1000, 0], color='black', linewidth=1)

		# test graphic object
		greenRectangle = GraphicsObject()
		greenRectangle \
				.newLineElements().setColor('green').setThickness(3).startFrom(600, 600) \
						.setAngle(absolute=0).moveBy(100) \
						.setAngle(absolute=90).moveBy(50) \
						.setAngle(absolute=180).moveBy(100) \
						.setAngle(absolute=270).moveBy(50).endElements() \
				.newLineElements().setColor('yellow').setThickness(2).startFrom(200, 200) \
						.setAngle(absolute=45).moveBy(50) \
						.setAngle(relative=90).moveBy(50) \
						.setAngle(relative=90).moveBy(50) \
						.setAngle(relative=90).moveBy(50).endElements()

		self.addGraphicsObject(greenRectangle)

	def addGraphicsObject(self, object: GraphicsObject):
		self._graphicsObjects.append(object)

	def renderGraphicsObjects(self):
		for object in self._graphicsObjects:
			allLineElements = object.getAllLineElements()

			for lineElement in allLineElements:
				print(lineElement.getXCoordinates())
				print(lineElement.getYCoordinates())

				plt.plot(lineElement.getXCoordinates(),
						lineElement.getYCoordinates(),
						color=lineElement.getColor(),
						linewidth=lineElement.getThickness())

	def drawBoard(self):
		self.renderGraphicsObjects()
		plt.show()
