from src.graphics.graphics_object import GraphicsObject

class Player:

	def __init__(self):
		self._moneyOwned = None
		self._currentPosition: int = None
		self._maal: GraphicsObject = None

		self._cardsOwned = None
		self._penaltyBuffer = None