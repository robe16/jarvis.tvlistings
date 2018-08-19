from log.log import log_internal
from resources.global_resources.log_vars import logException
from resources.lang.enGB.logs import *


def get_channel_item(chan_name):
    try:
        return channels[chan_name]
    except Exception as e:
        log_internal(logException,
                     logDesc_channel_functions_getItem,
                     description='channel "{chan_name}"'.format(chan_name=chan_name),
                     exception=e)
        return False


def get_channel_item_listingsrc_list(chan_name):
    try:
        chan = get_channel_item(chan_name)
        return chan.keys()
        # return channels['channels'][chan_name]['sources']
    except Exception as e:
        log_internal(logException,
                     logDesc_channel_functions_getSources,
                     description='channel "{chan_name}"'.format(chan_name=chan_name),
                     exception=e)
        return False


def get_channel_item_listingsrc(chan_name, src):
    try:
        item = get_channel_item(chan_name)
        if bool(item):
            return item[src]
        return False
    except Exception as e:
        log_internal(logException,
                     logDesc_channel_functions_getSource_details,
                     description='channel "{chan_name}" and source "{src}"'.format(chan_name=chan_name,
                                                                                   src=src),
                     exception=e)
        return False


def get_channel_item_listingsrc_id(chan_name, src):
    try:
        chan = get_channel_item_listingsrc(chan_name, src)
        return chan['id']
    except Exception as e:
        log_internal(logException,
                     logDesc_channel_functions_getSource_id,
                     description='channel "{chan_name}" and source "{src}"'.format(chan_name=chan_name,
                                                                                   src=src),
                     exception=e)
        return False


def get_channel_item_listingsrc_offset(chan_name, src):
    try:
        chan = get_channel_item_listingsrc(chan_name, src)
        return chan['offset']
    except Exception as e:
        log_internal(logException,
                     logDesc_channel_functions_getSource_offset,
                     description='channel "{chan_name}" and source "{src}"'.format(chan_name=chan_name,
                                                                                   src=src),
                     exception=e)
        return False
