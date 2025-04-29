#Author : Nikhil Uppar
#Description : Launching the engineering client
#Parameters : None
def launch_engg_client():
  TestedApps.EngineeringClient.Run()
  
#########################################################################################################################################
#Author : Nikhil Uppar
#Description : Topology and Project explorer view
#Parameters : None
def topology_exp():
 select_system = Sys.Process("EngineeringClient").WPFObject("HwndSource: Main").WPFObject("Main").WPFObject("Grid", "", 2).WPFObject("Grid", "", 1).WPFObject("WorkspaceControl").WPFObject("FrameHostContainer", "", 1).WPFObject("FrameHostControl", "", 1).WPFObject("UserControl", "", 1).WPFObject("ContentControl", "", 1).WPFObject("SystemsExplorer", "", 1).WPFObject("Grid", "", 1).WPFObject("SystemsTree").WPFObject("CoreGraph", "", 1).WPFObject("ExplorerNode", "", 4)
 select_system.Click()
 clk_topology = Sys.Process("EngineeringClient").WPFObject("HwndSource: Main").WPFObject("Main").WPFObject("MainBarGrid").WPFObject("Grid", "", 2).WPFObject("PartContent").WPFObject("PartMainBar").WPFObject("StackPanel", "", 1).WPFObject("MainToolBar").WPFObject("ContentPresenter", "", 5).WPFObject("PartContainer").WPFObject("PartButton")
 clk_topology.Click()
 sv_project_browser = Sys.Process("EngineeringClient").WPFObject("HwndSource: Main").WPFObject("Main").WPFObject("Grid", "", 2).WPFObject("Grid", "", 1).WPFObject("WorkspaceControl").WPFObject("FrameHostContainer", "", 1).WPFObject("FrameHostControl", "", 1).WPFObject("UserControl", "", 1).WPFObject("ContentControl", "", 1).WPFObject("ProjectExplorer", "", 1).WPFObject("Grid", "", 1).WPFObject("radDocking").WPFObject("RadSplitContainer", "", 1).WPFObject("ProjectBrowserPaneGroup").WPFObject("Grid", "", 1).WPFObject("BaseTreeListView", "", 1)
 cntlr_one = Sys.Process("EngineeringClient").WPFObject("HwndSource: Main").WPFObject("Main").WPFObject("Grid", "", 2).WPFObject("Grid", "", 1).WPFObject("WorkspaceControl").WPFObject("FrameHostContainer", "", 1).WPFObject("FrameHostControl", "", 1).WPFObject("UserControl", "", 1).WPFObject("ContentControl", "", 1).WPFObject("ProjectExplorer", "", 1).WPFObject("Grid", "", 1).WPFObject("radDocking").WPFObject("RadSplitContainer", "", 1).WPFObject("ProjectBrowserPaneGroup").WPFObject("Grid", "", 1).WPFObject("Tree").WPFObject("TreeListViewRow", "", 2).WPFObject("GridViewCell", "", 1)
 cntrl_prjt = Sys.Process("EngineeringClient").WPFObject("HwndSource: Main").WPFObject("Main").WPFObject("Grid", "", 2).WPFObject("Grid", "", 1).WPFObject("WorkspaceControl").WPFObject("FrameHostContainer", "", 1).WPFObject("FrameHostControl", "", 1).WPFObject("UserControl", "", 1).WPFObject("ContentControl", "", 1).WPFObject("ProjectExplorer", "", 1).WPFObject("Grid", "", 1).WPFObject("radDocking").WPFObject("RadSplitContainer", "", 1).WPFObject("ProjectBrowserPaneGroup").WPFObject("UnityProjectTreePane").WPFObject("Grid", "", 1).WPFObject("TextBlock", "Control Project", 1)
 if sv_project_browser.Exists:
  cntrl_prjt.Click()
  aqUtils.Delay(500)
  cntlr_one.ClickR()
 else:
  cntlr_one.ClickR()
  
  
############################################################################################################################################  
#Author : Nikhil Uppar
#Description : Topology and Project explorer view
#Parameters : menu items and buttons
def Menu(num):
  menu_items = Sys.Process("EngineeringClient").WPFObject("HwndSource: PopupRoot", "").WPFObject("PopupRoot", "", 1).WPFObject("Decorator", "", 1).WPFObject("NonLogicalAdornerDecorator", "", 1).WPFObject("ContextMenu", "", 1)
  menu_items.Click()
  items = menu_items.FindAllChildren("ClrClassName","ContextMenu",16)
  for item in items:
    if item.WPFControlOrdinalNo == num:
      item.Click()
      Log.Message(f"{item.WPFControlOrdinalNo} is clicked")
    else:
      Log.Warning("Button not clicked")
  p_2_p_conn = Sys.Process("EngineeringClient").WPFObject("HwndSource: ModalDialogWindow", "").WPFObject("ModalDialogWindow", "", 1).WPFObject("ManagePeerToPeer", "", 1).WPFObject("Grid", "", 1).WPFObject("Grid", "", 1).WPFObject("BtnOk")
  p_2_p_conn.Click()
  
############################################################################################################################################  
#Author : Nikhil Uppar
#Description : Topology and Project explorer view
#Parameters : menu items and buttons  
def try_mtd():
  topology_exp()
  Menu("9")
  