# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 15:21:55 2019

@author: leonardo Felipe
"""
import os
import sys
from pathlib import Path
import shutil
import pandas as pd
from datetime import date

def files_path(path):
    return [os.path.join(file) for p, _, files in os.walk(os.path.abspath(path)) for file in files]

def files_path1(*args):
    l = []
    k = []
    for item in args:
        for p, _, files in os.walk(os.path.abspath(item)):
            for file in files:
                l.append((file))
                k.append((p+'\\'+file))
    return (l, k)

diretorios = os.listdir('./contas/')
files2 = files_path1('./organização/')

for lista in diretorios:
    for i in files2[0]:
        for j in files2[1]:
            jn = j.split('\\')
            if i == jn[6] and lista[:9:] == i[:9:]:
                ondeVem = (jn[0]+'\\'+jn[1]+'\\'+jn[2]+'\\'+jn[3]+'\\'+jn[4]+'\\'+jn[5]+'\\'+jn[6])
                destino = ('./'+lista+'/')
                shutil.move(ondeVem, destino)

