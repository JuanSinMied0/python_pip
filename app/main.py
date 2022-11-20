#para llamar otros modulos propios se debe importar
import utils
import read_csv
import charts
def run():
  data = read_csv.read_csv('data.csv')
  data = list(filter(lambda item : item["Continent"] == "South America",data))
  paises, porcentaje_mundial = utils.get_world_population_percentage(data)
  country = input("Digite el pais => ")
  print(country) #recibe el pais y lo reduce en el csv
  charts.generate_pie_chart(paises, porcentaje_mundial)
  result = utils.population_by_country(data, country)
  if len(result) > 0:
    country = result[0]
    print(country)
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(country["Country"], labels, values)
  
if __name__ == '__main__': #si se ejecuta desde la terminal, entra a run si se ejecuta desde otro archivo no hacer nada
  run()