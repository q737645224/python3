# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import numpy as np
import numpy.fft as nf
import scipy.io.wavfile as wf  # 用来读取wav文件
import matplotlib.pyplot as mp

sample_rate, noised_sigs = wf.read(
    '../data/noised.wav')
print(sample_rate)
print(noised_sigs.shape)
print(noised_sigs.dtype)
# 声场强度本身是(0到1)浮点数,为了让计算机保留更多的有效数位
# 所以扩大了2的15次方倍

noised_sigs = noised_sigs / 2**15  # 还原真实的声场强度

times = np.arange(len(noised_sigs)) / sample_rate
# 采样率的倒数是每个采样点的时间间隔

# 时间域到频率域的转换:
freqs = nf.fftfreq(times.size, d=1 / sample_rate)
# 将时间域的采样值变成频率域的复数数组:
noised_ffts = nf.fft(noised_sigs)
# 求复数的模:
noised_pows = np.abs(noised_ffts)

# 信号中能量最大的下标给频率数组,得到基波的频率:
fund_freq = freqs[noised_pows.argmax()]
print(fund_freq)

# 将复数数组中噪声的部分过滤掉:
noised_indices = np.where(
    np.abs(freqs) != fund_freq)
filter_ffts = noised_ffts.copy()
filter_ffts[noised_indices] = 0

# 得到没有噪声的能量
filter_pows = np.abs(filter_ffts)

# 通过傅里叶逆变换,将声场强度从频率域映射回时间域:
filter_sigs = nf.ifft(filter_ffts).real

wf.write('../data/filter.wav', sample_rate,
         (filter_sigs * 2**15).astype(np.int16))


mp.figure('Filter', facecolor='lightgray')
mp.subplot(221)
mp.title('Time Domain', fontsize=16)
mp.ylabel('Signal', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(times[:178], noised_sigs[:178],
        c='orangered', label='Noised')
mp.legend()

mp.subplot(222)
mp.title('Frequency Domain', fontsize=16)
mp.ylabel('Power', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.semilogy(freqs[freqs >= 0],
            noised_pows[freqs >= 0],
            c='limegreen', label='Noised')
mp.legend()

mp.subplot(223)
mp.title('Time', fontsize=16)
mp.ylabel('Signal', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(times[:178], filter_sigs[:178],
        c='hotpink', label='Filter')
mp.legend()

mp.subplot(224)
mp.title('Frequency', fontsize=16)
mp.ylabel('Power', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(freqs[freqs >= 0],
        filter_pows[freqs >= 0],
        c='dodgerblue', label='Filter')
mp.legend()

mp.tight_layout()
mp.show()
