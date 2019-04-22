import random
import numpy as np
import scipy.signal as sg
import sounddevice as sd
sd.default.samplerate = 44100
def notePlayback(time, frequency, type):
    if type is 'sin':
        noteType = np.sin
    elif type is 'square':
        noteType = sg.square
    elif type is 'saw':
        noteType = sg.sawtooth
    samples = np.arange(44100 * time) / 44100.0
    wave = 1000 * noteType(2 * np.pi * frequency * samples)
    wav_wave = np.array(wave, dtype=np.int16)
    sd.play(wav_wave, blocking=True)
def introMusic():
    notePlayback(.25, 523, 'sin')
    notePlayback(.25, 783, 'sin')
    notePlayback(.3, 1046, 'sin')
    notePlayback(.15, 932, 'sin')
    notePlayback(.15, 880, 'sin')
    notePlayback(.25, 783, 'sin')
    notePlayback(.25, 783, 'sin')
    notePlayback(.4, 783, 'sin')
    notePlayback(.2, 880, 'sin')
    notePlayback(.25, 932, 'sin')
    notePlayback(.25, 932, 'sin')
    notePlayback(.25, 880, 'sin')
    notePlayback(.25, 698, 'sin')
    notePlayback(.2, 659, 'sin')
    notePlayback(.2, 698, 'sin')
    notePlayback(.5, 783, 'sin')
def jazzyMusic():
    notePlayback(.2, 261, 'saw')
    notePlayback(.2, 329, 'saw')
    notePlayback(.2, 392, 'saw')
    notePlayback(.2, 440, 'saw')
    notePlayback(.2, 466, 'saw')
    notePlayback(.2, 440, 'saw')
    notePlayback(.2, 392, 'saw')
    notePlayback(.2, 329, 'saw')
    notePlayback(.2, 261, 'saw')
    notePlayback(.2, 329, 'saw')
    notePlayback(.2, 392, 'saw')
    notePlayback(.2, 440, 'saw')
    notePlayback(.2, 466, 'saw')
    notePlayback(.2, 440, 'saw')
    notePlayback(.2, 392, 'saw')
    notePlayback(.2, 329, 'saw')
    notePlayback(.2, 349, 'square')
    notePlayback(.2, 440, 'square')
    notePlayback(.2, 523, 'square')
    notePlayback(.2, 587, 'square')
    notePlayback(.2, 622, 'square')
    notePlayback(.2, 587, 'square')
    notePlayback(.2, 523, 'square')
    notePlayback(.2, 440, 'square')
    notePlayback(.2, 261, 'saw')
    notePlayback(.2, 329, 'saw')
    notePlayback(.2, 392, 'saw')
    notePlayback(.2, 440, 'saw')
    notePlayback(.2, 466, 'saw')
    notePlayback(.2, 440, 'saw')
    notePlayback(.2, 392, 'saw')
    notePlayback(.2, 329, 'saw')
    notePlayback(.2, 392, 'sin')
    notePlayback(.2, 494, 'sin')
    notePlayback(.2, 587, 'sin')
    notePlayback(.2, 659, 'sin')
    notePlayback(.2, 698, 'sin')
    notePlayback(.2, 659, 'sin')
    notePlayback(.2, 587, 'sin')
    notePlayback(.2, 494, 'sin')
    notePlayback(.2, 349, 'square')
    notePlayback(.2, 440, 'square')
    notePlayback(.2, 523, 'square')
    notePlayback(.2, 587, 'square')
    notePlayback(.2, 622, 'square')
    notePlayback(.2, 587, 'square')
    notePlayback(.2, 523, 'square')
    notePlayback(.2, 440, 'square')
    notePlayback(.2, 261, 'saw')
    notePlayback(.2, 329, 'saw')
    notePlayback(.2, 392, 'saw')
    notePlayback(.2, 440, 'saw')
    notePlayback(.2, 466, 'saw')
    notePlayback(.2, 440, 'saw')
    notePlayback(.2, 392, 'saw')
    notePlayback(.2, 329, 'saw')
    notePlayback(.2, 261, 'saw')
    notePlayback(.2, 329, 'saw')
    notePlayback(.2, 392, 'saw')
    notePlayback(.2, 329, 'saw')
    notePlayback(.4, 261, 'saw')
    notePlayback(.4, 261, 'saw')

# jazzyMusic()


difficulty = None
soundOn = None
weapons = {'Worn Down Blade': ('A pretty shabby looking blade.', 2)
       , 'Wooden Blade': ('A well constructed wooden blade.', 5)
       , 'Limestone Blade': ('A blade made out of pure limestone', 10)
       , 'Copper Dagger': ('A sword made from melted down pennies', 20)
       , 'Iron Sword': ('A well crafted sword made of iron.', 35)
       , 'Steel Katana': ('A powerful sword from the orient', 50)
       , 'Arquebus': ('An early gun that can fire from afar, but requires ammo and may misfire.', 60)
       , 'Rifle': ('A well crafted and powerful gun', 100)
       , 'Flintlock Pistol': ('A handheld gun that can fire from afar, but requires ammo and may misfire. Can be dual weld', 40)
       , 'Revolver': ('A more powerful gun with better reliability. Can be dual weld', 75)
       , 'Ammo': 0}
