import numpy as np

input0 = inputs[0]

u1 = inputs[0].PointData["du_Udx"]
u2 = inputs[0].PointData["du_Udy"]
u3 = inputs[0].PointData["du_Udz"]

v1 = inputs[0].PointData["dv_Vdx"]
v2 = inputs[0].PointData["dv_Vdy"]
v3 = inputs[0].PointData["dv_Vdz"]

w1 = inputs[0].PointData["dw_Wdx"]
w2 = inputs[0].PointData["dw_Wdy"]
w3 = inputs[0].PointData["dw_Wdz"]

#M = np.array([[u1, u2, u3],[v1, v2, v3],[w1, w2, w3]])
#print(M.shape)
#u = inputs[0].PointData["Velocity"]
#print(u.shape)
#u_t = np.matmul(M,u)
#print(u_t.shape)
#DDProd = 1
## Add the new array to the output
##output.PointData.append(make_tensor(xx,yy,zz,xy,yz,xz), "DefTensor2")
#output.PointData.append(DDProd, "FakeValue")