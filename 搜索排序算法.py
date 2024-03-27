'搜索排序算法'
'''
注意：
def c(list):
    i = 0
    while i < 5:
        if i == 2:
            return list     #return list后，程序就没有继续往下运行了
        i += 1
        print(f'i:{i}')
    return 'yes'
list = [1,2]
b = c(list)
print(b)
'''


'''
二分搜索:顺序排序的基础下，每次从列表中间位置进行搜索，如果要搜索的元素大于中间的元素，
那么直接舍弃列表左边部分，同理，如果要搜索的元素小于中间的，直接舍弃右边的部分，之后每次
搜索列表中间部分，时间复杂度为O(logn)
'''

#1 二分搜索实现
def binary_serach(a_list, iteam):
    first = 0
    last = len(a_list) - 1

    while first <= last:
        mid_index = (first + last) // 2
        if a_list[mid_index] == iteam:
            return True
        elif a_list[mid_index] < iteam:#注意如果列表里包含str的话，str不能和int进行比较
            first = mid_index + 1
        else:
            last = mid_index - 1

    return False

a_list = [1,2,11,7,8,9,10]
a_list.sort()
print(a_list)
print(binary_serach(a_list,11))

#2 二分搜索递归版
def binary_search(a_list, iteam):
    if len(a_list) == 0:
        return False

    mid_index = len(a_list) // 2
    if a_list[mid_index] == iteam:
        return True
    elif a_list[mid_index] > iteam:
        return binary_search(a_list[:mid_index], iteam)
    else:
        return binary_search(
            a_list[mid_index+1:], iteam
        )

a_list = [1,2,11,7,8,9,10]
a_list.sort()
print(a_list)
print(binary_search(a_list,11))

'''
排序算法：
1.冒泡排序：每次比较两个相邻的元素，然后如果值比较大就交换两个值，在最终的顺序确定前需要进行很多多余的交换操作，时间复杂度为n2
2.选择排序：每次遍历选择其中值最大或最小的元素，将最大或最小的元素放在相邻的位置，时间复杂度为n2
3.插入排序：从左边开始看成一个顺序子序列，将后面的元素插入到子序列，时间复杂度为n2
4.希尔排序：将列表按一定的步长分成多个子列表，针对每个子列表都采用插入排序，慢慢减少步长，直到步长为1，合成一个列表，假设原始
列表为[1,7,2,3,6,5],如果步长为2，则划分为三个列表：[1,3],[7,6],[2,5]，注意这里的列表划分方式比较独特，再分别对每个子列表插入排序
5.归并排序：采用分而治之的思想，递归排序
6.快速排序：(1)选择一个基准，如第一个值。(2)从右往左找，如果找到的数比基准小，则交换位置。(3)从左往右找，如果找到的数比基准大，则交换位置，直到基准到达中间位置，对列表进行了分区。
(4)递归得采用快速排序分别对子列表进行排列。
'''

#1 冒泡排序
def bubble_insert(a_list):
    #每次迭代一轮都能确定能够将最大的值移动到列表的最后一项
    for i in range(len(a_list) - 1, 0, -1):
        for j in range(i):
            if a_list[j] > a_list[j+1]:
                #如果列表前面的值比后面的值大，那么交换两者的顺序
                a_list[j], a_list[j+1] = (
                    a_list[j+1], a_list[j]
                )
    return a_list
a_list = [1,3,2,5,4]
b = bubble_insert(a_list)
print(f'排序后的顺序:{b}')

#2选择排序
def select_insert(a_list):
    for i in range(len(a_list) - 1, 0, -1):
        min_idx = i
        #找到列表里的最大值
        for j in range(i):
            if a_list[j] > a_list[min_idx]:
                min_idx = j
        #每轮只交换一次，把最大值放在列表的最后位置
        a_list[i], a_list[min_idx] = (
            a_list[min_idx], a_list[i]
        )
    return a_list

a_list = [1,3,2,5,4]
b = select_insert(a_list)
print(f'排序后的顺序:{b}')

