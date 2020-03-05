# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 18:08:23 2020 --- @author: Shultzy
GUIL = Graphical User Interface Library
"""
#|--------------- Imports ---------------|
import sys
sys.path.append("C:\\Users\shult\Documents\PythonCode")
import ShultzyTools as ST
#|----------- Working Examples ------------|
"""
def ListAllElements():
    oDE = ST.UIA.GetRootControl()
    child = ST.UIA.Control.GetFirstChildControl(oDE)
    while child:
        try:
            print("Name:" + "  " + child.Name)
        except:
            child = child.GetNextSiblingControl()
            pass
        child = child.GetNextSiblingControl()
        
"""
#|--------------- Variables ---------------|
oTreeWalker = ST.UIA._AutomationClient()
counter = 0
ListElements = []
#|--------------- Functions ---------------|


def UIA_ListAllElements():
    oDE = ST.UIA.GetRootControl() #This is the Desktop Element --- This also Creates and Gets the TreeWalker Element for use in all future UIA calls
    child = ST.UIA.Control.GetFirstChildControl(oDE) #Gets the FirstChildElement of the Desktop Element and Walks Down one step of the TreeWalker
    while child:
        try:
            UIA_Print(child)
            child = child.GetNextSiblingControl()
        except:
            child = child.GetNextSiblingControl()
            pass
                
def UIA_ElementArray(Control, Depth: int=1):
    try:
        for c, d in ST.UIA.WalkControl(Control, True, Depth):
            ListElements.append(c)
        return ListElements
    except Exception as Ex:
        ST.ErrorLogList.append("GUICode --> UIA_FindElementByHwnd --> Element Not Found By Hwnd Error:  " + str(Ex))

def UIA_ElementArrayByControlType(strControlType, control):
    try:
        for c, d in ST.UIA.WalkControl(control, True, 1):
            if c.ControlTypeName.find(strControlType) == 0:
                ListElements.append(c)
        return ListElements
    except Exception as Ex:
        ST.ErrorLogList.append("GUICode --> UIA_FindElementByHwnd --> Element Not Found By Hwnd Error:  " + str(Ex))


def UIA_FindElementByHwnd(hwnd, control, maxDepth):
    """
        Find Element By Handle and Return It.
        control: `Control` or its subclass.
        maxDepth: int, enum depth.
        showAllName: True
        startDepth: int, control's current depth.
    """
    try:
        for c, d in ST.UIA.WalkControl(control, True, maxDepth):
            if str(c.NativeWindowHandle).find(str(hwnd)) == 0:
                return c
    except Exception as Ex:
        ST.ErrorLogList.append("GUICode --> UIA_FindElementByHwnd --> Element Not Found By Hwnd Error:  " + str(Ex))
        
def UIA_FindElementByName(strName, control, maxDepth):
    """
        Find Element By Name and Return It.
        control: `Control` or its subclass.
        maxDepth: int, enum depth.
        showAllName: True
        startDepth: int, control's current depth.
    """
    try:
        for c, d in ST.UIA.WalkControl(control, True, maxDepth):
            if c.Name.find(strName) == 0:
                return c
    except Exception as Ex:
        ST.ErrorLogList.append("GUICode --> UIA_FindElementByName --> WalkControl - Element Error:  " + str(Ex))
        
def UIA_FindElementByClassName(strClassName, control, maxDepth):
    """
        Find Element By ClassName and Return It.
        control: `Control` or its subclass.
        maxDepth: int, enum depth.
        showAllName: True
        startDepth: int, control's current depth.
    """
    try:
        for c, d in ST.UIA.WalkControl(control, True, maxDepth):
            if c.ClassName.find(strClassName) == 0:
                return c
    except Exception as Ex:
        ST.ErrorLogList.append("GUICode --> UIA_FindElementByClassName --> WalkControl - Element Error:  " + str(Ex))
        
def UIA_FindElementByControlTypeName(strCTName, control, maxDepth):
    """
        Find Element By ControlTypeName and Return It.
        control: `Control` or its subclass.
        maxDepth: int, enum depth.
        showAllName: True
        startDepth: int, control's current depth.
    """
    try:
        for c, d in ST.UIA.WalkControl(control, True, maxDepth):
            if c.ControlTypeName.find(strCTName) == 0:
                return c
    except Exception as Ex:
        ST.ErrorLogList.append("GUICode --> UIA_FindElementByControlTypeName --> WalkControl - Element Error:  " + str(Ex))

def UIA_FindElementByCTandName(strCTName, strName, control, maxDepth):
    """
        Find Element By ControlTypeName and Name Then Return It.
        control: `Control` or its subclass.
        maxDepth: int, enum depth.
        showAllName: True
        startDepth: int, control's current depth.
    """
    try:
        for c, d in ST.UIA.WalkControl(control, True, maxDepth):
            if c.ControlTypeName.find(strCTName) == 0 and c.Name.find(strName) == 0:
                return c
    except Exception as Ex:
        ST.ErrorLogList.append("GUICode --> UIA_FindElementByCTandName --> WalkControl - Element Error:  " + str(Ex))
        
def UIA_Print(element):
    try:
        print("\n|--------------------|")
        print("Name:" + "  " + str(element.Name))
        print("ClassName:" + "  " + str(element.ClassName))
        print("AutomationID:" + "  " + str(element.AutomationId))
        if element.NativeWindowHandle == 0:
            print("No Handle Found")
        else:
            print("NativeWindowHandle:" + "  " + str(element.NativeWindowHandle))
            
        print("FrameworkID:" + "  " + str(element.FrameworkId))
        print("ProcessID:" + "  " + str(element.ProcessId))
        print("ControlTypeName:" + "  " + str(element.ControlTypeName))
        print("ControlTypeID:" + "  " + str(element.ControlType))
        #print("Control:" + "  " + str(element.Control))
        #print("Element:" + "  " + str(element.Element))
        #print("LegacyIAccessiblePattern:" + "  " + str(element.GetLegacyIAccessiblePattern))
        #print("PropertyValue:" + "  " + str(element.GetPropertyValue))
        #print("RuntimeId:" + "  " + str(element.GetRuntimeId))
        #print("WindowText:" + "  " + str(element.GetWindowText))
        print("AccessKey:" + "  " + str(element.AccessKey))
        print("AcceleratorKey:" + "  " + str(element.AcceleratorKey))
        print("AriaRole:" + "  " + str(element.AriaRole))
        print("AriaProperties:" + "  " + str(element.AriaProperties))
        print("Culture:" + "  " + str(element.Culture))
        print("HelpText:" + "  " + str(element.HelpText))
        print("HasKeyboardFocus:" + "  " + str(element.HasKeyboardFocus))
        print("IsContentElement:" + "  " + str(element.IsContentElement))
        print("IsControlElement:" + "  " + str(element.IsControlElement))
        print("IsDataValidForForm:" + "  " + str(element.IsDataValidForForm))
        print("ItemStatus:" + "  " + str(element.ItemStatus))
        print("ItemType:" + "  " + str(element.ItemType))
        print("LocalizedControlType:" + "  " + str(element.LocalizedControlType))
        print("Orientation:" + "  " + str(element.Orientation))              
        if element.IsEnabled == 0:
            print("IsEnabled:" + "  " + str(element.IsEnabled) + " (False)")
        else:
            print("IsEnabled:" + "  " + str(element.IsEnabled) + " (True)")

        if element.IsOffscreen == 0:
            print("IsOffscreen:" + "  " + str(element.IsOffscreen) + " (False)")
        else:
            print("IsOffscreen:" + "  " + str(element.IsOffscreen) + " (True)")

        if element.IsKeyboardFocusable == 0:
            print("IsKeyboardFocusable:" + "  " + str(element.IsKeyboardFocusable) + " (False)")
        else:
            print("IsKeyboardFocusable:" + "  " + str(element.IsKeyboardFocusable) + " (True)")

        if element.IsRequiredForForm == 0:
            print("IsRequiredForForm:" + "  " + str(element.IsRequiredForForm) + " (False)")
        else:
            print("IsRequiredForForm:" + "  " + str(element.IsRequiredForForm) + " (True)")
            
    except Exception as Ex:
        ST.ErrorLogList.append("GUICode --> UIA_PrintDetails --> Element/Print Error:  " + str(Ex))
        pass
    
class ElementRecorderGUI():
    
    def SERUI():

        def StartRecorder():
            erDialog.destroy()
            ST.Utilities.MsgBox('SERUI Instructions:', 'Hover Over an Element and Press {CTRL} to Record Element.\\nPress {ESC} to Exit Recording Mode.', 1)
            ST.Utilities.UIA_ElementRecorder()
            ElementRecorderGUI.SERUI()
        
        def GetParents():
            ST.UIA.NotePadLogParents(ST.Utilities.ElementList)
            ST.Utilities.OpenFile('C:\Temp\ParentsTreeLog.txt')
            
        def RecorderResults():
            ST.Utilities.OpenFile('C:\Temp\ElementLog.txt')
            
        def Exit():
            erDialog.destroy()
            sys.exit('DERUI Successfully Closed')
            
        erDialog = ST.tk.Tk()
        erDialog.title('DERUI')
        erDialog.geometry('480x240')
        erDialog.configure(bg='Sky Blue')
        
        btnParents = ST.tk.Button(erDialog, text='Get Parents', bg='Grey69', font=('Arial Bold', 8), fg='Black', bd=3, command=GetParents)
        btnParents.place(x=290, y=190)
        btnResults = ST.tk.Button(erDialog, text='Results', bg='Grey69', font=('Arial Bold', 8), fg='Black', bd=3, command=RecorderResults)
        btnResults.place(x=108, y=190)

        
        txtDescript = ST.tk.Label(erDialog, text='Hover Over an Element and Press {CTRL} to Record Element.\nPress {ESC} to Exit Recording Mode.', bg='Sky Blue', fg='Black', font=('Arial Bold', 9))
        txtDescript.place(x=20, y=140)
        
        btnStart = ST.tk.Button(erDialog, text='Start', bg='Lime Green', font=('Arial Bold', 8), fg='Black', bd=3, command=StartRecorder)
        btnStart.place(x=180, y=190)
        btnExit = ST.tk.Button(erDialog, text='Exit', bg='Red', font=('Arial Bold', 8), fg='Black', bd=3, command=Exit)
        btnExit.place(x=240, y=190)

        erDialog.mainloop()