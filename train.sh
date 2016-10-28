

authors=(
	Corpora/treino/AlmadaNegreiros
	Corpora/treino/CamiloCasteloBranco
	Corpora/treino/EcaDeQueiros
	Corpora/treino/JoseRodriguesSantos
	Corpora/treino/JoseSaramago
	Corpora/treino/LuisaMarquesSilva
	#Corpora/test2.txt para adicionar mais filenames
	#devem estar separados por espacos
	)

for i in ${authors[*]}; 
do
	python proj.py $i bigrams
done