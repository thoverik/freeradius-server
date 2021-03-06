import radiusd
import threading

local = threading.local()

def authorize(p):
    global local
    radiusd.log(radiusd.L_DBG, 'Python - threading.local.tls()=' + str(hasattr(local, 'tls')))
    if hasattr(local, 'tls'):
        return radiusd.RLM_MODULE_OK
    else:
        local.tls = True
        return radiusd.RLM_MODULE_NOOP