#3 插入排序
def insert_insert(a_list):
    #这里是从1开始，因为列表0处就是一个顺序子序列，之后也一直是一个顺序子序列
    for i in range(1,len(a_list)):
        cus_pos = i
        cus_val = a_list[i]
        #如果前一个位置的元素比cus_pos还要大的话，就将前一个元素往后移
        while (
            cus_pos > 0 and cus_val < a_list[cus_pos - 1]
        ):
            a_list[cus_pos] = a_list[cus_pos - 1]
            cus_pos -= 1
        a_list[cus_pos] = cus_val
    return a_list

a_list = [1,3,2,5,4]
b = insert_insert(a_list)
print(f'排序后的顺序:{b}')

#4 希尔排序
def shell_insert(a_string):
    n = len(a_string)
    #设定初始步长
    dist = n // 2#假设n=16，那么初始步长为8

    while dist > 0:
        for i in range(dist,n):
            j = i
            #采用插入排序，对子列表进行排序
            while (
                j> dist and a_list[j-dist] > a_list[j]
            ):
                a_list[j-dist], a_list[j] = a_list[j], a_list[j-dist]
                j -= dist
        #更新步长，逐渐缩小步长
        dist = dist // 2
    return a_list

a_list = [1,3,2,5,4]
b = shell_insert(a_list)
print(f'排序后的顺序:{b}')

#5.1 归并排序
def merge_sort(lists):
    # 递归结束条件
    #递归分为子调用和父调用，如[2,6,10]调用递归函数后，产生[2]，那么[2,6,10]调用递归函数是调用[2]的父调用，[2]调用为子调用
    #当子调用结束后，会回归父调用，继续执行父调用之后的程序
    if len(lists) <= 1:#判断分割结束的标志
        return lists

    # 分治进行递归,子调用分割，每次分割到基本情况时，分割结束，即子调用结束，之后继续分别执行各个子调用的父调用
    middle = len(lists) // 2#分割线
    left = merge_sort(lists[:middle])#左边分割
    right = merge_sort(lists[middle:])#右边分割

    # 子调用分割结束后，进行父调用，将两个有序数组进行合并，这块的代码直接针对最小模块进行分析编写，别被其他东西给影响
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # 将未被扫描到的元素直接追加到result后面，比如，左边的是[1]，右边的是[2,3]，左右两边不相等，还有一个没有被扫描
    if i == len(left):
        result.extend(right[j:])
    else:
        result.extend(left[i:])

    print(f'result: {result}')
    return result

if __name__ == "__main__":
    a = [2, 6, 10, 3, 5, 8, 4]
    print(merge_sort(a))

#5.2 归并排序/递归清晰版
def merge(a, b):#合并
    c = []
    h = j = 0
    while j < len(a) and h < len(b):
        if a[j] < b[h]:
            c.append(a[j])
            j += 1
        else:
            c.append(b[h])
            h += 1
    if j == len(a):
        for i in b[h:]:
            c.append(i)
    else:
        for i in a[j:]:
            c.append(i)
    return c

def merge_sort(lists):
    if len(lists) <= 1:
        return lists
    #分治
    middle = len(lists) // 2
    left = merge_sort(lists[:middle])
    right = merge_sort(lists[middle:])

    return merge(left, right)#最终返回合并

if __name__ == '__main__':
    a = [14, 2, 34, 43, 21, 19]
    print(merge_sort(a))

#6 快速排序
def partition(a_list,low,high):
    i = low
    j = high
    pivot = a_list[low]

    while i < j:
        #从右往左数，如果右边的大于基准才是正常
        while i < j and a_list[j] >= pivot:
            j -= 1
        #否则交换两者位置
        a_list[i] = a_list[j]
        #从左往右数，如果左边的小于右边的才是正常
        while i < j and a_list[i] <= pivot:
            i += 1
        #否则交换两者位置
        a_list[j] = a_list[i]

    #将基准值放在正确的位置
    a_list[i] = pivot
    #返回基准值正确位置的索引
    return i

def quick_sort(a_list,low,high):
    if low < high:
        pi = partition(a_list,low,high)
        quick_sort(a_list,low,pi-1)
        quick_sort(a_list,pi+1,high)
    return a_list

if __name__ == "__main__":
    a = [2, 6, 10, 3, 5, 8, 4]
    print(quick_sort(a,0,len(a)-1))