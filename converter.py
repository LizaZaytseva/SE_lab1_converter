RATIO = {
    'gr ct': 5,
    'ct gr': 0.2,
    'gr oz': 0.03527,
    'oz gr': 28.34952,
    'ct oz': 0.00705,
    'oz ct': 141.74762
}


def converter():
    print('Weight converter: grams <-> carats <-> ounce')
    data = input('Enter the value and specify the unit of measurement (gr,ct,oz) e.g. 123 gr: ').split()
    unit = input('Enter the required unit of measurement (gr,ct,oz): ')
    round_a = input('Rounding accuracy: ')

    ratio = data[1] + " " + unit
    if len(data) < 2 or len(unit) != 2 or ratio not in RATIO:
        print('Invalid format!')
    else:
        try:
            print(f"Result:\t{round(float(data[0]) * RATIO[ratio], int(round_a))} {unit}")
        except:
            print('Invalid format!')


converter()