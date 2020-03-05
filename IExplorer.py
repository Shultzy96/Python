# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 19:11:53 2019 @author: Shultzy
"""
#|--------------- Imports ---------------|
import sys
sys.path.append("C:\\Users\shult\Documents\PythonCode")
import ShultzyTools as ST
#|--------------- Variables ---------------|

#|--------------- Functions ---------------|

def StartIE():
    ie = ST.c32.Dispatch("InternetExplorer.Application")
    ie.Visible = True
    return ie

def OpenIE(URL):    
    ie = ST.c32.Dispatch("InternetExplorer.Application")
    ie.Visible = True
    ie.Navigate(URL)
    return ie
    
def GetIE():
    ie = ST.c32.Dispatch("InternetExplorer.Application")
    return ie

def Navigate(ie, URL):
    ie.Navigate(URL)

def GoBack(ie):
    ie.GoBack
    
def GoForward(ie):
    ie.GoForward
    
def GoHome(ie):
    ie.GoHome
    
def GoSearch(ie):
    ie.GoSearch
    
def Refresh(ie):
    ie.Refresh
    
def NewWindow(ie):
    ie.NewWindow
    
    