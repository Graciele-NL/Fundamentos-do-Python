# Exercícios para praticar Python
Estes exercícios têm como objetivo a prática dos fundamentos de Python.
Os exercícios de 1 a 11 foram extraídos do livro Introdução à Computação Usando Python, de Ljubomir Perković.

### Exercício1
Implemente um programa que solicita uma lista de nomes de aluno do usuário e exiba aqueles nomes que começam com as letras de A até M.
>>>
EX:
Digite a lista: ['Ellie', 'Steve', 'Sam', 'Owen', 'Mavin']
Ellie
Gavinsoma

### Exercício2
Implemente um programa que solicita ao usuário que entre com as coordenadas x e y (cada um entre –10 e 10) de um dardo e calcula se 
o dardo atingiu o alvo, um círculo com centro (0,0) e raio 8. Se tiver atingido, a string Está dentro! deverá ser exibida na tela.
>>>
Digite x: 2.5
Digite y: 4
Está dentro!

### Exercício3
Implemente um programa que solicita um inteiro positivo n e exibe na tela todos os divisores positivos de n. Nota: 0 
não é um divisor de qualquer inteiro, e n divide por si mesmo.
>>>
Digite n: 49
1
7
49

### Exercício4
Escreva a função mult3(), que aceite como entrada uma lista de inteiros e exiba somente os múltiplos de 3, um por linha.

>>> mult3([3, 1, 6, 2, 3, 9, 7, 9, 5, 4, 5])
3
6
3
9
9

### Exercício5
Implemente a função quatro_letras(), que aceite como entrada uma lista de palavras (ou seja, strings) e retorne a sublista de 
todas as palavras de quatro letras na lista.
>>> quatro_letras(['cão', 'letra', 'pare', 'tela', 'bom', 'dica'])
['pare', 'tela', 'dica']

### Exercício6
O intervalo de uma lista de números é a maior diferença entre dois números quaisquer na lista.
Escreva uma expressão em Python que calcule o intervalo de uma lista de números lst. Se a lista lst for, digamos,
[3, 7, -2, 12], a expressão deverá ser avaliada como 14 (a diferença entre 12 e –2).

### Exercício7
implemente um programa que solicita um inteiro n do usuário e imprime na tela os quadrados de todos os números de 0 até,
mas não incluindo, n.
>>>
Digite n: 4
0
1
4
9

### Exercício8
Escreva uma função mês() que aceite um número entre 1 e 12 como entrada e retorne a abreviação em três letras do mês correspondente.
 Faça isso sem usar uma instrução if, apenas operações de strings. Dica: use uma string para armazenar as abreviações em ordem.
>>> mês(1)
'Jan'
>>> mês(11)
'Nov'

### Exercício9
Implemente a função parSoma(), que aceite como entrada uma lista de inteiros distintos lst e um inteiro n, 
e exiba os índices de todos os pares de valores em lst que somam n.
>>> parSoma([7, 8, 5, 3, 4, 6], 11)
0 4
1 3
2 5

### Exercício10
A imagem espelho da string vow é a string wov, e a imagem espelho de wood é a string boow. A imagem espelho da string bed, porém,
não pode ser representada como uma string, pois a imagem espelho de e não é um caractere válido.
Desenvolva a função espelho(), que apanhe uma string e retorne sua imagem espelho, mas somente se esta puder ser representada usando as
letras no alfabeto.
>>> espelho('vow')
'wov'
>>> espelho('wood')
'boow'
>>> espelho('bed')
'INVALID'

### Exercício11
Desenvolva um jogo simples que ensine a alunos de jardim da infância a somar números de um dígito. Sua função jogo() apanhará um inteiro 
n como entrada e depois fará n perguntas de adição com números de único dígito. Os números a serem somados deverão ser escolhidos
aleatoriamente a partir do intervalo [0, 9] (isto é, 0 a 9, inclusive). O usuário informará a resposta quando solicitado.
Sua função deverá exibir 'Correto' ou 'Incorreto', dependendo se a resposta é correta ou não. Depois de n perguntas,
sua função deverá exibir o número de respostas corretas.
>>> jogo(3)
8 + 2 =
Digite a resposta: 10
Correto.
6 + 7 =
Digite a resposta: 12
Incorreto.
7 + 7 =
Digite a resposta: 14
Correto.
Você teve 2 respostas corretas entre 3

### Exercício12
Encontrar o maior número entre dois valores sem utilizar o módulo Math e realizar
o tratamento de exceções.

### Exercício13
Fazer um programa que solicite um número e retorne o fatorial desse número, sem utilizar o módulo math.
 
## Autora
G Nunes
Projeto desenvolvido para fins de estudo e prática em Python.


```bash
python Desafios-Pratica/Exercícios