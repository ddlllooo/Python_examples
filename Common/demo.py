title = 1  # 用作标记L型骨牌编号
a = [[0] * 101 for _ in range(101)]  # 用以表示棋盘


def ChessBoard(tr, tc, dr, dc, size):
    global title
    global a
    if size == 1:
        return  # 递归出口

    s = size // 2
    t = title
    title += 1
    # 如果特殊点的位置在左上方
    if dr < tr + s and dc < tc + s:
        ChessBoard(tr, tc, dr, dc, s)
    else:
        # 填充其右下角格子
        a[tr + s - 1][tc + s - 1] = t
        ChessBoard(tr, tc, tr + s - 1, tc + s - 1, s)

    # 如果特殊点的位置在右上方
    if dr < tr + s and dc >= tc + s:
        ChessBoard(tr, tc + s, dr, dc, s)
    else:
        # 填充其左下角格子
        a[tr + s - 1][tc + s] = t
        ChessBoard(tr, tc + s, tr + s - 1, tc + s, s)

    # 如果特殊点的位置在左下方
    if dr >= tr + s and dc < tc + s:
        ChessBoard(tr + s, tc, dr, dc, s)
    else:
        # 填充其右上角格子
        a[tr + s][tc + s - 1] = t
        ChessBoard(tr + s, tc, tr + s, tc + s - 1, s)

    # 如果特殊点的位置在右下方
    if dr >= tr + s and dc >= tc + s:
        ChessBoard(tr + s, tc + s, dr, dc, s)
    else:
        # 填充其左上角格子
        a[tr + s][tc + s] = t
        ChessBoard(tr + s, tc + s, tr + s, tc + s, s)


def main():
    global a
    size = int(input("请输入棋盘大小："))
    # 初始化
    for i in range(size):
        for j in range(size):
            a[i][j] = 0

    x, y = map(int, input("特殊点所在位置为：").split())

    ChessBoard(0, 0, x - 1, y - 1, size)  # 因为chessBoard算法是从0行，0列开始算起的，所以对输入的x,y都进行自减操作

    # 输出棋盘
    for i in range(size):
        for j in range(size):
            print("%2d " % a[i][j], end='')
        print()


if __name__ == "__main__":
    main()
