from tkinter import *
import random
import datetime as dt

window = Tk()

#---GLOBAL VARIABLES ---
tNumber1 = 8
tNumber2 = random.randint(0,12)
tNumber3 = random.randint(0,12)

tNumber10 = random.randint(0,12)
tNumber11 = random.randint(0,12)
tNumber12 = random.randint(0,12)
tNumber13 = random.randint(0,12)

answer =[]
answerPos = []
questionCounter = 0
timeOfQuestion = ''

#---FUNCTIONS---
def getTest(event):

    global tNumber1, questionAnswer, tNumber1, tNumber2, answerPos1, answerPos2, answerPos3, answerPos4, finalVal, questionCounter
    
    #print("Hellow World")
    #print(event)
    #print(str(event.widget))
    print('---Pilih Sifir Button Position---')
    position = str(event.widget)

    #print(position[7])
       
    try:
        #print(position[16])
        vButton = position[16]
        
    except IndexError:
        #print('1')
        vButton = 1
        

    vFrame = position[7]

    if int(vFrame) == 2:
        finalVal = int(vButton)
        

    if int(vFrame) == 3:
        finalVal = int(vButton) + 6
       

    #print(vFrame)
    #print(vButton)
    print(str(finalVal))

    print('---Clear ResultList---')
    resultList.delete('0','end')

    print('---Clear Analisis Counter')
    questionCounter = 0
    label19.config(text=str(questionCounter))

    generateQuestion()

    return

def generateQuestion():

    global tNumber1, tNumber2, questionAnswer, questionCounter, timeOfQuestion

    print('---Generate Question---')
    timeOfQuestion = dt.datetime.now()
    print(timeOfQuestion)
    questionCounter += 1
    label19.config(text=str(questionCounter))

    tNumber1 = finalVal
    label2.config(text=tNumber1)

    tNumber2 = random.randint(0,12)
    label4.config(text=tNumber2)

    questionAnswer = int(tNumber1) * int(tNumber2)
    print('Question is ' + str(tNumber1) + ' x ' + str(tNumber2))

    generateAnswer()

    return

def generateAnswer():

    global answerPos, Answer
    print('---Generate Answer---')

    answer =[]
    answerPos = []

    answer.append(questionAnswer)
    answer.append(int(tNumber1) * random.randint(0,12))
    answer.append(int(tNumber1) * random.randint(0,12))
    answer.append(int(tNumber1) * random.randint(0,12))

    anwser = random.shuffle(answer)

    tNumber10 = answer[0]
    tNumber11 = answer[1]
    tNumber12 = answer[2]
    tNumber13 = answer[3]

    bs20.config(text=tNumber10)
    bs21.config(text=tNumber11)
    bs22.config(text=tNumber12)
    bs23.config(text=tNumber13)

    print(answer)
    
    answerPos.append(answer[0])
    answerPos.append(answer[1])
    answerPos.append(answer[2])
    answerPos.append(answer[3])

    print(answerPos)

    return

def result(event):

    print('---Result Event Button---')

    global finslResultB, answerPos, timeOfAnswer, timeTaken
    finalResultB = 0
    timeOfAnswer = dt.datetime.now()
    timeTaken= timeOfAnswer-timeOfQuestion
    
   
    #print('Result Debug')
    #print(str(event.widget))

    position = str(event.widget)
    
    try:
        vFrame = position[7]
    except IndexError:
        vFrame = 6

    try:
        vButton = position[16]

    except IndexError:
        vButton = 1
     
    print('Value of vFrame = ' + str(vFrame))
    print('value of vButton = ' + str(vButton))

    if int(vFrame) == 6:
        if int(vButton) == 1:
            finalResultB = int(0)

    if int(vFrame) == 6:
        if int(vButton) == 2:
            finalResultB = int(1)

    if int(vFrame) == 7:
        if int(vButton) == 1:
            finalResultB = int(2)

    if int(vFrame) == 7:
        if int(vButton) == 2:
            finalResultB = int(3)

    print('finalResultB ' + str(finalResultB))
    print('questionAnswer ' + str(questionAnswer))
    print('answerPos array = ' + str(answerPos))
    print('answerPos[finalResultB] = ' + str(answerPos[int(finalResultB)]))

    if int(questionAnswer) == int(answerPos[finalResultB]):
        print("Betul!")
        resultList.insert(0, str(timeTaken) + " Betul ")

    if int(questionAnswer) != int(answerPos[finalResultB]):
        print("Salah, jawapan yang betul adalah " + str(questionAnswer))
        resultList.insert(0, str(timeTaken) + " Salah, jawapan " + str(tNumber1) + " x " + str(tNumber2) + " = " + str(questionAnswer))

    generateQuestion()

    return

        
    
#---FRAMES---
window.title("Sifir App by Norzam")
aFrame = Frame(window) # Pilih sifir
aFrame.pack()

