#Name:Nikhil Uppar
#Description: Launching the Schneider server
#Parameters: None
def Launch_server():
  TestedApps.SystemServer.Run()
  test_boundary_data("SE_Moolyaas_Test","P@ssw0rd1234")
  open_console()
  start_server()
  
#Name:Nikhil Uppar
#Description: Login page 
#Parameters: Username ,Password and login button
def test_boundary_data(user, pwd):
  username = Sys.Process("SystemServer").WPFObject("HwndSource: LogOnDialog", "").WPFObject("LogOnDialog", "", 1).WPFObject("Grid", "", 1).WPFObject("Grid", "", 1).WPFObject("UserName")
  aqUtils.Delay(3000)
  password = Sys.Process("SystemServer").WPFObject("HwndSource: LogOnDialog", "").WPFObject("LogOnDialog", "", 1).WPFObject("Grid", "", 1).WPFObject("Grid", "", 1).WPFObject("PasswordBox")
  Login_btn = Sys.Process("SystemServer").WPFObject("HwndSource: LogOnDialog", "").WPFObject("LogOnDialog", "", 1).WPFObject("Grid", "", 1).WPFObject("Grid", "", 1).WPFObject("StackPanel", "", 1).WPFObject("Button", "Log In", 1)
  username.SetText(user)
  password.SetText(pwd)
  Login_btn.Click()
  
  Warning_message = Sys.Process("SystemServer").WPFObject("HwndSource: LogOnDialog", "").WPFObject("LogOnDialog", "", 1).WPFObject("Grid", "", 1).WPFObject("Grid", "", 3).WPFObject("TextBlock", "Wrong username or password or the user is disabled in the Security Editor on the system server computer", 1)
  if Warning_message.Exists:
    aqUtils.Delay(3000)
    Log.Error(Warning_message.WPFControlText)
  else:
    Log.Message("Success")

#Name:Nikhil Uppar
#Description: Hidden apps tray
#Parameters: none    
def open_console():
  abc = Sys.Process("explorer").Window("Shell_TrayWnd", "", 1)
  abc.ClickR(1569+75, 35)
  Sys.Keys("[Tab]")
  Sys.Keys("[Enter]")

#Name:Nikhil Uppar
#Description: Start Server
#Parameters: None
def start_server():
  action_menu = Sys.Process("SystemServer").WPFObject("HwndSource: MainWindow", "EcoStruxure Process Expert - System Server").WPFObject("MainWindow", "EcoStruxure Process Expert - System Server", 1).WPFObject("Grid", "", 1).WPFObject("MainMenu").WPFObject("ActionMenu").Click()
  start_btn = Sys.Process("SystemServer").WPFObject("HwndSource: PopupRoot", "").WPFObject("PopupRoot", "", 1).WPFObject("Decorator", "", 1).WPFObject("NonLogicalAdornerDecorator", "", 1).WPFObject("MenuItem", "Start", 1)
  start_btn.Click()
  server_console = Sys.Process("SystemServer").WPFObject("HwndSource: MainWindow", "EcoStruxure Process Expert - System Server").WPFObject("MainWindow", "EcoStruxure Process Expert - System Server", 1).WPFObject("Grid", "", 1).WPFObject("Terminal").WPFObject("Grid", "", 1).WPFObject("OutputWindow").WPFObject("Grid", "", 1).WPFObject("Console").wText
  if server_console.Exists:
    Log.Message("Server started")
    if wText("Server is ready").Exists:
      Log.Message("Server is ready")
  else:
    Log.Message("Server is not ready")