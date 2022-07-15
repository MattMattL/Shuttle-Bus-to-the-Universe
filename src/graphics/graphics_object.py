import math
from src.graphics.line_elements import LineElements

class GraphicsObject:

	_DEGREE_TO_RADIAN_FACTOR = math.pi / 180

	_allLineElements: list = []

	_currentLineElements: LineElements = None
	_currentAngle = 0

	def __init__(self):
		self._allLineElements = []
		pass

	def newLineElements(self):
		self._currentLineElements = LineElements()
		return self

	def setColor(self, color: str):
		self._currentLineElements.setColor(color)
		return self

	def setThickness(self, thickness):
		self._currentLineElements.setThickness(thickness)
		return self

	def startFrom(self, x, y):
		self._currentLineElements.addLineElement(x, y)
		return self

	def setAngle(self, relative=None, absolute=None): # in degree angles
		if relative is not None:
			self._currentAngle += relative * self._DEGREE_TO_RADIAN_FACTOR
		elif absolute is not None:
			self._currentAngle = absolute * self._DEGREE_TO_RADIAN_FACTOR
		else:
			self._currentAngle = 0

		return self

	def moveBy(self, length):
		x0, y0 = self._currentLineElements.getLastCoordinates()

		x = x0 + length * math.cos(self._currentAngle)
		y = y0 + length * math.sin(self._currentAngle)

		self._currentLineElements.addLineElement(x, y)

		return self

	def endElements(self):
		self._allLineElements.append(self._currentLineElements)
		return self

	def getAllLineElements(self):
		return self._allLineElements
