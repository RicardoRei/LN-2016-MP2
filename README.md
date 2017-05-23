# LN-2016-MP2
Segundo Mini Projecto para Lingua Natural (enunciado disponivel no ficheiro MP2.pdf) , Professora Luisa Coheur.

## Descrição

O projecto consistia na identificação correcta dos autores de determinados textos.

## Software necessário

Apenas é necessário o python 3 instalado.

## Algoritmo

A resolução do projecto foi resolvido com o auxilio de Bigramas. Numa fase de treino são criados todos os possiveis bigramas para cada autor tendo em conta os textos disponiveis na Corpora para esse mesmo autor.
Depois tendo todos os Bigramas de cada autor vamos contar as suas frequencia. Ex: Se nos textos do autor estiver escrito apenas 2 vezes "o rapaz" então é criado o bigrama [o, rapaz] e é atribuida a frequencia 2.

Depois numa fase de teste fazemos o mesmo com cada texto de teste, ou seja, criamos os bigramas para aquele texto e contamos as frequencias, e comparamos com todos os autores utilizando uma formula que faz o sumatorio da frequencia de cada bigrama no texto de teste na Corpora do autor e no final divide pelo nº de bigramas existentes para aquele autor. (isto permite normalizar as diferenças que existem entre o tamanho dos textos de treino de cada autor)

Nota: antes de criar os bigramas são realizadas algumas normalizações aos textos.

## Run

Correr o script run.sh
