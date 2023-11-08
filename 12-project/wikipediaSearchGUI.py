import wikipedia
from tkinter import *


def topicSummary():
    #userQuery = str(input("Enter a topic name <> "))
    #resultSummary = wikipedia.summary(userQuery)
    #print(resultSummary)
    q=get_q.get()
    text.insert(INSERT, wikipedia.summary(q))

def topicSearch():
    #userQuery = str(input("Topic Search <> "))
    #resultSearch = wikipedia.search(userQuery)
    #print(resultSearch)
    q=get_q.get()
    text.insert(INSERT, wikipedia.search(q))

root = Tk()

root.title("WIKI Search App")
question = Label(root, text='Question')
question.pack()
get_q=Entry(root,bd=5)
get_q.pack()

submit = Button(root, text='Topic Summary Search', command=topicSummary)
submit.pack()
submit = Button(root, text='Topic Search', command=topicSearch)
submit.pack()

text=Text(root)
text.pack()

root.mainloop()