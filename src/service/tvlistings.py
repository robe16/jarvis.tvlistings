import threading
import datetime
from time import sleep

from service.channel_list import *
from service import data_source_bleb
from log.log import log_internal
from resources.global_resources.log_vars import logPass, logFail, logException
from resources.lang.enGB.logs import *
from parameters import listing_retrieval_frequency


class TVlistings():

    _listings = {}

    def __init__(self):
        #
        self.thread_update()

    def thread_update(self):
        t = threading.Thread(target=self._listings_process)
        t.start()

    def _listings_process(self):
        #
        # TODO run once an hour (duration TBD) to remove times that have passed and add next 'batch' of listings
        while True:
            self.build_listing_dict()
            sleep(self._sleep_duration())

    def build_listing_dict(self):
        #
        for chan_name in channels:
            try:
                self._listings[chan_name] = self._getlisting(chan_name, channels[chan_name])
            except Exception as e:
                log_internal(logException,
                             logDesc_retrieve_listing.format(channel=chan_name),
                             description='-',
                             exception=e)


    # All channels

    def get_listings_all(self):
        return self._listings

    # Specificied channel

    def get_listings_channel(self, channame):
        return self._listings[channame]

    # General request code (checks if a listing source is available and then retrieves from relevant scripts)

    def _getlisting(self, chan_name, listing_srcs):
        #
        if not listing_srcs:
            log_internal(logException,
                         logDesc_retrieve_listing_no_source.format(channel=chan_name),
                         description='-')
            return {}
        #
        if len(listing_srcs)>0:
            for src, code in listing_srcs.items():
                try:
                    if src == 'bleb':
                        log_internal(logPass,
                                     logDesc_retrieve_listing.format(channel=chan_name),
                                     description=src)
                        return data_source_bleb.get(code)
                except Exception as e:
                    log_internal(logException,
                                 logDesc_retrieve_listing.format(channel=chan_name),
                                 description=src,
                                 exception=e)
        return {}

    # Common/general functions

    @staticmethod
    def _sleep_duration():
        t = datetime.datetime.today()
        future = datetime.datetime(t.year, t.month, t.day, listing_retrieval_frequency, 0)
        if t.hour >= listing_retrieval_frequency:
            future += datetime.timedelta(days=1)
        return (future - t).seconds
