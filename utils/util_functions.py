# some utility functions


def cal_on_off_time(data):
    """

    """

        d = np.diff(np.pad(c, pad_width=1, mode='constant'))
        r = np.flatnonzero(d == -1) - np.flatnonzero(d == 1)
