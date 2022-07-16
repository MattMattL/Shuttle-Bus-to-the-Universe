class Card:

	class CardAction: # enumerator
		PAY_MONEY = 1
		# add more?

	_uniqueIndex: int = None
	_name: str = None
	_information: str = None

	_type: CardAction = None

	def __init__(self):
		pass