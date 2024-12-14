import Cards

print('\n--- Simple 5-Card Draw Poker ---\n')
print('I will deal five cards.  At the prompt you can discard by entering')
print('card positions separated by commas.  Example to discard cards in')
print('positions one and three, enter 1,3.  To discard a single card just')
print('enter the position number.  To keep all cards, press enter.\n')
print("Let's begin...\n\n")

while True:
	deck = Cards.Deck()
	hand = Cards.Hand()
	discard_list = []

	for i in range(5):
		hand.add(deck.draw)

	'''
	#Manual hand assignment (for testing)
	hand.add(Cards.Card(11,'S'))
	hand.add(Cards.Card(12,'H'))
	hand.add(Cards.Card(4,'S'))
	hand.add(Cards.Card(10,'H'))
	hand.add(Cards.Card(13,'D'))
	'''

	print('Your hand:')
	Cards.draw_hand(hand)
	hand.outcome, hand.outcome_phrase = Cards.evaluateHand(hand)
	print(Cards.winning_hands[hand.outcome],hand.outcome_phrase)

	discard_list = input('Discard? ').split(',')

	#To-do:  Validate input before proceeding

	if discard_list != ['']:
		for i in discard_list:
			hand.replace(int(i)-1,deck.draw)

	Cards.draw_hand(hand)
	hand.outcome, hand.outcome_phrase = Cards.evaluateHand(hand)
	print(Cards.winning_hands[hand.outcome],hand.outcome_phrase)

	user_quit = input('Game Over\nEnter to play again, "X" to quit: ')
	if user_quit.upper() == 'X':
		break




