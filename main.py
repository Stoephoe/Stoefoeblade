                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                        
                                                                                                                                                                                                                                                                                                            
                                                                                                                                                                                                                                                                                                            
                                                                                                                                                                                                                                                                                                            
                                                                                                                                                                                                                                                                                                            
###############################################################################################################################################################################################################                                                                       
#-============================================================================================================================================================================================================                                                                       
#                                                                        .:---==--:.                                                                                                                                                                                                   
#                                                                  .-+###*+=--=--==+*##*=:                                                                                                                                                                                             
#                                                               .=%%+:       .@-       :=#%*:                                                                                                                                                                                          
#                                                            -#%=.          .@%           -*%=                                                                                                                                                                                        
#                                                          -%*:             .@@-            .=%+                                                                                                                                                                                      
#         -*%@@@@@@#+:      :####################         #%:               .@@#              .#@:           :##################.    :#################         .=#%@@@@@%*=           ##################-                                                                            
#       =@@@@@%##%@@@@#:    :@@@@@@@@@@@@@@@@@@@@       :%*                  @@@.               -@=          :@@@@@@@@@@@@@@@@@@.    -@@@@@@@@@@@@@@@@@       -#@@@@%###%@@@@*:        @@@@@@@@@@@@@@@@@@-                                                                            
#     +@@%-.      :*@@@=            %@@+              -@=                   @@@#                :@*         :@@@.                   -@@@                   .#@@@+:       -*@@@*       @@@-                                                                                           
#     @@@:          =@@@.           #@@+              @=                    @@@@:                :@=        :@@@                    -@@@                  .%@@%.           :@@@#      @@@-                                                                                           
#    .@@@.           #**.           #@@+             *#                     @@@@#                 =@        :@@@                    -@@@                  %@@#              :@@@*     @@@-                                                                                           
#     #@@%-                         #@@+            :@-                     @@@%=                  @+       :@@@                    -@@@                 -@@@.               =@@@.    @@@-                                                                                           
#     .%@@@@%*+-.                   #@@+            +@.                     ++-                    *%       :@@@:.............      -@@@                 +@@%                 @@@=    @@@=.............                                                                              
#       -*@@@@@@@@%*=.              #@@+            *@               ==-.  +@@* .                  +@       :@@@@@@@@@@@@@@@@@-     -@@@@@@@@@@@@@@@     #@@*                 %@@+    @@@@@@@@@@@@@@@@@-                                                                             
#          .:=+#@@@@@@#:            #@@+            *@             =%@@@@@:+@@**@#=:               *%       :@@@**************.     -@@@************     #@@*                 %@@+    @@@#*************:                                                                             
#                 :+@@@@-           #@@+            -@:          :%@@@@@+.  ** *@@@@%+:            %*       :@@@                    -@@@                 *@@#                 @@@=    @@@-                                                                                           
#    :--             *@@%           #@@+             @+        :#@@@%+:    .@@.:#@@@@@@%+:        .@:       :@@@                    -@@@                 -@@@.               -@@@.    @@@-                                                                                           
#   .@@@:            -@@@           #@@+             -@:     :#@@%=.       :@@.   .:=+#@@@@*-     %*        :@@@                    -@@@                  #@@#              .@@@*     @@@-                                                                                           
#    *@@@.           +@@#           #@@+              *@.  .*@%=.          -@@:          :=*#@#= #@.        :@@@                    -@@@                   %@@%.           :@@@#      @@@-                                                                                           
#     %@@@+-       -*@@@:           #@@+               #@:-#=.             =@@-               .:*%.         :@@@.                   -@@@                    *@@@+:       -*@@@*       @@@-                                                                                           
#      +@@@@@@%%%@@@@@*.            #@@+                =@=                =@@=               :%*           :@@@@@@@@@@@@@@@@@@#    -@@@                     -#@@@@%###%@@@@*:        @@@@@@@@@@@@@@@@@@@                                                                            
#        -*#@@@@@@%*=               *##=                 .%%:              +@@+              *@=            :##################*    :###                       .=*%@@@@@%*=           ###################                                                                            
#                                                          -##-            *@@*           :*%=                                                                                                                                                                                       
#                                                            :+%*=.        #@@*        -*%*:                                                                                                                                                                                         
#                                                               :=#%*=-.   %@@#  .:=*%%+:                                                                  *****+=   =+.        :**     *****+:   =******=                                                                           
#                                                                   .-=+*##@@@@##*+=:                                                                      @@===*@#  #@:        %@@#    @@+==#@#  #@+====-                                                                           
#                                                                          @@@@                                                                            @@:::=@*  #@:       #@=%@-   @@.   %@- #@-::::                                                                            
#                                                                         .@@@@                                                                            @@%%@@@=  #@:      -@% :@%   @@.   *@= #@%%%%%-                                                                           
#                                                                         :@@@@.                                                                           @@    #@- #@:      %@@%%@@+  @@.   %@- #@.                                                                                
#                                                                         -@@@@:                                                                           @@+++*@@. #@*++++.+@+....%@- @@+++#@*  #@*++++=                                                                           
#                                                                         =@@@@=                                                                           ++++++=.  =++++++:++     :+= +++++=.   =++++++=                                                                           
#=+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++=                                                                       
###############################################################################################################################################################################################################                                                                     
                                                                                                                                                                                                                                                                                                            

