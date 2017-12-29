import os
import numpy as np
'''
ZiTi=0.3

def Resize(img, flag=0):
    if(flag==1):
        return cv2.resize(img,(Unit//2-2,Unit//2-2), interpolation=cv2.INTER_AREA)
    return cv2.resize(img,(Unit-2,Unit-2), interpolation=cv2.INTER_AREA)
Unit=23
dir_str=os.path.dirname(os.path.realpath(__file__))+'/'
walls_image=Resize(cv2.imread(dir_str+'walls.png'))
boxes_image=Resize(cv2.imread(dir_str+'boxes.png'))
item_fig={}
item_fig['*']=Resize(cv2.imread(dir_str+'item1.png'))
item_fig['^']=Resize(cv2.imread(dir_str+'item2.png'))
bomb_pic=Resize(cv2.imread(dir_str+'bomb.png'),1)
P0=Resize(cv2.imread(dir_str+'player0.png'),1)
P1=Resize(cv2.imread(dir_str+'player1.png'),1)
def Get_State(env):
    def create_line(x0, y0, x1, y1):
        for i in range(x0,x1+1):
            for j in range(y0,y1+1):
                result[i,j]=(0,0,0)
    def wph(i, j, k):
        if(i>=0 and i<env.height*Unit and j>=0 and j<env.width*Unit):
            result[i,j]=k
    def Put_Image(img, pos, offset_x, offset_y):
        x,y = img.shape[0],img.shape[1]
        for i in range(x):
            for j in range(y):
                wph(i+pos[0]+offset_x, j+pos[1]+offset_y, img[i,j])
    def Text_bomb(xy, v, dis):
        cv2.putText(result, str(v), (xy[0]*Unit + Unit//8,xy[1]*Unit+Unit*7//8),cv2.FONT_HERSHEY_SIMPLEX, ZiTi, (0,0,0), 1)
        cv2.putText(result, str(dis), (xy[0]*Unit + Unit//8+Unit//2,xy[1]*Unit+Unit*7//8),cv2.FONT_HERSHEY_SIMPLEX, ZiTi, (0,0,0), 1)
    def Text_player(xy, v, flag):
        if(flag==0):
            cv2.putText(result, str(v), (xy[0]*Unit + Unit//8,xy[1]*Unit+Unit*3//8),cv2.FONT_HERSHEY_SIMPLEX, ZiTi, (0,0,0), 1)
        else :
            cv2.putText(result, str(v), (xy[0]*Unit+Unit//2 + Unit//8,xy[1]*Unit+Unit*3//8),cv2.FONT_HERSHEY_SIMPLEX, ZiTi, (0,0,0), 1)
            

    result = np.zeros((env.height*Unit,env.width*Unit,3),np.uint8)
    result[...]=255
    maze=env.maze
    players=env.players
    players[0].fig=P0
    players[1].fig=P1
    inpulse=env.inpulse
    boxes_xyk=env.boxes_xyk
    
    #self.bombs_data
    #self.bombs_xy

    # create grids
    for c in range(0, env.width * Unit, Unit):
        x0, y0, x1, y1 = c, 0, c, env.height * Unit-1
        create_line(y0, x0, y1, x1)
    for r in range(0, env.height * Unit, Unit):
        x0, y0, x1, y1 = 0, r, env.width * Unit-1, r
        create_line(y0, x0, y1, x1)
    
    #create wall,box,item,bombs
    boxes_xy=[]
    for box in boxes_xyk:
        boxes_xy.append((box[0],box[1]))
    for x in range(0,env.width):
        for y in range(0,env.height):
            if (maze[x][y]=='#'):
                wall_now = np.array([Unit*y+1, Unit*x+1])
                Put_Image(walls_image,wall_now, 0, 0)
            position =np.array([Unit*y+1, Unit*x+1])
            if (x,y) in boxes_xy:
                Put_Image(boxes_image, position, 0, 0)
            else:
                if(maze[x][y] in ['*','^']):
                    Put_Image(item_fig[maze[x][y]], position, 0, 0)
            if (x,y) in env.bombs_xy:
                Put_Image(bomb_pic, position, Unit//2, 0)
    
    # create players
    for player_id in range(2):
        xy_now=players[player_id].xy
        player_now = np.array([Unit*xy_now[1]+1, Unit*xy_now[0]+1])
        u,v=0,0
        if(player_id==1):
            u=0
            v=Unit//2
        Put_Image(players[player_id].fig, player_now, u, v)

    
    bombs_t=[([100] * env.height) for i in range(env.width)]
    
    # create text for bombs
    for i in range(env.bombs_cnt):
        xy=env.bombs_xy[i]
        bombs_t[xy[0]][xy[1]]=min(bombs_t[xy[0]][xy[1]], env.bombs_data[i][0])
    
    for x in range(0,env.width):
        for y in range(0,env.height):
            if (maze[x][y]=='b'):
                Text_bomb((x,y) , bombs_t[x][y], env.maze_[x][y])
    
    Text_player(players[0].xy, players[0].max_boom_num-players[0].boom_num, 0)
    Text_player(players[1].xy, players[1].max_boom_num-players[1].boom_num, 1)

    return result
'''
def Get_Simple_State(env):
    '''
    state
    -------------
    wall,box,item*,item^,player0(bomb)[0..5],bomb time[0-9]
    -------------
    '''
    result=np.zeros((env.height,env.width,20))
    boxes_xy=[]
    for box in env.boxes_xyk:
        boxes_xy.append((box[0],box[1]))
    for x in range(0,env.width):
        for y in range(0,env.height):
            if (env.maze[x][y]=='#'):
                result[y][x][0]=1
            if (x,y) in boxes_xy:
                result[y][x][1]=1
            else:
                if(env.maze[x][y]=='*'):
                    result[y][x][2]=1
                if(env.maze[x][y]=='^'):
                    result[y][x][3]=1
    '''
    for i in range(env.bombs_cnt):
        x,y=env.bombs_xy[i]
        result[y][x][8+env.bombs_data[i][0]]=1
        result[y][x][18+env.bombs_data[i][1]]=1
    '''
    x,y=env.players[0].xy
    bnum=env.players[0].max_boom_num-env.players[0].boom_num
    for i in range(bnum+1):
        result[y][x][4+i]=1
    
    #boom explosion
    maze=env.maze
    bfs=[]
    for i in range(env.bombs_cnt):
        x,y=env.bombs_xy[i]
        dd=[(0,1),(0,-1),(-1,0),(1,0),(0,0)]
        for d in dd:
            xx,yy=x,y
            xx+=d[0]
            yy+=d[1]
            if(xx<0 or yy<0 or xx>=env.width or yy>=env.height or maze[xx][yy]=='#'):
                break
            result[yy][xx][10+env.bombs_data[i][0]]=1
        if(env.bombs_data[i][0]==0):
            bfs.append((env.bombs_xy[i],env.bombs_data[i][2]))
        
    if(len(bfs)!=0):
        l=0
        r=len(bfs)-1
        dd=[(0,1),(0,-1),(-1,0),(1,0)]
        while(l<=r):
            ((x,y),player_id)=bfs[l]
            result[y][x][10]=1
            l+=1
            for d in dd:
                xx,yy=x,y
                for j in range(env.maze_[x][y]):
                    xx+=d[0]
                    yy+=d[1]
                    if(xx<0 or yy<0 or xx>=env.width or yy>=env.height or maze[xx][yy]=='#'):
                        break
                    result[yy][xx][10]=1
                    if(maze[xx][yy]=='b'):
                        for i in range(env.bombs_cnt):
                            if(env.bombs_xy[i]==(xx,yy)):
                                r+=1
                                bfs.append(((xx,yy),env.bombs_data[i][2]))
                        maze[xx][yy]=' '
                    if(maze[xx][yy]=='o'):
                        break
    return result
    
