class Card:

	class CardAction: # enumerator
		PAY_MONEY = 1
		# add more?

	def __init__(self):
		self._uniqueIndex: int = None
		self._name: str = None
		self._information: str = None

		self._type: CardAction = None

		pass