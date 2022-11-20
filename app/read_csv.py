import csv

def read_csv(path):
  with open(path, "r") as csvfile:
    reader = csv.reader(csvfile, delimiter= ",") #lo que nos entrega el archivo, revisar
    header = next(reader) #sacar manual cada grupo
    data = [] #para llenar el diccionario
    for row in reader: #para leer encabezamiento a fila
      iterable = zip(header,row)
      country_dict = {key: value for key, value in iterable} #diccionario
      #print(country_dict)
      data.append(country_dict) #creando lista de diccionare, llave valor
    return data #retorna pa llenar la lista

if __name__ == '__main__':
  data = read_csv('./app/data.csv')
  print(data[0])
  
def get_population_percentage(data,world):
  result1 = list(filter(lambda item:item["World Population Percentage"]==world, data))
  return print(result1)
#Transformar a listas clon diccionarios para mejor manipulacion de datos