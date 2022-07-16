from src.board.land import Land
from src.graphics.graphics_object import GraphicsObject

class Player:

	_moneyOwned = None
	_currentPosition: int = None
	_currentLand: Land = None
	_maal: GraphicsObject = None

	_cardsOwned = None
	_penaltyBuffer = None

	def __init__(self):
		pass