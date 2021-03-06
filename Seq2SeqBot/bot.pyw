import _thread
from bot_util import *
import tensorflow as tf
import execute

sess = tf.Session()
sess, model, enc_vocab, rev_dec_vocab = execute.init_session(sess, conf='seq2seq_serve.ini')

def ClickMe():
    # Write message to chat window
    EntryText = FilteredMessage(EntryBox.get("0.0", END))
    LoadMyEntry(ChatLog, EntryText, sess, model, enc_vocab, rev_dec_vocab)

    # Scroll to the bottom of chat windows
    ChatLog.yview(END)

    # Erase previous message in Entry Box
    EntryBox.delete("0.0", END)


def PressAction(event):
	EntryBox.config(state=NORMAL)
	ClickMe()
def Disable(event):
	EntryBox.config(state=DISABLED)

#Create a window
root = Tk()
root.title('NLP_Bot')
root.geometry("400x550")
#root.resizable(width=FALSE, height=FALSE)

#Chat window
ChatLog = Text(root, bd=0, bg="#FAFAFA", height="8", width="50", font="Arial",)
ChatLog.insert(END, "Hey there!\n")
ChatLog.config(state=DISABLED)

#Bind a scrollbar to the Chat window
sbar = Scrollbar(root, command=ChatLog.yview, cursor="heart")
ChatLog['yscrollcommand'] = sbar.set

#Button to send message
SendButton = Button(root, font=30, text="Send", width="5", height="5", bd=0, bg="#2ecc71", activebackground="#27ae60",
                    fg="#FFFFFF", command=ClickMe)

#Box to enter message
EntryBox = Text(root, bd=0, bg="white",width="29", height="5", font="Arial", padx=5,pady=5)
EntryBox.bind("<Return>", Disable)
EntryBox.bind("<KeyRelease-Return>", PressAction)

#Place on screen
sbar.place(x=376,y=6, height=486)
ChatLog.place(x=6,y=6, height=486, width=370)
EntryBox.place(x=110, y=501, height=40, width=280)
SendButton.place(x=6, y=501, height=40, width=100)

root.mainloop()
