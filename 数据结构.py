'''数据结构'''
'''
栈：后进先出，先进的在最低端，后进的在最上面，就和堆一堆书本一样，浏览器页面的前进和后退功能就是用的栈
队列：先进先出，添加操作在尾部，移除操作在头部，就和排队购买一样，排在前面的人买完东西就离开，后来的人排在队伍后面，用Queue表示，.enqueue()表示在队列后面添加元素，.dequeue()表示移除队列前面元素
双端队列：可以从队列的任意一端移除或添加新元素，用Deque表示，用.add_rear()/.add_front()分别在后面和前面添加元素，用.remove_rear()或.remove_front()分别表示在后面或前面移除元素
链表：无序，没有具体的位置信息，只有相对的位置信息
'''
#1 使用栈将十进制数转化为2进制数
from pythonds3.basic import Stack

def ten_to_two(number, basic):
    a_stack = Stack()
    while number > 0:
        a = number % basic #十进制数除以2取余
        number = number // basic #十进制数除以2取整
        a_stack.push(a)
    bin_string = ''
    while not a_stack.is_empty():
        bin_string = bin_string + str(a_stack.pop())
    return bin_string

number = 4583
basic = 2
print(f'二进制数为:{ten_to_two(number, basic)}')

#2 双端队列检测回文子串，如检测'acdca'是否是回文子串
from pythonds3.basic import Deque

def check_huiwen(a_string):
    a_deque = Deque()  #注意对于字符串"abdba"，也可以通过for i in 字符串的方式遍历字符串里的元素，和列表一样
    for i in a_string:
        print("i:",i)
        a_deque.add_rear(i)

    while a_deque.size() != 1:
        first = a_deque.remove_rear()
        second = a_deque.remove_front()
        if first != second:
            return False
    return True

a_string = 'adbcda'
print(check_huiwen(a_string))


