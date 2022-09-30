# Egyetemi féléves értékelő: írjatok egy olyan programot - függvények segíségével - ,
# amely az alábbi tanulók féléves jegyét meghatározza.
# Az értékelésnél a következő szabályokat kell betartani:

## a beadando a jegy 10%-át adja
## a vizsga a jegy 70%-át
## a labor gyakorlat pedig a jegy 20%-át

# Az eredmények a következők szerint kell meghatározni
# 90 - 100 => 5
# 80 - 89 => 4
# 70 - 79 => 3
# 60 - 69 => 2
# 0  - 59 => 1

# példa az elvárt eredményre:
#
#



# kriszta = { "tanulo":"Kriszta",
#           "beadando" : [70, 60, 30, 10],
#           "vizsga" : [70, 75],
#           "labor" : [68.20, 77.20]
#         }
# (ez egy lekalkulált eredmény)
# Kriszta
# =+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=
# Kriszta átlag pontszáma: 69.54
# Kriszta tanuló eredménye: 2

# 2. feladat: az osztály átlag eredményeit is határozzátok meg:
# példa outputra:
#
# Osztály átlag pontszáma 72.79
# Osztály eredménye 3


karcsi = { "tanulo":"Horváth Károly",
         "beadando" : [80, 50, 40, 20],
         "vizsga" : [75, 75],
         "labor" : [78.20, 77.20]
       }


jani = { "tanulo":"Potter János",
          "beadando" : [82, 56, 44, 30],
          "vizsga" : [80, 80],
          "labor" : [67.90, 78.72]
        }


denes = { "tanulo" : "Neumann Dénes",
          "beadando" : [77, 82, 23, 39],
          "vizsga" : [78, 77],
          "labor" : [80, 80]
        }


emese = { "tanulo" : "Morvai Emese",
         "beadando" : [67, 55, 77, 21],
         "vizsga" : [40, 50],
         "labor" : [69, 44.56]
       }


tomi = { "tanulo" : "Kiss Tamás",
        "beadando" : [29, 89, 60, 56],
        "vizsga" : [65, 56],
        "labor" : [50, 40.6]
      }

def points(my_dict):
  temp = []
  
  for key, value in my_dict.items():
    if type(value)==list:
      if key == 'beadando':
        value=(sum(value)/len(value)) * 0.1
        temp.append(value)
        
      elif key == 'vizsga':
        value=(sum(value)/len(value)) * 0.7
        temp.append(value)

      elif key == 'labor':
        value=(sum(value)/len(value)) * 0.2
        temp.append(value)
    

  temp=sum(temp)
  return temp
def grade(myFunc):
  if myFunc <= 59:
    return  1
  if  70 > myFunc >= 60:
    return  2
  if  80 > myFunc >= 70:
    return  3
  if  90 > myFunc >= 80:
    return  4
  else:
    return  5
  
print (points(tomi))
print(grade(points(tomi)))

def average(*args):
  point_list = [points(karcsi), points(jani), points(denes), points(emese), 
  points(tomi)]
  grade_list = [ grade(points(karcsi)), grade(points(jani)), grade(points(denes)),
  grade(points(emese)), grade(points(tomi))]
  grade_list= sum(grade_list)/len(grade_list)
  point_list = sum(point_list)/len(point_list)
  return print (f'Az osztály átlagpontszáma {point_list} érdemjegyeik átlaga pedig {int(grade_list)}')

print (average())