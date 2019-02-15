import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np

##########################################
# 1、使用Subplot多合一显示

# 定义绘制面板
plt.figure()
# 均匀多图合一
# 参数说明：图形窗口分为两行两列，当前位置为1
plt.subplot(2, 2, 1)
# 参数说明：x轴取值范围为[0,1]，y轴取值范围为[0,1]，将点[0,0]和[1,1]连起来成一条直线
plt.plot([0, 1], [0, 1])
plt.subplot(2, 2, 2)
plt.plot([0, 1], [0, 2])
# 223一样可以识别
plt.subplot(223)
plt.plot([0, 1], [0, 3])
plt.subplot(2, 2, 4)
plt.plot([0, 1], [0, 4])

# 不均匀多合一显示
plt.figure()
# 将整个图像窗口分为两行一列，当前位置为1
plt.subplot(2, 1, 1)
plt.plot([0, 1], [0, 1])
# 将整个图像窗口分为两行三列，当前位置为4，这里为什么是4，因为上面将图像分为两行一列，已经占了第一个位置即整一个第一行
# 这一步分为两行三列，于是整个图像窗口的第一行也就变成了三列，要想下图在第二行显示，必须把当前位置放在第四个位置才行
plt.subplot(2, 3, 4)
plt.plot([0, 1], [0, 2])
plt.subplot(2, 3, 5)
plt.plot([0, 1], [0, 3])
plt.subplot(2, 3, 6)
plt.plot([0, 1], [0, 4])


##########################################
# 2、使用subplot2grid分隔显示

# 定义绘制面板
plt.figure()
# 使用subplot2grid创建图，(3, 3)表示将整个图像窗口分成三行三列，(0, 0)表示从第0行第0列开始作图
# colspan=3表示列跨度为3
ax1 = plt.subplot2grid((3, 3), (0, 0), colspan=3)
ax1.plot([1, 2], [1, 2])
ax1.set_title('ax1_title')
# 使用subplot2grid创建图，(3, 3)表示将整个图像窗口分成三行三列，(1, 0)表示从第1行第0列开始作图
# colspan=2表示列跨度为2
ax2 = plt.subplot2grid((3, 3), (1, 0), colspan=2)
# 使用subplot2grid创建图，(3, 3)表示将整个图像窗口分成三行三列，(1, 2)表示从第1行第2列开始作图
# colspan=2表示行跨度为2
ax3 = plt.subplot2grid((3, 3), (1, 2), rowspan=2)
ax4 = plt.subplot2grid((3, 3), (2, 0))
ax5 = plt.subplot2grid((3, 3), (2, 1))
# 在ax4画散点
ax4.scatter([1, 2], [2, 2])
# 设置ax4的标签
ax4.set_xlabel('ax4_x')
ax4.set_ylabel('ax4_y')

##########################################
# 3、使用gridspec分隔显示

# 需要导入包：import matplotlib.gridspec as gridspec，已添加
# 定义绘制面板
plt.figure()
# 使用gridspec创建一个图像窗口，分为三行三列
gs = gridspec.GridSpec(3, 3)
# 使用subplot来作图
# gs[0, :]表示第0行和所有列；
# gs[1, :2]表示第1行和第2列之前的所有列
# gs[1:, 2]表示第1行以及第1行以后的所有行和第2列
# gs[-1, 0]表示最后一行和第0列
# gs[-1, -2]表示最后1行和倒数第2列
ax6 = plt.subplot(gs[0, :])
ax7 = plt.subplot(gs[1, :2])
ax8 = plt.subplot(gs[1:, 2])
ax9 = plt.subplot(gs[-1, 0])
ax10 = plt.subplot(gs[-1, -2])

##########################################
# 4、使用subuplots分隔显示

plt.figure()
# 使用plt.subplots建立一个2行2列的图像窗口，sharex=True, sharey=True表示共享x和y坐标
# ((ax11, ax12), (ax13, ax14))表示第1行从左至右依次放ax11和ax12, 第2行从左至右依次放ax13和ax14.
f, ((ax11, ax12), (ax13, ax14)) = plt.subplots(2, 2, sharex=True, sharey=True)
ax11.scatter([1, 2], [1, 2])
# 表示紧凑显示图像
plt.tight_layout()

##########################################
# 5、图中图显示

# 定义绘制面板
fig = plt.figure()
# 准备数据
x = [1, 2, 3, 4, 5, 6, 7]
y = [1, 3, 4, 2, 5, 8, 6]
# 大图绘制
# 设置大图左下角位置以及宽高
# 4个值都是占整个figure坐标系的百分比
# 假设figure的大小是10x10，那么大图就被包含在由(1, 1)开始，宽8，高8的坐标系内。
left, bottom, width, height = 0.1, 0.1, 0.8, 0.8
# 将大图坐标系添加到figure中，颜色为red，取名为title
ax15 = fig.add_axes([left, bottom, width, height])
ax15.plot(x, y, 'r')
ax15.set_xlabel('x')
ax15.set_ylabel('y')
ax15.set_title('title')
# 小图1绘制
left, bottom, width, height = 0.2, 0.6, 0.25, 0.25
ax16 = fig.add_axes([left, bottom, width, height])
ax16.plot(y, x, 'b')
ax16.set_xlabel('x')
ax16.set_ylabel('y')
ax16.set_title('title inside 1')
# 小图2绘制
# 可以直接添加坐标系，更简便
plt.axes([0.6, 0.2, 0.25, 0.25])
# 注意对y进行了逆序处理
plt.plot(y[::-1], x, 'g')
plt.xlabel('x')
plt.ylabel('y')
plt.title('title inside 2')

##########################################
# 6、主次坐标轴

# 定义绘制面板
plt.figure()
# 准备数据
# 在[0,10]中每隔0.1就取一个数据组成列表，0、0.1、0.2……9.9、10.0
x2 = np.arange(0, 10, 0.1)
# 两条直线 y2和y1是互相倒置的
y1 = 0.05*x2 ** 2
y2 = -1 * y1
# 获取figure默认的坐标系ax16，即第一个坐标系
fig, ax16 = plt.subplots()
# 第二个y坐标
# 对ax16调用twinx方法，生成如镜面效果后的ax17
ax17 = ax16.twinx()
# 绘图，绘制标签
ax16.plot(x2, y1, 'g-')   # green, solid line
ax16.set_xlabel('X data')
ax16.set_ylabel('Y1 data', color='g')
ax17.plot(x2, y2, 'b-')   # blue
ax17.set_ylabel('Y2 data', color='b')

# 显示
plt.show()