import ctypes
import numpy as np
import time

func=ctypes.CDLL('./sharedLib/edflib.so')
rms_c = ctypes.CDLL('./sharedLib/rmslib.so')
dms_c = ctypes.CDLL('./sharedLib/dmslib.so')
rr_c = ctypes.CDLL('./sharedLib/rrlib.so')
sjf_p = ctypes.CDLL('./sharedLib/sjfplib.so')
sjf_np = ctypes.CDLL('./sharedLib/sjfnplib.so')

#a=np.array([3,2,2], dtype=ctypes.c_int)
#b=np.array([7,4,8], dtype=ctypes.c_int)
#c=np.array([20,5,10], dtype=ctypes.c_int)
#res=np.zeros(20,dtype=ctypes.c_int)
#d=np.zeros(3,dtype=ctypes.c_int)
#n=ctypes.c_int(3)
#intp=ctypes.POINTER(ctypes.c_int)

#i=a.ctypes.data_as(intp)
#j=b.ctypes.data_as(intp)
#k=c.ctypes.data_as(intp)
#m=d.ctypes.data_as(intp)

#ans=res.ctypes.data_as(intp)
#func.edf(n,i,j,k,m,ans)
#print(res)

def edf(cap, ded, per, size, drawData, timeScale, canvas,root):
    intp=ctypes.POINTER(ctypes.c_int)

    val1=[i.get() for i in per]
    val2= [i.get() for i in cap]
    val3= [i.get() for i in ded]
    peri=np.zeros(size, dtype = ctypes.c_int)
    capa=np.zeros(size, dtype = ctypes.c_int)
    dead=np.zeros(size, dtype = ctypes.c_int)
    for i in range (0,size):
        peri[i]=val1[i]
        capa[i]=val2[i]
        dead[i]=val3[i]
        
    period=peri.ctypes.data_as(intp)
    capacity= capa.ctypes.data_as(intp)
    deadline= dead.ctypes.data_as(intp)

    lcm=func.lcm(period,size)
    ans = np.zeros(lcm,  dtype = ctypes.c_int)
    answer = ans.ctypes.data_as(intp)
    ar=np.zeros(lcm, dtype =ctypes.c_int)
    arrival = ar.ctypes.data_as(intp)
    func.edf(lcm, size, capacity, deadline, period, arrival, answer )
    
    downShift = np.zeros(size, dtype= ctypes.c_int)
    upShift = np.arange(size)
    downShift.fill(40)
    upShift.fill(10)
    for i in range(0,lcm):
        if ans[i]!=0:
            drawData(canvas, ans[i], downShift[ans[i]-1],upShift[ans[i]-1])
            root.update()
            time.sleep(timeScale)
            downShift[ans[i]-1]+=30;
            upShift[ans[i]-1]+=30;


def rms(cap, per, size, drawData, timeScale, canvas,root):
    intp=ctypes.POINTER(ctypes.c_int)

    val1=[i.get() for i in per]
    val2= [i.get() for i in cap]

    peri=np.zeros(size, dtype = ctypes.c_int)
    capa=np.zeros(size, dtype = ctypes.c_int)
    for i in range (0,size):
        peri[i]=val1[i]
        capa[i]=val2[i]

        
    period=peri.ctypes.data_as(intp)
    capacity= capa.ctypes.data_as(intp)


    lcm=rms_c.lcm(period,size)
    ans = np.zeros(lcm,  dtype = ctypes.c_int)
    answer = ans.ctypes.data_as(intp)
    ar=np.zeros(lcm, dtype =ctypes.c_int)
    arrival = ar.ctypes.data_as(intp)
    rms_c.rms(lcm, size, capacity, period, arrival, answer )
    downShift = np.zeros(size, dtype= ctypes.c_int)
    upShift = np.arange(size)
    downShift.fill(40)
    upShift.fill(10)
    for i in range(0,lcm):
        if ans[i]!=0:
            drawData(canvas, ans[i], downShift[ans[i]-1],upShift[ans[i]-1])
            root.update()
            time.sleep(timeScale)
            downShift[ans[i]-1]+=30;
            upShift[ans[i]-1]+=30;
 
