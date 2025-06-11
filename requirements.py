
import pip
def import_or_install(package):
    try:
        __import__(package)
    except ImportError:
        pip.main(['install','--user', package])
import_or_install("tkinter")
import_or_install("PIL")
import_or_install("customtkinter")
import_or_install("matplotlib")
import_or_install("numpy")
import_or_install("webbrowser")
import_or_install("datetime")

from tkinter import *
from tkinter import ttk, messagebox, font, Text
from tkinter.font import Font
from PIL import Image, ImageTk
from customtkinter import *
import matplotlib.pyplot as plt
import numpy as np
import csv
from tkinter.font import nametofont
import webbrowser
from datetime import datetime
import warnings
import pandas as pd
from tkinter import font as tkfont


warnings.filterwarnings('ignore')
BG = "#4c5f61"
text_color = "#46e0eb"
adder_Font_tuple = ("Comic Sans MS", 16, "bold")
Font_tuple = ("Comic Sans MS", 20, "bold")
menuFont_tuple = ("Comic Sans MS", 18, "bold")
names = ["pcmc","pcmb", "Select"]
terms = ["Periodic 1","Mid Term", "Periodic 2","Anual Exam","Overall", "Select"]
resFont_tuple = ("JasmineUPC", 22, "bold")
titlefont = ("Comic Sans MS", 30, "bold")
apptitlefont = ("Comic Sans MS", 70, "bold")
t = "     "
color = {"nero": "#252726", "orange": "#FF8700", "darkorange": "#FE6101"}