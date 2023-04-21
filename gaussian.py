import numpy as np #首先确保python安装了numpy包


def gauss(a, b):   #自己定义一个函数，自变量是a，b
    cout = 0           #定义计算次数
    m, n = a.shape   #矩阵a的行数和列数
    if ( m < n ):
        print("There is a 解空间。")#保证方程个数大于未知数个数
    else:
        l = np.zeros((n,n))
        for i in range(n):
            # 限制条件
            if (a[i][i] == 0):
                print("no answer")


        # j表示列
        for k in range(n - 1):          # k表示第一层循环，(0，n-1)行
            for i in range(k + 1, n):   # i表示第二层循环,(k+1,n)行,计算该行消元的系数
                l[i][k] = a[i][k] / a[k][k]     #计算l
                cout += 1               #计算次数加一
                for j in range(m):      # j表示列，对每一列进行运算
                    a[i][j] = a[i][j] - l[i][k] * a[k][j]
                    cout += 1
                b[i] = b[i] - l[i][k] * b[k]
        # 回代求出方程解
        x = np.zeros(n)                       #先将解赋值为零，再一一计算
        x[n - 1] = b[n - 1] / a[n - 1][n - 1] #先算最后一位的x解

        for i in range(n - 2, -1, -1):      #依次回代倒着算每一个解
            for j in range(i + 1, n):
                b[i] -= a[i][j] * x[j]       #自增自减
            x[i] = b[i] / a[i][i]
        for i in range(n):
            print("x" + str(i + 1) + " = ", x[i])
        print("x" " = ", x)
        print("计算次数", "=", cout)

#---------------以上是主程序，以下是输入程序

if __name__ == '__main__':      #当模块被直接运行时，以下代码块将被运行，当模块是被导入时，代码块不被运行。
    a = np.array([[4,1,0,0,2], [0,-1,2,0,3], [-2,2,1,0,5],[-2,3,4,1,4]])    #输入的系数矩阵
    b = np.array([6, -8, -1, -8])                                      #增广的一列矩阵
    gauss(a, b)                                                          #进行函数guassin运算


