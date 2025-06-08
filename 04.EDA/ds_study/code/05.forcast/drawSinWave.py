import matplotlib.pyplot as plt
import numpy as np

### 함수로 구현
def plotSinWave(**kwargs):

    ### 기본값 세팅
    amp=kwargs.get("amp",1)
    freq=kwargs.get("freq",1)
    endTime=kwargs.get("endTime",1)
    sampleTime=kwargs.get("sampleTime",0.01)
    startTime=kwargs.get("startTime",0)
    bias=kwargs.get("bias",0)
    figsize=kwargs.get("figsize",(12,8))

    time = np.arange(startTime, endTime, sampleTime)
    result = amp * np.sin(2 * np.pi * freq * time) + bias
    plt.figure(figsize=figsize)
    plt.plot(time, result)
    plt.grid(True)
    plt.xlabel('Time')
    plt.ylabel('sin')
    plt.title (str(amp) + ' * sin(2 * pi * ' + str(freq) + ' * t) + ' + str(bias))
    plt.show()

if __name__ == '__main__':
    print("Test Graph Drawing")
    plotSinWave(amp=1,endTime=2)
