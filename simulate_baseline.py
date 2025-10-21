import time
import random

def boundary(L=512,N=100000,T=1000):
    #生成粒子的坐标
    x = [random.randint(0,L-1) for _ in range(N)]
    y = [random.randint(0,L-1) for _ in range(N)]
    #生成粒子的移动方向机选择上下左右四个方向之一
    moveDirections = [(0,1),(0,-1),(1,0),(-1,0)]
    # 中心区域
    centerMax = 3*L//4
    centerMin = L//4
    SimulationTime = time.time() 
    totalCenterT = 0
    for _ in range(T):
        for i in range(N):
            dx, dy = random.choice(moveDirections)
            x[i] += dx
            y[i] += dy
            #周期性边界条件（即从右边界走出 = 从左边界进入）
            x[i] %= L 
            y[i] %= L

        totalCenterTCount = 0
        for i in range(N):
            #判断粒子是否在中心区域
            if (centerMin <= x[i] < centerMax) and (centerMin <= y[i] < centerMax):
                totalCenterTCount += 1
        totalCenterT += totalCenterTCount
        
    totalT = N * T
    dwellRatiox = totalCenterT/totalT

    print(f"Average dwell ratiox: {dwellRatiox:.4f}")
    print("Simulation time:",time.time()-SimulationTime)
    
if __name__ == "__main__":
    boundary(L=512, N=100000, T=1000)  
