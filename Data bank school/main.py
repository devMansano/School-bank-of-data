import tkinter as tk
import sqlite3
import DataControls as dc

def InserirCursos(dados):
  for row in dados:
    lstAlunosCurso.clearData()
    lstAlunoTurma.clearData()
    lstCursos.insertData(row[0],row[1])

def CursosSelecao(event):

  try:
    indice=lstCursos.curselection()[0]
    id=lstCursos.listData[indice]
    cursor.execute('SELECT Alunos.ra, Alunos.nome, Alunos.sobrenome FROM Alunos INNER JOIN AlunosCurso ON Alunos.ra=AlunosCurso.ra WHERE AlunosCurso.idcurso=?;',(id,))
    rows=cursor.fetchall()
    lstAlunosCurso.clearData()
    lstAlunoTurma.clearData()
    for row in rows:
      lstAlunosCurso.insertData(row[0],row[1]+" "+row[2])
  except:
    print()

def AlunosSelecao(event):
  try:
    indice=lstAlunosCurso.curselection()[0]
    id=lstAlunosCurso.listData[indice]
    cursor.execute('Select Turmas.idTurma, AtividadesPedagogicas.nome from Turmas,AtividadesPedagogicas WHERE Turmas.aluno=? AND AtividadesPedagogicas.idAtividade=Turmas.atividadepedagogica;' ,(id,))
    

   
    rows=cursor.fetchall()
    print(rows)
    lstAlunoTurma.clearData()
    
    for row in rows:
      
      lstAlunoTurma.insertData(row[0], row[0] + ' ' + row[1])

    cursor.execute('SELECT Reprovados.ra, Reprovados.idAtividade, Reprovados.ano FROM Reprovados INNER JOIN Alunos ON Alunos.ra=Reprovados.ra WHERE Reprovados.ra=?;',(id,))
  
    cursor.execute('Select Reprovados.idAtividade,AtividadesPedagogicas.nome from Reprovados,AtividadesPedagogicas WHERE Reprovados.ra=? AND AtividadesPedagogicas.idAtividade=Reprovados.idAtividade;' ,(id,))
  
    rows=cursor.fetchall()
    print(rows)
    lstReprov.clearData()
   
    for row in rows:
      
      lstReprov.insertData(row[0],row[1])

    
    cursor.execute('Select Aprovados.nome,AtividadesPedagogicas.nome from Aprovados,AtividadesPedagogicas WHERE Aprovados.ra=? AND AtividadesPedagogicas.idAtividade=Aprovados.idAtividade;' ,(id,))

    rows=cursor.fetchall()
    print(rows)
    lstAprovad.clearData()
    
    for row in rows:
      
      lstAprovad.insertData(row[0],row[1])
      
   # cursor.execute('SELECT ACursar.ra, ACursar.idAtividade, ACursar.curso FROM ACursar INNER JOIN Alunos ON ACursar.ra=Alunos.ra WHERE ACursar.ra=?;',(id,))

    cursor.execute('Select ACursar.nome,AtividadesPedagogicas.nome from ACursar,AtividadesPedagogicas WHERE ACursar.ra=? AND AtividadesPedagogicas.idAtividade=ACursar.idAtividade;' ,(id,))


    rows=cursor.fetchall()
    print(rows)
    lstAcursar.clearData()
    for row in rows:
      
      lstAcursar.insertData(row[0], row[1])
      
  except:
    
    print()





conn=sqlite3.connect('UniversidadeP1.db')
cursor=conn.cursor()
cursor.execute("PRAGMA foreign_keys=ON")

window = tk.Tk()
window.title("Sistema Universitário")
window.geometry("700x400")

frmTopo=tk.Frame(window);
frmTopo.pack(side=tk.TOP,anchor=tk.W)
frmBaixo=tk.Frame(window);
frmBaixo.pack(side=tk.TOP,anchor=tk.N)

frmCursos=tk.Frame(frmTopo)
frmCursos.pack(side=tk.LEFT,anchor=tk.N)
lblCursos=tk.Label(frmCursos,width=10,text="Cursos")
lblCursos.pack(side=tk.TOP)

lstCursos = dc.RListBox(frmCursos,width=20,height=5)
lstCursos.bind('<<ListboxSelect>>', CursosSelecao)
lstCursos.configure(exportselection=False)
lstCursos.pack(side=tk.LEFT)

frmAlunos=tk.Frame(frmTopo)
frmAlunos.pack(side=tk.RIGHT,anchor=tk.N)
lblAlunos=tk.Label(frmAlunos,width=10,text="Alunos")
lblAlunos.pack(side=tk.TOP)

lstAlunosCurso=dc.RListBox(frmAlunos,width=20,height=5)
lstAlunosCurso.bind('<<ListboxSelect>>', AlunosSelecao)
lstAlunosCurso.configure(exportselection=False)
lstAlunosCurso.pack(side=tk.RIGHT)

frmSituacoes=tk.Frame(frmBaixo)
frmSituacoes.pack(side=tk.LEFT,anchor=tk.W)
lblSituacoes=tk.Label(frmSituacoes,width=10,text="Cursando")
lblSituacoes.pack(side=tk.TOP)

frmReprov=tk.Frame(frmBaixo)
frmReprov.pack(side=tk.LEFT,anchor=tk.W)
lblReprov=tk.Label(frmReprov,width=10,text="Reprovado ")
lblReprov.pack(side=tk.TOP)

lstReprov=dc.RListBox(frmReprov,width=17,height=10)
lstReprov.bind('<<ListboxSelect>>', AlunosSelecao)
lstReprov.configure(exportselection=False)
lstReprov.pack(side=tk.LEFT)

frmAprovad=tk.Frame(frmBaixo)
frmAprovad.pack(side=tk.LEFT,anchor=tk.W)
lblAprovad=tk.Label(frmAprovad,width=10,text="Aprovado")
lblAprovad.pack(side=tk.TOP)

lstAprovad=dc.RListBox(frmAprovad,width=17,height=10)
lstAprovad.bind('<<ListboxSelect>>', AlunosSelecao)
lstAprovad.configure(exportselection=False)
lstAprovad.pack(side=tk.RIGHT)

frmAcursar=tk.Frame(frmBaixo)
frmAcursar.pack(side=tk.LEFT,anchor=tk.W)
lblAcursar=tk.Label(frmAcursar,width=10,text="Cursar")
lblAcursar.pack(side=tk.TOP)

lstAcursar=dc.RListBox(frmAcursar,width=17,height=10)
lstAcursar.bind('<<ListboxSelect>>', AlunosSelecao)
lstAcursar.configure(exportselection=False)
lstAcursar.pack(side=tk.RIGHT)

lstAlunoTurma=dc.RListBox(frmSituacoes,width=17,height=10)
lstAlunoTurma.bind('<<ListboxSelect>>', AlunosSelecao)
lstAlunoTurma.configure(exportselection=False)
lstAlunoTurma.pack(side=tk.LEFT)

cursor.execute('Select idcurso,nome from Cursos;')
rows=cursor.fetchall()
InserirCursos(rows)
tk.mainloop()

frmCursos=tk.Frame(frmBaixo)
frmCursos.pack(side=tk.LEFT,anchor=tk.W)
lblSituacoes=tk.Label(frmSituacoes,width=10,text="Reprovados")
lblSituacoes.pack(side=tk.TOP)

