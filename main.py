"""
FelipedelosH

Thsi program read a .txt .csv or whatever file with information
And say:



"""

def rtnArcheveInfo(path):
    info = None
    try:
        f = open(path, 'r', encoding="utf-8")
        return f.read()
    except:
        return info

arch = "destinos_turismoi.csv"


#Vars
delimiter = "|"
totals_rows_counter = [] # Say a quantity of rows
control_totals_rows_counter = [] # Save a diferent tipes of rows

counter = 0


# Charge a general Staticstis
for i in rtnArcheveInfo(arch).split("\n"):
    total_reg = len(str(i).split(delimiter))
    totals_rows_counter.append((counter,total_reg)) # Save a quantity of rows
    if total_reg not in control_totals_rows_counter:
        control_totals_rows_counter.append(total_reg)
    
    counter = counter + 1

control_count_row = {}
for i in control_totals_rows_counter:
    control_count_row[i] = []


current_value = None # Temp to make operations
# Charge a rich data
for i in totals_rows_counter:
    # What line?
    line = i[0]
    # Quantuty=
    qty = i[1]
    # If the rows change save event
    if qty != current_value:
        current_value = qty
        control_count_row[qty].append(line)



print("El total de lineas del archivo es: ")
print(str(counter))
print("las cantidades de registros por linea son:")
print(str(control_totals_rows_counter))
print("Cambios de cantidades de registros")
for i in control_count_row:
    print("Cantidad>"+str(i)+" /"+str(control_count_row[i]))
print("======Ver Archivo.txt======")

txt = ""
for i in totals_rows_counter:
    txt = txt + "Line: " + str(i[0]) + "  Count:" + str(i[1]) + "\n"

f = open('Archivo.txt', 'w', encoding="UTF-8")
f.write(txt)
f.close()






