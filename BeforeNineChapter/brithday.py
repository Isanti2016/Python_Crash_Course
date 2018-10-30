age = 23/2
message = "Happy " + str(age) + "rd Birthday!"
print(message)
print("***********************列表*******************************")
bicycles = ['trek','cannondale','redline','specialized']
print(bicycles)

bicycles[1] = 'wang'
print(bicycles[1])
bicycles.insert(1, 'bei')
print(bicycles[1])
bicycles.append('nihao')
print(bicycles[-1])

bicycles[3] = 5
print( 2 * bicycles[3] )

print(bicycles)

"""下面是元组"""

print("***********************元组*******************************")

dimensions = ('wang', 'bei', 5, 6)
print(dimensions)
print( 5 * dimensions[2] )

"""下面是字典"""

print("*************************字典*****************************")

alien_0 = {'color':'green', 'point':5, 6:'nihao', 7:2 }
print(alien_0)
print( 5 * alien_0['point'])
print( alien_0[6] )
print( 5 * alien_0[7] )
