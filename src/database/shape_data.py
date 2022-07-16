from src.graphics.graphics_object import GraphicsObject

class ShapeData:

	def __init__(self):
		self.BLUE_SQUARES_EXAMPLE = GraphicsObject()
		self.GREEN_SQUARES_EXAMPLE = GraphicsObject()

		self.initialiseShapes()

	def initialiseShapes(self):
		self.BLUE_SQUARES_EXAMPLE \
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
				.updateCenter()

		self.GREEN_SQUARES_EXAMPLE \
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
				.updateCenter() \
				.rotate(30)