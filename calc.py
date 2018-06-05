#encoding:utf-8
# import numpy as np  
# import matplotlib.pyplot as plt  
import math
import sys
def linefit(x , y):
    N = float(len(x))
    sx,sy,sxx,syy,sxy=0,0,0,0,0
    for i in range(0,int(N)):
        sx  += x[i]
        sy  += y[i]
        sxx += x[i]*x[i]
        syy += y[i]*y[i]
        sxy += x[i]*y[i]
    a = (sy*sx/N -sxy)/( sx*sx/N -sxx)
    b = (sy - a*sx)/N
    r = abs(sy*sx/N-sxy)/math.sqrt((sxx-sx*sx/N)*(syy-sy*sy/N))
    return a,b,r

# 给水管道费用模型计算，返回值为(bi, ai, a, r)
def calc(X , Y) :
    N = len(X)
    M = 10
    da = 1.0 / (M - 1)
    result = ()
    minsumdt = sys.maxsize
    for la in xrange(0, M):
        a = 1 + la * da
        newX = map(lambda x : x ** a, X)
        bi,ai,r=linefit(newX,Y)
        sumdtdt = 0
        for n in xrange(0, N):
            cj = Y[n]
            D = X[n]
            Di = bi*(D ** a) + ai
            sumdtdt = sumdtdt + (cj - Di) * (cj - Di)
            if (minsumdt > sumdtdt):
                minsumdt = sumdtdt
                result = (bi, ai, a, r)
    return result


if __name__ == '__main__':
    # X=[ 1 ,2  ,3 ,4 ,5 ,6]
    # Y=[ 2.5 ,3.51 ,4.45 ,5.52 ,6.47 ,7.51]
    X=[200,250,300,350,400,450,500,600,700,800,900,1000,1100,1200]
    Y=[82.90,102.10,120.69,140.78,166.15,229.08,257.21,324.17,399.89,452.46,517.40,659.19,747.94,854.47]
    bi, ai, a, r= calc(X, Y)
    print(bi, ai, a)
    # newY = map(lambda x : bi *(x ** a) + ai, X)
    # plt.plot(X,Y,color='g',linestyle='',marker='o',label=u'raw') 
    # plt.plot(X,newY,color='b',linestyle='-',marker='',label=u'dst') 
    # # 把拟合的曲线在这里画出来
    # plt.legend(loc='upper left')
    # plt.show()

