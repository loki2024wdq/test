'''递归算法'''

'''
递归就是有去（递去）有回（归来）。“有去”：递归问题必须可以分解为若干个规模较小，与原问题形式相同的子问题，这些问题有相同的逻辑；
“有回”: 这些问题的演化过程是一个从大到小，由近及远的过程，并且会有一个明确的终点(临界点)，一旦到达了这个临界点，就不用再往更小、更远的地方走下去。
最后，从这个临界点开始，原路返回到原点，原问题解决。
'''

'''
递归三大定律：
（1）递归算法必须要有结束条件（最小规模问题的直接解决）。会有 if...>..的判断语句来判断是否满足基本情况
（2）递归算法必须能改变状态向基本结束条件演进（减小问题规模）。问题规模逐渐减少
（3）递归算法必须调用自身（解决减小了规模的相同问题）。必须调用自身，也就是有重复的逻辑
'''

#1找零问题
def change_problem(coins_list, total_value):
    min_coins = total_value #初始化需要的硬币数量，最多需要total_value个1美元的硬币兑换
    #基本情况，如果最后需要兑换的金额刚好在coins_list里面，那么刚好兑换结束
    if total_value in coins_list:
        return 1
    else:
        #没有特殊的币值刚好能够兑换，那么依次遍历每个币值，哪种币值最少就用哪种币值兑换
        for coins in coins_list:
            if total_value > coins:
                #找到每种币值兑换需要的硬币数量，对该币值进行兑换后，后续还要对total_value - coins的金额进行兑换，所用的最少硬币数量为1+后续需要兑换total_value - coins的硬币数量，
                # 通过total_value - coins减少问题规模，直到满足基本条件
                current_coins_num = 1 + change_problem(coins_list, total_value - coins)
                #如果采用当前币值进行兑换所需的最少硬币数量比min_coins还少，那么更新min_coins
                if current_coins_num <= min_coins:
                    min_coins = current_coins_num

    return min_coins

min_coins = change_problem([1,5,10,25], 63)
print(f'min_coins:{min_coins}')

#2数列求和
#数列求和如 1+2+3+4+5+6 本身是一个大规模的问题，递归需要把它分解成小规模的问题，并且需要具备相同的逻辑结构：如分解成首个数+剩余数列的求和，直到剩余数列只有一个数时
#此时的求和就是它本身
def sum_list(a_list):
    #基本情况，剩余数列求和就只剩下它本身，它本身就是和
    if len(a_list) == 1:
        # print(f'a_list2:{a_list}')
        return a_list[0]
    else:
        return a_list[0] + sum_list(a_list[1:])
total_sum = sum_list([1,2,3,4,5,6])
print(f'递归求和:{total_sum}')

#3求阶乘
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
val = factorial(4)
print(f'阶乘为:{val}')

#4斐波那契数列
'''
斐波拉契数列，是这样的一个数列：0、1、1、2、3、5、8、13、21、......
斐波拉契数列的核心思想是:
从第三项起，每一项都等于前两项的和，即F(N) = F(N - 1) + F(N - 2) (N >= 2)
并且规定F(0) = 0，F(1) = 1
'''
#构造一个指定项数的斐波那契数列
def fib_list(n):
    #先把第n项的斐波那契数计算出来
    if n == 1 or n == 2:
        return 1
    else:
        return fib_list(n-1) + fib_list(n-2)
fibList = [0]
#打印出项数为10的斐波那契数列
n = 10
temp = 1
while temp < n:
    fibList.append(fib_list(temp))
    temp += 1
print(f'斐波那契数列为:{fibList}')

#4 绘制螺旋曲线
import turtle

my_turtle = turtle.Turtle()
my_win = turtle.Screen()

def draw_spiral(tur, line_len):

  if line_len > 0:#递归基本情况为line_len = 0
    my_turtle.forward(line_len)
    my_turtle.right(90)
    draw_spiral(tur, line_len - 1)

draw_spiral(my_turtle, 100)
my_win.exitonclick()

#5绘制二叉树
import turtle

my_tree = turtle.Turtle()
my_win = turtle.Screen()

def draw_tree(branch_length, t):
  if branch_length > 5:
    t.forward(branch_length)
    t.right(20)
    draw_tree(branch_length-20, t)
    t.left(40)
    draw_tree(branch_length-20, t)
    t.right(20)
    t.backward(branch_length)

my_tree.left(90)
my_tree.up() # 抬起尾巴
my_tree.backward(200)
my_tree.down() # 放下尾巴
my_tree.color('green')
draw_tree(100, my_tree)
my_win.exitonclick()