import sys

sys.path.append('D:\prjs_all\prjs_edk')

import pyedk

pe=pyedk.ras.ras_server.rasServer();
pe.run();