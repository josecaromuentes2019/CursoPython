import pickle
from serializarObjetos import Vehiculo

vehiculos = open('VehiculoBinario','rb')

misVehiculos = pickle.load(vehiculos)

vehiculos.close()

for c in misVehiculos:

    c.estado()
    print()


