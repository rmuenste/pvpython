
#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

main16926pvtu = GetActiveSource()

# create a new 'Gradient Of Unstructured DataSet'
gradientOfUnstructuredDataSet1 = GradientOfUnstructuredDataSet(registrationName='GradientOfUnstructuredDataSet1', Input=main16926pvtu)

# Properties modified on gradientOfUnstructuredDataSet1
gradientOfUnstructuredDataSet1.ScalarArray = ['POINTS', 'Velocity']
gradientOfUnstructuredDataSet1.ResultArrayName = 'Gradients'

UpdatePipeline(time=0.0, proxy=gradientOfUnstructuredDataSet1)

# create a new 'Gradient Of Unstructured DataSet'
gradientOfUnstructuredDataSet2 = GradientOfUnstructuredDataSet(registrationName='GradientOfUnstructuredDataSet2', Input=gradientOfUnstructuredDataSet1)

# Properties modified on gradientOfUnstructuredDataSet2
gradientOfUnstructuredDataSet2.ScalarArray = ['POINTS', 'BigU']
gradientOfUnstructuredDataSet2.ResultArrayName = 'GradientBigU'

UpdatePipeline(time=0.0, proxy=gradientOfUnstructuredDataSet2)

##########################################
# create a new 'Programmable Filter'
programmableFilter1_1 = ProgrammableFilter(registrationName='ProgrammableFilter1', Input=gradientOfUnstructuredDataSet2)

# Properties modified on programmableFilter1_1
programmableFilter1_1.Script = """from paraview.vtk.numpy_interface import dataset_adapter as dsa
import numpy as np

input0 = inputs[0]
numPoints = input0.GetNumberOfPoints() #

u1 = inputs[0].PointData["Velocity"][:,0] 
u2 = inputs[0].PointData["Velocity"][:,1]
u3 = inputs[0].PointData["Velocity"][:,2]

dx = inputs[0].PointData["Gradients"][:,0]
dudx = inputs[0].PointData["Gradients"][:,0,0]
dvdx = inputs[0].PointData["Gradients"][:,0,1]
dwdx = inputs[0].PointData["Gradients"][:,0,2]

dy = inputs[0].PointData["Gradients"][:,1]
dudy = inputs[0].PointData["Gradients"][:,1,0]
dvdy = inputs[0].PointData["Gradients"][:,1,1]
dwdy = inputs[0].PointData["Gradients"][:,1,2]

dz = inputs[0].PointData["Gradients"][:,2]
dudz = inputs[0].PointData["Gradients"][:,2,0]
dvdz = inputs[0].PointData["Gradients"][:,2,1]
dwdz = inputs[0].PointData["Gradients"][:,2,2]

####################################################

# u nabla u
u_n_u1 = u1 * dudx + u2 * dudy + u3 * dudz
u_n_u2 = u1 * dvdx + u2 * dvdy + u3 * dvdz
u_n_u3 = u1 * dwdx + u2 * dwdy + u3 * dwdz


####################################################

U1 = inputs[0].PointData["BigU"][:,0] 
U2 = inputs[0].PointData["BigU"][:,1]
U3 = inputs[0].PointData["BigU"][:,2]

dUdx = inputs[0].PointData["GradientBigU"][:,0,0]
dVdx = inputs[0].PointData["GradientBigU"][:,0,1]
dWdx = inputs[0].PointData["GradientBigU"][:,0,2]

dUdy = inputs[0].PointData["GradientBigU"][:,1,0]
dVdy = inputs[0].PointData["GradientBigU"][:,1,1]
dWdy = inputs[0].PointData["GradientBigU"][:,1,2]

dUdz = inputs[0].PointData["GradientBigU"][:,2,0]
dVdz = inputs[0].PointData["GradientBigU"][:,2,1]
dWdz = inputs[0].PointData["GradientBigU"][:,2,2]

####################################################

U_n_U1 = U1 * dUdx + U2 * dUdy + U3 * dUdz
U_n_U2 = U1 * dVdx + U2 * dVdy + U3 * dVdz
U_n_U3 = U1 * dWdx + U2 * dWdy + U3 * dWdz

####################################################

udiffU1 = u_n_u1 - U_n_U1
udiffU2 = u_n_u2 - U_n_U2
udiffU3 = u_n_u3 - U_n_U3

#udiffU1 = udiffU1 * U1 
#udiffU2 = udiffU2 * U2 
#udiffU3 = udiffU3 * U3 

dotProd = udiffU1 * U1 + udiffU2 * U2 + udiffU3 * U3 

output.PointData.append(dotProd, "uGradUDotU")

# u nabla u
output.PointData.append(u_n_u1, "u_n_u1")
output.PointData.append(u_n_u2, "u_n_u2")
output.PointData.append(u_n_u3, "u_n_u3")

# U nabla U
output.PointData.append(U_n_U1, "U_n_U1")
output.PointData.append(U_n_U2, "U_n_U2")
output.PointData.append(U_n_U3, "U_n_U3")

# u gradient single component
output.PointData.append(dudx, "dudx")
output.PointData.append(dvdx, "dvdx")
output.PointData.append(dwdx, "dwdx")

output.PointData.append(dudy, "dudy")
output.PointData.append(dvdy, "dvdy")
output.PointData.append(dwdy, "dwdy")

output.PointData.append(dudz, "dudz")
output.PointData.append(dvdz, "dvdz")
output.PointData.append(dwdz, "dwdz")

# BigU gradient single component
output.PointData.append(dUdx, "dUdx")
output.PointData.append(dVdx, "dVdx")
output.PointData.append(dWdx, "dWdx")

output.PointData.append(dUdy, "dUdy")
output.PointData.append(dVdy, "dVdy")
output.PointData.append(dWdy, "dWdy")

output.PointData.append(dUdz, "dUdz")
output.PointData.append(dVdz, "dVdz")
output.PointData.append(dWdz, "dWdz")

# Add the new array to the output
output.PointData.append(u1, "u1")
output.PointData.append(u2, "u2")
output.PointData.append(u3, "u3")

output.PointData.append(U1, "U1")
output.PointData.append(U2, "U2")
output.PointData.append(U3, "U3")

u_U1=u1 - U1
u_U2=u2 - U2
u_U3=u3 - U3

# Create an empty 3D vector array
udiff = vtk.vtkDoubleArray()
udiff.SetNumberOfComponents(3)
udiff.SetNumberOfTuples(numPoints)
udiff.SetName('udiff')

# Fill the vector array with values from the scalar arrays
for i in range(numPoints):
    udiff.SetTuple3(i, u_U1[i], u_U2[i], u_U3[i])


output.PointData.append(U1, "U1")
output.PointData.append(U2, "U2")
output.PointData.append(U3, "U3")

output.PointData.append(u_U1, "u_U1")
output.PointData.append(u_U2, "u_U2")
output.PointData.append(u_U3, "u_U3")
output.GetPointData().AddArray(udiff)
"""

