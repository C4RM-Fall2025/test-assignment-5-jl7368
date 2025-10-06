import numpy as np

def getBondPrice(y, face, couponRate, m, ppy=1):
    t = np.arange(1, m * ppy + 1)
    pv = 1 / (1 + y / ppy) ** t
    cf = couponRate * face / ppy * np.ones(m * ppy - 1)
    cf = np.append(cf, couponRate * face / ppy + face)
    price = sum(pv * cf)
    return price 