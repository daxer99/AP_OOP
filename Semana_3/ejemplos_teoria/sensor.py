from abc import ABC,abstractmethod

class Sensor(ABC):
    def __int__(self):
        self.__batery_level = 100
    @abstractmethod
    def medir(self):
        pass
class Sensor_temperatura(Sensor):
    def medir(self):
        print("medir temp")
class Sensor_humedad(Sensor):
    def medir(self):
        print("medir humedad")

s1 = Sensor_temperatura()
s2 = Sensor_temperatura()
s3 = Sensor_humedad()
sensores = [s1,s2,s3]

for sensor in sensores:
    sensor.medir()
