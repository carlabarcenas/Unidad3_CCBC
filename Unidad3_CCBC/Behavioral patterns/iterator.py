# autor:Carla del Carmen Barcenas Castillo
# Grupo: GITI9072
# nombre: behaviral patterns


def count_to(count):

    numbers_in_german = ["eins", "zwei", "drei", "vier", "funf"]

    iterator = zip(range(count), numbers_in_german)

    for position, number in iterator:

        yield number

for num in count_to(3):
    print("{}".format(num))

for num in count_to(4):
    print("{}".format(num))