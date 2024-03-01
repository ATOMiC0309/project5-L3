#1 - topshiriq-------------------------------------------------

# def item_append_cars(cars: list):
#     new_cars = cars.copy()
#     while True:
#         car = input("Avtomobil nomini kiriting: ")
#         if car.lower() == 'stop':
#             break
#         new_cars.append(car)
#     return new_cars
#
# cars = ["Malibu", "Gentra"]
# print(item_append_cars(cars))
# print(cars)

#2 - topshiriq-------------------------------------------------

# def add_user(users: dict):
#     new_users = users.copy()
#     while True:
#         key = input("Key: ")
#         if key.lower() == 'stop':
#             break
#         new_users[key] = input("Value: ")
#     return new_users
# users = {"Ism": "Toxir", "Fam": "Toxirov"}
# print(add_user(users))
# print(users)

#3 - topshiriq-------------------------------------------------

# taomlar = ["Osh", "Somsa", "Manti"]
# print(taomlar)
# taomlar.append("Sho'rva")
# print(tuple(taomlar))
# taomlar.insert(0, "Lag`mon")
# print(tuple(taomlar))

#4 - topshiriq-------------------------------------------------

# l = ["A", "a", "B", "b", "C", "c", "D", "c", "/", ","]
# low_let = []
# upp_let = []
# oth_sym = []
# for item in l:
#     if item.islower():
#         low_let.append(item)
#     elif item.isupper():
#         upp_let.append(item)
#     else:
#         oth_sym.append(item)
# print(f"Kichik: {tuple(low_let)}\nKatta: {tuple(upp_let)}\nBoshqa: {tuple(oth_sym)}")

#5 - topshiriq-------------------------------------------------

# l = ["Akmal", "abror", "toxir", "Sobir", "Bakir", "jalil"]
# low_title = []
# upp_title = []
# for item in l:
#     if item.istitle():
#         upp_title.append(item)
#     else:
#         low_title.append(item)
# print("Katta:", tuple(upp_title))
# print("Kichik:", tuple(low_title))

#6 - topshiriq-------------------------------------------------

# def phone_filter(phone_nnumbers: list):
#     uz_num = []
#     ru_num = []
#     us_num = []
#     oth_num = []
#     for num in phone_nnumbers:
#         if str(num).startswith('+998', 0, 4):
#             uz_num.append(num)
#         elif str(num).startswith('+7', 0, 2):
#             ru_num.append(num)
#         elif str(num).startswith('+1', 0, 2):
#             us_num.append(num)
#         else:
#             oth_num.append(num)
#     return f"uz: {tuple(uz_num)}\nru: {tuple(ru_num)}\nus: {tuple(us_num)}\nother numbers: {tuple(oth_num)}"
#
# p_numbers = ["+99812345678", "+7123456684", "+1354846135"]
# print(phone_filter(p_numbers))

#7 - topshiriq-------------------------------------------------

# n = int(input("n ni kiriting: "))
# print(list(range(1, n+1, 2)))

# 8 - topshiriq-----------------------------------------------

# sumbers = [ 386, 462, 47, 418, 907, 344, 236, 375, 823,
#             566, 597, 978, 328, 615, 953, 345, 399,
#             162, 758, 219, 918, 237, 412, 566, 826, 248,
#             866, 950, 626, 949, 687, 217, 815, 67, 104,
#             58, 512, 24, 892, 894, 767, 553, 81, 379,
#             843, 831, 445, 742, 717, 958,743, 527 ]
# for num in sumbers:
#     if num == 815:
#         break
#     print(num)

# 9 - topshiriq-----------------------------------------------

# d = {"fruit": "apple", "name": "Toxir", "food": "Plaov"}
# key = input("Key: ")
# value = input("Value: ")
# if d.get(key):
#     print("Lug'atda bunday kalit mavjud!")
# else:
#     d[key] = value
#
# print(d)

# 10 - topshiriq-----------------------------------------------

# d = {'a': 1, 'b': 2, 'c': 3}
# sum = 0
# for i in d.values():
#     sum += i
# print("Yig'indi:", sum)

# 11 - topshiriq-----------------------------------------------

# d = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36}
# sum = 0
# for i in d.keys():
#     sum += i
# print("Yig'indi:", sum)

# 12 - topshiriq-----------------------------------------------

# d = {}
# for i in range(1, int(input("n = "))+1):
#     d[i] = i*i
# print(d)

# 13 - topshiriq-----------------------------------------------

# d = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# sum = 0
# for i in d.values():
#     sum += i
# print("O'rta arifmetigi:", sum/len(d.values()))

# 14 - topshiriq-----------------------------------------------

# keys = ["name", "age", "phone"]
# values = ["Toxir", 35, "+9981121"]
# d = {}
# for i in range(0, len(keys)):
#     d[keys[i]] = values[i]
#
# print(d)
