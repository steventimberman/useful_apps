import random
class Round:
	"""Reps a round of c_lo, players is a list player objects""" 
	
	def __init__(self, players=[], bet=1):
		self.bet = bet
		self.players = players
		self.best_roller = []
		self.best_roll_val = 0
		self.pool = self.bet*len(self.players)

		self.empty_val_dict = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}

	def get_players(self):
		"""Gets a safe copy of a list of Player objects"""
		return self.players.copy()

	def add_player(self, player):
		"""Add a player to the game"""
		self.players.append(player)

	def set_bet(self, new_bet):
		"""Sets the bet attribute of the class"""
		self.bet = new_bet

	def reset_round(self):
		"""Resets the round to init, in order to play another round"""
		self.best_roller = []
		self.best_roll_val = 0
		self.pool = self.bet*len(self.players)

	def get_roll_val(self, dice):
		"""input a tuple of 3 ints, repping three dice
			returns a value, that is used to rank rolls 
			in an order (the actual value is arbitrary, 
			but if a roll is better than another, it 
			will have a higher score)"""
		val_dict = dict(self.empty_val_dict)
		if len(dice) != 3:
			raise ValueError
		for val in dice:
			val_dict[val]+= 1
		
		cur_val = 0
		take_val = False
		#check for win
		if val_dict[4] == 1 and val_dict[5] == 1 and val_dict[6] == 1:
			return 25
		#check loss on 1,2,3
		if val_dict[1] == 1 and val_dict[2] == 1 and val_dict[3] == 1:
			return -1
		#check for any val 
		for val in val_dict:
			if val_dict[val] == 1:
				if take_val:
					return val
				cur_val = val
			elif val_dict[val] == 2:
				take_val = True
			elif val_dict[val] == 3:
				return 6+val

		if take_val:
			return cur_val
		return 0

	def update_best_val(self, player, val):
		if val > self.best_roll_val:
			self.best_roll_val = val
			self.best_roller = [player]
			return "Congrats " + player.get_name() + ", you are now the top roller this turn!"
		elif val == self.best_roll_val and self.best_roll_val > 0:
			self.best_roller.append(player)
			return "Congrats " + player.get_name() + ", you tied the top roller this turn!"
		elif val == 0:
			return "Try again!"
		return "Wow what a loser!"



	def roll(self, player):
		roll_dies = (random.randrange(1,7), random.randrange(1,7), random.randrange(1,7))
		print ("You rolled a " + str(roll_dies[0])+ ", " + str(roll_dies[1]) + ", and " + str(roll_dies[2]) + ".")
		roll_val = self.get_roll_val(roll_dies)
		update = self.update_best_val(player, roll_val)
		print (update)
		print ("------------------")
		return roll_val

	def make_bet(self):
		for player in self.get_players():
			player.take_money(self.bet)

	def win_bet(self, player):
		player.add_money(self.pool)

	def double_down(self, current_players):
		self.pool += self.bet*len(current_players)
		for player in current_players:
			player.take_money(self.bet)
	
	
	def player_roll(self, player):
		while True:
			enter_to_roll = input(player.get_name() + " press enter to roll!")
			print ("--------")
			cur_roll = self.roll(player)
			if cur_roll != 0:
				break

	def play_round(self):
		self.make_bet()
		print ("Let's roll some dice boiiis (and gurlz)!" )
		cur_players = self.get_players()
		while True:
			print ("The current bet pool has $" + str(self.pool) + ".")
			for player in cur_players:
				self.player_roll(player)
			if len(self.best_roller) == 1:
				break
			cur_players = self.best_roller.copy()
			self.best_roller = []
			self.best_roll_val = 0
			to_double_down = input("Wanna double down? Write yes or no (lower case): " )
			if to_double_down == "yes": self.double_down(cur_player)
		winner = self.best_roller[0]
		self.win_bet(winner)
		print ("Congrats " + winner.get_name() + ", you won $"+str(self.pool)+"!")




class Player():
	
	def __init__(self, name, money=1):
		self.name = name
		self.money = money

	def get_name(self):
		return self.name + ""

	def get_money(self):
		return self.money

	def take_money(self, amount):
		self.money -= amount

	def add_money(self, amount):
		self.money += amount



def simulate_game():


	players = []
	while True:
		name = input("Either enter a players name, or write 'done' in all lowercase and hit enter: ")
		if name.lower() == 'done':
			break
		money = int(input("How much money do you have in whole dollars?: $"))
		player = Player(name, money)
		players.append(player)
	bet = int(input("How much do you want to bet?: "))
	game = Round(players, bet)
	game.play_round()

simulate_game()



