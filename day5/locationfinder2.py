import re
from numpy import inf

file = open("input.txt", "r")
Lines = file.readlines()

seedNums = list(map(int, re.findall(r'\d+', Lines[0])))

def mapReader(mapName):
    outList = []
    read = False
    for line in Lines:
        if mapName in line:
            read = True
        elif read and not re.search(r'\d+', line):
            read = False
            break
        elif read:
            outList.append(list(map(int, re.findall(r'\d+', line))))
    return outList

seedToSoil = mapReader("seed-to-soil")
soilToFertilizer = mapReader("soil-to-fertilizer")
fertilizerToWater = mapReader("fertilizer-to-water")
waterToLight = mapReader("water-to-light")
lightToTemperature = mapReader("light-to-temperature")
temperatureToHumidity = mapReader("temperature-to-humidity")
humidityToLocation = mapReader("humidity-to-location")

def mapper(mapList, value):
    for range in mapList:
        if value >= range[1] and value < range[1] + range[2]:
            return value + range[0] - range[1]
    return value

minimum = inf

for i in range(0, len(seedNums), 2):
    print(i)
    for j in range(seedNums[i], seedNums[i] + seedNums[i + 1]):
        minimum = min(mapper(humidityToLocation,
               mapper(temperatureToHumidity,
                      mapper(lightToTemperature,
                             mapper(waterToLight,
                                    mapper(fertilizerToWater,
                                           mapper(soilToFertilizer,
                                                  mapper(seedToSoil,
                                                  j
                                                  )
                                                  ))))
                   
               )
            
        ), minimum)


print(minimum)