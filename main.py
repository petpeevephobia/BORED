from os import system
from time import sleep

## OUTPUT FUNCTIONS
def netflix():
    print('\nShows to watch:')
    print('1. Gotham\n2. BeastStars S2\n3. History Documentaries\n')

def reflect():
    print('\nRandom thoughtful questions to answer:')
    print('1. What is your favourite trait in yourself, that is not physical?')
    print('2. Do you know what your family expects of you? How much are you living up to their expectations?')
    print('3. What is a memorable compliment you received?\n')

def read():
    print('\nBooks to read:')
    print('1. The Psychology of Money, by Morgan Housel')
    print('2. Everything is F*cked, by Mark Manson')
    print('3. Algorithms to Live By, by Brian Christian & Tom Griffiths\n')

def code():
    print('\nCode-spiration:')
    print('1. Machine learning (predict homosexuality)')
    print('2. Bot (WhatsApp, Discord, Instagram)')
    print('3. Data dashboard (pretend you are a professional data analyst)\n')

def games():
    print('\nSuggestions:')
    print('1. Minecraft')
    print('2. The Sims 4')
    print('3. Roblox\n')

def outdoors():
    print('\nPlaces to go:')
    print('1. Woodlands Town Park East')
    print('2. Seah Im Bunker')
    print("3. Former Queen's Theatre\n")

def social():
    print('\nPeople to speak to:')
    print('1. Haram Gang')
    print('2. Juniors')
    print('3. Poly friends\n')





## WELCOME
print()
print('\t\t\t\t\t\tmmmmm   mmmm  mmmmm  mmmmmm mmmm')
print('\t\t\t\t\t\t#    # m"  "m #   "# #      #   "m')
print('\t\t\t\t\t\t#mmmm" #    # #mmmm" #mmmmm #    #')
print('\t\t\t\t\t\t#    # #    # #   "m #      #    #')
print('\t\t\t\t\t\t#mmmm"  #mm#  #    " #mmmmm #mmm"')

print('\nBurnt out? Going through a breakup? Questioning life itself and you need a distraction? BORED is the answer to problems alike.')
print('This application gives you a list of light activities that are neither demanding nor dull. \nIf necessary, these activities can be modified by you to suit your needs.')
cont = input('\nPress Enter to continue ...')

system('cls')
system('clear')



check = True
while check == True:
    print()
    print('\t\t\t\t\t\tmmmmm   mmmm  mmmmm  mmmmmm mmmm')
    print('\t\t\t\t\t\t#    # m"  "m #   "# #      #   "m')
    print('\t\t\t\t\t\t#mmmm" #    # #mmmm" #mmmmm #    #')
    print('\t\t\t\t\t\t#    # #    # #   "m #      #    #')
    print('\t\t\t\t\t\t#mmmm"  #mm#  #    " #mmmmm #mmm"')
    print('\n-------------------------------------------------------------------------------------------------------------------------------\n')




    ## CHECK USER ENERGY LEVEL
    # ask user for current health info
    mp_list = []
    mental = int(input('On a scale of 1 to 10, where is your MENTAL energy at?\n>> '))
    while mental < 1 or mental > 10:
        print('\n\tERROR: Only from 1 to 10.')
        mental = int(input('\tWhere is your MENTAL energy at?\n>> '))

    print()

    physical = int(input('On a scale of 1 to 10, where is your PHYSICAL energy at?\n>> '))
    while physical < 1 or physical > 10:
        print('\n\tERROR: Only from 1 to 10.')
        physical = int(input('\tWhere is your PHYSICAL energy at?\n>> '))


    # create list
    mp_list.append(mental)
    mp_list.append(physical)





    print('\n-------------------------------------------------------------------------------------------------------------------------------')





    ## LOOK FOR SMTH TO DO
    # LOW: netflix, self-reflect [1 - 5]
    # NORMAL: read, code, games [5 - 10]
    # HIGH: outdoors, socialise [5 - 10]


    activities_list = []
    if (mp_list[0] >= 1 or mp_list[1] >= 1) and (mp_list[0] <= 4 or mp_list[1] <= 4):
        activities_items = ['Netflix','Self-reflect']
        activities_list.append(activities_items)

    if (mp_list[0] >= 5 or mp_list[1] >= 5) and (mp_list[0] <= 7 or mp_list[1] <= 7):
        activities_items = ['Read', 'Code', 'Game']
        activities_list.append(activities_items)

    if (mp_list[0] >= 8 or mp_list[1] >= 8) and (mp_list[0] <= 10 or mp_list[1] <= 10):
        activities_items = ['Outdoors', 'Socialise']
        activities_list.append(activities_items)


    # print activities list
    print('Activities You Can Do:')
    user_list = []
    c = 0
    for level in activities_list:
        print()
        for item in level:
            user_list.append(item)
            c += 1
            print(f'{str(c)}. {item}')





    print('\n-------------------------------------------------------------------------------------------------------------------------------\n')





    ## LOOK FOR SMTH TO DO - part 2
    sleep(3)
    more = input('Which activity would you like to do from the above?\n>> ')

    while more not in user_list:
        print('\n\tERROR: Input cannot be found in list.')
        more = input('\t>> ')


    if more == 'Netflix':
        netflix()
    if more == 'Self-reflect':
        reflect()
    if more == 'Read':
        read()
    if more == 'Code':
        code()
    if more == 'Game':
        games()
    if more == 'Outdoors':
        outdoors()
    if more == 'Socialise':
        social()




    
    print('\n-------------------------------------------------------------------------------------------------------------------------------\n')





    ## REPEAT
    sleep(3)
    check_ask = input('Would you like to input again? (Y/N)\n>> ')
    print()

    if check_ask == 'Y' or check_ask == 'y':
        check = True
        system('cls')
        system('clear')
    elif check_ask == 'N' or check_ask == 'n':
        check = False
    else:
        while (check_ask != 'Y' or check_ask != 'y') or (check_ask != 'N' or check_ask != 'n'):
            print('\t\nERROR: Invalid input.')
            check_ask = input('\tWould you like to input again? (Y/N)\t\n>> ')
            print()


## ADD ITEM

## REMOVE ITEM