import numpy as np
import time
import matplotlib.pyplot as plt

def boundary(L=512,N=100000,T=1000):
    #生成粒子的坐标
    x = np.random.randint(0, L, N,dtype=np.int32)
    y = np.random.randint(0, L, N,dtype=np.int32)
    #生成粒子的移动方向机选择上下左右四个方向之一
    moveDirections = np.array([[0,1],[0,-1],[1,0],[-1,0]],dtype=np.int32)
    # 中心区域
    centerMax = 3*L//4
    centerMin = L//4
    SimulationTime = time.time() 
    totalCenterT = 0
    for _ in range(T):
        dx, dy = np.take(moveDirections, np.random.randint(0,4,N), axis=0).T
       
        #周期性边界条件（即从右边界走出 = 从左边界进入）
        x += dx  
        y += dy
        x = np.where(x < 0, x + L, np.where(x >= L, x - L, x))
        y = np.where(y < 0, y + L, np.where(y >= L, y - L, y))
        #判断粒子是否在中心区域
        totalCenterT += ((x >= centerMin) & (x < centerMax) & (y >= centerMin) & (y < centerMax)).sum()
        
    
    totalT = N * T
    dwellRatiox = totalCenterT/totalT

    print(f"Average dwell ratiox: {dwellRatiox:.4f}")
    # 模拟时间
    print("Simulation time:",time.time()-SimulationTime)
    # map
    resultMap,_,_ = np.histogram2d(x,y,bins=L,range=[[0,L],[0,L]])
    # 可视化生成
    plt.figure(figsize=(10,10))
    plt.imshow(resultMap, cmap='viridis',extent=[0, L, 0, L], origin='lower')  # 使y轴从下到上递增显示更合理
    plt.colorbar(label='Reference') #增加颜色条 使显示更直观)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.savefig('map.png')

if __name__ == "__main__":
    boundary(L=512, N=100000, T=1000)  
