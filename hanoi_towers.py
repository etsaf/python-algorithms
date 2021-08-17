#show all optimal steps of how to move n discs from rod 1 to rod 3
#for each step print(i, j, h), where i is the number of the disk,
#j is the number of the rod it is taken from, h is the number of the rod it is placed on
def moveOne(ind, fromRod, toRod):
    print(ind, fromRod, toRod)


def moveTower(indfirst, indlast, height, fromRod, toRod, Rod):
    if height >= 1:
        moveTower(indfirst, indlast - 1, height - 1, fromRod, Rod, toRod)
        moveOne(indlast, fromRod, toRod)
        moveTower(indfirst, indlast - 1, height - 1, Rod, toRod, fromRod)


def move(n, x, y):
    moveTower(1, n, n, x, y, y - 1)


n = int(input())
move(n, 1, 3)