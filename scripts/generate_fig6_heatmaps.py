"""
生成 图6：注意力热图与角–距能量随时间漂移图（合成示例）
输出文件：outputs/fig6_heatmaps.png
"""
import os
import numpy as np
import matplotlib.pyplot as plt

os.makedirs("outputs", exist_ok=True)
np.random.seed(1)

# 合成角-距能量(随时间缓慢漂移)
T = 60
angles = np.linspace(-60, 60, 41)
ranges = np.linspace(0.5, 4.0, 36)
A = len(angles); R = len(ranges)

# 时间上的主峰漂移轨迹
theta_traj = np.linspace(-10, 10, T)
range_traj = np.linspace(2.0, 2.6, T)

energy_series = np.zeros((T, A, R))
for t in range(T):
    mu_a = np.argmin(np.abs(angles - theta_traj[t]))
    mu_r = np.argmin(np.abs(ranges - range_traj[t]))
    ga = np.exp(-0.5*((np.arange(A)-mu_a)/3)**2)
    gr = np.exp(-0.5*((np.arange(R)-mu_r)/2)**2)
    energy_series[t] = np.outer(ga, gr) + 0.05*np.random.randn(A, R)

# 合成通道注意力(质量引导)
C = 12
attn = np.abs(np.random.randn(T, C))
attn = attn / (attn.sum(axis=1, keepdims=True) + 1e-8)

# 绘图
fig, axes = plt.subplots(1, 2, figsize=(12, 4), constrained_layout=True)

# 左：角-距能量随时间漂移（展示某几个时间切片）
axes[0].imshow(energy_series[20].T, aspect='auto',
               extent=[angles[0], angles[-1], ranges[0], ranges[-1]],
               origin='lower', cmap='magma')
axes[0].set_title('角-距能量(示例切片, t=20)')
axes[0].set_xlabel('角度(度)'); axes[0].set_ylabel('距离(m)')

# 右：通道注意力热图(时间×通道)
im = axes[1].imshow(attn.T, aspect='auto', cmap='YlGnBu', origin='lower')
axes[1].set_title('通道注意力(质量引导) 热图')
axes[1].set_xlabel('时间步'); axes[1].set_ylabel('通道索引')
fig.colorbar(im, ax=axes[1], fraction=0.046, pad=0.04)

plt.savefig("outputs/fig6_heatmaps.png", dpi=200)
print("Saved to outputs/fig6_heatmaps.png")