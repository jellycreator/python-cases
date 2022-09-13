import turtle
# https://docs.python.org/zh-cn/3/library/turtle.html?highlight=turtle#module-turtle
# 这里涉及的数学计算省略了,多角星的角数和内角互补度数的关系

# 窗口标题
turtle.title('多角星绘制')
# 画图
while True:
    # 前进距离像素
    turtle.forward(200)
    # 左转弯角度
    turtle.left(135)
    # 当与原点坐标距离小于1px时停笔
    if abs(turtle.pos()) < 1:
        break
# 窗口维持
turtle.mainloop()