import math as m
import numpy as np
import pandas as pd
import sys
import matplotlib.pyplot as plt
import scipy as sp
from scipy.ndimage import uniform_filter1d

###############################################################################################################################################################################################################
################################################################################################# Input Parameters ############################################################################################
###############################################################################################################################################################################################################

U_free=8                                                                       # Incoming free wind                                                     [m/s]                                                                    
Eff_v=1                                                                        # Vehicle efficiency  (ratio between driving speed and freewind speed)   [-/-]                                                                 
Eff_t=0.8                                                                      # Transmission efficiency                                                [-/-]                     
Eff_p=0.8                                                                      # Propulsion efficiency                                                  [-/-]                    
TSR=4                                                                          # Tipspeed ratio (ratio between tipspeed and freewind speed)             [-/-]                                                         
D_t=2                                                                          # Turbine Diameter                                                       [m]              
D_r=1.8                                                                        # Rotor diameter                                                         [m]           
D_h=0.15                                                                       # Hub diameter                                                           [m]       
N_seg=10                                                                       # Number of blade elements                                               [-/-]                      
Blades=3                                                                       # Number of blades                                                       [-/-]              
Max_c=0.15                                                                     # Maximum cord length                                                    [m]                
Min_c=0.05                                                                     # Minimum cord length                                                    [m]               
Res_c=100                                                                      # Cordlength resolution                                                  [-/-]                
Rotorfoil='Eppler e422'                                                        # Desired rotor foil                                                     [-/-]               
Max_itt_BEM=100                                                                # maximum amount of Bem itterations                                      [-/-]                               

nu=1.51*10**-5                                                                 # Kinematic viscosity of the medium                                      [some kind of a unit]                               
rho=1.225                                                                      # Density of the medium                                                  [kg/m^3]                     

###############################################################################################################################################################################################################
################################################################################################## Calculation ################################################################################################
###############################################################################################################################################################################################################


np.set_printoptions(threshold=sys.maxsize,precision=3, suppress=True)          # adjusts the precision of the results printed to the terminal
global aa,at,itter1,var,res                                                    # This function is used several times to make certain variables global


res=[]                                                                         # Creates an empty array to store the results


def reset_inputs():                                                            # This function is used to reset certain variables after completing calculations for one segment                                    
    global aa,at,c,itter1,Max_c,res,var,blade
    aa=0
    at=0
    itter1=0

reset_inputs()

