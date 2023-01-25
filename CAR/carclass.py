class CarClass:
    def __init__(self, brand,model, year,run):
        self.brand = brand
        self.model = model
        self.year = year
        self.run = int(run)

    def show_car(self):
        print(f'{self.brand}, {self.model}, {self.year} year, {self.run} km/h')

        