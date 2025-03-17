def Test1():
  edit = Aliases.notepad.wndNotepad.Edit
  edit.DblClick(7, 9)
  edit.Keys("Good Moring[Enter]")
  
def Test2():
  Aliases.notepad.wndNotepad.Edit.wText = "someone was here"
