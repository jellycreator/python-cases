matrix = [
    [[' '], [' '], [' ']],
    [[' '], [' '], [' ']],
    [[' '], [' '], [' ']]
]
count = 0
while True:
    for i in matrix:
        for j in i:
            print(j, end='')
        print()
    if count == 0:
        player_x = input('请输入x(横列):')
        player = 'x'
        matrix[int(player_x[0])-1][int(player_x[1])-1] = ['x']
        count = 1
    elif count == 1:
        player_o = input('请输入o(横列):')
        player = 'o'
        matrix[int(player_o[0])-1][int(player_o[1])-1] = ['o']
        count = 0

    # 第一行
    if (matrix[0][0] == matrix[0][1] == matrix[0][2] == ['x']) or (matrix[0][0] == matrix[0][1] == matrix[0][2] == ['o']):
        print('%s玩家赢了' % player)
        break
    # 第二行
    elif (matrix[1][0] == matrix[1][1] == matrix[1][2] == ['x']) or (matrix[1][0] == matrix[1][1] == matrix[1][2] == ['o']):
        print('%s玩家赢了' % player)
        break
    # 第三行
    elif (matrix[2][0] == matrix[2][1] == matrix[2][2] == ['x']) or (matrix[2][0] == matrix[2][1] == matrix[2][2] == ['o']):
        print('%s玩家赢了' % player)
        break
    # 第一列
    elif (matrix[0][0] == matrix[1][0] == matrix[2][0] == ['x']) or (matrix[0][0] == matrix[1][0] == matrix[2][0] == ['o']):
        print('%s玩家赢了' % player)
        break
    # 第二列
    elif (matrix[0][1] == matrix[1][1] == matrix[2][1] == ['x']) or (matrix[0][1] == matrix[1][1] == matrix[2][1] == ['o']):
        print('%s玩家赢了' % player)
        break
    # 第三列
    elif (matrix[0][2] == matrix[1][2] == matrix[2][2] == ['x']) or (matrix[0][2] == matrix[1][2] == matrix[2][2] == ['o']):
        print('%s玩家赢了' % player)
        break
    # 左上右下斜角
    elif (matrix[0][0] == matrix[1][1] == matrix[2][2] == ['x']) or (matrix[0][0] == matrix[1][1] == matrix[2][2] == ['o']):
        print('%s玩家赢了' % player)
        break
    # 左下右上斜角
    elif (matrix[2][0] == matrix[1][1] == matrix[0][2] == ['x']) or (matrix[2][0] == matrix[1][1] == matrix[0][2] == ['o']):
        print('%s玩家赢了' % player)
        break
    else:
        pass