def blade (seg):                                                               # This funcion preforms the calculations for every given blade segment                                     

    global aa,at,itter1,var,res

    def segment(c):                                                            # This function preforms the calculations for every given cord length                                     

        global aa,at,itter1,var,res

        def calc(itter):                                                       # This function preforms the calculations for a given cordlenght (used to refine the axial induction)                                    

            global aa,at,itter1,var,res

            U_gen=U_free+U_free*Eff_v                                          # Calculates generative windspeed                                                [m/s]
            r=(((D_r-D_h)/2)/N_seg)*seg                                        # Calculates radius (distance from rotating axis to element)                     [m]
            Local_speedratio=(TSR/N_seg)*seg                                   # Calculates local speedratio (ratio between element speed and freewind speed)   [-/-]
            V_rot=TSR*U_gen                                                    # Calculates rotationspeed                                                       [m/s]  
            V_app=m.sqrt(((U_gen*(1-aa))**2)+((V_rot*r*(1+at))**2))            # Calculates apparent windspeed                                                  [m/s]
            Re=(V_app*c)/nu                                                    # Calculates local Reynolds number                                               [-/-]

            arr=np.array([100000,150000,200000,250000,300000,                  # List of known Reynold numbers (make sure to add a polar for every given airfoil and Re value to the polars folder)
                          350000,400000,450000,500000,550000,                
                          650000,700000,750000,800000,850000,
                          900000,950000,1000000])  
            array_diff=np.absolute(arr-Re)                                     # Subtracts the "real" reynolds number from the different given reynolds values
            index=array_diff.argmin()                                          # Checks which known reynoldnumber gives the smallest result from the function above, and gets its location in the array
            Re1=arr[index]                                                     # Gives temporary variable 'Re1' the value of the closest known reynolds number

            a_app=m.atan((U_gen*(1-aa))/(V_rot*r*(1+at)))                      # Calculates the angle of the apparent wind      [rad]
            A_rot=m.pi*(D_r/2)**2                                              # Calculates frontal area of the rotor           [m^2]
            Solidity=(Blades*c)/(2*m.pi*r)                                     # Calculates rotor solidity                      [-/-]

            handle = ("polars\\{airfoil} {Re}.dat"                             # Formats the filepath for the necessary polar
                      .format(Re = Re1, airfoil=Rotorfoil))                    

            data=pd.read_csv(handle,delim_whitespace=True,                     # Creates Panda dataframe from polar
                             skiprows=15, dtype=np.float64)
            data=np.array(data)                                                # Converts pada dataframe to numpy array

            cl_array=data[:,1]                                                 # Defines the location (column) of cL (Lift coefficient)
            cd_array=data[:,2]                                                 # Defines the location (column) of cD (Drag coefficient)

            glide_ratio=np.divide(cl_array,cd_array)                           # Calculates glideratio per AOA (cL/cD)
            clcd_opt=np.max(glide_ratio)                                       # Looks for highest glideratio as calculated from the given dataset
            index_clcd = np.where(glide_ratio == clcd_opt)                     # Gets the position (row) of the values giving the highest glideratio  

            AOA=float(data[index_clcd,0])                                      # Gets corresponding AOA at max glide ratio
            cl=float(data[index_clcd,1])                                       # Makes variable 'cl' the corresponding cL value
            cd=float(data[index_clcd,2])                                       # Makes variable 'cd' the corresponding cD value

            V_vehicle=U_free*Eff_v                                             # Calculates vehicle speed                           [m/s]
            dr=(m.pi*(r+0.0000000000001)**2)-(m.pi*(r)**2)                     # Substitute for intergral, 
                                                                                # creates thin blade slice for further calculations [-/-]

            cn=cl*(m.cos(a_app))+cd*(m.sin(a_app))                             # Calculates 'cN' (Normal force coefficient)         [-/-]
            ct=cl*(m.sin(a_app))-cd*(m.cos(a_app))                             # Calculates 'cT' (Tangential force coefficient)     [-/-]

            P=2*rho*(U_gen**3)*(aa*((1-aa)**2))*A_rot                          # Calculates turbine power                           [W]
            T=2*rho*(U_gen**2)*(aa*(1-aa))*A_rot                               # Calculates turbine thrust                          [N]

            cP=4*(aa*(1-aa)**2)                                                # Calculates turbine power coefficient               [-/-]
            cT=4*(aa*(1-aa))                                                   # Calculates turbine thrust coefficient              [-/-]

            ct_local=(T/dr)/(m.pi*rho*(U_gen**2)*r)                            # Calculates local thrust coefficient                [-/-]
            cp_local=(P/dr)/(m.pi*rho*(U_gen**3)*r)                            # Calculates local power coefficient                 [-/-]

            #aa=float(1-(abs((1/(
            # ((4*(m.sin(a_app)*m.sin(a_app)))/(Solidity*cn))+1)))))           # Temporary fix for a bug regarding the axial induction
            aa=float(abs((1/(
                ((4*(m.sin(a_app)*m.sin(a_app)))/(Solidity*cn))+1))))          # Calculates axial induction                         [-/-]
            at=float(abs(1/((
                (4*(m.cos(a_app)*m.sin(a_app)))/(Solidity*ct))-1)))            # Calculates tangential induction                    [-/-]
            c_opt=float(abs((
                (Eff_p*Eff_t)*(1+(1/(V_vehicle/U_free)))*cp_local)-ct_local))  # Calculates optimisation coefficient                [-/-]
            Twist=float(np.degrees(a_app)-float(AOA))                          # Calculates resulting element twist                 [deg]

            if itter1==Max_itt_BEM:                                            # Adds the calculated results from the last BEM itteration to the results array
                var=[seg,aa,c,Twist,c_opt]                                     # Defines which results get added to the array (you can add variabels you wish to be saved between 'aa' and 'c')                                
                for i in var:
                    res.append(i)
                    
                itter1=0  
            else:
                itter1=itter1+1

        itter=np.full((1,Max_itt_BEM),c)                                       # Determines for what values the 'itter' function is run
        function=np.vectorize(calc)
        function(itter)
    
    reset_inputs()                                                             # Resets the variables as determined in the 'reset_inputs' function
    a1=np.linspace(Min_c,Max_c,Res_c)                                          # Determines for what values the 'segment' function is run
    function=np.vectorize(segment)
    function(a1)
   
