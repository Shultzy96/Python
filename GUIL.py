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
ElementList = []
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

def ElementArray(Control, Depth: int=1):
    try:
        for c, d in ST.UIA.WalkControl(Control, True, Depth):
            ElementList.append(c)
        return ElementList
    except Exception as Ex:
        ST.ErrorLogList.append("GUICode --> UIA_FindElementByHwnd --> Element Not Found By Hwnd Error:  " + str(Ex))

def ElementArrayByControlType(strControlType, control):
    try:
        for c, d in ST.UIA.WalkControl(control, True, 1):
            if strControlType in str(c.ControlTypeName):
                ElementList.append(c)
    except Exception as Ex:
        ST.ErrorLogList.append("GUICode --> UIA_FindElementByHwnd --> Element Not Found By Hwnd Error:  " + str(Ex))
    return ElementList

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
            if str(hwnd) in str(c.NativeWindowHandle):
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
            if strName in str(c.Name):
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
            if strClassName in str(c.ClassName):
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
            if strCTName in str(c.ControlTypeName):
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
            if strCTName in str(c.ControlTypeName) and strName in str(c.Name):
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
    
#TODO
#class ElementRecorder():
    
