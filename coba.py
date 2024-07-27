# name = "MALIK ARROSID"
# age = 20
# is_marriage = False
# # print(name, age)
# # print("name : " + name)
# # print(f"name : {name}")
# # print(f"age : {age}")
# # print("
# #       ")
# # print('''      
# #       coba triple single quotes
# #       ''')
# print(f''' 
#       nama saya adalah {name}
#       dan usia saya {age}
#       ''')

# i = 0
# while i < 10:
#     print(i)
#     i = i + 1

# for i in range(5):
#     print(i)

cave_shape = "|_|"
cave = [cave_shape] * 4
# null_cave = cave
null_cave = cave.copy()
null_cave[2] = "MALIK"
null_cave[0] = "ARSID"
print(null_cave)
print(cave)