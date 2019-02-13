import matplotlib.pyplot as plt  # 导入matplotlib
import numpy as np

plt.figure()  # 创建图形显示的窗口

# 定义函数点数
x = np.linspace(-3, 3, 50)  # 定义x：范围是(-3,3);个数是50.
y1 = 2*x + 1
y2 = x ** 2
# 在figure上绘制图像
l1, = plt.plot(x, y2, label='up')
# 在figure上绘制图像，并定义这条直线颜色为红色，线宽为1.0，线的样式为虚线
l2, = plt.plot(x, y1, label='down', color='red', linewidth=1.0, linestyle='--')

# 坐标的取值范围
plt.xlim((-1, 2),)
plt.ylim((-2, 3))

# 坐标的标签
plt.xlabel('i am x')
plt.ylabel('i am y')

# 设置坐标分辨率
new_ticks = np.linspace(-1, 2, 5)
print(new_ticks)
plt.xticks(new_ticks)
# 设置坐标轴上要显示的点和对应的文字
plt.yticks([-2, -1.8, -1, -1.22, 3], [r'$Really\ bad$', r'$bad$', r'$normal$', r'$good$', r'$really\ good$'])

# 获得现在的坐标轴，并把右边和上边的边去掉
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# 设置坐标轴起点位置 所有位置：top，bottom，both，default，none
# 第一句是把刻度数字或名称设置在x坐标轴线的底部
# 第二句是把x坐标轴线设置到y轴的0刻度上
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
# 第一句是把刻度数字或名称设置在x坐标轴线的左边
# 第二句是把x坐标轴线设置到x轴的0刻度上
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))

# 打印图例
# 直接打印，请读者自己尝试
# plt.legend()
# 带参数的，handles传入线段，labels传入图例信息，loc:把图例显示在最好的位置
plt.legend(handles=[l1, l2], labels=['aaa', 'bbb'], loc='best')

# 显示某一个点
x0 = 0.5
y0 = 2*x0+1
# 这个函数就是专门描述散点图的
# 其中s代表点的大小，r代表红色（b代表蓝色）
plt.scatter(x0, y0, s=50, color='r')
# 第一个参数和第二个参数分别是x和y的取值范围，能够生成一条线，‘k--’代表的是黑色的虚线，lw代表线宽
plt.plot([x0, x0], [y0, 0], 'k--', lw=2.5)

# 添加注释 有两种方法
# method 1
# $$代表的是一种字体，xy=(x0,y0)即需要注释的坐标，xycoords基于数据的值来选注释位置
# xytext在原本数据的基础上x0+30，y0-30，得到注释位置，fontsize设置字体大小，arrowprops是箭头的设置
plt.annotate(r'$2x+1=%s$' % y0, xy=(x0, y0), xycoords='data', xytext=(+30, -30),
             textcoords='offset points', fontsize=16,
             arrowprops=dict(arrowstyle='->', connectionstyle="arc3,rad=.2"))

# method 2
# 第一个参数和第二个参数代表显示的x和y轴的位置，然后是文本、字体设置
plt.text(-1, 1, r'$This\ is\ the\ some\ text$', fontdict={'size': 16, 'color': 'r'})

# 显示窗口
plt.show()