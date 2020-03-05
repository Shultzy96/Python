# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 17:27:51 2019 @author: Shultzy
"""
#|--------------- Variables ---------------|
ErrorLogList = []

#|--------------- Imports ---------------|
import sys
sys.path.append("C:\\Users\shult\Documents\PythonCode")

import os
import win32com.client as c32
import win32api as api32
import win32gui as gui32
import ctypes
import comtypes
import comtypes.client 
import time
import datetime as dt
import psutil as pu
import logging
import pathlib
import textwrap
import tkinter as tk
import re

#|--------------- Custom Imports ---------------|

#|--------------- Excel Import ---------------|
try:
    import Excel  
except Exception as Ex:
    ErrorLogList.append("Failed to import Excel in the 'Custom Imports' Section of *ShultzyTools.py*  Error:  " + str(Ex))
  
#|--------------- IExplorer Import ---------------|
try:
    import IExplorer    
except Exception as Ex:
    ErrorLogList.append("Failed to import IExplorer in the 'Custom Imports' Section of *ShultzyTools.py*  Error:  " + str(Ex))

#|--------------- Utilities Import ---------------|
try:
    import Utilities   
except Exception as Ex:
    ErrorLogList.append("Failed to import Utilities in the 'Custom Imports' Section of *ShultzyTools.py*  Error:  " + str(Ex))

#|--------------- UIAutoLib Import ---------------|
try:
    import UIAutoLib as UIA    
except Exception as Ex:
    ErrorLogList.append("Failed to import UIAutoLib in the 'Custom Imports' Section of *ShultzyTools.py*  Error:  " + str(Ex))

#|--------------- GUIL Import ---------------|
try:
    import GUILib    
except Exception as Ex:
    ErrorLogList.append("Failed to import GUIL in the 'Custom Imports' Section of *ShultzyTools.py*  Error:  " + str(Ex))

#|--------- Copy/Paste Code Templates ---------|
"""    
try:
    import CodeLibrary    
except Exception as Ex:
    ErrorLogList.append("Failed to import CodeLibrary in the 'Custom Imports' Section of *ShultzyTools.py*  Error:  " + strt(Ex))
   
------------------------------------------------------------------------------------|    
    
    
"""    
    