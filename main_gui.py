from tkinter import *
import tkinter.messagebox as msgbox

root = Tk()





## FUNCTIONS
# store scored in mp_list
def createList(mental_score, physical_score):
    mp_list = []
    mp_list.append(mental_score)
    mp_list.append(physical_score)

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





def remove_previous_info():
    global l

    scores.destroy()
    msg.destroy()
    activities.destroy()

    if l > 190:
        l -= 280
    # # root.geometry('580x' + str(l))





## SECOND WINDOW
def secondWindow():
    global top
    global slider_mental
    global slider_physical
    global user_list

    global qn_mental
    global qn_physical
    global btn_submit
    global btn_back

    global submitScore

    # remove previous widgets
    welcome.destroy()
    btn_continue.destroy()

    btn_exit.destroy()


    # get score function
    def submitScore():
        global user_list
        global slider_mental
        global slider_physical

        global qn_mental
        global slider_mental
        global qn_physical
        global slider_physical
        global btn_submit
        global btn_back

        mp_list = createList(int(slider_mental.get()), int(slider_physical.get()))
        user_list = giveActivities(mp_list)
        btn_submit.destroy()

        def warning():
            global btn_submit

            exists = activities.winfo_exists()
            if exists == 1:
                msgbox.showinfo("Oops!", "Remove the previous output first:)")
            else:
                btn_submit.destroy()
                btn_submit = Button(root, text='OK', command=submitScore)
                btn_submit.pack()
        
        btn_submit = Button(root, text='OK', command=warning)
        btn_submit.pack()

        thirdWindow()

    root.geometry('580x290')

    # create widgets
    qn_mental = Label(root, text='\nOn a scale of 1 to 10, where is your MENTAL energy at?')
    slider_mental = Scale(root, from_=1, to=10, orient=HORIZONTAL, length=300, tickinterval=3)

    qn_physical = Label(root, text='\nOn a scale of 1 to 10, where is your PHYSICAL energy at?')
    slider_physical = Scale(root, from_=1, to=10, orient=HORIZONTAL, length=300, tickinterval=3)

    btn_submit = Button(root, text='OK', command=submitScore)
    btn_back = Button(root, text='Remove', command=remove_previous_info)

    # packing
    qn_mental.pack()
    slider_mental.pack()

    qn_physical.pack()
    slider_physical.pack()

    btn_back.pack()
    btn_submit.pack()





## ROOT WINDOW
l = 190
root.geometry('580x' + str(l))
root.title('BORED')
root.iconbitmap('C:/Users/qamar/OneDrive/Documents/DEV/BORED/v1/sleepy.ico')

# create widgets
welcome = Label(root, text='\n\nBurnt out from Math? Going through a breakup? Questioning existence and you need a distraction?\nBORED is the answer to all problems alike.\nThis application gives you a list of light activities that are neither too demanding nor too dull.\n\n\n')
btn_continue = Button(root, text='CONTINUE', command=secondWindow)

btn_exit = Button(root, text='Quit', command=root.quit)

# packing
welcome.pack()
btn_continue.pack()

btn_exit.pack()





## THIRD WINDOW
def thirdWindow():
    global msg
    global activities
    # global btn_back
    global scores
    global l

    l += 280
    root.geometry('580x' + str(l))

    # create widgets
    scores_text = f'\n\nMental: {slider_mental.get()}/10\nPhysical: {slider_physical.get()}/10'
    scores = Label(root, text=scores_text)
    msg = Label(root, text='Here are some activities to do!')
    activities = Label(root, text=user_list)

    # btn_back = Button(root, text='Remove', command=remove_previous_info)

    # packing
    scores.pack()
    msg.pack()
    activities.pack()
    # btn_back.pack()





root.mainloop()