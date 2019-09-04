planet_list = ["Mercury", "Mars"]

planet_list.append("Jupiter")
planet_list.append("Saturn")

planet_list.extend(["Uranus", "Neptune"])

planet_list.insert(2, "Venus")
planet_list.insert(3, "Earth")

planet_list.append("Pluto")

rocky_planets = planet_list[slice(0, 4)]

del planet_list[8]

print(planet_list)
print(rocky_planets)


# Iterate over your list of planets, and inside that loop, iterate over the list of tuples. Print, for each planet, which spacecraft have visited it.

spacecraft = [
   ("Cassini", "Saturn"),
   ("Viking", "Mars"),
   ("Juno", "Jupiter"),
   ("Galileo", "Jupiter")
]

for planet in planet_list:
    for value in spacecraft:
        if planet == value[1]:
            print(value[0])