import math
import talib
import numpy as np
from alphas.funcs import *


def get_signal(close, open, high, low, volume, days, mode):
    # print("close", close, "open", open, "high", high, "low", low, "volume", volume, "days", days, "mode", mode)
    if mode != 1:
        return 0

    # Ensure the length of volume is sufficient for calculations
    if len(volume) < 3:
        return 0

    # Calculate the log of the ratio of volume[today - 1] to volume[today - 2]
    today = len(close) - 1
    try:
        log_value = math.log(volume[today - 1] / volume[today - 2])
    except (IndexError, ZeroDivisionError, ValueError):
        return 0

    # Return the log value if it's between 1.1 and 1.3, otherwise return 0
    return log_value if 1.1 <= log_value <= 1.3 else 0


class Alpha:
    def create(self, global_data, xml_node):
        # self.__global_data = global_data
        # print("global_data..."clear, global_data)
        self.delay = int(xml_node.get("delay", 1))
        self.days = int(xml_node.get("days", 7))
        self.mode = int(xml_node.get("mode", 0))
        np.set_printoptions(threshold=np.inf)
        self.close = global_data["u_close"]
        self.open = global_data["u_open"]
        self.high = global_data["u_high"]
        self.low = global_data["u_low"]
        self.volume = global_data["u_volume"]
        valid_univ = xml_node.get("valid", "ALL")
        self.valid = global_data[valid_univ]

    def generate(self, di):
        
        d = di - self.delay
        # if (self.mode == 2): time.sleep(0.0001*self.days)
        for ii in range(len(self.alpha)):
            if (not self.valid[di][ii]):
                continue
            self.alpha[ii] = get_signal(
                self.close[ii, 0:d + 1], self.open[ii, 0:d + 1],
                self.high[ii, 0:d + 1], self.low[ii, 0:d + 1],
                self.volume[ii, 0:d + 1], self.days,
                self.mode)
