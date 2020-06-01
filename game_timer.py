# -*- coding: utf-8 -*-
#
# @author Epsirom

import math
import time


class GameTimer(object):

    def __init__(self, trigger, interval=1.0):
        """Initializes GameTimer with trigger function and interval seconds."""
        if not hasattr(trigger, '__call__'):
            raise TypeError("trigger should be callable")
        if not isinstance(interval, float):
            raise TypeError("interval should be float")
        assert interval > 0
        self.interval = interval
        self.trigger = trigger
        self.is_running = False

    def start(self):
        self.is_running = True
        while self.is_running:
            time.sleep(math.ceil(time.time() / self.interval) * self.interval - time.time())
            if self.is_running:
                self.trigger()

    def stop(self):
        self.is_running = False
