class Car:
    def __init__(self,color,license_plate,vin_number):
        self.color=color
        self._license_plate=license_plate
        self.__vin_number=vin_number

my_car=Car("red","1234ABCD",12340987)
ext_color="red"
ext_license_plate="1234ABCD"
ext_vin_number=12340987