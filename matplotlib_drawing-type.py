import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
#######################################
# 1、散点图：scatter

# 定义绘图面板
plt.figure()
# 生成1024个呈标准正态分布的二维数据组 (平均数是0，方差为1)
n = 1024
X1 = np.random.normal(0, 1, n)
Y = np.random.normal(0, 1, n)
# 每一点的颜色用T来表示
T = np.arctan2(Y, X1)
# 绘制图像 鼠标放上去会发现有很多参数提醒，可以选填其中的参数 ，下面的c代表颜色，alpha代表透明度
plt.scatter(X1, Y, c=T, alpha=5)
# x和y坐标轴显示的范围
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)
# 取消显示坐标轴数字
plt.xticks(())
plt.yticks(())
# 显示图像


#######################################
# 2、柱状图

# 定义绘图面板
plt.figure()
# X为0到11的整数，Y是均匀分布的随机数据
n = 12
X2 = np.arange(n)
Y1 = (1 - X2/float(n))*np.random.uniform(0.5, 1.0, n)
Y2 = (1 - X2/float(n))*np.random.uniform(0.5, 1.0, n)
# 柱形图的函数是plt.bar,以下生成两条柱形图，一上一下
# 基础版，直接采用默认颜色
# plt.bar(X2, +Y1)
# plt.bar(X2, -Y2)
# 加强版，配置了块颜色和边框颜色
plt.bar(X2, +Y1, facecolor='#9999ff', edgecolor='white')
plt.bar(X2, -Y2, facecolor='#ff9999', edgecolor='white')
# X的坐标轴范围为-5到12，Y的坐标轴范围为-1.25到1.25
plt.xlim(-.5, n)
plt.ylim(-1.25, 1.25)
# 去除X和Y坐标轴数值
plt.xticks(())
plt.yticks(())
# 下面这句话意思是把X2和Y1的每组数据赋值到x，y上，在这个基础上加减某数得到文本位置，保留两位小数，
for x, y in zip(X2, Y1):
    # ha: horizontal alignment
    # va: vertical alignment
    plt.text(x + 0.04, y + 0.05, '%.2f' % y, ha='center', va='bottom')
# 下面这句话意思是把X2和Y1的每组数据赋值到x，y上，在这个基础上加减某数得到文本位置，保留两位小数，
for x, y in zip(X2, Y2):
    # ha: horizontal alignment
    # va: vertical alignment
    plt.text(x + 0.04, -y - 0.05, '%.2f' % y, ha='center', va='top')


#######################################
# 3、等高线

# 定义绘制面板
plt.figure()
def f(x, y):
    # 高度函数
    return (1 - x/2 + x**5 + y**3)*np.exp(-x**2 - y**2)

n = 256
# x,y分别在区间[-3, 3]中均匀分布256个值
a = np.linspace(-3, 3, n)
b = np.linspace(-3, 3, n)
# 在二维平面中将每一个x和每一个y分别对应起来，编织成栅格
X3, Y3 = np.meshgrid(a, b)
# 使用函数plt.contourf把颜色加进去，位置参数：X3,Y3,f(X3,Y3);8指的是分层数量;alpha指透明度;cmap指的是暖色组，根据数值变更颜色
plt.contourf(X3, Y3, f(X3, Y3), 8, alpha=.75, cmap=plt.cm.hot)
# 使用函数plt.contour函数划线
C = plt.contour(X3, Y3, f(X3, Y3), 8, color='black', linewidth=.5)
# 添加高度数字，inline为True表示把字写在线内，fontsize指字体大小
plt.clabel(C, inline=True, fontsize=10)
# 去除坐标轴的值
plt.xticks(())
plt.yticks(())


#######################################
# 4、image图片的显示

# 定义绘制面板
plt.figure()
# 打印出的是纯粹的数字，而非自然图像，利用3X3的矩阵来表示点的颜色，每个点就是一个像素
pic = np.array([0.313660827978, 0.365348418405, 0.423733120134,
              0.365348418405, 0.439599930621, 0.525083754405,
              0.423733120134, 0.525083754405, 0.651536351379]).reshape(3, 3)
# 显示图片，参数分别是：出图方式、颜色组、选择原点的位置
# 其中，出图方式可以在这里看到：https://matplotlib.org/examples/images_contours_and_fields/interpolation_methods.html
# 我们采用的是最近邻插法
plt.imshow(pic, interpolation='nearest', cmap='bone', origin='lower')
# 颜色条形注释，将颜色条形注释的长度压缩成图像长度的0.92倍
plt.colorbar(shrink=.92)


#######################################
# 5、3D图形显示

# 3D绘图需要导入一个模块，即3D坐标轴的显示：from mpl_toolkits.mplot3d import Axes3D，上面已添加
# 定义绘制面板,并添加3D坐标轴
fig= plt.figure()
ax = Axes3D(fig)
# 给x和y进行复制，并将x和y编织成栅格
X4 = np.arange(-4, 4, 0.25)
Y4 = np.arange(-4, 4, 0.25)
# 把X4和Y4编织成栅格
X4, Y4 = np.meshgrid(X4, Y4)
# 使用这个函数得到每个点的高度
R = np.sqrt(X4 ** 2 + Y4 ** 2)
Z = np.sin(R)
# 参数：前三个是坐标信息;第四个第五个是网格面积跨度，读者可自行修改查看效果;第六个参数是颜色设置为彩虹色
ax.plot_surface(X4, Y4, Z, rstride=1, cstride=1, cmap='rainbow')
# 添加等高线，zdir = 'z' 说明把图形投影在xy平面上，同理，若 = 'x',则把图像投影在yz平面上;offset为-1.5说明投影的坐标轴为-1.5;最后一个参数是颜色
ax.contourf(X4, Y4, Z, zdir='z', offset=-1.5, cmap=plt.get_cmap('rainbow'))

# 显示图像
plt.show()