bFrame = Frame(window) # Row pilihan pertama
bFrame.pack()

cFrame = Frame(window) # Row pilihan kedua
cFrame.pack()

dFrame = Frame(window) # Soalan
dFrame.config(relief=GROOVE)
dFrame.pack()

eFrame = Frame(window) # Pilih kenyataan
eFrame.pack()

fFrame = Frame(window) # Row Jawapan Pertama
fFrame.pack()

gFrame = Frame(window) # Row Jawapan Keuda
gFrame.pack()

g1Frame = Frame(window) # Keputusan
g1Frame.pack()

g2Frame = Frame(window) # Scroll keputusan
g2Frame.pack()

#---Scroll bar FRAME---

hFrame = Scrollbar(g2Frame)
hFrame.pack(side=RIGHT, fill=Y)

resultList = Listbox(g2Frame, width=50, yscrollcommand = hFrame.set)

resultList.pack(side=LEFT, fill=Y)
hFrame.config(command = resultList.yview)

#----FRAME continue

iFrame = Frame(window) #Analisis Title
iFrame.pack()

jFrame = Frame(window) #Bil Soalan
jFrame.pack()


#---LABEL----
label1 = Label(aFrame,text="Pilih sifir yang hendak diuji")
label1.pack(side=LEFT)

#label2a = Label(dFrame,text='Pilih jawapan yang betul kepada masalah di bawah:')
#label2a.pack()

label2 = Label(dFrame,text=tNumber1, font=('',50))
label2.pack(side=LEFT)

label3 = Label(dFrame,text=' x ', font=('',50))
label3.pack(side=LEFT)

label4 = Label(dFrame,text=tNumber2, font=('',50))
label4.pack(side=LEFT)

label5 = Label(eFrame,text='Pilih jawapan yang betul bagi masalah di atas:')
label5.pack()

label6 = Label(g1Frame,text='Keputusan :')
label6.pack()

label7 = Label(iFrame, text='Analisis')
label7.pack()

label18 = Label(jFrame, text='Bil. Soalan :')
label18.pack(side=LEFT)

label19 = Label(jFrame, text=questionCounter)
label19.pack(side=LEFT)
#---ENTRIES---

#---BUTTON---

#B Frame

bs1 = Button(bFrame, text='1', width=5, font=('',12))
bs2 = Button(bFrame, text='2', width=5, font=('',12))
bs3 = Button(bFrame, text='3', width=5, font=('',12))
bs4 = Button(bFrame, text='4', width=5, font=('',12)) 
bs5 = Button(bFrame, text='5', width=5, font=('',12)) 
bs6 = Button(bFrame, text='6', width=5, font=('',12)) 
bs7 = Button(cFrame, text='7', width=5, font=('',12)) 
bs8 = Button(cFrame, text='8', width=5, font=('',12)) 
bs9 = Button(cFrame, text='9', width=5, font=('',12)) 
bs10 = Button(cFrame, text='10', width=5, font=('',12)) 
bs11 = Button(cFrame, text='11', width=5, font=('',12)) 
bs12 = Button(cFrame, text='12', width=5, font=('',12))

#F Frame

bs20 = Button(fFrame, text=tNumber10, font=('',20), width = 10)
bs21 = Button(fFrame, text=tNumber11, font=('',20), width = 10)

#G Frame

bs22 = Button(gFrame, text=tNumber12, font=('',20), width = 10)
bs23 = Button(gFrame, text=tNumber13, font=('',20), width = 10)

bs1.pack(side=LEFT)
bs2.pack(side=LEFT)
bs3.pack(side=LEFT)
bs4.pack(side=LEFT)
bs5.pack(side=LEFT)
bs6.pack(side=LEFT)
bs7.pack(side=LEFT)
bs8.pack(side=LEFT)
bs9.pack(side=LEFT)
bs10.pack(side=LEFT)
bs11.pack(side=LEFT)
bs12.pack(side=LEFT)

bs20.pack(side=LEFT)
bs21.pack(side=LEFT)
bs22.pack(side=LEFT)
bs23.pack(side=LEFT)

#---BUTTON EVENTS---
bs1.bind("<Button-1>", getTest)
bs2.bind("<Button-1>", getTest)
bs3.bind("<Button-1>", getTest)
bs4.bind("<Button-1>", getTest)
bs5.bind("<Button-1>", getTest)
bs6.bind("<Button-1>", getTest)
bs7.bind("<Button-1>", getTest)
bs8.bind("<Button-1>", getTest)
bs9.bind("<Button-1>", getTest)
bs10.bind("<Button-1>", getTest)
bs11.bind("<Button-1>", getTest)
bs12.bind("<Button-1>", getTest)

bs20.bind("<Button-1>", result)
bs21.bind("<Button-1>", result)
bs22.bind("<Button-1>", result)
bs23.bind("<Button-1>", result)

window.mainloop()
