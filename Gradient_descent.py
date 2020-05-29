def min_max_standard(x,y):
    x1=[]
    y1=[]
    for i,j in zip(x,y):
        i=(i-min(x))/(max(x)-min(x))
        j=(j-min(y))/(max(y)-min(y))
        i=round(i,2)
        j=round(j,2)
        x1.append(i)
        y1.append(j)
    x=x1
    y=y1
    return x,y
def cal_error(X,Y,m,b):
    error=0
    for x,y in zip(X,Y):
        error+=(m*x+b-y)**2
    error/=2
    return error
def update_w(m,b,X,Y,r):
    dssem=0
    dsseb=0
    for x,y in zip(X,Y):
        yp=m*x+b
        dssem=dssem-(y-yp)*x
        dsseb=dsseb-(y-yp)
    m_new=m-r*dssem
    b_new=b-r*dsseb
    return [b_new,m_new]  
def run_(X,Y,m,b,r,steps):
    stepcount=0
    olderror=cal_error(X,Y,m,b)
    while (stepcount<=steps or newerror-olderror>=0.001):
        b,m=update_w(m,b,X,Y,r)
        newerror=cal_error(X,Y,m,b)
        if stepcount%10==0:
            print("{0:5d}{1:10.4f}{2:10.4f}{3:10.4f}".format(stepcount,b,m,newerror))
        stepcount+=1
    return [b,m]       
x=[1100,1400,1425,1550,1600,1700,1700,1875,2350,2450]
y=[199000,245000,319000,240000,312000,279000,310000,308000,405000,324000]
X,Y=min_max_standard(x,y)
m_current=0.45
b_current=0.75
print('Starting...')
print("{0:10.2f}{1:10.4f}{2:10.4f}".format(b_current,m_current,cal_error(X,Y,m_current,b_current)))
l_rate=0.01
steps=300
b_current,m_current=run_(X,Y,m_current,b_current,l_rate,steps)
print('Running...')
print('After {0} iterations m is {1:10.4f} and b is {2:10.4f} with error {3:10.4f}'.format(steps,m_current,b_current,cal_error(X,Y,m_current,b_current)))

