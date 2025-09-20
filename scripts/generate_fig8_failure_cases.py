"""
生成 图8：失败案例与误差来源可视化（合成示例）
输出文件：outputs/fig8_failure_cases.png
"""
import os
import numpy as np
import matplotlib.pyplot as plt

os.makedirs("outputs", exist_ok=True)
np.random.seed(3)

fs = 50.0
T = 40.0
t = np.arange(0, T, 1/fs)

def synth_signal(motion=False, low_snr=False):
    f_resp = 0.28; f_heart = 1.1
    s = 0.8*np.sin(2*np.pi*f_resp*t) + 0.3*np.sin(2*np.pi*f_heart*t)
    if motion:
        s += (np.random.randn(len(t))*0.06) * (np.sin(2*np.pi*0.1*t)>0.9)
    if low_snr:
        s += 0.3*np.random.randn(len(t))
    return s

cases = [
    ('体动污染', synth_signal(motion=True, low_snr=False)),
    ('强遮挡/低SNR', synth_signal(motion=False, low_snr=True)),
    ('多径闪烁', synth_signal(motion=False, low_snr=False) + 0.1*np.sin(2*np.pi*0.4*t + 3*np.sin(2*np.pi*0.03*t)))
]

fig, axes = plt.subplots(3, 1, figsize=(10,6), sharex=True)
for ax, (title, sig) in zip(axes, cases):
    ax.plot(t, sig, lw=0.8)
    ax.set_title(title)
    ax.grid(alpha=0.3)
axes[-1].set_xlabel('时间 (s)')
plt.tight_layout()
plt.savefig("outputs/fig8_failure_cases.png", dpi=200)
print("Saved to outputs/fig8_failure_cases.png")