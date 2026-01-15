import pandas as pd

dataset = pd.read_csv("calificaciones.csv")

def row():
    print(f"El número de registros en el dataset es: {len(dataset)}")

def blank():
    if dataset["calificacion"].isna().sum() != 0:
        print(f"La cantidad de calificaciones faltantes es: {dataset["calificacion"].isna().sum()}")
        print("Los registros faltantes son los siguientes:")
        print(dataset[dataset.isna().any(axis=1)])

def individual_mean():
    print(dataset.groupby(["matricula", "nombre"])["calificacion"].mean().reset_index().rename(
        columns={"calificacion": "promedio"}))

def assignament_mean():
    print(dataset.groupby(["materia"])["calificacion"].mean().reset_index().rename(columns={"calificacion": "promedio materia"}))

def failed_student():
    new_dataset = dataset.groupby(["matricula", "nombre"])["calificacion"].mean().reset_index().rename(columns={"calificacion" : "promedio"})
    print(new_dataset[new_dataset["promedio"] < 70])

def group_mean():
    new_dataset = dataset.groupby("grupo")["calificacion"].mean().reset_index()
    print("El grupo con mejor promedio general es: ")
    print(new_dataset.iloc[new_dataset["calificacion"].idxmax()])

def sum_group():
    print(dataset.groupby("grupo")["matricula"].nunique().reset_index())

sum_group()

"""
Preguntas que debes responder:
¿Cuántos registros tiene el dataset? 
R= 15

¿Hay calificaciones faltantes? ¿En dónde?
R=Sí, una. En el registro 10.

¿Cuál es el promedio por alumno?
R=

¿Cuál es el promedio por materia?
R=

¿Qué alumnos están reprobados (promedio < 70)?
R=

¿Cuál grupo tiene mejor promedio general?
R=

¿Cuántos alumnos hay por grupo?
R=

"""