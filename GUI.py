import re
from Bio import SeqIO
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import sqlite3
from sqlite3 import Error
from tkinter import messagebox
root = Tk()
root.title('PSIM Scan')
root.geometry("662x800") 

#podanie sekwencji w formacie FASTA

fi_label = Label(root, text = 'Enter your FASTA sequence').grid(row = 0, columnspan = 4)
fasta_input = Text(root,height = 10, width = 82, borderwidth = 2).grid(row = 1, columnspan = 4)

#wyszukiwanie FASTA z komputera
def open():
    root.fastabrowse = filedialog.askopenfilename(initialdir = '/', title = 'Choose FASTA file', filetypes = (('fasta files','*.fasta'), ('fna files','*.fna'), ('fa files','*.fa'), ('fsa files','*.fsa') ))
    

empty_label1 = Label(root, text = '').grid(row = 2, columnspan = 4)
fb_label = Label(root, text = 'or browse your FASTA sequence').grid(row = 3, column = 0, columnspan = 4)
fb_button = Button(root, text = 'Browse', command = open).grid(row = 4, column = 0, columnspan = 4)


#Wybór query subrange
empty_label2 = Label(root, text = '').grid(row = 5, columnspan = 4)
options_label = Label(root, text = 'Query options').grid(row = 6, columnspan = 4)

query_label = Label(root, text = 'Enter query subrange (from - to)').grid(row = 7, columnspan = 2)
query_subrange = Entry(root, width = 5, borderwidth = 2).grid(row = 8, column = 0)
query_subrange = Entry(root, width = 5, borderwidth = 2).grid(row = 8, column = 1)





#Wybieranie bazy danych


def function(x):
    
    if x == 'Baza1':
        
        
        parse = SeqIO.read('Glycerophosphocholine (GroPCho) phosphodiesterase.fasta', 'fasta')
        info = messagebox.showinfo('Database Info', parse.description)
        
        
    if x == 'Baza2':
        
        parse = SeqIO.read('fusion protein.fasta', 'fasta')
        info = messagebox.showinfo('Database Info', parse.description)
        
        
        
    if x == 'Baza3':
        
        parse = SeqIO.read('ATP-binding cassette (ABC) transporter.fasta', 'fasta')
        info = messagebox.showinfo('Database Info', parse.description)

lbl = StringVar()
lbl.set('default')

lista_baza = ['Baza1','Baza2','Baza3','Baza4']

clicked1 = StringVar()
clicked1.set(lista_baza[0])


bases_label = Label(root, text = 'Choose database').grid(row = 7, column = 3)
bases_drop = OptionMenu(root, clicked1, *lista_baza).grid(row = 8, column = 3)
bases_but = Button(root, text = 'Show info about chosen database', command = lambda: function(clicked1.get()))
bases_but.grid(row = 9, column = 3)






#Wprowadzenie tytułu wyszukiwania
title_label = Label(root, text = 'Enter your search title (optional)').grid(row = 9, column = 0, columnspan = 2)
title_input = Entry(root, width = 20, borderwidth = 2).grid(row = 10, column = 0, columnspan = 2)

#Wybór rozmiaru krotki
lista_krotka = [
    3,
    6
]
clicked2 = IntVar()
clicked2.set(lista_krotka[0])
tuple_label = Label(root, text = 'Choose k-tuple size').grid(row = 10, column = 3)
tuple_drop = OptionMenu(root, clicked2, *lista_krotka ).grid(row = 11, column = 3)

#maksymalna liczba podobnych sekwencji do znalezienia

    

lista_targetseq = [
    10,
    50,
    100,
    250
]
clicked3 = IntVar()
clicked3.set(lista_targetseq[0])
target_label = Label(root, text = 'Max target sequences').grid(row = 12, column = 3)

target_drop = OptionMenu(root, clicked3, *lista_targetseq).grid(row = 13, column = 3)

#threshold
threshhold_label = Label(root, text = 'Threshold').grid(row = 11, column = 0, columnspan = 2)
threshhold_entry =  Entry(root, width = 20, borderwidth = 2)
threshhold_entry.insert(0, 0.05)
threshhold_entry.grid(row = 12, column = 0, columnspan = 2)
#wybór macierzy scoringu

lista_matrix = [
    'matrixx',
    'matrixy',
    'matrixz'
]
clicked4 = StringVar()
clicked4.set(lista_matrix[0])

matrix_label = Label(root, text = 'Choose scoring matrix').grid(row = 14, column = 3, columnspan = 2)
matrix_drop = OptionMenu(root, clicked4, *lista_matrix ).grid(row = 15, column = 3)
#Przycisk Search

search_button = Button(root, text = 'Search!', width = 40)
search_button.grid(row = 16, columnspan = 4)

#Miejsce na wykresy?



root.mainloop()
