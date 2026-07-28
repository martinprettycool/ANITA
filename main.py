import pandas
from datetime import date


CURRENT_DATE = date.today()

print("ANITA\n")

data = pandas.read_csv("habitos.csv")
log = pandas.read_csv("habit_log.csv")



habits_dic = {row.habit_name:{
    "type": row.type,
    "unit": row.unidad,
    "frequency": row.frecuencia,
    "objetive": row.objetivo
}  for (index, row) in data.iterrows()}



log_dict = {row.habit_name:{
    "date": row.date,
    "value": row.value
} for (index, row) in log.iterrows()}


print(log_dict)

def calculate_percentage(value_1, percentage):
    number_1 = int(value_1)
    number_2 = int(percentage)
    division = number_1 / number_2
    mult = division * 100
    return f"{mult}%"

def check_state(habit, log):
    if log[habit]["value"] == "S":
        print("✔")
        print("\n")
        print("------------------------------------")
    elif log[habit]["value"] == "N":
        print("✘")
        print("\n")
        print("------------------------------------")



def display_measurable_habit(habit, habit_data, habit_logs):
    n_1 = (habit_logs[habit]["value"])
    n_2 = (habit_data[habit]["objetive"])
    print(f"{n_1}/{n_2}")
    print(calculate_percentage(n_1, n_2))
    print("\n")
    print("------------------------------------")

def display_data(dic,log_data):
    for key in dic:
        print(key)
        print("\n")
        if check_type(key, dic):
            check_state(key, log_data)
        if not check_type(key, dic):
            display_measurable_habit(key, dic, log_data)


def check_type(habit, dic):
    return dic[habit]["type"] == "check"



def add_to_habits(new_append):
    df_row = pandas.DataFrame([new_append])
    df_row.to_csv("habitos.csv", mode="a", header=False, index=False, encoding="utf-8")
    print("Habito creado correctamente")


def add_to_habit_log(select, value):
    new_row = {
        "date": CURRENT_DATE,
        "habit_name": select,
        "value": value
    }
    df_row = pandas.DataFrame([new_row])
    df_row.to_csv("habit_log.csv", mode="a", header=False, index=False, encoding="utf-8")
    print("Tu progreso se resgitro correctamente")


def record_habits(select, dic):
    print("\n" * 10)
    print("------------------------------------")
    print(select.upper())
    print("\n")
    print(f"Tipo de habito:\n{dic[select]["type"]}\n")
    if check_type(select, dic):
        value = input("¿Completaste este habito hoy?"
                      "(S/N)\n").upper()
        add_to_habit_log(select, value)
    elif not check_type(select, dic) :
        print(f"Unidad:\n{dic[select]["unit"]}\n")
        print(f"Objetivo diario:\n{dic[select]["objetive"]}\n")
        value = input("Cuanto realizaste hoy?\n")
        add_to_habit_log(select, value)


def display_habits(dic):
    for index, key in enumerate(dic,start =1):
        print(index, key)




    print("\n")

print("Tus habitos acutales:\n")

display_habits(habits_dic)


function = input("Selecciona una opcion:\n\n1. Resgistrar progreso\n\n2. Crear un nuevo habito\n\n"
      "3. Ver estadisticas\n\n4. Salir\n\n")

#Funcion para registrar el progreso del usuario
if function == "1":

    print("Seleccion un habito:\n")
    display_habits(habits_dic)
    choice = input().title()
    if choice in habits_dic:
        record_habits(choice, habits_dic)

# Funcion encargada de agregar un habito nuevo
elif function == "2":
    new_habit_name = input("Nombre del habito:\n").title()
    print("¿Como deseas medir este habito?\n1. Medible\n2. Check")
    new_habit_type = input().title()
    print("Frecuencia\n1. Diario\n2. Semanal\n3. Mensual")
    new_habit_frequency = input("Escribe. (D/S/M)\n").upper()
    if new_habit_type == "Medible":
        new_habit_unit = input("Cual es la unidad de tu habito?\n")
        new_habit_objetive = input("Objetivo\n")
        new_row ={
            "habit_name": new_habit_name,
            "type": new_habit_type,
            "frecuencia": new_habit_frequency,
            "unidad": new_habit_unit,
            "objetivo": new_habit_objetive
        }
        add_to_habits(new_row)

    elif new_habit_type == "Check":
        new_row = {
            "habit_name": new_habit_name,
            "type": new_habit_type,
            "frecuencia": new_habit_frequency

        }
        add_to_habits(new_row)

elif function == "3":
    print("\n"*50)
    print("====================================")
    print("Resumen del dia")
    print("====================================\n")
    display_data(habits_dic, log_dict)
