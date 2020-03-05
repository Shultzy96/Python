# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 17:27:51 2019 @author: Shultzy
"""
#|--------------- Imports ---------------|
import sys
sys.path.append("C:\\Users\Documents\PythonCode")
import ShultzyTools as ST
#|--------------- Variables ---------------|

#|--------------- Functions ---------------|

def StartExcel():
    xl = ST.c32.Dispatch("Excel.Application")
    xl.Visible = True
    return xl

def OpenExcel():    
    xl = ST.c32.Dispatch("Excel.Application")
    xl.Visible = True
    xl.Workbok.Open(FileName)
    return xl
    
def GetExcel():
    xl = ST.c32.Dispatch("Excel.Application")
    return xl

def ActivateSheet(wb, SheetName):
    wb.Sheet(SheetName).activate
    
def SelectRange(wb, iCells):
    wb.ActiveSheet.Range(iCells).Select

def SetCellValue(wb, iCell, iValue):
    wb.ActiveSheet.Range(iCell).Value = iValue

def Copy(wb, iCells):
    SelectRange(wb, iCells)
    wb.ActiveSheet.Range(iCells).Copy

def Paste(wb, iCell):
    wb.ActiveSheet.Range(iCell).Paste

def NewWorkbook(wbName):
    xl = StartExcel()
    xl.Add(wbName)
    
def AddSheet(ws, SheetName):
    ws.Add(SheetName)
    
def SaveAs(wb, SaveName):
    wb.SaveAs(SaveName)

def DeleteSheet(wb, SheetName):
    wb.Sheet(SheetName).Delete
    
def RenameWorkbook(wb, wbName):
    wb.Name = wbName
    
def RenameSheet(ws, wsName):
    ws.Name = wsName
    
def ExportPDF(wb, pdfName):
    wb.ExportAsFixedFormat(0, pdfName, 0)
    
def ExportXPS(wb, xpsName):
    wb.ExportAsFixedFormat(1, xpsName, 0)

def GetPath(wb):
    wbPath = wb.Path
    return wbPath
