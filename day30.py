#sets methods
s1={1,2,4,6}
s2={3,6,7}
print(s1.union(s2)) 
s1.update(s2)
print(s1,s2)

cities= {"tokyo","madrid","berlin","delhi"}
cities2={"tokyo","seoul","kabul","madrid"}
cities3=cities.union(cities2)
print(cities3)

cities= {"tokyo","madrid","berlin","delhi"}
cities2={"tokyo","seoul","kabul","madrid"}
cities3=cities.intersection(cities2)
print(cities3)

cities= {"tokyo","madrid","berlin","delhi"}
cities2={"tokyo","seoul","kabul","madrid"}
cities3=cities.intersection_update(cities2)
print(cities)

cities= {"tokyo","madrid","berlin","delhi"}
cities2={"tokyo","seoul","kabul","madrid"}
cities3=cities.symmetric_difference(cities2)
print(cities3)

cities= {"tokyo","madrid","berlin","delhi"}
cities2={"tokyo","seoul","kabul","madrid"}
cities3=cities.difference(cities2)
print(cities3)

#there are several in built methods used for the manupulation of set.
#isdisjoint() method
cities= {"tokyo","madrid","berlin","delhi"}
cities2={"tokyo","seoul","kabul","madrid"}
print(cities.isdisjoint(cities2))

#issuperset() method
cities= {"tokyo","madrid","berlin","delhi"}
cities2={"seoul","kabul"}
print(cities.issuperset(cities2))
cities3={"tokyo","mandrid","delhi"}
print(cities.issuperset(cities3))
print(cities3.issubset(cities))

cities= {"tokyo","madrid","berlin","delhi"}
cities.add("helsinki")
print(cities)
cities.remove("delhi")
print(cities)
cities.discard("berlin")
print(cities)