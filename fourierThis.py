import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack
import csv

import csv
with open('dataBeforeFFT.csv', 'r') as file:
    reader = csv.reader(file)
    raw = []
    for row in reader:
        raw.append(row[12])

raw = raw[1:]

raw = np.array(raw).astype(np.float64)
avg = np.mean(raw)
raw = [x - avg for x in raw]

# Number of samplepoints
N = raw.__len__()
# sample spacing
T = 1.0 / 100.0
x = np.linspace(0.0, N*T, N)
y = raw
yf = scipy.fftpack.fft(y)
xf = np.linspace(0.0, 1.0/(2.0*T), N/2)

n = 100

xf2 = xf.copy()
xf2[n:] = [0.0] * np.int(np.abs(((N/2)-n)))
yf2 = yf.copy()
yf2[n:] = [0.0] * np.int(np.abs(((N)-n)))

plt.subplot(2, 1, 1)
plt.plot(np.fft.ifft(yf))
plt.subplot(2, 1, 2)
plt.plot(np.fft.ifft(yf2))

fig, ax = plt.subplots()
ax.plot(xf2, 2.0/N * np.abs(yf2[:N//2]))
plt.show()