reset_inputs()                                                                 # Resets the variables as determined in the 'reset_inputs' function
a1=np.linspace(1,N_seg,N_seg)                                                  # Determines for what values the 'blade' function is run
function=np.vectorize(blade)
function(a1)
 
###############################################################################################################################################################################################################
################################################################################################## Data processing ################################################################################################
###############################################################################################################################################################################################################

res=np.array(res)                                                              # Converts results array 'res' to a numpy array

df=pd.DataFrame(res)                                                           # Defines pandas dataframe from 'res'
df.to_csv("datage.csv", sep='\t')                                              # Writes the dataframe to a .csv file

res=np.reshape(res,(((N_seg+1)*(Res_c+1)),(len(var))))                         #                                   
res=np.split(res,((N_seg+1)),axis=0)                                           # Reformats the 'res' array to make finding the maximum value of 'c_opt' easier
res=np.array(res)                                                              #
res=np.delete(res,0,axis=1)                                                    #

output=[]                                                                      # Finds maximum value of 'c_opt' and isolates the corresponding parameters                                                                  
for p in range (1,N_seg+1):
    t1=(res[p,:,-1])
    t2=np.max(t1)
    index=np.where(t1==t2)
    output.append(res[p][index][:])


output=np.array(output)                                                        #                                  
output=np.array(output)                                                        # 
output=np.squeeze(output)                                                      # Reformats output array to be more readable
output=np.rot90(output,3)                                                      #
output=np.flip(output,1)    	                                               #

seg_res=output[0][:]                                                           #                           
a_res=output[-2][:]                                                            # Isolates results from output array for making the resulting plots          
c_res=output[-3][:]                                                            #

a_res_uni=uniform_filter1d(a_res, size=5)                                      # Uses 1D filter to make trendline of average values
c_res_uni=uniform_filter1d(c_res, size=5)                                      #
print("Twist: ",a_res_uni)                                                     # Prints resulting twist values to terminal
print("Koordenlengten: ",c_res_uni)                                            # Prints resulting cord values to terminal

fig,(axs1,axs2)=plt.subplots(2)                                                #
fig.suptitle('StoefoeBlade')                                                   #
axs1.plot(seg_res,c_res*1000,'o')                                              # Creates the resulting plot
axs1.plot(seg_res,c_res_uni*1000)                                              #
axs1.set(ylabel='Cord Length [mm]')                                            #

axs2.plot(seg_res,a_res,'o')
axs2.plot(seg_res,a_res_uni)
axs2.set(xlabel='Segment Nr', ylabel='Twist Angle [deg]')

plt.show()