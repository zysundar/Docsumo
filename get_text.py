import pandas as pd
def get_point(pos,x0,y0,x2,y2):
    if pos[0]<=x0 and (pos[2]+100)>= x2 and pos[1]<= y0 and (pos[3]+100)>=y2: 
        return True

def text(filename,position):
    file=pd.read_csv(filename)
    r,c=file.shape
    s=''
    for i in range(0,r):
        x0=file.loc[[i],['x0']].values[0][0]
        y0=file.loc[[i],['y0']].values[0][0]
        x2=file.loc[[i],['x2']].values[0][0]
        y2=file.loc[[i],['y2']].values[0][0]
        if get_point(position,x0,y0,x2,y2):
            s=s+file.loc[[i],['Text']].values[0][0]+" "
    return s.rstrip()
   