programmableFilter1_1.RequestInformationScript = ''
programmableFilter1_1.RequestUpdateExtentScript = ''
programmableFilter1_1.CopyArrays = 1
programmableFilter1_1.PythonPath = ''

UpdatePipeline(time=0.0, proxy=programmableFilter1_1)

# create a new 'Gradient Of Unstructured DataSet'
gradientOfUnstructuredDataSet3 = GradientOfUnstructuredDataSet(registrationName='GradientOfUnstructuredDataSet2', Input=programmableFilter1_1)

# Properties modified on gradientOfUnstructuredDataSet2
gradientOfUnstructuredDataSet3.ScalarArray = ['POINTS', 'udiff']
gradientOfUnstructuredDataSet3.ResultArrayName = 'GradientuU'

UpdatePipeline(time=0.0, proxy=gradientOfUnstructuredDataSet3)

# create a new 'Programmable Filter'
programmableFilter1_2 = ProgrammableFilter(registrationName='ProgrammableFilter3', Input=gradientOfUnstructuredDataSet3)

# Properties modified on programmableFilter1_1
programmableFilter1_2.Script = """from paraview.vtk.numpy_interface import dataset_adapter as dsa
import numpy
def make_tensor(xx,yy,zz, xy, yz, xz):
  t = numpy.vstack([xx,yy,zz,xy, yz, xz]).transpose().view(dsa.VTKArray)
  t.DataSet = xx.DataSet
  t.Association = xx.Association
  return t

input0 = inputs[0]

dudx = inputs[0].PointData["GradientuU"][:,0,0]
dvdx = inputs[0].PointData["GradientuU"][:,0,1]
dwdx = inputs[0].PointData["GradientuU"][:,0,2]

dudy = inputs[0].PointData["GradientuU"][:,1,0]
dvdy = inputs[0].PointData["GradientuU"][:,1,1]
dwdy = inputs[0].PointData["GradientuU"][:,1,2]

dudz = inputs[0].PointData["GradientuU"][:,2,0]
dvdz = inputs[0].PointData["GradientuU"][:,2,1]
dwdz = inputs[0].PointData["GradientuU"][:,2,2]

xx = dudx 
yy = dvdy 
zz = dwdz 
xy = (dudy + dvdx) * 0.5
yz = (dvdz + dwdy) * 0.5
xz = (dudz + dwdx) * 0.5

xxB = inputs[0].PointData["dUdx"]
yyB = inputs[0].PointData["dVdy"]
zzB = inputs[0].PointData["dWdz"]
xyB = (inputs[0].PointData["dUdy"] + inputs[0].PointData["dVdx"]) * 0.5
yzB = (inputs[0].PointData["dVdz"] + inputs[0].PointData["dWdy"]) * 0.5
xzB = (inputs[0].PointData["dUdz"] + inputs[0].PointData["dWdx"]) * 0.5

DDProd = xx * xxB + yy * yyB + zz * zzB + 2.0 * xy * xyB + 2.0 * xz * xzB + 2.0 * yz * yzB 

####################################################################
xxD = inputs[0].PointData["dUdx"]
yyD = inputs[0].PointData["dVdy"]
zzD = inputs[0].PointData["dWdz"]
xyD = (inputs[0].PointData["dUdy"] + inputs[0].PointData["dVdx"]) * 0.5
yzD = (inputs[0].PointData["dVdz"] + inputs[0].PointData["dWdy"]) * 0.5
xzD = (inputs[0].PointData["dUdz"] + inputs[0].PointData["dWdx"]) * 0.5

denominator = xxD * xxD + yyD * yyD + zzD * zzD + 2.0 * xyD * xyD + 2.0 * xzD * xzD + 2.0 * yzD * yzD 

# Add the new array to the output
output.PointData.append(denominator, "denominator")
output.PointData.append(DDProd, "DoubleDot")
output.PointData.append(make_tensor(xxB,yyB,zzB,xyB,yzB,xzB), "D(U)")
output.PointData.append(make_tensor(xx,yy,zz,xy,yz,xz), "D(u-U)")"""

