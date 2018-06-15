import threading

from bottle import get
from bottle import request, run

from config.config import get_cfg_port_listener
from log.log import log_internal
from resources.global_resources.log_vars import logPass
from resources.lang.enGB.logs import *
from service.tvlistings import TVlistings

from apis.get_config import get_config
from apis.get_tvlistings_all import get_tvlistings_all
from apis.get_tvlistings_channel import get_tvlistings_channel


def start_bottle(port_threads):

    ################################################################################################
    # Create device
    ################################################################################################

    _tvlistings = TVlistings()

    log_internal(logPass, logDescDeviceObjectCreation, description='success')

    ################################################################################################
    # APIs
    ################################################################################################

    @get('/config')
    def api_get_config():
        return get_config(request)

    @get('/tvlistings/all')
    def api_get_tvlistings_all():
        return get_tvlistings_all(request, _tvlistings)

    @get('/tvlistings/channel/<channame>')
    def api_get_tvlistings_channel(channame):
        return get_tvlistings_channel(request, _tvlistings, channame)

    ################################################################################################

    def bottle_run(x_host, x_port):
        log_internal(logPass, logDescPortListener.format(port=x_port), description='started')
        run(host=x_host, port=x_port, debug=True)

    ################################################################################################

    host = 'localhost'
    ports = get_cfg_port_listener()
    for port in ports:
        t = threading.Thread(target=bottle_run, args=(host, port,))
        port_threads.append(t)

    # Start all threads
    for t in port_threads:
        t.start()
    # Use .join() for all threads to keep main process 'alive'
    for t in port_threads:
        t.join()
