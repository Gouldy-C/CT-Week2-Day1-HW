import random
import os
import time

playerDmgRes = [0]

healthValue = 800

enemies = [
    'Slimes',
    'Goblins',
    'Skeleton',
    'Zombie',
    'Dragon',
    'Troll',
    'Giant',
    'Vampire',
    'Ghost',
    'Wolves',
    'Zombies',
]

player_atk = {
    'st': [50, 225],
    'sl': [60, 200],
    'sp': [25, 150],
}

enemies_atk = {
    'Slimes': [15, 50],
    'Goblins': [20, 70],
    'Skeleton': [25, 99],
    'Zombie': [30, 99],
    'Dragon': [50, 400],
    'Troll': [50, 125],
    'Giant': [50, 150],
    'Vampire': [75, 200],
    'Ghost': [25, 75],
    'Wolves': [10, 60],
    'Zombies': [75, 150],
}

enemies_res = {
    'Slimes': {'st': 70, 'sl': 0, 'sp': 40},
    'Goblins': {'st': 10, 'sl': 15, 'sp': 40},
    'Skeleton': {'st': 100, 'sl': 25, 'sp': 0},
    'Zombie': {'st': 100, 'sl': 15, 'sp': 0},
    'Dragon': {'st': 80, 'sl': 80, 'sp': 50},
    'Troll': {'st': 50, 'sl': 60, 'sp': 35},
    'Giant': {'st': 60, 'sl': 70, 'sp': 35},
    'Vampire': {'st': 3, 'sl': 40, 'sp': 35},
    'Ghost': {'st': 90, 'sl': 100, 'sp': 0},
    'Wolves': {'st': 5, 'sl': 5, 'sp': 40},
    'Zombies': {'st': 100, 'sl': 10, 'sp': 40},
}


def main():
    os.system('cls')
    print(
        f'\nThis is a monster fighting game. Player Damage Resistance = {playerDmgRes[0]} percent, to get this stat up you must play and win.\n')
    while True:
        play = input('Would you like to play? [y/n] ').lower()
        if play == 'y':
            print('\n')
            break
        elif play == 'n':
            exit()
        else:
            print('Please try again. We wil only accept y for yes and n for no.')
    game()


def game():
    playerHealth = healthValue
    enemyHealth = healthValue
    enemy = enemies[random.randrange(0, len(enemies))]
    print(f'You are fighting a {enemy}!\n')
    while playerHealth >= 1 and enemyHealth >= 1:
        while True:
            atkType = input(
                '\nPlease enter if you would like to stab [st], slash [sl] or cast a spell [sp]: [st/sl/sp] ').lower()
            if atkType in ['st', 'sl', 'sp']:
                print('\n')
                break
            else:
                print('Please enter a valid input.')

        playerRoundDmg = playerDmgToEnemy(enemy, atkType)
        enemyHealth -= playerRoundDmg
        print(f'You did {playerRoundDmg} damage to the {enemy}!')

        healthCheck('Its', enemyHealth)

        enemyRoundDmg = enemyAttack(enemy)
        playerHealth -= enemyRoundDmg
        print(f'The {enemy} did {enemyRoundDmg} damage to the You!')

        healthCheck("You're", playerHealth)

    if playerHealth <= 0:
        print('Sorry but you died!  -Wait 10 sec.\n')
        playerDmgRes[0] = 0
        time.sleep(10)
        main()
    if enemyHealth <= 0:
        print('Wow, You won! I am totally impressed! I have given you 10 percent damage resistance if you want to play again.  -Wait 10 sec.\n')
        playerDmgRes[0] = playerDmgRes[0] + 10
        time.sleep(10)
        main()


def healthCheck(who, health):
    if health > 650:
        print(f'{who} looking a ok!\n\n')
    elif 650 >= health > 450:
        print(f'{who} a little worse for wear!\n\n')
    elif 450 >= health > 250:
        print(f'{who} starting to get a bit injured!\n\n')
    elif 250 >= health > 80:
        print(f'This fights about to be over and {who} about to die\n\n')
    elif 80 >= health > 0:
        print(f'{who} going to die!\n\n')


def enemyAttack(enemy):
    atk_values = enemies_atk[enemy]
    dmg = random.randrange(atk_values[0], atk_values[1])
    trueDmg = int((dmg / 100) * (100 - playerDmgRes[0]))
    return trueDmg


def playerAttack(atk):
    atk_values = player_atk[atk]
    return random.randrange(atk_values[0], atk_values[1])


def playerDmgToEnemy(enemy, atkType):
    dmg = playerAttack(atkType)
    enemyRes = enemies_res[enemy][atkType]
    trueDmg = int((dmg / 100) * (100 - enemyRes))
    return trueDmg


if __name__ == "__main__":
    main()
