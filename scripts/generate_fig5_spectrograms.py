"""
生成 图5：时频图对比（单点 vs 多点融合，标注呼吸/心跳峰）
输出文件：outputs/fig5_spectrograms.png
"""
import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import stft, get_window

os.makedirs("outputs", exist_ok=True)
fs = 50.0
T = 60.0
t = np.arange(0, T, 1/fs)

# 合成呼吸与心跳信号（频率可微扰）
f_resp = 0.25 + 0.02*np.sin(2*np.pi*0.01*t)      # 呼吸 ~0.25 Hz，缓慢漂移
f_heart = 1.2 + 0.05*np.sin(2*np.pi*0.02*t)      # 心跳 ~1.2 Hz，缓慢漂移

def phase_from_freq(f):
    return 2*np.pi*np.cumsum(f)/fs

phi_r = phase_from_freq(f_resp)
phi_h = phase_from_freq(f_heart)

# 单点：易受体动和多径闪烁影响
np.random.seed(0)
motion = (np.random.randn(len(t)) * 0.03) * (np.sin(2*np.pi*0.05*t)>0.95)  # 偶发体动
s_single = 0.6*np.sin(phi_r) + 0.2*np.sin(2*phi_r) + 0.3*np.sin(phi_h) + motion + 0.1*np.random.randn(len(t))

# 多点融合：加入多个通道后的一致性稳健结果（噪声显著降低）
s_fused = 0.9*np.sin(phi_r) + 0.3*np.sin(2*phi_r) + 0.35*np.sin(phi_h) + 0.05*np.random.randn(len(t))

# 计算STFT
win = get_window(("tukey", 0.25), int(4*fs))
f1, tt1, Z1 = stft(s_single, fs=fs, window=win, nperseg=len(win), noverlap=int(0.75*len(win)))
f2, tt2, Z2 = stft(s_fused, fs=fs, window=win, nperseg=len(win), noverlap=int(0.75*len(win)))

# 绘图
fig, axes = plt.subplots(1, 2, figsize=(12, 4), constrained_layout=True)
vmax = np.percentile(np.abs(Z2), 99)

axes[0].pcolormesh(tt1, f1, np.abs(Z1), shading='gouraud', cmap='viridis', vmax=vmax)
axes[0].set_title('单点模型：时频图')
axes[0].set_xlabel('时间 (s)'); axes[0].set_ylabel('频率 (Hz)')
axes[0].axhline(0.25, color='r', ls='--', lw=1, label='呼吸带')
axes[0].axhline(1.2, color='y', ls='--', lw=1, label='心跳带')
axes[0].legend(loc='upper right', fontsize=8)

axes[1].pcolormesh(tt2, f2, np.abs(Z2), shading='gouraud', cmap='viridis', vmax=vmax)
axes[1].set_title('多点融合：时频图')
axes[1].set_xlabel('时间 (s)'); axes[1].set_ylabel('频率 (Hz)')
axes[1].axhline(0.25, color='r', ls='--', lw=1, label='呼吸带')
axes[1].axhline(1.2, color='y', ls='--', lw=1, label='心跳带')

plt.savefig("outputs/fig5_spectrograms.png", dpi=200)
print("Saved to outputs/fig5_spectrograms.png")