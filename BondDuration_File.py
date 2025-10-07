import numpy as np

def getBondDuration(y, face, couponRate, m, ppy = 1):
    t = np.linspace(1/ppy, m, m * ppy)

    pv = 1 / (1 + y / ppy) ** (t*ppy)
    print(pv)

    cf = couponRate * face / ppy * np.ones(m * ppy - 1)
    cf = np.append(cf, couponRate * face / ppy + face)

    weighted_pv = sum(t * pv * cf)

    pvcf = sum(pv * cf)
    dur = weighted_pv / pvcf

    return dur
print(getBondDuration(0.03, 2000000, 0.04, 10, 2))