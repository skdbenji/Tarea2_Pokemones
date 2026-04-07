import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#__________LIMPIEZA DE DATOS 
df = pd.read_csv("pokemon_primera_gen.csv")
df_limpia = pd.read_csv("lista_limpia_de_pokemones_de_primera_generacion.csv")
#Eliminar errores de escritura
df["Nombre"] = df["Nombre"].str.strip()
df["Tipo 1"] = df["Tipo 1"].str.strip()
df["Tipo 2"] = df["Tipo 2"].str.strip()

#Verificar que no hay datos negativos
columnas_numericas = ["PS", "Ataque", "Defensa", "Velocidad"]
for columna in columnas_numericas:
    df = df[df[columna] >= 0]

#Ve y hay algun pokemon que este repetido
duplicado = df[df.duplicated(subset="Nombre")]
print("Estos datos estan repetidos:")
print(duplicado)
df = df.drop_duplicates(subset="Nombre")
df = df.reset_index(drop=True) #Lo investigamos y sirve para reseatear el indice

#Verificar que haya solo pokemones de la primera generacion
df = df[df["Nombre"].isin(df_limpia["Nombre"])]
df = df.reset_index(drop=True)

#Verificar los tipos 
validar_tipos = [
    "Normal", "Fuego", "Agua", "Planta", "Eléctrico", "Hielo", "Lucha",
    "Veneno", "Tierra", "Volador", "Psiquico", "Bicho", "Roca", "Fantasma", "Dragón"
]
df = df[df["Tipo 1"].isin(validar_tipos)]
df = df[df["Tipo 2"].isna() | df["Tipo 2"].isin(validar_tipos)]
df = df.reset_index(drop=True)


print(df)


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
    
    idx_max = df.groupby("Tipo 1")["PS"].idxmax()#Se obtienen los índices mayores de PS para cada tipo principal
    idx_min = df.groupby("Tipo 1")["PS"].idxmin()#Se obtienen los índices minimos de PS para cada tipo principal
#Se crean dos tablas con los datos pedidos, renombrando columnas para que sean mas claras
    maximos = df.loc[idx_max, ["Tipo 1", "Nombre", "PS"]].rename(columns={"Nombre": "Pokémon_Max", "PS": "PS_Max"})
    minimos = df.loc[idx_min, ["Tipo 1", "Nombre", "PS"]].rename(columns={"Nombre": "Pokémon_Min", "PS": "PS_Min"})
    
    resultado = pd.merge(maximos, minimos, on="Tipo 1")#Unión de tablas

    return resultado

#7. Análisis exploratorio 
def comparacion_stat_por_tipo(df):
    promedios = df.groupby("Tipo 1")[["Ataque", "Defensa"]].mean().sort_values(by="Ataque", ascending=False)
    return promedios

def calcular_correlacion(df):
    r = df["Ataque"].corr(df["Velocidad"])
    return r

def dispersion(df):
    desviacion = df.groupby("Tipo 1")["PS"].std().sort_values(ascending=False)
    return desviacion

def identificar_outliers(df):
    plt.figure(figsize=(10, 5))

    # Boxplot para Ataque
    plt.subplot(1, 2, 1)
    sns.boxplot(y=df["Ataque"], color="skyblue")
    plt.title("Outliers en Ataque")

    # Boxplot para PS
    plt.subplot(1, 2, 2)
    sns.boxplot(y=df["PS"], color="salmon")
    plt.title("Outliers en PS")

    plt.tight_layout()
    plt.show()

#8. Ejercicios de interpretación de resultados

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
#print(MayoryMenor_PS(df))
