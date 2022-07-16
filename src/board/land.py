from src.board.player import Player

class Land:

	_name: str = None
	_landInformation: str = None
	_initialPrice: int = None

	_currentPlayers: [Player] = []
	_owner: Player = None

	_basicBuildingPrice: int = None
	_mediumBuildingPrice: int = None
	_advancedBuildingPrice: int = None
	_basicBuildingsCount: int = None
	_mediumBuildingsCount: int = None
	_advancedBuildingsCount: int = None

	def __init__(self):
		pass

	def getCurrentPrice(self):
		pass