import matplotlib.pyplot as plt

from src.board.player import Player
from src.board.land import Land
from src.graphics.graphics_object import GraphicsObject
from src.database.shape_data import ShapeData

class Board:

	def __init__(self):
		# global
		self._players: [Player] = []
		self._lands: [Land] = []

		self._figure = plt.figure(figsize=(10, 6))
		self._graphicsObjects: [GraphicsObject] = []

		# add panels
		self._boardPanel = self._addPanel([0.01, 0.01, 0.588, 0.98], 100, 1)
		self._controlPanel = self._addPanel([0.6, 0.01, 0.39, 0.98], 100, 1)

		self.addGraphicsObject(ShapeData().GREEN_SQUARES_EXAMPLE)
		self.addGraphicsObject(ShapeData().BLUE_SQUARES_EXAMPLE)

	def _addPanel(self, location: list, size: int, margin: int):
		axes = plt.axes(location)

		# set size
		axes.set_xlim(-margin, size + margin)
		axes.set_ylim(-margin, size + margin)
		axes.axis("off")

		# draw boundary lines
		axes.plot([0, size], [0, 0], color='black', linewidth=1)
		axes.plot([size, size], [0, size], color='black', linewidth=1)
		axes.plot([size, 0], [size, size], color='black', linewidth=1)
		axes.plot([0, 0], [size, 0], color='black', linewidth=1)

		return axes

	def addGraphicsObject(self, object: GraphicsObject):
		self._graphicsObjects.append(object)

	def renderGraphicsObjects(self):
		for object in self._graphicsObjects:
			allLineElements = object.getAllLineElements()

			for lineElement in allLineElements:
				self._boardPanel.plot(lineElement.getXCoordinates(),
						lineElement.getYCoordinates(),
						color=lineElement.getColor(),
						linewidth=lineElement.getThickness())

	def drawBoard(self):
		self.renderGraphicsObjects()
		plt.show()
