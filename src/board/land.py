from src.board.player import Player

class Land:

	def __init__(self):
		self._name: str = None
		self._landInformation: str = None
		self._initialPrice: int = None

		self._currentPlayers: [Player] = []
		self._owner: Player = None

		self._basicBuildingPrice: int = None
		self._mediumBuildingPrice: int = None
		self._advancedBuildingPrice: int = None
		self._basicBuildingsCount: int = None
		self._mediumBuildingsCount: int = None
		self._advancedBuildingsCount: int = None

	def getCurrentPrice(self):
		pass