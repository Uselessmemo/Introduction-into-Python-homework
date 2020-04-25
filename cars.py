import os
import csv

class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.car_type = None
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying
    
    def get_photo_file_ext(self):
        file_ext = os.path.splitext(self.photo_file_name)
        return file_ext

class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = passenger_seats_count
    
class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        try:
            self.body_whl = body_whl.split('x')
            for i in range(3):
                self.body_whl[i] = float(self.body_whl[i])
        except (IndexError, ValueError):
            self.body_whl = [0,0,0]

    def get_body_volume(self):
        volume = self.body_whl[0] * self.body_whl[1] * self.body_whl[1]
        return volume

class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra

def get_car_list(csv_path):
    car_list = []
    with open(csv_path, 'r') as csv_fd:
        reader = csv.reader(csv_fd, delimiter = ';')
        next(reader, None)
        for row in reader:
            tmp = None
            try:
                if row[0] == 'car':
                    tmp = Car(brand = row[1], photo_file_name = row[3], carrying = row[5], passenger_seats_count = row[2])
                    tmp.car_type = 'car'
                elif row[0] == 'truck':
                    tmp = Truck(brand = row[1], photo_file_name = row[3], carrying = row[5], body_whl = row[4])
                    tmp.car_type = 'truck'
                elif row[0] == 'spec_machine':
                    tmp = SpecMachine(brand = row[1], photo_file_name = row[3], carrying = row[5], extra = row[-1])
                    tmp.car_type = 'spec_machine'
                if tmp:
                    car_list.append(tmp)
            except IndexError:
                continue
    return car_list

