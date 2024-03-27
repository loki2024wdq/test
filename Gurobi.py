# from gurobipy import *
#
# #创建模型
# m = Model('liner')
# m.Params.TimeLimit = 1
# #定义变量
# x = m.addVar(vtype = GRB.BINARY, name = 'x')
# y = m.addVar(vtype = GRB.BINARY, name = 'y')
# z = m.addVar(vtype = GRB.BINARY, name = 'z')
# #建立目标函数
# m.setObjective(x+y+2*z, GRB.MAXIMIZE)
# #增加约束条件
# m.addConstr(x+2*y+3*z<=4, 'c0')
# m.addConstr(x+y>=1, 'c1')
# #优化器
# m.optimize()
# #输出
# for v in m.getVars():
#     print(f'变量名:{v.varName},变量值:{v.x}')
# print(f'目标函数值:{m.objval}')

#求解MIP
# from gurobipy import *
# import numpy as np
#
# m = Model('MIP')
# m.Params.TimeLimit = 10
#
# N_i = 4
# N_j = 4
# x = m.addVars(N_i, N_j, vtype = GRB.BINARY, name = 'x')
# m.setObjective(sum(x[i, j] for i in range(N_i) for j in range(N_j)), GRB.MAXIMIZE)
#
#
# m.addConstrs((sum(x[i, j] for j in range(N_j)) <= 1 for i in range(N_i)), 'con1')
# m.addConstrs((sum(x[i, j] for i in range(N_i)) <= 1 for j in range(N_j)), 'con2')
#
# m.optimize()
# x_dp = [[0]* N_i for _ in range(N_j)]
# x_dp2 = np.zeros((N_i, N_j))
# print(f'x_dp:{x_dp}')
# print(f'x_dp2:{x_dp2}')
#
# for i in range(N_i):
#     for j in range(N_j):
#         x_dp2[i][j] = x[i, j].x
#
# print("x_dp2", x_dp2)

# from gurobipy import *
# import numpy as np
# import matplotlib.pyplot as plt
#
# m = Model()
# #输入VRP数据，客户点数量、横纵坐标轴
# n = 10
# rnd = np.random
# rnd.seed(1)
# xc = np.random.rand(n+1) * 100
# xy = np.random.rand(n+1) * 200
# print(xc)
# plt.plot(xc[0], xy[0], c = 'r', marker = 's')
# plt.scatter(xc, xy, c = 'b')
# plt.show()
#
# #设置运行时间限制
# # m.Params.TimeLimit = 20
#
# #定义集合
# N = list(range(1, n+1))#客户点集合
# V = list(range(0, n+1))#包含仓库点的所有客户点集合
# A = [(i, j) for i in V for j in V if i != j]#定义所有弧线
# # B = [(i, j) for i in N for j in N if i != j]#定义所有弧线
# C_ij = {(i, j) : np.hypot(xc[i] - xc[j], xy[i] - xy[j]) for i,j in A}
# Q_i = {i: np.random.randint(1, 10) for i in N}
# load = 50
#
# #定义变量
# x = m.addVars(A, vtype = GRB.BINARY) #A是变量的下标范围集合
# u = m.addVars(N, vtype = GRB.CONTINUOUS)
#
# #定义目标函数
# m.setObjective(quicksum(x[i,j] * C_ij[i, j] for i,j in A), GRB.MINIMIZE)
#
# #添加约束条件
# m.addConstrs(quicksum(x[i,j] for i in N if i != j) == 1 for j in V)
# m.addConstrs(quicksum(x[i,j] for i in V if i != j) == quicksum(x[j,i] for i in V if i != j) for j in N)
# m.addConstrs(u[i] <= load for i in N)
# m.addConstrs(u[i] >= Q_i[i] for i in N)
# m.addConstrs(u[j] <= u[i] - Q_i[i] * x[i,j] + load * (1 - x[i,j]) for i in N for j in N if i != j)#只能用<=,>=或==，而不能使用<,>或=
#
# #优化模型
# m.optimize()
#
# #输出结果
# print(f'最优解:{m.ObjVal}')
# result = [a for a in A if x[a].x > 0.9]
# for index,(i,j) in enumerate(result):#索引:数值，先索引
#     plt.plot([xc[i], xc[j]], [xy[i], xy[j]], c = 'r')
# plt.plot(xc[0], xy[0], c = 'b', marker = 's')
# plt.scatter(xc, xy, c = 'y')

'''Gurobi求解VRPTW'''
from gurobipy import *
import csv