programmableFilter1_2.RequestInformationScript = ''
programmableFilter1_2.RequestUpdateExtentScript = ''
programmableFilter1_2.CopyArrays = 1
programmableFilter1_2.PythonPath = ''

UpdatePipeline(time=0.0, proxy=programmableFilter1_2)

# create a new 'Point Data to Cell Data'
pointDatatoCellData1 = PointDatatoCellData(registrationName='pointDatatoCellData1', Input=programmableFilter1_2)

UpdatePipeline(time=0.0, proxy=pointDatatoCellData1)

# create a new 'Mesh Quality'
meshQuality1 = MeshQuality(registrationName='MeshQuality1', Input=pointDatatoCellData1)

# Properties modified on meshQuality1
meshQuality1.HexQualityMeasure = 'Volume'

UpdatePipeline(time=0.0, proxy=meshQuality1)

# create a new 'Calculator'
calculator10 = Calculator(registrationName='Calculator10', Input=meshQuality1)
calculator10.AttributeType = 'Cell Data'
calculator10.Function = ''

# Properties modified on calculator10
calculator10.ResultArrayName = 'vol'
calculator10.Function = 'abs(Quality)'

UpdatePipeline(time=0.0, proxy=calculator10)

# create a new 'Programmable Filter'
programmableFilter4 = ProgrammableFilter(registrationName='ProgrammableFilter4', Input=calculator10)

# Properties modified on programmableFilter1_1
programmableFilter4.Script =f"""
import numpy as np

inp = self.GetInput()
out = self.GetOutput()

input0 = inputs[0]

numCells  = inp.GetNumberOfCells()

# Get arrays
u = input0.CellData['uGradUDotU']
denom = input0.CellData['denominator']
DoubleDot = input0.CellData['DoubleDot']
vol = input0.CellData['vol']

# Convective term
array_sum = np.sum(u * vol)

# Double Dot term
sum2 = 0.1 * np.sum(DoubleDot*vol)

# Denominator
d = np.sum(denom*vol)

i = 0
t = inp.GetInformation().Get(vtk.vtkDataObject.DATA_TIME_STEP())
val = (array_sum + sum2)
print("(u Nabla U) * U = ", array_sum, t)
print("D(u-U):D(U) = ", sum2, t)
print("nominator = ", val, t)
print("denominator = ", d, t)
print("SigmaP = ", val/d, t)
print("mu_eff = ", 0.1 + val/d, t)
"""

programmableFilter4.RequestInformationScript = ''
programmableFilter4.RequestUpdateExtentScript = ''
programmableFilter4.CopyArrays = 1
programmableFilter4.PythonPath = ''

UpdatePipeline(time=0.0, proxy=programmableFilter4)

