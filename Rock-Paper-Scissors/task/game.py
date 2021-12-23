import math
import random


class RockPaperScissors:
    
    def __init__(self):
        self.name = self.player = self.comp = ''
        self.options = self.list_wins = []
        self.score = 0

    # printing greetings
    def greeting(self):
        self.name = input('Enter your name:')
        self.check_name()
        print('Hello,', self.name, sep=' ')
        
    # check if there's a record for the user(name) in the file
    def check_name(self):
        with open('rating.txt', 'r') as ratings_list:
            for line in ratings_list:
                if self.name in line:
                    self.score = int(line.split()[1])
    
    # determine playing set
    def set_options(self):
        options = input()
        if options == '':
            self.options = ['rock', 'paper', 'scissors']
        else:
            self.options = options.split(',')
        print("Okay, let's start")
        
    # start playing
    def make_choice(self):
        while True:
            try:
                self.player = input()
                if self.player == '!exit':
                    self.exit_game()
                    break
                elif self.player == '!rating':
                    self.rating()
                elif self.player in self.options:
                    self.play()
                else:
                    raise ValueError
            except ValueError:
                print('Invalid input')

    def play(self):
        self.comp = random.choice(self.options)
        if self.player == self.comp:
            self.score += 50
            print(f'There is a draw ({self.comp})')
        else:
            self.determine_options()
            # determine weaker options
            h = math.ceil(len(self.list_wins) / 2)
            weaker_half = self.list_wins[h:]
            if self.comp in weaker_half:
                self.score += 100
                print(f'Well done. The computer chose {self.comp} and failed')
            else:
                print(f'Sorry, but the computer chose {self.comp}')
       
    # determine which options are stronger or weaker
    def determine_options(self):
        # find position of user's choice
        i = self.options.index(self.player)
        current_options = self.options[i:]
        current_options.extend(self.options[:i])
        self.list_wins = current_options

    # printing user's rating
    def rating(self):
        print('Your rating:', self.score, sep=' ')
        
    @staticmethod
    def exit_game():
        print('Bye!')


def main():
    game = RockPaperScissors()
    game.greeting()
    game.set_options()
    game.make_choice()


if __name__ == "__main__":
    main()
