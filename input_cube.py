import numpy as np

def input_relation():
    relations = {0:''}
    for i in range(1,7):
        relations[i] = input(str(i) + '对应的颜色是:')
    return relations

def input_cube(rela_str):
    cube = np.zeros((5, 5, 5))
    for axis in ['x','y','z']:
        for i in [0,4]:
            if axis == 'x':
                x = i
            elif axis == 'y':
                y = i
            else:
                z = i
            if axis == 'x':
                for y in range(1,4):
                    for z in range(1,4):
                        print(rela_str)
                        cube[x, y, z] = input('请输入（%d%d%d）位的数据'%(x,y,z))
            elif axis == 'y':
                for x in range(1, 4):
                    for z in range(1, 4):
                        print(rela_str)
                        cube[x, y, z] = input('请输入（%d%d%d）位的数据' % (x, y, z))
            elif axis == 'z':
                for x in range(1, 4):
                    for y in range(1, 4):
                        print(rela_str)
                        cube[x, y, z] = input('请输入（%d%d%d）位的数据' % (x, y, z))

    return cube
