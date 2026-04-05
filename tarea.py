import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("pokemon_primera_gen.csv")

#Retorna los datos de los pokemones que sean tipo fuego
def fuego_columnas(df):
    return df[df["Tipo 1"] == "Fuego"][["Nombre", "Tipo 1", "Ataque", "Velocidad"]]

#La media de los ataque
def media(df):
    return df["Ataque"].mean()

#La mediana de los ataque
def mediana(df):
    return df["Ataque"].median()

#La mota de ataque
def moda(df):
    return df["Ataque"].mode()

#Retorna el pokemon con la mayor defensa
def mayor_defensa(df):
    indice =  df["Defensa"].idxmax()
    return df.loc[indice, "Nombre"]

#Retorna el pokemon con la menor velocidad
def menor_velocidad(df):

    indice = df["Velocidad"].idxmin()
    return df.loc[indice, "Nombre"]

#Retorna la cantidad de pokemones que tienen dos tipos 
def dos_tipos(df):

    return len(df[df["Tipo 2"].notna()])

#Retorna el rango de los ps
def calcular_rango(df):

    return df["PS"].max() - df["PS"].min()

#Retorna la desviacion de los PS
def desviacion_estandar(df):
    return df["PS"].std()

#Histograma de ataque
def histograma_ataque(df):
    df["Ataque"].hist()
    plt.title("Histograma de los valores de Ataque")
    plt.xlabel("Ataque")
    plt.ylabel("Frecuencia")
    plt.show() #Esta la despliega

#Grafico de dispersion entre ataque y velocidad
def grafico_dispersion_AtaqueYvelocidad(df):
    plt.scatter(df["Ataque"], df["Velocidad"])
    plt.title("Grafico de dispersion entre ataque y velocidad")
    plt.xlabel("Ataque")
    plt.ylabel("Velocidad")
    plt.show()

#Diegrama de caja de los PS
def boxplot_PS(df):
    
    df.boxplot(column ="PS" , by="Tipo 1")
    plt.title("..")
    plt.suptitle("")
    plt.xlabel("Tipo 1")
    plt.ylabel("PS")
    plt.xticks(rotation =45) #Rotar los nombre para que no se estorben
    plt.show()

#Diagrama violin de la defensa
def diagrama_violin_defensa(df):
    plt.figure(figsize=(8,6))
    sns.violinplot(y=df["Defensa"])

    plt.title("Distribucion de la defensa")
    plt.xlabel("Defensa")
    plt.show()

#Crear la columna de poder total
def crear_PoderTotal(df):

    df["Poder total"] = df["Ataque"] + df["Defensa"] + df["Velocidad"] + df["PS"]
    df.to_csv("pokemon_primera_gen_actualizado.csv", index=False)
    return df

#Ordenar la columna por poder de mayor a menor
def Ordenar(df):
    df = df.sort_values(by = "Poder total", ascending = False)

    return df
def calcular_tipo(df):

    resultado = df.groupby("Tipo 1")["Ataque"].agg(["mean" , "median" , "std"]) #agg para sacar varias operaciones a la vez

    return resultado

def mayorPromedio_velocidad(df):
    resultado = df.groupby("Tipo 1")["Velocidad"].mean().idxmax()


    return resultado
#Esta no se como hacerla XD
def MayoryMenor_PS(df):
    
#Filtrado y seleccion 
print("-----------Datos de pokemones con tipo fuego------")
print(fuego_columnas(df))
#Estadistica descriptiva. Promedio, mediana y moda deñ ataque de todos los pokemones
print("La media de todos los pokemones es: ",media(df))
print("La mediana de todos los pokemones es: ",mediana(df))
print("La moda de todos los pokemones es: ", moda(df))
print("El pokemon de mayor defensa es: " , mayor_defensa(df))
print("El pokemon de menor velocidad es: ", menor_velocidad(df))
print("Hay", dos_tipos(df) , "que tienen dos tipos")
print("El rango de los PS es:" , calcular_rango(df))
print("Desviacion estandar", desviacion_estandar(df))
print("Desplegando histograma...",histograma_ataque(df))
print("Desplegando grafico de dispersion...", grafico_dispersion_AtaqueYvelocidad(df))
print(boxplot_PS(df))
print(diagrama_violin_defensa(df))
print(crear_PoderTotal(df))
print(Ordenar(df))
print(calcular_tipo(df))
print("El tipo con mayor promedio en velocidad es: " ,mayorPromedio_velocidad(df))
print(MayoryMenor_PS(df))
