import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator


def separate():#Separador
    print("#" * 20)
    print("")

def clean_data(df):#Limpieza de datos
    df = df.copy()
    df["calificacion"] = df.groupby(["matricula", "nombre"])["calificacion"].transform(lambda x: x.fillna(x.mean()))
    return df

def row(df):#¿Cuántos registros tiene el dataset?
    print(f"El número de registros en el dataset son: {len(df)}")
    separate()

def blank(df):#¿Hay calificaciones faltantes? ¿En dónde?
    if df["calificacion"].isna().sum() != 0:
        empty_sum = df["calificacion"].isna().sum()
        empty_fields = df[df.isna().any(axis=1)]
        print(f"La cantidad de calificaciones faltantes es: {empty_sum}")
        print("Los registros faltantes son los siguientes:")
        print(empty_fields)
        separate()
    else:
        print("No hay calificaciones faltantes")
        separate()

def individual_mean(df):#¿Cuál es el promedio por alumno?
    ind_mean = df.groupby(["matricula", "nombre"])["calificacion"].mean().reset_index().rename(
        columns={"calificacion": "promedio"})
    return(ind_mean)

def individual_mean_plot(df):
    plt.figure(figsize=(10,10))
    plt.bar(df["nombre"], df["promedio"], color="blueviolet")
    plt.title("Promedio por alumno")
    plt.xlabel("Nombre")
    plt.ylabel("Promedio")
    plt.xticks(rotation=45, ha="right")
    plt.show()

def assignment_mean(df):#¿Cuál es el promedio por materia?
    assign_mean = df.groupby(["materia"])["calificacion"].mean().reset_index().rename(columns={"calificacion": "promedio_materia"})
    return (assign_mean)

def assignment_mean_plot(df):
    plt.figure(figsize=(6, 4))
    plt.bar(df["materia"], df["promedio_materia"], color="mediumvioletred")
    plt.title("Promedio por materia")
    plt.xlabel("Materia", fontsize=10, fontweight="bold")
    plt.ylabel("Promedio", fontsize=10, fontweight="bold")
    plt.show()

def failed_student(df):#¿Qué alumnos están reprobados (promedio < 70)?
    new_dataset = df.groupby(["matricula", "nombre"])["calificacion"].mean().reset_index().rename(columns={"calificacion" : "promedio"})
    fail_students = new_dataset[new_dataset["promedio"] < 70]
    print("Los alumnos reprobados (menores a 7) son:")
    print(fail_students)

def group_mean(df):#¿Cuál grupo tiene mejor promedio general?
    new_dataset = df.groupby("grupo")["calificacion"].mean().reset_index()
    return(new_dataset)

def group_mean_plot(df):
    plt.figure(figsize=(5, 4))
    plt.bar(df["grupo"], df["calificacion"], color="orange")
    plt.title("Mejor promedio general")
    plt.xlabel("Grupo", fontweight="bold")
    plt.ylabel("Promedio", fontweight="bold")
    plt.show()

def sum_group(df):#¿Cuántos alumnos hay por grupo?
    students_group = df.groupby("grupo")["matricula"].nunique().reset_index(name="total_alumnos")
    return(students_group)

def sum_group_plot(df):
    plt.figure(figsize=(5, 4))
    plt.bar(df["grupo"], df["total_alumnos"], color="darkslategray")
    plt.title("Número de alumnos por grupo")
    plt.xlabel("Grupo", fontweight="bold")
    plt.ylabel("Cantidad de alumnos", fontweight="bold")
    ax = plt.gca()#Obtener los ejes actuales
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))#Forzar el uso de números enteros en los ejes Y
    plt.show()

def main():
    dataset = pd.read_csv("calificaciones.csv")

    blank(dataset)

    dataset_clean = clean_data(dataset)

    row(dataset_clean)

    #Gráficar el promedio por alumno
    ind_mean = individual_mean(dataset_clean)
    individual_mean_plot(ind_mean)

    #Gráfica el promedio por materia
    assig_mean = assignment_mean(dataset_clean)
    assignment_mean_plot(assig_mean)

    #Alumnos reprobados
    failed_student(dataset_clean)

    #Grupo con mejor promedio general
    gmean = group_mean(dataset_clean)
    group_mean_plot(gmean)

    #Alumnos por grupo
    sgroup = sum_group(dataset_clean)
    sum_group_plot(sgroup)

main()

