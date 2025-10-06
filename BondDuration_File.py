import numpy as np

def getBondDuration(y, face, couponRate, m, ppy = 1):
    t = np.linspace(1/ppy, m, m * ppy)

    pv = 1 / (1 + y / ppy) ** t

    cf = couponRate * face / ppy * np.ones(m * ppy - 1)
    cf = np.append(cf, couponRate * face / ppy + face)

    weighted_pv = t * pv

    price = pv @ cf.transpose()
    dur = (weighted_pv @ cf).transpose() / price

    return dur