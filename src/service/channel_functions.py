from log.log import log_internal
from resources.global_resources.log_vars import logException
from resources.lang.enGB.logs import *
from service.channels import channels


def get_channel_item(chan_id):
    try:
        return channels[chan_id]
    except Exception as e:
        log_internal(logException,
                     logDesc_channel_functions_getItem,
                     description='channel "{chan_id}"'.format(chan_id=chan_id),
                     exception=e)
        return False


def get_channel_item_listingsrc_list(chan_id):
    try:
        chan = get_channel_item(chan_id)
        return chan['dataSources'].keys()
    except Exception as e:
        log_internal(logException,
                     logDesc_channel_functions_getSources,
                     description='channel "{chan_id}"'.format(chan_id=chan_id),
                     exception=e)
        return False


def get_channel_item_listingsrc(chan_id, src):
    try:
        item = get_channel_item(chan_id)
        if bool(item):
            return item['dataSources'][src]
        return False
    except Exception as e:
        log_internal(logException,
                     logDesc_channel_functions_getSource_details,
                     description='channel "{chan_id}" and source "{src}"'.format(chan_id=chan_id, src=src),
                     exception=e)
        return False


def get_channel_item_listingsrc_id(chan_id, src):
    try:
        chan = get_channel_item_listingsrc(chan_id, src)
        return chan['id']
    except Exception as e:
        log_internal(logException,
                     logDesc_channel_functions_getSource_id,
                     description='channel "{chan_id}" and source "{src}"'.format(chan_id=chan_id, src=src),
                     exception=e)
        return False


def get_channel_item_plus1(chan_id):
    try:
        item = get_channel_item(chan_id)
        return item['hasPlus1']
    except Exception as e:
        log_internal(logException,
                     logDesc_channel_functions_getSource_offset,
                     description='channel "{chan_id}"'.format(chan_id=chan_id),
                     exception=e)
        return False