def readCsvFile(node_file, link_file):

    #定义集合
    # C = []#客户点集合
    V = []#所有节点的集合，包括depot
    S_i = {}#服务时间的集合
    Q_i = {}#demend集合
    start_time = {}#开始的时间窗
    end_time = {}#结束的时间窗
    with open(node_file, 'r') as f:
        CsvData = csv.DictReader(f)
        for row in CsvData:
            # print(f'row:{row}')
            node_id = row['id']
            node_demand = float(row['demand'])
            node_service = float(row['service_time'])
            node_start = float(row['start_time'])
            node_end = float(row['end_time'])
            V.append(node_id)
            # if node_id != 0:
            #     C.append(node_id)
            # print(f'C:{C}')
            Q_i[node_id] = node_demand
            S_i[node_id] = node_service
            start_time[node_id] = node_start
            end_time[node_id] = node_end

    Travel_Time = {}#定义旅行时间
    Cost_ij = {}
    with open(link_file, 'r') as f:
        CsvData = csv.DictReader(f)
        for row in CsvData:
            from_node = row['from_node_id']
            to_node  = row['to_node_id']
            Travel_Time[from_node, to_node] = float(row['travel_time'])
            Cost_ij[from_node, to_node] = float(row['link_cost'])


    # print(f'V:{V}')
    # V = tuplelist(V)
    # print(f'V2:{V}')
    # print(f'S_i:{S_i}')
    return  V, S_i, Q_i, start_time, end_time, Travel_Time, Cost_ij

def VRPTW_model( V, S_i, Q_i, start_time, end_time, Travel_Time, Cost_ij, K, Q_load):

    C = V[1:]
    depot = V[0]
    #建立模型
    m = Model('VRPTW')
    M = 1000
    #定义决策变量
    x = m.addVars(V,V,K,vtype = GRB.BINARY, name = 'x[i,j,k]')
    # print(x)
    a = m.addVars(V, K, vtype = GRB.CONTINUOUS, name = 'a[i,k]')
    #定义目标函数
    m.setObjective(quicksum(x[i,j,k] * Cost_ij[i,j] for i in V for j in V for k in K if i != j), GRB.MINIMIZE)
    #添加约束条件,quicksum(x[0,j,k] for j in C)相当于x0jk求和 = ∑x0jk
    #约束1：每辆车只从仓库出去1次
    m.addConstrs(quicksum(x[depot,j,k] for j in V) == 1 for k in K)
    #约束2：流量守恒约束
    m.addConstrs(quicksum(x[i,j,k] for i in V if i != j) == quicksum(x[j,i,k] for i in V if i != j) for j in C for k in K)
    #约束3：每辆车回到仓库
    m.addConstrs(quicksum(x[i,depot,k] for i in V) == 1 for k in K)
    #约束4：保证每个客户点被服务1次
    m.addConstrs(quicksum(x[i,j,k] for j in V for k in K ) == 1 for i in C)
    #约束5：服务时间关系
    m.addConstrs(a[i,k] + S_i[i] + Travel_Time[i,j] - M * (1-x[i,j,k]) <= a[j,k] for i in C for j in C for k in K if i != j)
    #约束6：时间窗约束
    m.addConstrs(start_time[i] <= a[i,k] for i in V for k in K)
    m.addConstrs(a[i,k] <= end_time[i] for i in V for k in K)
    #约束7：负载约束
    m.addConstrs(quicksum(x[i,j,k] * Q_i[i] for i in C for j in V if i!=j )<= Q_load for i in C  for k in K )

    "设置求解时间限制"
    m.Params.TimeLimit = 300
    "求解"
    m.optimize()

    "判断状态+输出结果"
    if m.status == GRB.Status.OPTIMAL or m.status == GRB.Status.TIME_LIMIT:
        for i in V:
            for j in V:
                for k in K:
                    if x[i,j,k].x > 0.9:
                        print('yes')
                        # print("决策变量值:",x[i,j,k])
    else:
        print('no solution')


node_file = 'C://Users//86137//Desktop//VRPTW+Gurobi//dataset//VRPTW//node_for_gurobi.csv'
link_file = 'C://Users//86137//Desktop//VRPTW+Gurobi//dataset//VRPTW//link_for_gurobi.csv'
V, S_i, Q_i, start_time, end_time, Travel_Time, Cost_ij = readCsvFile(node_file, link_file)
K = list(range(1,16))
VRPTW_model(V, S_i, Q_i, start_time, end_time, Travel_Time, Cost_ij, K, Q_load = 80)