def dms(cap, ded, per, size, drawData, timeScale, canvas,root):
    intp=ctypes.POINTER(ctypes.c_int)

    val1=[i.get() for i in per]
    val2= [i.get() for i in cap]
    val3= [i.get() for i in ded]
    peri=np.zeros(size, dtype = ctypes.c_int)
    capa=np.zeros(size, dtype = ctypes.c_int)
    dead=np.zeros(size, dtype = ctypes.c_int)
    for i in range (0,size):
        peri[i]=val1[i]
        capa[i]=val2[i]
        dead[i]=val3[i]
        
    period=peri.ctypes.data_as(intp)
    capacity= capa.ctypes.data_as(intp)
    deadline= dead.ctypes.data_as(intp)

    lcm=dms_c.lcm(period,size)
    ans = np.zeros(lcm,  dtype = ctypes.c_int)
    answer = ans.ctypes.data_as(intp)
    ar=np.zeros(lcm, dtype =ctypes.c_int)
    arrival = ar.ctypes.data_as(intp)
    dms_c.dms(lcm, size, capacity, deadline, period, arrival, answer )
    
    downShift = np.zeros(size, dtype= ctypes.c_int)
    upShift = np.arange(size)
    downShift.fill(40)
    upShift.fill(10)
    for i in range(0,lcm):
        if ans[i]!=0:
            drawData(canvas, ans[i], downShift[ans[i]-1],upShift[ans[i]-1])
            root.update()
            time.sleep(timeScale)
            downShift[ans[i]-1]+=30;
            upShift[ans[i]-1]+=30;

def rr(a_t, b_t, size, drawData, timeScale, canvas,root):
    intp=ctypes.POINTER(ctypes.c_int)

    val1=[i.get() for i in a_t]
    val2= [i.get() for i in b_t]

    arriv=np.zeros(size, dtype = ctypes.c_int)
    burst=np.zeros(size, dtype = ctypes.c_int)
    for i in range (0,size):
        arriv[i]=val1[i]
        burst[i]=val2[i]

        
    arrival_time = arriv.ctypes.data_as(intp)
    burst_time = burst.ctypes.data_as(intp)
    n = 0
    for i in range(0,size):
        n=n+int(val2[i])
    ans = np.zeros(n,  dtype = ctypes.c_int)
    answer = ans.ctypes.data_as(intp)
    rr_c.rr(size, arrival_time, burst_time,  answer )
    downShift = np.zeros(size, dtype= ctypes.c_int)
    upShift = np.arange(size)
    downShift.fill(40)
    upShift.fill(10)
    #print(ans)
    for i in range(0,n):
        if ans[i]!=0:
            drawData(canvas, ans[i], downShift[ans[i]-1],upShift[ans[i]-1])
            root.update()
            time.sleep(timeScale)
            downShift[ans[i]-1]+=30;
            upShift[ans[i]-1]+=30;
 
def sjfp(a_t, b_t, size, drawData, timeScale, canvas,root):
    intp=ctypes.POINTER(ctypes.c_int)

    val1=[i.get() for i in a_t]
    val2= [i.get() for i in b_t]

    arriv=np.zeros(size, dtype = ctypes.c_int)
    burst=np.zeros(size, dtype = ctypes.c_int)
    for i in range (0,size):
        arriv[i]=val1[i]
        burst[i]=val2[i]

        
    arrival_time = arriv.ctypes.data_as(intp)
    burst_time = burst.ctypes.data_as(intp)
    n = 0
    for i in range(0,size):
        n=n+int(val2[i])
    ans = np.zeros(n,  dtype = ctypes.c_int)
    answer = ans.ctypes.data_as(intp)
    sjf_p.sjfp(size, arrival_time, burst_time,  answer )
    downShift = np.zeros(size, dtype= ctypes.c_int)
    upShift = np.arange(size)
    downShift.fill(40)
    upShift.fill(10)
    #print(ans)
    for i in range(0,n):
        if ans[i]!=0:
            drawData(canvas, ans[i], downShift[ans[i]-1],upShift[ans[i]-1])
            root.update()
            time.sleep(timeScale)
            downShift[ans[i]-1]+=30;
            upShift[ans[i]-1]+=30;
 
 
def sjfnp(a_t, b_t, size, drawData, timeScale, canvas,root):
    intp=ctypes.POINTER(ctypes.c_int)

    val1=[i.get() for i in a_t]
    val2= [i.get() for i in b_t]

    arriv=np.zeros(size, dtype = ctypes.c_int)
    burst=np.zeros(size, dtype = ctypes.c_int)
    for i in range (0,size):
        arriv[i]=val1[i]
        burst[i]=val2[i]

        
    arrival_time = arriv.ctypes.data_as(intp)
    burst_time = burst.ctypes.data_as(intp)
    n = 0
    for i in range(0,size):
        n=n+int(val2[i])
    ans = np.zeros(n,  dtype = ctypes.c_int)
    answer = ans.ctypes.data_as(intp)
    sjf_np.sjfnp(size, arrival_time, burst_time,  answer )
    downShift = np.zeros(size, dtype= ctypes.c_int)
    upShift = np.arange(size)
    downShift.fill(40)
    upShift.fill(10)
    #print(ans)
    for i in range(0,n):
        if ans[i]!=0:
            drawData(canvas, ans[i], downShift[ans[i]-1],upShift[ans[i]-1])
            root.update()
            time.sleep(timeScale)
            downShift[ans[i]-1]+=30;
            upShift[ans[i]-1]+=30;
 


           
