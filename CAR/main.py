from CAR import elcectrocar

def main():
    ecar = elcectrocar.ElectroCar('Tesla', 'T', 2020, 5000)
    ecar.show_car()
    ecar.description_battery()

if __name__ == '__main__':
    main()