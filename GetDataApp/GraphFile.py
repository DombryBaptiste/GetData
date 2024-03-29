import csv
import os
import sys
from tkinter import messagebox as mb
import numpy as np
import matplotlib.pyplot as plt
from tools.showGraph import TestWindow, getListFenetre

class GraphFile:
    def __init__(self, f, sd, ed, m):
        self.filepath = f
        self.startDate = sd
        self.endDate = ed
        self.mean = m

    def getTypeDataFile(self):
        return self.filepath.split('_')[1]

    def getFilePath(self):
        return self.filepath

    def getStartDate(self):
        return self.startDate

    def getEndDate(self):
        return self.endDate
    
    def getMean(self):
        return self.mean

class ListGrapheFile:
    def __init__(self, l):
        self.list = l
    
    def getList(self):
        return self.list

    def addInList(self, graph : GraphFile):
        self.list.append(graph)

    def show(self):
        fenetre_list = []
        type_list = []
        fileList = self.getList()
        for file in fileList:
            splitd = file.getStartDate().split('_')
            splite = file.getEndDate().split('_')
            sd = splitd[0]
            sh = splitd[1]
            ed = splite[0]
            eh = splite[1]
            fen = getListFenetre(file.getFilePath(), sd, sh, ed, eh)
            if(fen == False):
                mb.showerror("ERREUR", "Revoyez votre fenetre, il n'a a pas toutes les donnée dans cette fenetre")
                return
            fenetre_list.append(fen)
            type_list.append(file.getTypeDataFile())
        for i in range(0,len(fileList)):
            x = []
            y = []
            for row in fenetre_list[i]:
                
                if(type_list[i] == "distance"):
                    res = float(row[2]) * (1609.34)
                    y.append(res)
                    x.append(row[0] + " " + row[1])
                elif(type_list[i] == "calories"):
                    y.append(float(row[4]))
                    x.append(row[0] + " " + row[3])
                else:
                    y.append(int(row[2]))
                    x.append(row[0] + " " + row[1])
                    
            plt.figure(i)
            plt.title(fileList[i].getFilePath())
            a = []
            b = []
            for i in range(1,len(x)):
                if (i % file.getMean() == 0):
                    a.append(i)
                    b.append(x[i])
            plt.xticks(a,b, rotation="vertical")
            plt.plot(x,y)
        plt.show()

    def showIn(self):
        fenetre_list = []
        fileList = self.getList()
        type_list = []
        for file in fileList:
            splitd = file.getStartDate().split('_')
            splite = file.getEndDate().split('_')
            sd = splitd[0]
            sh = splitd[1]
            ed = splite[0]
            eh = splite[1]
            fen = getListFenetre(file.getFilePath(), sd, sh, ed, eh)
            if(fen == False):
                mb.showerror("ERREUR", "Revoyez votre fenetre, il n'a a pas toutes les donnée dans cette fenetre")
                return
            fenetre_list.append(fen)
            type_list.append(file.getTypeDataFile())
                
        if(not(TestWindow(fenetre_list))):
            mb.showerror("Erreur", "Le graphe n'a pas pus etre créer car vous n'avez pas le meme nombre de valeurs sur cette fenetre de temps")
            return
        title = ""
        for i in range(0,len(fileList)):

            x = []
            y = []
            title = title + fileList[i].getFilePath() + '\n' 
            for row in fenetre_list[i]:
                x.append(row[0] + " " + row[1])
                print(row[2].isdigit())
                if(row[2].isdigit()):
                    y.append(row[2])
                else:
                    y.append(int(row[2]))
            GraphLegend = fileList[i].getFilePath().split('_')[1]
            
            plt.plot(x,y, label= GraphLegend)
        a = []
        b = []
        for i in range(1,len(x)):
            if (i % file.getMean() == 0):
                a.append(i)
                b.append(x[i])
        plt.xticks(a,b, rotation="vertical")
        plt.legend()
        plt.title(title)
        plt.show()