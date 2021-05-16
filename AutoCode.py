from Tkinter import *
 
#Creating the first window that opens and titling it "Code Auto-Completer" 
root = Tk()
root.geometry("600x600")
root.title("Code Auto-Completer")

#Variable list
variables = [1,2,3,4,5]
loop = [0,1,2,3,4]

#For list
autofor = ['i = 0; i < 10; i++)', 'j = 10; j > 0; j--)', '', '', '']
autoforloop = [0,1,2,3,4]

#While list
autowhile = ['x > y)', 'x != y)', '', '', '']
autowhileloop = [0,1,2,3,4]

#Count for the Save_input function
count = 0

#Counts for the save_for_input and save_while_input functions. Starts at 2 so that the user does not overwrite the original cases
#Until the count loops around
Whilecount = 2
Forcount = 2

#Function to take whatever is written in the text box and open a new window with relevent code
def Take_input():

    #Defines INPUT as everything written in the text box
    INPUT = inputtxt.get("1.0", "end-1c")

    #For commands:
    #If statement to make sure INPUT has enough characters to run the check on "for(". If this if statement is omitted, there will be an error if
    #3 or less characters are in INPUT and the user presses CTRL
    if len(INPUT) > 3:
        if(INPUT[-4] == "f" and INPUT[-3] == "o" and INPUT[-2] == "r" and INPUT[-1] == "("):
            
            #Creates a small window that holds all the code that matches what the user might have wanted to write
            match = Tk()
            match.geometry("150x200")
            match.title("Matches Found:")
            match.focus_force()

            #Loops twice, printing out all the defined cases in autofor (as long as they aren't empty)
            for i in autoforloop:
                if autofor[i] != "":
                    match_list = Button(match, height = 1,
                             width = 20, 
                             text = autofor[i],
                             command = lambda x=i:[inputtxt.insert(END, autofor[x]), match.destroy()])

                    match_list.pack()

    #While commands:
    #If statement to make sure INPUT has enough characters to run the check on "while(". If this if statement is omitted, there will be an error if
    #5 or less characters are in INPUT and the user presses CTRL
    if len(INPUT) > 5:
        if(INPUT[-6] == "w" and INPUT[-5] == "h" and INPUT[-4] == "i" and INPUT[-3] == "l" and INPUT[-2] == "e" and INPUT[-1] == "("):
            
            #Creates a small window that holds all the code that matches what the user might have wanted to write
            match = Tk()
            match.geometry("150x200")
            match.title("Matches Found:")
            match.focus_force()
            
            #Loops twice, printing out all the defined cases in autowhile (as long as they aren't empty)
            for i in autowhileloop:
                if autowhile[i] != "":
                    match_list = Button(match, height = 1,
                             width = 20, 
                             text = autowhile[i],
                             command = lambda x=i:[inputtxt.insert(END, autowhile[x]), match.destroy()])

                    match_list.pack()

    #Can insert a user defined variable/ function at the beginning of a line or at any time during a line (after a space)
    if(INPUT[-1] == "\n" or INPUT[-1] == " "):
        
        #Creates a small window that holds all the variables/ function names a user has saved previously
        match = Tk()
        match.geometry("150x200")
        match.title("Matches Found:")
        match.focus_force()

        #Loops 5 times, printing out all the user defined variables/functions as buttons
        for i in loop:
            #Only print the button if the list element was changed. (i.e., don't print the initialized list)
            if variables[i] != i+1: 
                match_list = Button(match, height = 1,
                         width = 20, 
                         text = variables[i],
                         command = lambda x=i:[inputtxt.insert(END, variables[x]), match.destroy()])

                match_list.pack()

#Affects the GUI of the inputtxt text box
inputtxt = Text(root, height = 300,
                width = 300,
                bg = "gray26",
                font=("Courier", 14),
                insertbackground = "white",
                fg = "snow")

#Allows the keypress of CTRL to call the Take_input() function
def Key_input(event):
    Take_input()

#Allows the keypress of ALT to save a user-defined variable/ function
def Save_input(event):
        
        #Taking the variable "count" that was defined at the beginning of the code
        global count

        #Using (count % 5) for the user variables' place because after 5 saved variables, it will loop over and save over the first variables
        #This way, the user does not have to worry about only saving 5 variables.
        place = count % 5
        count += 1

        INPUT = inputtxt.get("1.0", "end-1c")
        inputlength = len(INPUT)

        #String to hold the user's variable that will be saved into the variables list
        userVariable = ""

        #For loop to go backwards through INPUT
        for i in range(1, inputlength):

            #Copies the user's variable/ function name up until it reaches a \n character. userVariable will end up reversed
            if INPUT[-i] != "\n":
                userVariable += INPUT[-i]

            #Exits the loop once a \n character is read
            else:
                break

        #Because userVariable is in reverse order, reverse it again to make it the right way. 
        #Then, add that into its rightful place in the variables list
        variables[place] = userVariable[::-1]

#Allows the keypress of DOWN to save a user-defined while loop condition
def Save_while_input(event):

        #Taking the variable "Whilecount" that was defined at the beginning of the code
        global Whilecount

        #Using (Whilecount % 5) for the user conditions' place because after 5 saved conditions, it will loop over and save over the first condition
        #This way, the user does not have to worry about only saving 5 conditions.
        place = Whilecount % 5
        Whilecount += 1

        INPUT = inputtxt.get("1.0", "end-1c")
        inputlength = len(INPUT)

        userWhile = ""

        for i in range(1, inputlength):

            #Exits the loop once "e(" is read
            if INPUT[-i] == "(" and INPUT[-i-1] == "e":
                break

            #Copies the user's condition up until it reaches the characters "e(" in "while(". userWhile will end up reversed
            else:
                userWhile += INPUT[-i]

        #Because userWhile is in reverse order, reverse it again to make it the right way. 
        #Then, add that into its rightful place in the autowhile list
        autowhile[place] = userWhile[::-1]

#Allows the keypress of UP to save a user-defined for loop condition
def Save_for_input(event):

        #Taking the variable "Forcount" that was defined at the beginning of the code
        global Forcount

        #Using (Forcount % 5) for the user conditions' place because after 5 saved conditions, it will loop over and save over the first condition
        #This way, the user does not have to worry about only saving 5 conditions.
        place = Forcount % 5
        Forcount += 1

        INPUT = inputtxt.get("1.0", "end-1c")
        inputlength = len(INPUT)

        userFor = ""

        for i in range(1, inputlength):

            #Exits the loop once "r(" is read
            if INPUT[-i] == "(" and INPUT[-i-1] == "r":
                break

            #Copies the user's condition up until it reaches the characters "r(" in "for(". userFor will end up reversed
            else:
                userFor += INPUT[-i]

        #Because userFor is in reverse order, reverse it again to make it the right way. 
        #Then, add that into its rightful place in the autofor list
        autofor[place] = userFor[::-1]

#Binds CTRL to bringing up the matches window
inputtxt.bind("<Control_L>", Key_input)

#Binds ALT to saving the user's variable/ function
inputtxt.bind("<Alt_L>", Save_input)

#Binds DOWN to saving the user's while condition
inputtxt.bind("<Down>", Save_while_input)

#Binds UP to saving the user's for condition
inputtxt.bind("<Up>", Save_for_input)

inputtxt.pack()
  
mainloop()