'''DP:动态规划'''
'''
动态规划本质是将原问题划分为子问题，子问题之间不是相互独立而是相互联系的，
因此，如果之前已经计算过某个子问题后，不需要再重复计算，如1+1+1+1=4，1+1+1+1+1=5，
是在4的基础上+1=5，也就是状态转移，通常用f(n) = f(n-1) + f(n-2)来表示
'''

'''
动态规划求的解是否一定是最优解？——如果问题具有最优子结构和重叠子问题性质，那么动态规划通常可以得到最优解。
最优子结构指的是原问题的最优解可以通过子问题的最优解来计算得到，而重叠子问题指的是在解决问题时需要多次计算相同的子问题。
'''
#矩阵行列
a= [[1,2,3],[2,3,4]]
print(len(a))#默认为行，即最大的列表里的元素个数，有两个元素[1,2,3]和[2,3,4]
print(len(a[0]))#为列，即[1,2,3]的长度

#1网格问题1,有一个m*n规格的网格，每次只能向下或向右走，从左上角走到右下角，问共有多少路径可以走？
def find_route(m, n):
    path_martrix = [[1 for i in range(m)]for j in range(n)]
    print(f'path_martrix:{path_martrix}')
    for line in range(1, m):
        for col in range(1, n):
            path_martrix[line][col] = path_martrix[line-1][col] + path_martrix[line][col-1]
    return path_martrix[m-1][n-1]
route_nums = find_route(3, 3)
print(f'route_nums:{route_nums}')


#2网格问题2,有一个m*n规格的网格，每次只能向下或向右走，从左上角走到右下角，每个格子里都存放一定数量的苹果，最多能拾取多少苹果？
def most_apple(in_matrix):
    #读取矩阵行列
    m = len(in_matrix)
    n = len(in_matrix[0])
    #对于处于边界位置的地方，计算累积路径
    for i in range(1, m):
        in_matrix[0][i] += in_matrix[0][i-1]
    for j in range(1, n):
        in_matrix[j][0] += in_matrix[j-1][0]
    #对于处于非边界位置的地方，计算累积路径=min（a, b) + 本身
    for x in range(1, m):
        for y in range(1, n):
            in_matrix[x][y] += max(in_matrix[x-1][y], in_matrix[x][y-1])
    print(f'最小路径:{in_matrix[-1][-1]}')
    print(in_matrix)

    return in_matrix[-1][-1], in_matrix

matrix = [[1,2,3],[3,2,1],[1,1,1]]
most_apple(matrix)

#3跳台阶问题：共有n阶台阶，每次只能跳1阶或2阶，有多少种跳法？
def up(n):
    L= []
    L.append(1)
    L.append(2)
    for i in range(2, n):
        L.append(L[i-1] + L[i-2])
    print(L[n-1])
    return L[n-1]
up_nums = up(5)

#4背包问题——0/1背包问题：每个物品要么放入要么不放，不能部分放入；关键在于[i][j]，当背包容量比现在想要放置的物品容量大时，判断是否需要
#换置之前那个物品
def bagpack(capacity, weights, values):
    dp = [[0]*(capacity+1) for _ in range(len(weights)+1)]
    print(dp)
    for i in range(1, len(weights)+1):
        for j in range(1, capacity+1):
            if j < weights[i-1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-weights[i-1]]+values[i-1])#可以把dp[i-1][j-weights[i-1]]理解为放入weights[i-1]的前一个状态的价值

    w, v = capacity, dp[len(weights)][capacity]
    selected = []
    for i in range(len(weights), 0, -1):
        if dp[i][w] != dp[i][w-1]:
            selected.append(i)
            w -= weights[i-1]#注意dp其实是多加了一列0边界，weights[i-1]就对应着dp[i]

    return dp[len(weights)][capacity], selected[::-1]#序列[开始:结束:步长],::-1意味着反转序列

capacity = 3
weights = [1, 2, 1]
values = [3, 1, 1]
max_values, selected = bagpack(capacity, weights, values)
print(f'最大价值为:{max_values}')
print(f'所选的物品为:{selected}')


#5最长递增子序列，如[1,4,3,1,3,5]的最长递增子序列为[1,3,5]长度为3
def LIS(nums):
    #每个dp列表均储存每个子问题的最优解，DP就是要用到dp[i]，即上一个子问题的最优解求解全局最优
    dp = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            #遍历i前面的元素，看j是否能接在i后面
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j]+1)#这里的dp[j]其实就是相对于dp[i]之前的一个子问题的最优解

    return max(dp)
nums = [6, 10, 9, 2, 3, 6, 10, 661, 66]
length = LIS(nums)
print(f'最长子序列长度:{length}')


#6找零问题：首先，假设有两种零钱[3,5]如果用这两种零钱去找零4，那么是不存在这样的找零方案的，也就是无解，其次，要找零11
#那么它可以由11-3=8或者11-5=6两个子问题再加1得到，即L[11]=L[8]+1或L[11] = L[6]+1，如果找零金额是value，零钱金额是coins，则L[valus] = L[values - coins] + 1
def find_coins(total_value, coins_list):
    #初始化dp列表,' '与" "的作用是一样的，但是注意，如果只是单纯的引号，那么它是字符串，需要加上float才能转变为无穷大
    dp = [float('inf')] * (total_value + 1)
    dp[0] = 0

    #数组dp用来储存每个子问题的最优解，需要对数组进行遍历，这种dp问题一般都涉及两个循环嵌套
    for item in range(1, total_value+1):
        for coins in coins_list:
            if item >= coins:
                dp[item] = min(dp[item], dp[item-coins]+1)#状态转移

    return dp[-1] if dp[-1] != float('inf') else -1

total_value = 22
coins_list = [3, 5]
coins_num = find_coins(total_value, coins_list)
print(f'最少硬币数量:{coins_num}')
