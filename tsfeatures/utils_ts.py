import numpy as np
def scalets(x):
    # Scaling time series
    scaledx = (x - x.mean())/x.std()
    #ts = pd.Series(scaledx, index=x.index)
    return scaledx

def poly(x, p):
    x = np.array(x)
    X = np.transpose(np.vstack(list((x**k for k in range(p+1)))))
    return np.linalg.qr(X)[0][:,1:]

def embed(x, p):
    x = np.array(x)
    x = np.transpose(np.vstack(list((np.roll(x, k) for k in range(p)))))
    x = x[(p-1):]

    return x

def hurst_ernie_chan(p, lags=12):
    #taken from
    #https://stackoverflow.com/questions/39488806/hurst-exponent-in-python

    variancetau = []; tau = []

    for lag in range(2, lags):

        #  Write the different lags into a vector to compute a set of tau or lags
        tau.append(lag)

        # Compute the log returns on all days, then compute the variance on the difference in log returns
        # call this pp or the price difference
        pp = np.subtract(p[lag:], p[:-lag])
        variancetau.append(np.var(pp))

    # we now have a set of tau or lags and a corresponding set of variances.
    #print tau
    #print variancetau

    # plot the log of those variance against the log of tau and get the slope
    m = np.polyfit(np.log10(tau),np.log10(variancetau),1)

    hurst = m[0] / 2

    return hurst


WWWusage = [88,84,85,85,84,85,83,85,88,89,91,99,104,112,126,
            138,146,151,150,148,147,149,143,132,131,139,147,150,
            148,145,140,134,131,131,129,126,126,132,137,140,142,150,159,
            167,170,171,172,172,174,175,172,172,174,174,169,165,156,142,
            131,121,112,104,102,99,99,95,88,84,84,87,89,88,85,86,89,91,
            91,94,101,110,121,135,145,149,156,165,171,175,177,
            182,193,204,208,210,215,222,228,226,222,220]

USAccDeaths = [9007,8106,8928,9137,10017,10826,11317,10744,9713,9938,9161,
               8927,7750,6981,8038,8422,8714,9512,10120,9823,8743,9129,8710,
               8680,8162,7306,8124,7870,9387,9556,10093,9620,8285,8466,8160,
               8034,7717,7461,7767,7925,8623,8945,10078,9179,8037,8488,7874,
               8647,7792,6957,7726,8106,8890,9299,10625,9302,8314,
               8850,8265,8796,7836,6892,7791,8192,9115,9434,10484,
               9827,9110,9070,8633,9240]
