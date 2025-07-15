#Analizando los datos de registro de empleados 
import pandas as pd

#cargar los datos a analizar 
datosEmpleados=pd.read_csv("datos_empleados_bar.csv")
print(datosEmpleados)

#aplicando tranformaciones y filtros
#clasificar los empleados con salario a tre millones
salariosMayoresATres=datosEmpleados.query("`Salario (COP)`>3000000")

#obtener los empleados con mas de 10 años de experienciA
empleadosExperienciaDiez=datosEmpleados.query("`Experiencia (años)`>10")

#empleados que trabajan mas de 180 horas
empleados180=datosEmpleados.query("`Horas laboradas/mes`>180")


 #necesito optener empleados cuyo cargo es bartender
bartenders=datosEmpleados.query("`Cargo en el bar`==`Bartender`") 