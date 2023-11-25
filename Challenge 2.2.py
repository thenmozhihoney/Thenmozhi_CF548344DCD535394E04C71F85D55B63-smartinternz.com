class Player:
    def play(self):
        print("The player is playing cricket.")

class Batsman(Player):
    def play(self):
        print("The batsman is batting.")

class Bowler(Player):
    def play(self):
        print("The bowler is bowling.")

# Taking user input to determine the player type
player_type = input("Enter player type (Batsman/Bowler): ").lower()

# Creating objects based on user input
if player_type == "batsman":
    player = Batsman()
elif player_type == "bowler":
    player = Bowler()
else:
    print("Invalid player type entered. Defaulting to Player.")
    player = Player()

# Calling the play() method for the chosen player
player.play()