# 生成数值型图的脚本说明

## 依赖
- Python 3.9+
- numpy, scipy, matplotlib

可用如下命令安装：
```
pip install -r requirements.txt
```

## 运行方式
- 图5（时频图对比）：
```
python scripts/generate_fig5_spectrograms.py
```

- 图6（注意力热图）：
```
python scripts/generate_fig6_heatmaps.py
```

- 图7（Bland-Altman一致性图）：
```
python scripts/generate_fig7_bland_altman.py
```

- 图8（失败案例可视化）：
```
python scripts/generate_fig8_failure_cases.py
```

## 输出
所有生成的图像保存在 `outputs/` 目录下，以PNG格式输出，分辨率为200 DPI。

## 说明
这些脚本生成合成的示例数据用于可视化，展示了：
- 单点vs多点融合的时频图对比
- 角-距能量分布与通道注意力热图  
- Bland-Altman一致性分析图
- 典型失败案例（体动、低SNR、多径闪烁）的信号特征