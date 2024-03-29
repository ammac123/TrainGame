import operator
import random
from itertools import combinations_with_replacement, permutations
from ast import literal_eval

math_operators = {'+': operator.add, 
             '-': operator.sub,
             '*': operator.mul,
             '/': operator.truediv
             }

pre_dict = {'+':2,'-':2,'*':3,'/':3, '^':4}

class Node:
    def __init__(self, x, op, y=None):
        self.pre = pre_dict[op]
        self.op = op
        self.x,self.y = x,y
    
    def __str__(self):

        if self.y == None:
            return f'{self.op}({str(self.x)})'
        
        str_y = str(self.y)
        if self.y < self:
            str_y = f'( {str_y} )'

        str_x = str(self.x)
        str_op = self.op
        # if self.op in ['+','-'] and not isinstance(self.x, Node):
        #     str_x = str_x[1:]
        if self.x < self or (self.x == self):
            str_x = f'( {str_x} )'
        
        return ' '.join([str_y, str_op, str_x])
    
    def __repr__(self):
        return f'Node({repr(self.x)},{repr(self.op)},{repr(self.y)})'

    def __lt__(self, other):
        if isinstance(other, Node):
            return self.pre < other.pre
        return self.pre < pre_dict.get(other, 9)
    
    def __gt__(self, other):
        if isinstance(other, Node):
            return self.pre > other.pre
        return self.pre > pre_dict.get(other, 9)
    
    def __eq__(self, other):
        if isinstance(other, Node):
            return self.pre == other.pre
        return self.pre == pre_dict.get(other, 9)
    
def calc(expr):
    tokens = [str(x) for x in expr]
    res = []
    for t in tokens:
        if t in math_operators:
            res[-2:] = [math_operators[t](res[-2],res[-1])]
            
        else:
            res.append(literal_eval(t))

    return res[0] if res else 0

def repr_calc(expr):
    tokens = [str(x) for x in expr]
    res = []
    for t in tokens:
        if t in math_operators:
            res.append(Node(res.pop(),t,res.pop()))
        else:
            res.append(t)

    return str(res[0])

class FalseOperation(ValueError):
    pass

def return_calc_expr(expr):
    try:
        calc_res = calc(expr)
    except ZeroDivisionError:
        raise FalseOperation('Division by zero')
    if int(calc_res) != calc_res:
        raise FalseOperation('non-int value')
    if calc_res < 0:
        raise FalseOperation('negative value')
    return calc_res


def run(base_numbers, target):
    
    assert len(base_numbers) > 0, 'List must not be empty'
    assert target >= 0, 'Target must be non-negative'
    assert (all(isinstance(ele,int) for ele in base_numbers) and all(ele >= 0 for ele in base_numbers)), 'List must be non-negative integers'

    res = []
    for n_comb in permutations(base_numbers, 2):
        tmp_numb = base_numbers.copy()
        for n_ in n_comb:
            tmp_numb.remove(n_)
        tmp_numbs = tmp_numb.copy()
        for op_comb in combinations_with_replacement(math_operators.keys(),len(base_numbers)-2):
            tmp_expression = tmp_numbs + list(op_comb) 
            for tmp_permutation in permutations(tmp_expression,len(tmp_expression)):
                for final_op in math_operators.keys():
                    expr = list(n_comb) + list(tmp_permutation) + [final_op]
                    try:
                        calc_expr = return_calc_expr(expr)
                        if (calc_expr == target) and (expr not in res):
                            res.append(expr)
                    except:
                        pass

    if res == []:
        return '', None
    else:
        return repr_calc(random.sample(res,1)[0]), True

if __name__ == '__main__':
    print('Input a list of numbers, separated by a comma (e.g. "1,2,3,4"):')
    base_numbers_val = input()
    print('Select a target value:')
    target_val = input()
    run(base_numbers_val, target_val)