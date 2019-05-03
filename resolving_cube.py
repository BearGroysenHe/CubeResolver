import numpy as np
import random
from input_cube import *
from function import *

relations = input_relation()
rela_str = make_rela_str(relations)
cube = input_cube(rela_str)
np.save('cube',cube)
while True:
    cube = np.load('cube.npy')
    operations = []
    count = 0
    print('开始重新尝试')
    while count < 10000:
        condition = check(cube)
        if condition == True:
            break
        axis = random.randint(0,2)
        num = random.randint(1,3)
        init_cube = np.load('cube.npy')
        direction = random.randint(0,1)
        if axis == 0:
            axis = 'x'
        elif axis == 1:
            axis = 'y'
        else:
            axis = 'z'
        rotation_cube(cube,axis,num,direction)
        equal = init_cube == cube
        operations.append(axis + str(num)+str(direction))
        count += 1
        print('正在尝试第%d次'%(count))
    else:
        print('尝试超过次数')
    if condition == True:
        break
print('共用了%d步'%(count))
print(operations)
