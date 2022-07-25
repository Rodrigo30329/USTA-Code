
import re
from typing import OrderedDict

mensaje="asmeleeeee"
patron = r'(\w)'
mensaje = re.sub(patron, r'\1 ', mensaje)

print(mensaje)