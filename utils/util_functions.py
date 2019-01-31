# some utility functions


def cal_on_off_time(data):
    """
    inputs:
    ------
    data: 1D numpy array with only 0, 1 entries
    
    return:
    ------
    1D array: number of uninterrupted repeats for "1"
    """
    # source: https://stackoverflow.com/questions/54446907/how-to-calculate-numbers-of-uninterrupted-repeats-in-an-array-in-python?noredirect=1#comment95703294_54446907 
    d = np.diff(np.pad(data, pad_width=1, mode='constant'))
    r = np.flatnonzero(d == -1) - np.flatnonzero(d == 1)
    return r

