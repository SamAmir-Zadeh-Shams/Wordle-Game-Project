from tkinter import *
import random

row = 0
word = ""
word_list = ["about","above","abuse","actor","acute","admit","adopt","adult",
"after","again","agent","agree","ahead","alarm","album","alert",
"alike","alive","allow","alone","along","alter","among","anger",
"angle","angry","apart","apple","apply","arena","argue","arise",
"array","aside","asset","audio","audit","avoid","award","aware",

"badly","baker","bases","basic","basis","beach","began","begin",
"begun","being","below","bench","billy","birth","black","blame",
"blind","block","blood","board","boost","booth","bound","brain",
"brand","bread","break","breed","brief","bring","broad","broke",
"brown","build","built","buyer",

"cable","calif","carry","catch","cause","chain","chair","chart",
"chase","cheap","check","chest","chief","child","china","chose",
"civil","claim","class","clean","clear","click","clock","close",
"coach","coast","could","count","court","cover","craft","crash",
"cream","crime","cross","crowd","crown","curve","cycle",

"daily","dance","dated","dealt","death","debut","delay","depth",
"doing","doubt","dozen","draft","drama","drawn","dream","dress",
"drill","drink","drive","drove",

"eager","early","earth","eight","elite","empty","enemy","enjoy",
"enter","entry","equal","error","event","every","exact","exist",
"extra",

"faith","false","fault","fiber","field","fifth","fifty","fight",
"final","first","fixed","flash","fleet","floor","fluid","focus",
"force","forth","forty","forum","found","frame","frank","fraud",
"fresh","front","fruit","fully","funny",

"giant","given","glass","globe","going","grace","grade","grand",
"grant","grass","great","green","gross","group","grown","guard",
"guess","guest","guide",

"happy","harry","heart","heavy","hence","henry","horse","hotel",
"house","human",

"ideal","image","index","inner","input","issue","japan","jimmy",
"joint","jones","judge",

"known","label","large","laser","later","laugh","layer","learn",
"lease","least","leave","legal","level","lever","light","limit",
"links","lives","local","logic","loose","lower","lucky","lunch",

"magic","major","maker","march","maria","match","maybe","mayor",
"meant","media","metal","might","minor","minus","mixed","model",
"money","month","moral","motor","mount","mouse","mouth","movie",
"music",

"needs","never","newly","night","noise","north","novel","nurse",

"occur","ocean","offer","often","order","other","ought","paint",
"panel","paper","party","peace","peter","phase","phone","photo",
"piece","pilot","pitch","place","plain","plane","plant","plate",
"point","pound","power","press","price","pride","prime","print",
"prior","prize","proof","proud","prove","queen","quick","quiet",
"quite",

"radio","raise","range","rapid","ratio","reach","ready","refer",
"right","rival","river","robin","roger","roman","rough","round",
"route","royal","rural",

"scale","scene","scope","score","sense","serve","seven","shall",
"shape","shard","share","sharp","sheet","shelf","shell","shift","shirt",
"shock","shoot","short","shown","sight","since","sixth","sixty",
"sized","skill","sleep","slide","small","smart","smile","smith",
"smoke","solid","solve","sorry","sound","south","space","spare",
"speak","speed","spend","spent","split","spoke","sport","staff",
"stage","stake","stand","start","state","steam","steel","stick",
"still","stock","stone","stood","store","storm","story","strip",
"stuck","study","stuff","style","sugar","suite","super","sweet",

"table","taken","taste","taxes","teach","teeth","terry","texas",
"thank","their","theme","there","these","thick","thing","think",
"third","those","three","threw","throw","tight","times","tired",
"title","today","topic","total","touch","tough","tower","track",
"trade","train","treat","trend","trial","tried","tries","truck",
"truly","trust","truth","twice",

"under","union","unity","until","upper","upset","urban","usage",
"usual",

"valid","value","video","virus","visit","vital","voice",

"waste","watch","water","wheel","where","which","while","white",
"whole","whose","woman","women","world","worry","worse","worst",
"worth","would","wound","write","wrong","wrote",

"yield","young","youth"]

def validateLength(p):
  if len(p)<=1:
    return True
  return False


def clearframe(frame):
  for widget in frame.winfo_children():
    widget.destroy()

