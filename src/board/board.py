import matplotlib.pyplot as plt

from src.board.player import Player
from src.board.land import Land
from src.graphics.graphics_object import GraphicsObject
from src.database.shape_data import ShapeData

class Board:

	def __init__(self):
		# global
		self.PLOT_MARGIN = 1
		self.PLOT_SIZE = 100

		self._players: [Player] = []
		self._lands: [Land] = []
		self._graphicsObjects: [GraphicsObject] = []

		# set graphics properties
		figure = plt.figure(figsize=(7, 7))

		plt.xlim(-self.PLOT_MARGIN, self.PLOT_SIZE + self.PLOT_MARGIN)
		plt.ylim(-self.PLOT_MARGIN, self.PLOT_SIZE + self.PLOT_MARGIN)
		plt.axis("off")

		# draw the basic map
		plt.plot([0, self.PLOT_SIZE], [0, 0], color='black', linewidth=1)
		plt.plot([self.PLOT_SIZE, self.PLOT_SIZE], [0, self.PLOT_SIZE], color='black', linewidth=1)
		plt.plot([self.PLOT_SIZE, 0], [self.PLOT_SIZE, self.PLOT_SIZE], color='black', linewidth=1)
		plt.plot([0, 0], [self.PLOT_SIZE, 0], color='black', linewidth=1)

		shapeData = ShapeData()
		self.addGraphicsObject(shapeData.GREEN_SQUARES_EXAMPLE)
		self.addGraphicsObject(shapeData.BLUE_SQUARES_EXAMPLE)

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
