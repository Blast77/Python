# Playing card classes and procedures
import random

card_ranks = { 1:'A', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9', 10:'10', 11:'J', 12:'Q', 13:'K', 14:'A' }
card_suits = { 'S':'\u2660', 'C':'\u2663', 'D':'\u2666', 'H':'\u2665' }
winning_hands = { 1:'High', 2:'Pair', 3:'Two Pair', 4:'Three of a Kind', 5:'Straight', 6:'Flush', 7:'Full House', 8:'Four of a Kind', 9:'Straight Flush', 10:'Royal Flush' }

class Card:
	def __init__(self,rank,suit):
			self._suit = suit
			self._rank = rank

	@property
	def suit(self):
		return self._suit
	@suit.setter
	def suit(self,suitVal):
		if not suitVal:
			self._suit = None
		self._suit = suitVal
	
	@property
	def rank(self):
		return self._rank
	@rank.setter
	def rank(self,rankVal):
		if not rankVal:
			self._rank = none
		self._rank = rankVal

	@property
	def display(self):
		return(card_ranks[self._rank]+card_suits[self._suit])

class Deck:
	def __init__(self):
		self.cards = []
		for suit in card_suits:
			for rank in card_ranks:
				if rank == 1:
						continue
				the_card = Card(rank,suit)
				self.cards.append(the_card)
		self.dealt_card = Card(None,None)

	@property
	def draw(self):
		drawn_card = random.choice(self.cards)
		self.cards.remove(drawn_card)
		return drawn_card

	@property
	def count(self):
		return len(self.cards)

class Hand:
	def __init__(self):
		self._cards = []
		self._outcome = None
		self._outcome_phrase = ''

	def show(self):
		show_hand = ''
		for card in self._cards:
			show_hand = show_hand + card.display + ' '
		print(show_hand)

	def add(self,card_to_add):
		self._cards.append(card_to_add)

	def replace(self,card_to_replace,replacement_card):
		self._cards[card_to_replace] = replacement_card

	@property
	def cards(self):
		return self._cards

	@property
	def outcome(self):
		return self._outcome
	@outcome.setter
	def outcome(self,outcomeVal):
		self._outcome = outcomeVal

	@property
	def outcome_phrase(self):
		return self._outcome_phrase
	@outcome_phrase.setter
	def outcome_phrase(self,outcome_phraseVal):
		self._outcome_phrase = outcome_phraseVal

def draw_hand(hand):
	print('   1       2       3       4       5   ')
	print('┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐ ┌─────┐')
	print('│'+card_ranks[hand.cards[0].rank].ljust(2)+'   │ │'+card_ranks[hand.cards[1].rank].ljust(2)+'   │ │'+card_ranks[hand.cards[2].rank].ljust(2)+'   │ │'+card_ranks[hand.cards[3].rank].ljust(2)+'   │ │'+card_ranks[hand.cards[4].rank].ljust(2)+'   │')
	print('│  '+card_suits[hand.cards[0].suit]+'  │ │  '+card_suits[hand.cards[1].suit]+'  │ │  '+card_suits[hand.cards[2].suit]+'  │ │  '+card_suits[hand.cards[3].suit]+'  │ │  '+card_suits[hand.cards[4].suit]+'  │')
	print('│   '+card_ranks[hand.cards[0].rank].rjust(2)+'│ │   '+card_ranks[hand.cards[1].rank].rjust(2)+'│ │   '+card_ranks[hand.cards[2].rank].rjust(2)+'│ │   '+card_ranks[hand.cards[3].rank].rjust(2)+'│ │   '+card_ranks[hand.cards[4].rank].rjust(2)+'│')
	print('└─────┘ └─────┘ └─────┘ └─────┘ └─────┘')

def evaluateHand(hand):

	# -------------------- Determine High Card
	high_card = hand.cards[0]
	for this_card in hand.cards:
		if this_card.rank > high_card.rank:
			high_card = this_card
	
	# -------------------- Flush?
	flush = True
	prev_suit = hand.cards[0].suit
	for this_card in hand.cards:
		suit = this_card.suit
		if suit != prev_suit:
			flush = False

	# -------------------- Straight?
	straight = True
	sorted_ranks = []
	# Straight check using high ace rank sequence
	for i in range(0,len(hand.cards)):
		sorted_ranks.append(hand.cards[i].rank)
	sorted_ranks.sort()
	for i in range(0,len(sorted_ranks)):
		if i > 0:
			if sorted_ranks[i] - sorted_ranks[i-1] != 1:
				straight = False
				break
	# Straight check using low ace rank sequence
	if straight == False:
		try:
			i = sorted_ranks.index(14)
			sorted_ranks[i] = 1
			sorted_ranks.sort()
			straight = True
			for i in range(0,len(sorted_ranks)):
				if i > 0:
					if sorted_ranks[i] - sorted_ranks[i-1] != 1:
						straight = False
						break
		except: 
			straight = False
	
	# -------------------- Prepare rank list for comparisons
	rank_list = []
	for this_card in hand.cards:
		rank_list.append(this_card.rank)

	# -------------------- Determine outcome

	outcome_phrase = ''

	#Royal Flush
	if high_card.rank == 14 and flush == True and straight == True:
		outcome_phrase = card_suits[high_card.suit]
		return 10,outcome_phrase

	#Straight Flush
	if flush == True and straight == True:
		outcome_phrase = card_suits[high_card.suit]+' '+card_ranks[high_card.rank]+' high'
		return 9,outcome_phrase

	#Four of a Kind
	for this_rank in range(0,len(card_ranks)):
		rank_count = len([this_card for this_card in hand.cards if this_card.rank == this_rank])
		if rank_count == 4:
			outcome_phrase = card_ranks[this_rank]+"'s"
			return 8,outcome_phrase

	#Full House
	first_rank = 0
	for this_rank in range(0,len(card_ranks)):
		rank_count = len([this_card for this_card in hand.cards if this_card.rank == this_rank])
		if rank_count == 3:
			first_rank = this_rank
	if first_rank != 0:
		for this_rank in range(0,len(card_ranks)):
			if this_rank == first_rank:
				continue
			rank_count = len([this_card for this_card in hand.cards if this_card.rank == this_rank])
			if rank_count == 2:
				outcome_phrase = card_ranks[first_rank]+"'s & "+card_ranks[this_rank]+"'s"
				return 7,outcome_phrase

	#Flush
	if flush == True:
		outcome_phrase = card_suits[high_card.suit]
		return 6,outcome_phrase

	#Straight
	if straight == True:
		outcome_phrase = card_ranks[high_card.rank]+' high'
		return 5,outcome_phrase

	#Three of a Kind
	for this_rank in range(0,len(card_ranks)):
		rank_count = len([this_card for this_card in hand.cards if this_card.rank == this_rank])
		if rank_count == 3:
			outcome_phrase = card_ranks[this_rank]+"'s"
			return 4,outcome_phrase

	#Two Pair
	first_rank = 0
	for this_rank in range(0,len(card_ranks)):
		rank_count = len([this_card for this_card in hand.cards if this_card.rank == this_rank])
		if rank_count == 2:
			first_rank = this_rank
	if first_rank != 0:
		for this_rank in range(0,len(card_ranks)):
			if this_rank == first_rank:
				continue
			rank_count = len([this_card for this_card in hand.cards if this_card.rank == this_rank])
			if rank_count == 2:
				outcome_phrase = card_ranks[first_rank]+"'s & "+card_ranks[this_rank]+"'s"
				return 3,outcome_phrase

	#One Pair
	for this_rank in range(0,len(card_ranks)):
		rank_count = len([this_card for this_card in hand.cards if this_card.rank == this_rank])
		if rank_count == 2:
			outcome_phrase = card_ranks[this_rank]+"'s"
			return 2,outcome_phrase

	#High Card
	outcome_phrase = card_ranks[high_card.rank]
	return 1,outcome_phrase
