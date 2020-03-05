# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 16:20:17 2019  @author: Shultzy
"""
#|--------------- Imports ---------------|
import sys
sys.path.append("C:\\Users\shult\Documents\PythonCode")
import ShultzyTools as ST
#|--------------- Variables ---------------|
ElementList = []
#|--------------- Functions ---------------|

def KillProcess(processName):
    ST.os.kill(processName)
    
def OpenFile(fileName):
    ST.os.startfile(fileName)
    
def IndentTxt(strVar, amt):
    try:
        ch = " "
        return ST.textwrap.indent(strVar, ch * amt)
    except Exception as Ex:
        ST.ErrorLogList.append("Utilities --> IndentTxt --> Indent Error:  " + str(Ex))

def MsgBox(strTitle, strBody, style: int=1):
    try:
        return ST.ctypes.windll.user32.MessageBoxW(0, strBody, strTitle, style)
    except Exception as Ex:
        ST.ErrorLogList.append("Utilities --> MsgBox --> MsgBox Error:  " + str(Ex))

def UIA_ElementRecorder():
    try:
        while ST.UIA.IsKeyPressed(0x1B) != True:
            if ST.UIA.IsKeyPressed(0x11) == True:
                element = ST.UIA.ControlFromCursor()
                ST.GUILib.UIA_Print(element)
                ElementList.append(element)
        ST.UIA.NotePadElementLogger(ElementList)
    except Exception as Ex:
        ST.ErrorLogList.append("GUICode --> UIA_ElementRecorder --> Element Recorder Failed Error:  " + str(Ex))

def PopUpBox(txtTitle, txtBody):
    try:
        pubtxt = open("C:\Temp\PuB.py", "w")
        pubtxt.write("import sys\n")
        pubtxt.write("sys.path.append('C:\\\\Users\\shult\\Documents\\PythonCode')\n")
        pubtxt.write("import ShultzyTools as ST\n\n")
        pubtxt.write("ST.ctypes.windll.user32.MessageBoxW(0, '" + txtBody + "', '" + txtTitle + "', 1)\n")
        pubtxt.close
    except Exception as Ex:
        ST.ErrorLogList.append("Utilities --> IndentTxt --> Indent Error:  " + str(Ex))
        
def CreateLogFile(error):
    try:
        lF = open("LogFile.txt", "w")
        lF.write("An Exception Has Occured at: " + ST.logging.getLevelName(error))
        lF.write("\n\nA Detailed StackTrace is as Follows:  " + str(error))
        lF.write("\n\nAdditional Information is as Follows:  " + str(ST.logging.info(error)))
        lF.write("\n\nDebug Information is as Follows:  " + str(ST.logging.debug(error)))
        lF.write("\n\n\n" + "This Exception Has Been Logged!\n")
        lF.close
    except Exception as Ex:
        ST.ErrorLogList.append("Utilities --> IndentTxt --> Indent Error:  " + str(Ex))
    
def UpdateLogFile(error):
    try:
        prog_obj = ST.os.startfile("LogFile.txt")
    except Exception as Ex:
        ST.ErrorLogList.append("Utilities --> UpdateLogFile --> Indent Error:  " + str(Ex))
        
    if prog_obj.Name != "LogFile.txt":
        ST.Utilities.CreateLogFile(error)
    
    lF = open("LogFile.txt", "a")
    lF.write("An Exception Has Occured at: " + ST.logging.getLevelName(error))
    lF.write("\n\nA Detailed StackTrace is as Follows:  " + str(error))
    lF.write("\n\nAdditional Information is as Follows:  " + str(ST.logging.info(error)))
    lF.write("\n\nDebug Information is as Follows:  " + str(ST.logging.debug(error)))
    lF.write("\n\n\n" + "This Exception Has Been Logged!\n")
    lF.close

def DeleteLogFile():
    ST.os.remove("LogFile.txt")
    print("LogFile Deleted From The System")
    
def DeleteFile(fileName):
    ST.os.remove(fileName)
    print(fileName + " Has Been Deleted From The System.")
    
    
    
    
    
    
    
    
    