class Player:
    difficulty = None
    def __init__(self, name):
        self.name = name
    health = 0
    level = 1
    exp = 0

    baseAttack = 2
    def levelUp(self):
        self.exp -= 10
        self.level += 1
        self.baseAttack = 2 ** self.level
        print('Level Up!')
        print('You are now level', self.level, '\n'
              'Your base health is now', self.health,
              'Your base attack is now', self.baseAttack, '\n')
    if difficulty == 1:
        health = 50
    elif difficulty == 2:
        health = 30
    elif difficulty == 3:
        health = 15

    def normalAttack(self):
        finalAttack = random.randint(self.baseAttack + 1, self.baseAttack + 3)
        return finalAttack

    def strongAttack(self):
        finalAttack = random.randint(self.baseAttack + 4, self.baseAttack + 10)
        return finalAttack

    def critAttack(self):
        finalAttack = random.randint(self.baseAttack + 15, self.baseAttack + 30)
        return finalAttack
    inventory = weapons
class Enemy:
    global difficulty
    if difficulty == 1:
        attackFactor = 1
    elif difficulty == 2:
        attackFactor = 2
    elif difficulty == 3:
        attackFactor = 3
    def defend(self, damage, defendFactor):
        self.life -= (damage - damage(defendFactor))
        print(self.life)

    def normalAttack(self):
        finalAttack = random.randint(self.baseAttack - 10, self.baseAttack + 10)
        return finalAttack

    def strongAttack(self):
        finalAttack = random.randint(2(self.baseAttack - 20), 2(self.baseAttack + 20))
        return finalAttack

    def critAttack(self):
        finalAttack = random.randint(5(self.baseAttack - 50), 5(self.baseAttack + 50))
        return finalAttack
class Crow(Enemy):
    life = random.randint(5, 20)
    baseAttack = 5
    def __init__(self):
        self.name = 'Crow'
class Cube(Enemy):
    life = random.randint(10, 30)
    baseAttack = 10
    def __init__(self):
        self.name = 'Cube'
class PaperPlane(Enemy):
    life = random.randint(20, 45)
    baseAttack = 15
    def __init__(self):
        self.name = 'Paper Plane'

def visualExp(player):
    print('Current Exp\n',
          '[' + ('▮' * player.exp) + ('▯' * (10 - player.exp)), ']')
def playerIntro():
    global soundOn
    global playerOne
    global difficulty
    choiceSelected = False
    soundOn = input('Enable sound? (yes/no)\n')
    if soundOn == 'yes':
        introMusic()
        jazzyMusic()
    print('Hello!\n', 'Welcome to Dyventure Alpha!\n')
    playerOne = Player(input('Enter your name.\n'))

    while choiceSelected is False:
        difficulty = input('Select your difficulty.\n'
                           '1. Easy\n'
                           '2. Medium\n'
                           '3. Hard\n')
        if difficulty not in ('1', '2', '3'):
            print('Please select a valid difficulty.')
        else:
            difficulty = int(difficulty)
            playerOne.difficulty = difficulty
            choiceSelected = True


def viewInventory(player):
    for key, value in player.inventory.items():
        print(key, ':', value, 'damage.\n')
def encounterGame(player, areaEnemies):
    global soundOn
    enemies = random.randrange(5,10)
    while enemies > 0:
        if enemies is 1:
            print('There is 1 enemy left.')
        else:
            print('There are', enemies, 'enemies left.')
        currentEnemy = random.choice(areaEnemies)
        print("You encountered a wild", currentEnemy.name, "! ")
        while currentEnemy.life > 0:
            print('Your current health is', player.health, '.\n')
            print("The", currentEnemy.name, "has", currentEnemy.life, "HP\n")
            invAnswer = input("View inventory? (yes/no)\n")
            if invAnswer == 'yes':
                viewInventory(player)

            input("Press enter to attack!\n\n")
            print("=|>>>>>>>")
            currentAttack = random.randint(1, 100)
            if currentAttack < 75:
                if soundOn == 'yes':
                    notePlayback(.2, 659, 'sin')
                    notePlayback(.2, 698, 'sin')
                    notePlayback(.5, 783, 'sin')
                currentEnemy.life -= player.normalAttack()
                print('You dealt', player.normalAttack(), 'damage!\n')
            elif 75 <= currentAttack < 95:
                if soundOn == 'yes':
                    notePlayback(.2, 880, 'sin')
                    notePlayback(.2, 988, 'sin')
                    notePlayback(.5, 1047, 'sin')
                currentEnemy.life -= player.strongAttack()
                print('Strong Attack!')
                print('You dealt', player.strongAttack(), 'damage!\n')
            elif 95 <= currentAttack <= 100:
                if soundOn == 'yes':
                    notePlayback(.2, 1175, 'sin')
                    notePlayback(.2, 1319, 'sin')
                    notePlayback(.5, 1397, 'sin')
                currentEnemy.life -= player.critAttack()
                print('CRITICAL HIT!')
                print('You dealt', player.critAttack(), 'damage!\n')

        enemies -= 1
        print('You have defeated the', currentEnemy.name, '!')
        expGained = player.level * random.randint(1, 3)
        player.exp += expGained
        print('You have gained', expGained, 'experience')
        visualExp(player)
        if player.exp >= 10:
            player.levelUp()
        areaEnemies.remove(currentEnemy)
    print('You have beaten all the enemies!')
def main():
    playerIntro()
    grassEnemies = [Crow(), Crow(), Crow(), Crow(), Crow(), Crow(), Crow(), Crow(), Cube(), Cube(), Cube()]
    encounterGame(playerOne, grassEnemies)
main()