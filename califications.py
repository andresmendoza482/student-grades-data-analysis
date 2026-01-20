import pandas as pd

def separate():#Separador
    print("#" * 20)
    print("")

def clean_data(df):#Limpieza de datos
    df = df.copy()
    df["calificacion"] = df.groupby(["matricula", "nombre"])["calificacion"].transform(lambda x: x.fillna(x.mean()))
    separate()
    return df

def row(df):#¿Cuántos registros tiene el dataset?
    print(f"El número de registros en el dataset es: {len(df)}")
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
    print(ind_mean)
    separate()

def assignment_mean(df):#¿Cuál es el promedio por materia?
    assign_mean = df.groupby(["materia"])["calificacion"].mean().reset_index().rename(columns={"calificacion": "promedio_materia"})
    print(assign_mean)
    separate()

def failed_student(df):#¿Qué alumnos están reprobados (promedio < 70)?
    new_dataset = df.groupby(["matricula", "nombre"])["calificacion"].mean().reset_index().rename(columns={"calificacion" : "promedio"})
    fail_students = new_dataset[new_dataset["promedio"] < 70]
    print(fail_students)
    separate()

def group_mean(df):#¿Cuál grupo tiene mejor promedio general?
    new_dataset = df.groupby("grupo")["calificacion"].mean().reset_index()
    better_mean = new_dataset.iloc[new_dataset["calificacion"].idxmax()]
    print("El grupo con mejor promedio general es: ")
    print(better_mean)
    separate()

def sum_group(df):#¿Cuántos alumnos hay por grupo?
    students_group = df.groupby("grupo")["matricula"].nunique().reset_index(name="total_alumnos")
    print(students_group)
    separate()

def main():
    dataset = pd.read_csv("calificaciones.csv")

    blank(dataset)

    dataset_clean = clean_data(dataset)

    row(dataset_clean)
    individual_mean(dataset_clean)
    assignment_mean(dataset_clean)
    failed_student(dataset_clean)
    group_mean(dataset_clean)
    sum_group(dataset_clean)

main()

