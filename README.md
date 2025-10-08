# 随机游走模拟优化考核

## 考核简介

随机游走模型常在计算机领域用于研究系统动态，随着问题规模增大，如何提升模拟效率成为突破计算优化的关键。

本考核要求在 Ubuntu 22.04 环境下，对 L×L 网格上 N 个粒子进行 T 步随机游走模拟（L=512，N=100000，T=1000）。粒子随机选方向、允许多粒子同格、网格采用周期性边界。需用纯 Python 实现串行基线，并通过不限手段优化，缩短运行时间。最终输出粒子在中心区域平均停留比例与模拟时间，可视化可加分，考查并行计算与优化能力。

## 考核目标

本考核要求您在虚拟机中安装 Ubuntu 22.04 并配置，在 L×L 网格上模拟 N 个相互独立的粒子进行 T 步随机游走，统计所有粒子在中心区域的平均停留比例，并优化模拟速度。

## 考核题流程

### 1. 安装虚拟机
- 安装 Ubuntu 22.04 LTS
- 配置网络连接

### 2. 配置编程环境
- 选择合适版本的Python解释器（要求Python 3.8+）
- 安装必要的开发工具

### 3. 考核题场景

模拟规则：
- 每个粒子每步独立随机选择上下左右四个方向之一（等概率1/4）
- 允许多个粒子占据同一格子（无碰撞约束）
- 网格采用周期性边界条件（从边界走出会从对面边界进入）
- 中心区域定义为：x ∈ [L//4, 3*L//4) 且 y ∈ [L//4, 3*L//4)
- 粒子初始位置随机分布在整个L×L网格上
- 坐标范围：x, y ∈ [0, L-1]

### 4. 考核要求

#### 基础要求
- 用纯 Python 实现串行版本（baseline）
- 优化目标：固定 L=512, N=100000, T=1000，总运行时间最短
- 不限优化手段

#### 可选加分项
- **可视化**：绘制最终粒子分布热力图
- **深度优化**：展示多种优化思路和实现
- **性能分析**：详细的性能对比和分析

#### 核心能力考查
- 理解并行计算思想和优化理念
- 掌握Python性能优化技术

### 5. 优化方向建议

- **算法优化**：向量化计算、减少循环嵌套
- **数据结构优化**：选择合适的数据结构
- **并行计算**：多进程、多线程
- **编译优化**：Numba JIT、Cython
- **使用其他语言重写**：C/C++、Rust等
- **调用高速计算库**：NumPy、CuPy等

### 6. 输入输出格式

#### 输入
```bash
python simulate.py 512 100000 1000
#可以不严格遵守，你同样可以使用 bash 脚本来辅助运行
```

参数说明：
- `<L>`：网格边长（512）
- `<N>`：粒子数量（100000）
- `<T>`：模拟步数（1000）

#### 输出
```
Average dwell ratio: 0.2501
Simulation time: 2.34s
```

输出说明：
- **dwell ratio** = 所有粒子在中心区域的总步数 / (N × T)
- **Simulation time** = 模拟运行时间（秒）

### 7. 实验报告要求

本考核实验报告应应用 LaTeX 或 Markdown 语法撰写：

#### 报告内容要求
- **有图有真相**：希望你可视化的展示你的结果
- **行文流畅**：能正常的描述出你的整个探索过程
- **技术深度**：展示对优化技术的理解和应用

## 提交要求

### 必须提交
- **主程序**：`simulate.py` 或等效的可执行程序
- **基线实现**：纯Python串行版本
- **优化版本**：至少一个优化实现
- **实验报告**：PDF格式，包含算法说明、优化分析、性能对比
- **运行说明**：如何在Ubuntu 22.04环境下运行你的代码

### 可选提交
- 可视化结果图片
- 性能测试脚本
- requirements.txt（如使用第三方库）
- 其他辅助文件

## 参考资源

### Python优化相关
- [NumPy官方文档](https://numpy.org/doc/)
- [Numba用户手册](https://numba.pydata.org/)
- [Python性能优化指南](https://wiki.python.org/moin/PythonSpeed/PerformanceTips)

### 并行计算相关
- [Python多进程编程](https://docs.python.org/3/library/multiprocessing.html)
- [Python多线程编程](https://docs.python.org/3/library/threading.html)
- [joblib并行计算库](https://joblib.readthedocs.io/)

### 可视化相关
- [Matplotlib用户指南](https://matplotlib.org/stable/users/index.html)
- [Seaborn统计可视化](https://seaborn.pydata.org/)

### 性能分析工具
- [cProfile性能分析](https://docs.python.org/3/library/profile.html)
- [line_profiler逐行分析](https://github.com/pyutils/line_profiler)

## 常见问题

### Q: 可以使用第三方库吗？
A: 可以，但需要在requirements.txt中声明依赖。鼓励使用各种优化库和工具。

### Q: 必须在Ubuntu 22.04上运行吗？
A: 是的，这是考核环境要求。最终提交的代码需要能在Ubuntu 22.04上正常运行。

### Q: 如何验证结果的正确性？
A: 重点关注算法逻辑的正确性，dwell ratio的数值会因随机性有所不同，但应该在合理范围内。建议验证方法：
- 检查边界条件是否正确处理（周期性边界）
- 验证中心区域判断逻辑是否准确
- 测试小规模参数确保基本逻辑正确
- 对于标准参数(L=512, N=100000, T=1000)，dwell ratio通常在0.22-0.28范围内

### Q: 优化程度有上限吗？
A: 没有上限，鼓励大胆尝试各种优化手段，包括但不限于算法优化、并行计算、编译优化等。

## 快速开始

### 环境设置
```bash
# 克隆仓库
git clone https://github.com/THINKER-ONLY/2025-Autumn-2025-Perf-Opt-Challenge.git
cd 2025-Autumn-2025-Perf-Opt-Challenge

# 或手动安装依赖
pip install -r requirements.txt
```

## 项目结构

```
random-walk-optimization-exam/
├── README.md                 # 项目说明文档
├── LICENSE                   # 开源许可证
├── requirements.txt          # Python依赖
├── .gitignore               # Git忽略规则
├── src/                     # 源代码目录
    └── __init__.py          # Python包文件
```

## 联系方式

如有问题，请联系超算俱乐部：
- 邮箱: Zhengyang_Li@email.ncu.edu.cn
- QQ群: 95878716159

## 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

---

**祝各位同学在考核中取得优异成绩！展现你们的技术实力和创新能力！**