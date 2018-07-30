from bottle import request, run, route, get

from config.config import get_cfg_port
from common_functions.request_enable_cors import response_options
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

    @route('/config', method=['OPTIONS'])
    @route('/tvlistings/all', method=['OPTIONS'])
    @route('/tvlistings/channel/<channame>', method=['OPTIONS'])
    def api_cors_options(**kwargs):
        return response_options()

    @get('/config')
    def api_get_config():
        response = get_config(request)
        return response

    @get('/tvlistings/all')
    def api_get_tvlistings_all():
        response = get_tvlistings_all(request, _tvlistings)
        return response

    @get('/tvlistings/channel/<channame>')
    def api_get_tvlistings_channel(channame):
        response = get_tvlistings_channel(request, _tvlistings, channame)
        return response

    ################################################################################################

    host = '0.0.0.0'
    port = get_cfg_port()
    run(host=host, port=port, server='paste', debug=True)

    log_internal(logPass, logDescPortListener.format(port=port), description='started')

    ################################################################################################
