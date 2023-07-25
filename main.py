import pandas as pd
from data.platos import platosPopulares
from data.reservas import Reservas
from data.proveedor import proveedores
from data.creartabla import crearTabla

tablaPlatos=pd.DataFrame(platosPopulares)
print(tablaPlatos)
crearTabla(tablaPlatos, "Tabla Platos Populares")

tablaReservas=pd.DataFrame(Reservas)
print(tablaReservas)
crearTabla(tablaReservas, "Tabla Reservas")

tablaProveedor=pd.DataFrame(proveedores)
print(tablaProveedor)
crearTabla(tablaProveedor, "Tabla Proveedores")