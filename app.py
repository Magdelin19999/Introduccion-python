#Este es un comentario de una sola linea
"""Este comentario este multiples lineas """

#Variables

nombre ='Magdelin'    #String
cantidadMaterias = 3  #integer
numeroDecimal =17.2   #float


diaSemana =['lunes','Martes','Miercoles','Jueves','Viernes'] #Listas = Array
listaDinamica =[0,'Hola',12.5,[0,1]]

print(diaSemana[2])#Miercoles
print(listaDinamica[3][1])#[0,1]=1

esMayorEdad = False
# Diccionarios -JSON-objetos

persona ={
    'nombre':'magdeli',
    'apellidos':'pai',
    'materias':['Bases de datos II','Lenjuage de cuarta generacion'],
  
}
print(persona['nombre'])#magdelis
print(persona['materias'][1])#Lenjuage de cuarta 

#Listas de Diccionarios

personas =[
    {
    'nombre':'made',
    'apellidos':'potosi',
    'edad':'25',
    'materia':'eventos'   
    },
    {
    'nombre':'made',
    'apellidos':'potosi',
    'edad':'25',
    'materias':'Lenhuaje orientado a objetos'
    },
    {
     'nombre':'yoli',
     'apellidos':'Pai',
     'edad':'23',
     'materia':'Español'   
    },
    
]

print(personas[1]['apellidos'][0])

#Condiciones

esMayorEdad= True
esMayorEdad = input('Ingrese edad\n\t')

# IF
if esMayorEdad==True:
    print('Es mayor de edad')
else:
    print('No es mayor de edad')
    print('Mensaje de prueba')


#For
for per in personas:
    print(per)

#Holiiii

