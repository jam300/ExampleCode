import random

class Card(object):
	def __init__(self,suit,value):
		self.suit=suit
		self.value=value

	def showCard(self):
		print("{0} of {1}".format(self.value,self.suit))

	def __str__(self):
		return "{0} of {1}".format(self.value,self.suit)

class Deck(object):
	def __init__(self):
		self.cards = []
		self.build()

	def build(self):
		for s in ["Spades", "Clubs", "Diamods", "Hearts"]:
			for v in range(1,14):
				self.cards.append(Card(s,v))
				#print ("{0} of {1}".format(v,s))

	def showDeck(self):
		for c in self.cards:
			print(c)

	def shuffle(self):
		for i in range (len(self.cards)-1,0,-1):
			rand = random.randint(0,i)
			self.cards[i],self.cards[rand] = self.cards[rand],self.cards[i]

	def drawCard(self):
		return self.cards.pop()


	def __str__(self):
		for c in self.cards:
			c.showCard()

class Player(object):

	def __init__(self,name):
		self.name = name
		self.hand = []

	def draw(self,deck):
		self.hand.append(deck.drawCard())
		return self

	def showhand(self):
		for card in self.hand:
			card.showCard()

	def discard(self):
		return self.hand.pop()


def main():
	deck = Deck()
	deck.shuffle()
	deck.showDeck()
	#print(deck)
	#bob = Player("Bob")
	#bob.draw(deck).draw(deck)
	#bob.showhand()


if __name__ == '__main__':
	main()