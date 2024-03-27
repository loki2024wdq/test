class SomeOptimizationModel:
# ...类的其他部分和属性

def add_pipe_constraints(self):
        for (start_node, end_node, time) in self.data[DataName.PIPE_IS_OPEN_LABEL_LIST]:
            if (start_node, end_node) in self.data[DataName.DICT_PIPE_VOL_UB]:
                # 注意这里引用了特定键的变量
                pipe_is_open_var = self.vars[VarName.PIPE_IS_OPEN][(start_node, end_node, time)]
                pipe_vol_ub = self.data[DataName.DICT_PIPE_VOL_UB][(start_node, end_node)]
                pipe_qty_var = self.vars[VarName.PIPE_QTY][(start_node, end_node, time)]

                # 添加约束，管道流量小于等于管道开启状态乘以最大流量上界
                self.model.addConstr(
                    pipe_is_open_var * pipe_vol_ub >= pipe_qty_var,
                    name=f'pipe_vol_ub_{start_node}_{end_node}_{time}'
                )
# ...类的其他方法