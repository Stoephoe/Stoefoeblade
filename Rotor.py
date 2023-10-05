import main
import math as m
import numpy as np

cl=main.cl
cd=main.cd
a_app=main.a_app
rho=main.rho
U_free=main.U_free
U_gen=main.U_gen
aa=main.aa
A_rot=main.A_rot
r=main.r
Eff_p=main.Eff_p
Eff_t=main.Eff_t
Eff_v=main.Eff_v
a_app=main.a_app
solidity=main.Solidity



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

aa=float(abs((1/(((4*(m.sin(a_app)*m.sin(a_app)))/(solidity*cn))+1))))          
at=float(abs(1/(((4*(m.cos(a_app)*m.sin(a_app)))/(solidity*ct))-1)))          
c_opt=float(abs(((Eff_p*Eff_t)*(1+(1/(V_vehicle/U_free)))*cp_local)-ct_local))


print(c_opt)