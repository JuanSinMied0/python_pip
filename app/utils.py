def get_population(country_dict):
  population_dict = {
    "2022" : int(country_dict["2022 Population"]),
    "2020" : int(country_dict["2020 Population"]),
    "2015" : int(country_dict["2015 Population"]),
    "2010" : int(country_dict["2010 Population"]),
    "2000" : int(country_dict["2000 Population"]),
    "1990" : int(country_dict["1990 Population"]),
    "1980" : int(country_dict["1980 Population"]),
    "1970" : int(country_dict["1970 Population"])
  }
  labels = population_dict.keys() #keys
  values = population_dict.values()
  return labels, values
  
def population_by_country(data, country):
  result = list(filter(lambda item: item["Country"] == country, data))
  return result

def get_world_population_percentage(data):
  #Para obtener columna de paises y porcentage
  paises = list(map(lambda item:item["Country"],data))
  porcentaje_mundial = list(map(lambda item:item["World Population Percentage"],data))
  return paises, porcentaje_mundial