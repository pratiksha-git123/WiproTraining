from circle import areaofcircle, perimeterofcircle

radius = int(input('Enter Radius: '))

print('Area: ', areaofcircle(radius))
print('Peri: ', perimeterofcircle(radius))

si = int(input('Enter side of sq: '))
print('Area: ', si * si)
print('Peri: ', 4 * si)

l = int(input('Enter length: '))
b = int(input('Enter breadth: '))
print('Area: ', l * b)