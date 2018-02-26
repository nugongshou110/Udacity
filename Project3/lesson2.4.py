import vector

# vector1 = vector.Vector([8.218, -9.341])
# vector2 = vector.Vector([-1.129, 2.111])
# print(vector1.plus2(vector2))
#
# vector3 = vector.Vector([7.119, 8.215])
# vector4 = vector.Vector([-8.223, 0.878])
# print(vector3.minus2(vector4))
#
# vector5 = vector.Vector([1.671, -1.012, -0.318])
# print(vector5.scalar_multiply2(7.41))

# vector6 = vector.Vector([-0.221, 7.437])
# print(vector6.magnitude())
#
# vector7 = vector.Vector([8.813, -1.331, -6.247])
# print(vector7.magnitude())
#
# vector8 = vector.Vector([5.581, -2.136])
# print(vector8.normalized())
#
# vector9 = vector.Vector([1.996, 3.108, -4.554])
# print(vector9.normalized())

# vector10 = vector.Vector([7.887, 4.138])
# print(vector10.dot_product(vector.Vector([-8.802, 6.776])))
#
# vector11 = vector.Vector([-5.955, -4.904, -1.874])
# print(vector11.dot_product(vector.Vector([-4.496, -8.755, 7.103])))
#
# vector12 = vector.Vector([3.183, -7.627])
# print(vector12.angle_rad(vector.Vector([-2.668, 5.319])))
#
# vector13 = vector.Vector([7.35, 0.221, 5.188])
# print(vector13.angle_degrees(vector.Vector([2.751, 8.259, 3.985])))

vector14 = vector.Vector([-7.579, -7.88])
vector15 = vector.Vector([22.737, 23.64])
print('parallel = ' + vector14.parallelism(vector15) + ", orthogonal = " + str(vector14.orthogonality(vector15)))

vector16 = vector.Vector([-2.029, 9.97, 4.172])
vector17 = vector.Vector([-9.231, -6.639, -7.245])
print('parallel = ' + vector16.parallelism(vector17) + ", orthogonal = " + str(vector16.orthogonality(vector17)))

vector18 = vector.Vector([-2.328, -7.284, -1.214])
vector19 = vector.Vector([-1.821, 1.072, -2.94])
print('parallel = ' + vector18.parallelism(vector19) + ", orthogonal = " + str(vector18.orthogonality(vector19)))

vector20 = vector.Vector([2.118, 4.827])
vector21 = vector.Vector([0, 0])
print('parallel = ' + vector20.parallelism(vector21) + ", orthogonal = " + str(vector20.orthogonality(vector21)))