def submit_press():
  global row
  global word
  lettersFilled = True

  if row < 6:
    for i in range(5):
      if letter[row][i].get().strip():
        continue
      else:
        lettersFilled = False
        break

    
    if lettersFilled:
      colors = ["gray","gray","gray","gray","gray"]
      wordCopy = list(word)
      for i in range(5):
        if letter[row][i].get() == word[i]: 
          colors[i] = "green"
          wordCopy.remove(letter[row][i].get())

      for i in range(5):
        if colors[i] != "green":
          if letter[row][i].get() in wordCopy:
            colors[i] = "yellow"
            wordCopy.remove(letter[row][i].get())
        if colors[i] == "green":
          letter[row][i].config(state=DISABLED,disabledbackground="green",fg="black")
        elif colors[i] == "yellow":
          letter[row][i].config(state=DISABLED,disabledbackground="yellow",fg="black")
        else:
          letter[row][i].config(state=DISABLED,disabledbackground="gray",fg="black")
      row = row + 1

      if "".join(letter[row-1][j].get() for j in range(5)) == word:
        frame2Label.config(text="Congrats, you guessed the word correctly!")
        row = 7
      elif row == 6:
        frame2Label.config(text="Sorry, you have lost the game.")
      else:
        frame2Label.config(text=f"Current row: {row+1}" )

      if row < 6: gridDisplayer()

      

def gridDisplayer():
  for j in range (5):
    letter[row][j] = (Entry(frame1, width=3, font=("Helvetica", 24),justify = 'center', bg = "white", fg = "black", validate = 'key',validatecommand=vcmd))
    letter[row][j].grid(row=row,column=j)
    letter[row][j].bind("<KeyPress>", lambda e, j=j: auto_tab(e,j))
    letter[row][0].focus()


def resetButton():
  global row
  
  row = 0
  for i in range (6):
    for j in range (5):
      letter[i][j] = ""

  clearframe(frame1)

  frame2Label.config(text = f"Current row: {row+1}")

  wordGenerator()

  gridDisplayer()


def wordGenerator():
  global word
  word = random.choice(word_list)
  print(word)

def auto_tab(event,i):

  before_text = event.widget.get() # the widget has what was typed before

  if event.keysym != "BackSpace" and event.char.isalpha():
    if i!=4:
      event.widget.tk_focusNext().focus() # puts the focus on to the next entrybox after a letter is typed
  elif i == 4 and before_text.isalpha() and event.keysym == "Return":
    submit_press()
  elif i == 4 and before_text == "" and event.keysym == "BackSpace": # makes it focus on the last entrybox if there is no text and backspacced is pressed
    previous = event.widget.tk_focusPrev()
    previous.focus()
    previous.delete(0,'end')
  elif event.keysym == "BackSpace" and i != 0 and i!=4: # deletes what in the entry box and puts focus on last entry box
    previous = event.widget.tk_focusPrev()
    previous.focus()
    previous.delete(0,'end')
  elif not event.char.isalpha() and not event.keysym == "BackSpace": # if what was just typed is not a letter and not a BackSpace
    return "break" # prevents what was just typed from being inputted

window = Tk()
window.geometry("500x500")

window.title("Wordle Game")

frame = Frame(window)
frame.grid(row=0,column=0)

frame1 = Frame(window)
frame1.grid(row=1,column=0)

frame2 = Frame(window)
frame2.grid(row=2,column=0)

frame2Label = Label(frame2, text = f"Current row: {row+1}" )
frame2Label.grid(row=0,column=0)

reset = Button(frame2, text = "Reset", state = NORMAL, command = lambda: resetButton())
reset.grid(row=1,column=0)
letter = [[0 for _ in range(5)] for _ in range(6)]

vcmd = (window.register(validateLength),'%P')

# checkIfFilled_var = [[StringVar() for j in range(5)] for i in range(6)]
# checkIfFilled_var[0][0].trace_add("write",check_var)

submit = Button(frame, text = "Submit", state = NORMAL, command = lambda: submit_press())
submit.grid(row=0,column=0)

for i in range(5):
  letter[0][i] = (Entry(frame1, width=3, font=("Helvetica", 24),justify = 'center', bg = "white", fg = "black", validate = 'key',validatecommand=vcmd))
  letter[0][i].grid(row=0,column=i)
  letter[0][i].bind("<KeyPress>", lambda e, i=i: auto_tab(e,i))
  letter[0][0].focus()
  #letter[0][0].grab_set()

wordGenerator()



window.mainloop()
