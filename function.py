def overturn_row(face):
    for i in range(5):
        face[i, 0], face[i, 4] = face[i, 4], face[i, 0]
        face[i,1],face[i,3] = face[i,3],face[i,1]
def overturn_diagonal(face):
    for i in range(5):
        for j in range(i+1):
            face[i,j],face[j,i] = face[j,i],face[i,j]
# 0为逆时针旋转，1为顺时针旋转
def rotation_face(face,direction):
    if direction == 0 :
        overturn_row(face)
        overturn_diagonal(face)
    elif direction == 1 :
        overturn_diagonal(face)
        overturn_row(face)

def rotation_side_face(face,direction):
    if direction == 0 :
        overturn_row(face)
        overturn_diagonal(face)
    elif direction == 1 :
        overturn_diagonal(face)
        overturn_row(face)

def rotation_cube(cube,axis,num,direction):
    if axis == 'x':
        if int(num) == 2:
            rotation_side_face(cube[2,:,:],direction)
        elif int(num) == 1:
            rotation_side_face(cube[1,:,:],direction)
            rotation_face(cube[0,:,:],direction)
        elif int(num) == 3:
            rotation_side_face(cube[3,:,:],direction)
            rotation_face(cube[4,:,:],direction)
    elif axis == 'y':
        if int(num) == 2:
            rotation_side_face(cube[:,2,:],direction)
        elif int(num) == 1:
            rotation_side_face(cube[:,1,:],direction)
            rotation_face(cube[:,0,:],direction)
        elif int(num) == 3:
            rotation_side_face(cube[:,3,:],direction)
            rotation_face(cube[:,4,:],direction)
    elif axis == 'z':
        if int(num) == 2:
            rotation_side_face(cube[:,:,2],direction)
        elif int(num) == 1:
            rotation_side_face(cube[:,:,1],direction)
            rotation_face(cube[:,:,0],direction)
        elif int(num) == 3:
            rotation_side_face(cube[:,:,3],direction)
            rotation_face(cube[:,:,4],direction)

def check(cube):
    for i in [0,4]:
#检查左右面
        for j in range(1,4):
            for k in range(1,3):
                if cube[i,j,k] != cube[i,j,k+1]:
                    return False
            if j !=3:
                if cube[i,j,1] != cube[i,j+1,1]:
                    return False
#检查前后面
        for j in range(1,4):
            for k in range(1,3):
                if cube[j,i,k] != cube[j,i,k+1]:
                    return False
            if j !=3:
                if cube[j,i,1] != cube[j+1,i,1]:
                    return False
#检查上下面
        for j in range(1,4):
            for k in range(1,3):
                if cube[k,j,i] != cube[k+1,j,i]:
                    return False
            if j !=3:
                if cube[1,j,i] != cube[1,j+1,i]:
                    return False
    return True

def make_rela_str(relations):
    rela_str = ''
    for i, j in relations.items():
        rela_str += str(j) + ':' + str(i) + '|'
    return rela_str
