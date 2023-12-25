import Livro
from interface import AlunoGraduacao, Professor, AlunoPos
import Exemplar


#  Exemplares
um = Exemplar.Exemplar(100, '01')
dois = Exemplar.Exemplar(100, '02')
tres = Exemplar.Exemplar(101, '03')
quatro = Exemplar.Exemplar(200, '04')
cinco = Exemplar.Exemplar(201, '05')
seis = Exemplar.Exemplar(300, '06')
sete = Exemplar.Exemplar(300, '07')
oito = Exemplar.Exemplar(400, '08')

exemplares = [um, dois, tres, quatro, cinco, seis, sete, oito]


#  Livros
Engenharia_de_Software = Livro.Livro(100, 'Engenharia de Software', 'Addison-Wesley', 'Ian Sommervile', '6ª', 2000, [um, dois])
UML_Guia_do_Usuario = Livro.Livro(101, 'UML – Guia do Usuário', 'Campus', 'Grady Booch, James Rumbaugh, Ivar Jacobson', '7ª', 2000, [tres])
Code_Complete = Livro.Livro(200, 'Code Complete', 'Microsoft Press', 'Steve McConnell', '2ª', 2014, [quatro])
Agile_Software_Development = Livro.Livro(201, 'Agile Software Development, Principles, Patterns, and Practices', 'Prentice Hall', 'Robert Martin', '1ª', 2002, [cinco])
Refactoring = Livro.Livro(300, 'Refactoring: Improving the Design of Existing Code', 'Addison-Wesley Professional', 'Martin Fowler', '1ª', 1999, [seis, sete])
Software_Metrics = Livro.Livro(301, 'Software Metrics: A Rigorous and Practical Approach', 'CRC Press', 'Norman Fenton, James Bieman', '3ª', 2014, None)
Design_Patterns = Livro.Livro(400, 'Design Patterns: Elements of Reusable Object-Oriented Software', 'Addison-Wesley Professional', 'Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides', '1ª', 1994, [oito])
UML_Distilled = Livro.Livro(401, 'UML Distilled: A Brief Guide to the Standard Object Modeling Language', 'Addison-Wesley Professional', 'Martin Fowler', '3ª', 2003, None)

livros = [Engenharia_de_Software, UML_Guia_do_Usuario, Code_Complete, Agile_Software_Development, Refactoring, Software_Metrics, Design_Patterns, UML_Distilled]


Joao = AlunoGraduacao.AlunoGraduacao(123, 'João da Silva')
Luiz = AlunoPos.AlunoPos(456, 'Luiz Fernando Rodrigues')
Pedro = AlunoGraduacao.AlunoGraduacao(789, 'Pedro Paulo')
Carlos = Professor.Professor(100, 'Carlos Lucena')

usuarios = [Joao, Luiz, Pedro, Carlos]



