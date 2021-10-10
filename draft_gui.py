from tkinter import *
root = Tk()





## FUNCTIONS
# store scored in mp_list
def createList(mental_score, physical_score):
    mp_list = []
    mp_list.append(mental_score)
    mp_list.append(physical_score)

    print(mp_list)
    return mp_list


# give activities
def giveActivities(mp_list):
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
    
    # return activities_items
    user_list = '\n'
    c = 0
    for level in activities_list:
        for item in level:
            c += 1
            item_processed = f'{str(c)}. {item}\n'
            user_list += item_processed

    # print(user_list)
    # print(type(user_list))
    return user_list





############################################################################################################################################################################################





## SECOND WINDOW
def secondWindow():
    global top
    global slider_mental
    global slider_physical
    global user_list

    # get score function
    def submitScore():
        global user_list
        global slider_mental
        global slider_physical

        mp_list = createList(int(slider_mental.get()), int(slider_physical.get()))
        user_list = giveActivities(mp_list)
        top.destroy()

        thirdWindow()

    top = Toplevel()
    top.geometry('400x200')
    top.title('BORED')
    top.iconbitmap('BORED/v1/sleepy.ico')

    qn_mental = Label(top, text='\nOn a scale of 1 to 10, where is your MENTAL energy at?').pack()
    slider_mental = Scale(top, from_=1, to=10, orient=HORIZONTAL)
    slider_mental.pack()

    qn_physical = Label(top, text='\nOn a scale of 1 to 10, where is your PHYSICAL energy at?').pack()
    slider_physical = Scale(top, from_=1, to=10, orient=HORIZONTAL)
    slider_physical.pack()

    space = Label(root, text=' ').pack()
    btn_submit = Button(top, text='OK', command=submitScore).pack()





## THIRD WINDOW
def thirdWindow():
    global top3

    top3 = Toplevel()
    top3.geometry('400x200')
    top3.title('BORED')
    top3.iconbitmap('BORED/v1/sleepy.ico')

    msg = Label(top3, text='Here are some activities to do!').pack()
    activities = Label(top3, text=user_list).pack()





## ROOT WINDOW
root.geometry('600x220')
root.title('BORED')
root.iconbitmap('BORED/v1/sleepy.ico')

welcome = Label(root, text='\nBurnt out from Math? Going through a breakup? Questioning existence and you need a distraction?\nBORED is the answer to all problems alike.\nThis application gives you a list of light activities that are neither too demanding nor too dull.\n').pack()
btn_continue = Button(root, text='CONTINUE', command=secondWindow).pack()

warning = Label(root, text='\n\n\n** Keep this window open while using the app.').pack()
btn_exit = Button(root, text='Quit', command=root.quit).pack()

space = Label(root, text='\n').pack()





root.mainloop()