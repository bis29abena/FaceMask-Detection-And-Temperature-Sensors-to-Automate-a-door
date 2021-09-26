from smbus2 import SMBus
from mlx90614 import MLX90614
bus = SMBus(1)
sensor = MLX90614(bus, address=0x5A)
print(f"Ambient Temperature : {sensor.get_ambient()}")
print(f"Object Temperature : {sensor.get_object_1()}") 
bus.close()