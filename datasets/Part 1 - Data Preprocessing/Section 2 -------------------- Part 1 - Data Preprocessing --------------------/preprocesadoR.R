#importar dataset
dataset = read.csv('Data.csv')




#divir los datos en conjunto de entrenamiento y conjunto de testing 
#se instala el paquete caTools para dividir 
#install.packages("caTools")
library(caTools)
set.seed(123) #esto remplaza el randomstate de python
split = sample.split(dataset$Purchased, SplitRatio = 0.8)

training_set = subset(dataset,split== TRUE)
testing_set = subset(dataset, split == FALSE)

# #Escalado de valores en la variables
# 
# training_set[, 2:3] = scale(training_set[, 2:3])
# testing_set[, 2:3] = scale(testing_set[, 2:3])














