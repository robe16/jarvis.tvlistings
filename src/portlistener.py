from bottle import get
from bottle import request, run

from config.config import get_cfg_port
from log.log import log_internal
from resources.global_resources.log_vars import logPass
from resources.lang.enGB.logs import *
from service.tvlistings import TVlistings

from apis.get_config import get_config
from apis.get_tvlistings_all import get_tvlistings_all
from apis.get_tvlistings_channel import get_tvlistings_channel


def start_bottle():

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

    host = '0.0.0.0'
    port = get_cfg_port()
    run(host=host, port=port, server='paste', debug=True)

    log_internal(logPass, logDescPortListener.format(port=port), description='started')

    ################################################################################################
