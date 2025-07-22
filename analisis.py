#Analizando los datos de registro de empleados 
import pandas as pd

#cargar los datos a analizar 
datosEmpleados=pd.read_csv("datos_empleados_bar.csv")


#aplicando tranformaciones y filtros
#clasificar los empleados con salario a tre millones
salariosMayoresATres=datosEmpleados.query("`Salario (COP)`>3000000")
print(salariosMayoresATres.head(5))
#obtener los empleados con mas de 10 años de experienciA
empleadosExperienciaDiez=datosEmpleados.query("`Experiencia (años)`>10")
print(empleadosExperienciaDiez.head(5))

#empleados que trabajan mas de 180 horas
empleados180=datosEmpleados.query("`Horas laboradas/mes`>180")
print(empleados180.head(5))


 #necesito optener empleados cuyo cargo es bartender
bartenders=datosEmpleados.query("`Cargo en el bar`=='Bartender'") 
print(bartenders.head(5))