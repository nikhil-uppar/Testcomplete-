def calcu():
  Log.Message(Project.Variables.first_name)

def kaboom():
  #Log.Message(1/0)
  try:
    Log.Message(first_name)
    Log.Message(1/0)
  except (ZeroDivisionError,NameError):
    Log.Message("Cant divide by zero")
    Log.Message("Name is not available")
  