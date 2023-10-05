import math as m
import numpy as np
import pandas as pd
import sys
import matplotlib.pyplot as plt
import scipy as sp
from scipy.ndimage import uniform_filter1d

U_free=8                                                                                                            
Eff_v=1                                                                                                             
Eff_t=0.8                                                                                                           
Eff_p=0.8                                                                                                           
TSR=4                                                                                                               
D_t=2                                                                                                               
D_r=1.8                                                                                                            
D_h=0.15                                                                                                         
N_seg=10                                                                                                            
Blades=3                                                                                                            
Max_c=0.15                                                                                                         
Min_c=0.05                                                                                                        
Res_c=100                                                                                                       
Rotorfoil='Eppler e422'                                                                                           
Max_itt_BEM=100                                                                                                    

nu=1.51*10**-5                                                                                                      
rho=1.225                                                                                                            




np.set_printoptions(threshold=sys.maxsize,precision=3, suppress=True)
global aa,at,itter1,var,res


res=[]


def reset_inputs():                                                                                                 
    global aa,at,c,itter1,Max_c,res,var,blade
    aa=0
    at=0
    itter1=0

reset_inputs()

def blade (seg):                                                                                                    

    global aa,at,itter1,var,res

    def segment(c):                                                                                                 

        global aa,at,itter1,var,res

        def calc(itter):                                                                                           

            global aa,at,itter1,var,res

            U_gen=U_free+U_free*Eff_v
            r=(((D_r-D_h)/2)/N_seg)*seg
            Local_speedratio=(TSR/N_seg)*seg
            V_rot=TSR*U_gen
            V_app=m.sqrt(((U_gen*(1-aa))**2)+((V_rot*r*(1+at))**2))
            Re=(V_app*c)/nu

            arr=np.array([100000,150000,200000,250000,300000,350000,400000,450000,500000,550000,                
                          650000,700000,750000,800000,850000,900000,950000,1000000])  
            array_diff=np.absolute(arr-Re) 
            index=array_diff.argmin()
            Re1=arr[index]

            a_app=m.atan((U_gen*(1-aa))/(V_rot*r*(1+at)))
            A_rot=m.pi*(D_r/2)**2
            Solidity=(Blades*c)/(2*m.pi*r)

            handle = "polars\\{airfoil} {Re}.dat".format(Re = Re1, airfoil=Rotorfoil)

            data=pd.read_csv(handle,delim_whitespace=True, skiprows=15, dtype=np.float64)
            data=np.array(data)

            cl_array=data[:,1]
            cd_array=data[:,2]

            glide_ratio=np.divide(cl_array,cd_array)
            clcd_opt=np.max(glide_ratio)
            index_clcd = np.where(glide_ratio == clcd_opt)

            AOA=float(data[index_clcd,0])
            cl=float(data[index_clcd,1])
            cd=float(data[index_clcd,2])

            V_vehicle=U_free*Eff_v
            dr=(m.pi*(r+0.0000000000001)**2)-(m.pi*(r)**2)  

            cn=cl*(m.cos(a_app))+cd*(m.sin(a_app))
            ct=cl*(m.sin(a_app))-cd*(m.cos(a_app))

            P=2*rho*(U_gen**3)*(aa*((1-aa)**2))*A_rot
            T=2*rho*(U_gen**2)*(aa*(1-aa))*A_rot

            cP=4*(aa*(1-aa)**2)
            cT=4*(aa*(1-aa))

            ct_local=(T/dr)/(m.pi*rho*(U_gen**2)*r)
            cp_local=(P/dr)/(m.pi*rho*(U_gen**3)*r)

            #aa=float(1-(abs((1/(((4*(m.sin(a_app)*m.sin(a_app)))/(Solidity*cn))+1)))))
            aa=float(abs((1/(((4*(m.sin(a_app)*m.sin(a_app)))/(Solidity*cn))+1))))       
            at=float(abs(1/(((4*(m.cos(a_app)*m.sin(a_app)))/(Solidity*ct))-1)))          
            c_opt=float(abs(((Eff_p*Eff_t)*(1+(1/(V_vehicle/U_free)))*cp_local)-ct_local))
            Twist=float(np.degrees(a_app)-float(AOA))    

            if itter1==Max_itt_BEM:
                var=[seg,aa,c,Twist,c_opt]                                                                      
                for i in var:
                    res.append(i)
                    
                itter1=0  
            else:
                itter1=itter1+1

        itter=np.full((1,Max_itt_BEM),c)
        function=np.vectorize(calc)
        function(itter)
    
    reset_inputs()
    a1=np.linspace(Min_c,Max_c,Res_c)
    function=np.vectorize(segment)
    function(a1)
   
reset_inputs()
a1=np.linspace(1,N_seg,N_seg)
function=np.vectorize(blade)
function(a1)
 
res=np.array(res)

df=pd.DataFrame(res)
df.to_csv("datage.csv", sep='\t')

res=np.reshape(res,(((N_seg+1)*(Res_c+1)),(len(var))))                                                            
res=np.split(res,((N_seg+1)),axis=0)
res=np.array(res)
res=np.delete(res,0,axis=1)

output=[]                                                                                                                                      
for p in range (1,N_seg+1):
    t1=(res[p,:,-1])
    t2=np.max(t1)
    index=np.where(t1==t2)
    output.append(res[p][index][:])


output=np.array(output)                                                                                         
output=np.array(output)
output=np.squeeze(output)
output=np.rot90(output,3)
output=np.flip(output,1)

seg_res=output[0][:]                                                                                               
a_res=output[-2][:]
c_res=output[-3][:]

a_res_uni=uniform_filter1d(a_res, size=5)
c_res_uni=uniform_filter1d(c_res, size=5)
print("Twist: ",a_res_uni)
print("Koordenlengten: ",c_res_uni)

fig,(axs1,axs2)=plt.subplots(2)
fig.suptitle('StoefoeBlade')

axs1.plot(seg_res,c_res*1000,'o')
axs1.plot(seg_res,c_res_uni*1000) 
axs1.set(ylabel='Cord Length [mm]')

axs2.plot(seg_res,a_res,'o')
axs2.plot(seg_res,a_res_uni)
axs2.set(xlabel='Segment Nr', ylabel='Twist Angle [deg]')

plt.show()