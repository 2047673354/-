"""
生成 图7：Bland–Altman 一致性图（合成示例）
输出文件：outputs/fig7_bland_altman.png
"""
import os
import numpy as np
import matplotlib.pyplot as plt

os.makedirs("outputs", exist_ok=True)
np.random.seed(2)

# 合成 RR 或 HR 标签与预测
n = 120
y_true = 12 + 2*np.sin(np.linspace(0, 3*np.pi, n))       # 比如 RR: 12±2
noise = np.random.randn(n)*0.4
bias = 0.2
y_pred = y_true + bias + noise

mean_vals = (y_true + y_pred)/2
diff_vals = y_pred - y_true
md = np.mean(diff_vals)
sd = np.std(diff_vals, ddof=1)
loa_upper = md + 1.96*sd
loa_lower = md - 1.96*sd

plt.figure(figsize=(6,4))
plt.scatter(mean_vals, diff_vals, c='tab:blue', s=20, alpha=0.7, label='样本')
plt.axhline(md, color='r', linestyle='--', label=f'均差={md:.2f}')
plt.axhline(loa_upper, color='g', linestyle='--', label=f'上限={loa_upper:.2f}')
plt.axhline(loa_lower, color='g', linestyle='--', label=f'下限={loa_lower:.2f}')
plt.xlabel('均值(预测与真实)'); plt.ylabel('差值(预测-真实)')
plt.title('Bland–Altman 一致性图(示例)')
plt.legend(fontsize=8)
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("outputs/fig7_bland_altman.png", dpi=200)
print("Saved to outputs/fig7_bland_altman.png")