# Processo Seletivo Navi Capital - Teste de Python

# André Osorio Magaldi Netto  19/12/2020


from math import log2 as ln


#---------------- Questão 1 --------------------
def questao1():
    n = 0;
    for k in range(1, 5000001):
        if k%2 == 0 and k%49 == 0 and k%37 == 0 : n+=1; #Condicoes a serem satisfeitas
    return n;




#---------------- Questão 2 --------------------
def fact(n): #Fatorial de n
    if n==0:    return 1;
    else:     return n*fact(n-1);

class vetorX(list):
    def __init__(self):
        
        for i in range(0, 10):
            if i%2 == 0:  self.append( 3**i + 7*fact(i) ); #Se for par
            else:  self.append( 2**i + 4*ln(i) ); #Se for impar

        self.posMaior = self.index(max(self)); #Posicao do maior elemento

        self.media = 0;
        for n in self: self.media += n/10; #Media dos elementos contidos no vetor
        self.media = round(self.media,2);
        
        


#---------------- Questão 3 --------------------
class leitorDeNotas():
    def __init__(self, aluno1, nota1, aluno2, nota2, aluno3, nota3, aluno4, nota4, aluno5, nota5):

        self.dict = {aluno1:nota1, aluno2:nota2, aluno3:nota3, aluno4:nota4, aluno5:nota5}; #Dicionario

        aluno = max(self.dict, key=self.dict.get);
        self.melhorAluno = ( aluno, self.dict[aluno] ); #Aluno com maior nota e sua respectiva nota


    
