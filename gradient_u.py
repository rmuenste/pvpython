#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

main16926pvtu = GetActiveSource()

# create a new 'Gradient Of Unstructured DataSet'
gradientOfUnstructuredDataSet1 = GradientOfUnstructuredDataSet(registrationName='GradientOfUnstructuredDataSet1', Input=main16926pvtu)

# Properties modified on gradientOfUnstructuredDataSet1
gradientOfUnstructuredDataSet1.ScalarArray = ['POINTS', 'Velocity']

UpdatePipeline(time=0.0, proxy=gradientOfUnstructuredDataSet1)

# create a new 'Calculator'
calculator1 = Calculator(registrationName='Calculator1', Input=gradientOfUnstructuredDataSet1)
calculator1.AttributeType = 'Point Data'

# Properties modified on calculator1
calculator1.ResultArrayName = 'dudx'
calculator1.Function = 'Gradients_0'

UpdatePipeline(time=0.0, proxy=calculator1)

# create a new 'Calculator'
calculator2 = Calculator(registrationName='Calculator2', Input=calculator1)
calculator2.AttributeType = 'Point Data'

# Properties modified on calculator2
calculator2.ResultArrayName = 'dudy'
calculator2.Function = 'Gradients_1'

UpdatePipeline(time=0.0, proxy=calculator2)

# create a new 'Calculator'
calculator3 = Calculator(registrationName='Calculator3', Input=calculator2)
calculator3.AttributeType = 'Point Data'

# Properties modified on calculator3
calculator3.ResultArrayName = 'dudz'
calculator3.Function = 'Gradients_2'

UpdatePipeline(time=0.0, proxy=calculator3)

# create a new 'Calculator'
calculator4 = Calculator(registrationName='Calculator4', Input=calculator3)
calculator4.AttributeType = 'Point Data'

# Properties modified on calculator4
calculator4.ResultArrayName = 'dvdx'
calculator4.Function = 'Gradients_3'

UpdatePipeline(time=0.0, proxy=calculator4)

# create a new 'Calculator'
calculator5 = Calculator(registrationName='Calculator5', Input=calculator4)
calculator5.AttributeType = 'Point Data'

# Properties modified on calculator5
calculator5.ResultArrayName = 'dvdy'
calculator5.Function = 'Gradients_4'

UpdatePipeline(time=0.0, proxy=calculator5)

# create a new 'Calculator'
calculator6 = Calculator(registrationName='Calculator6', Input=calculator5)
calculator6.AttributeType = 'Point Data'

# Properties modified on calculator6
calculator6.ResultArrayName = 'dvdz'
calculator6.Function = 'Gradients_5'

UpdatePipeline(time=0.0, proxy=calculator6)

# create a new 'Calculator'
calculator7 = Calculator(registrationName='Calculator7', Input=calculator6)
calculator7.AttributeType = 'Point Data'

# Properties modified on calculator7
calculator7.ResultArrayName = 'dwdx'
calculator7.Function = 'Gradients_6'

UpdatePipeline(time=0.0, proxy=calculator7)

# create a new 'Calculator'
calculator8 = Calculator(registrationName='Calculator8', Input=calculator7)
calculator8.AttributeType = 'Point Data'

# Properties modified on calculator8
calculator8.ResultArrayName = 'dwdy'
calculator8.Function = 'Gradients_7'

UpdatePipeline(time=0.0, proxy=calculator8)

# create a new 'Calculator'
calculator9 = Calculator(registrationName='Calculator9', Input=calculator8)
calculator9.AttributeType = 'Point Data'

# Properties modified on calculator8
calculator9.ResultArrayName = 'dwdz'
calculator9.Function = 'Gradients_8'

UpdatePipeline(time=0.0, proxy=calculator9)

# create a new 'Calculator'
calculator10 = Calculator(registrationName='Calculator10', Input=calculator9)
calculator10.AttributeType = 'Point Data'

# Properties modified on calculator10
calculator10.ResultArrayName = 'u1'
calculator10.Function = 'Velocity_X'

UpdatePipeline(time=0.0, proxy=calculator10)

# create a new 'Calculator'
calculator11 = Calculator(registrationName='Calculator11', Input=calculator10)
calculator11.AttributeType = 'Point Data'

# Properties modified on calculator11
calculator11.ResultArrayName = 'u2'
calculator11.Function = 'Velocity_Y'

UpdatePipeline(time=0.0, proxy=calculator11)

# create a new 'Calculator'
calculator12 = Calculator(registrationName='Calculator12', Input=calculator11)
calculator12.AttributeType = 'Point Data'

# Properties modified on calculator11
calculator12.ResultArrayName = 'u3'
calculator12.Function = 'Velocity_Z'

UpdatePipeline(time=0.0, proxy=calculator12)

# set active source
SetActiveSource(calculator12)

# create a new 'Calculator'
calculator13 = Calculator(registrationName='Calculator13', Input=calculator12)
calculator13.AttributeType = 'Point Data'

# Properties modified on calculator12
calculator13.ResultArrayName = 'U1'
calculator13.Function = 'BigU_X'

UpdatePipeline(time=0.0, proxy=calculator13)

# create a new 'Calculator'
calculator14 = Calculator(registrationName='Calculator14', Input=calculator13)
calculator14.AttributeType = 'Point Data'

# Properties modified on calculator13
calculator14.ResultArrayName = 'U2'
calculator14.Function = 'BigU_Y'

UpdatePipeline(time=0.0, proxy=calculator14)

# create a new 'Calculator'
calculator15 = Calculator(registrationName='Calculator15', Input=calculator14)
calculator15.AttributeType = 'Point Data'

# Properties modified on calculator14
calculator15.ResultArrayName = 'U3'
calculator15.Function = 'BigU_Z'

UpdatePipeline(time=0.0, proxy=calculator15)

# set active source
SetActiveSource(calculator15)

# create a new 'Gradient Of Unstructured DataSet'
gradientOfUnstructuredDataSet2 = GradientOfUnstructuredDataSet(registrationName='GradientOfUnstructuredDataSet2', Input=calculator15)

# Properties modified on gradientOfUnstructuredDataSet2
gradientOfUnstructuredDataSet2.ScalarArray = ['POINTS', 'BigU']
gradientOfUnstructuredDataSet2.ResultArrayName = 'GradientBigU'

UpdatePipeline(time=0.0, proxy=gradientOfUnstructuredDataSet2)

# create a new 'Calculator'
calculator13 = Calculator(registrationName='Calculator13', Input=gradientOfUnstructuredDataSet2)

# Properties modified on calculator13
calculator13.ResultArrayName = 'dUdx'
calculator13.Function = 'GradientBigU_0'

UpdatePipeline(time=0.0, proxy=calculator13)

# create a new 'Calculator'
calculator14 = Calculator(registrationName='Calculator14', Input=calculator13)

# Properties modified on calculator14
calculator14.ResultArrayName = 'dUdy'
calculator14.Function = 'GradientBigU_1'

UpdatePipeline(time=0.0, proxy=calculator14)

# create a new 'Calculator'
calculator15 = Calculator(registrationName='Calculator15', Input=calculator14)

# Properties modified on calculator15
calculator15.ResultArrayName = 'dUdz'
calculator15.Function = 'GradientBigU_2'

UpdatePipeline(time=0.0, proxy=calculator15)

# create a new 'Calculator'
calculator16 = Calculator(registrationName='Calculator16', Input=calculator15)

# Properties modified on calculator16
calculator16.ResultArrayName = 'dVdx'
calculator16.Function = 'GradientBigU_3'

UpdatePipeline(time=0.0, proxy=calculator16)

# set active source
SetActiveSource(calculator15)

# set active source
SetActiveSource(calculator16)

# create a new 'Calculator'
calculator17 = Calculator(registrationName='Calculator17', Input=calculator16)

# Properties modified on calculator17
calculator17.ResultArrayName = 'dVdy'
calculator17.Function = 'GradientBigU_4'

UpdatePipeline(time=0.0, proxy=calculator17)

# set active source
SetActiveSource(calculator16)

# set active source
SetActiveSource(calculator17)

# create a new 'Calculator'
calculator18 = Calculator(registrationName='Calculator18', Input=calculator17)

# Properties modified on calculator18
calculator18.ResultArrayName = 'dVdz'
calculator18.Function = 'GradientBigU_5'

UpdatePipeline(time=0.0, proxy=calculator18)

# create a new 'Calculator'
calculator19 = Calculator(registrationName='Calculator19', Input=calculator18)

# Properties modified on calculator19
calculator19.ResultArrayName = 'dWdx'
calculator19.Function = 'GradientBigU_6'

UpdatePipeline(time=0.0, proxy=calculator19)

# create a new 'Calculator'
calculator20 = Calculator(registrationName='Calculator20', Input=calculator19)

# Properties modified on calculator20
calculator20.ResultArrayName = 'dWdy'
calculator20.Function = 'GradientBigU_7'

UpdatePipeline(time=0.0, proxy=calculator20)

# create a new 'Calculator'
calculator21 = Calculator(registrationName='Calculator21', Input=calculator20)

# Properties modified on calculator21
calculator21.ResultArrayName = 'dWdz'
calculator21.Function = 'GradientBigU_8'

UpdatePipeline(time=0.0, proxy=calculator21)


# create a new 'Programmable Filter'
programmableFilter1_1 = ProgrammableFilter(registrationName='ProgrammableFilter1', Input=calculator21)

# Properties modified on programmableFilter1_1
programmableFilter1_1.Script = """from paraview.vtk.numpy_interface import dataset_adapter as dsa
import numpy as np

input0 = inputs[0]
numPoints = input0.GetNumberOfPoints() #

u1 = inputs[0].PointData["u1"] 
u2 = inputs[0].PointData["u2"]
u3 = inputs[0].PointData["u3"]

dudx = inputs[0].PointData["dudx"]
dudy = inputs[0].PointData["dudy"]
dudz = inputs[0].PointData["dudz"]

dvdx = inputs[0].PointData["dvdx"]
dvdy = inputs[0].PointData["dvdy"]
dvdz = inputs[0].PointData["dvdz"]

dwdx = inputs[0].PointData["dwdx"]
dwdy = inputs[0].PointData["dwdy"]
dwdz = inputs[0].PointData["dwdz"]

unu1 = u1 * dudx + u2 * dudy + u3 * dudz 
unu2 = u1 * dvdx + u2 * dvdy + u3 * dvdz 
unu3 = u1 * dwdx + u2 * dwdy + u3 * dwdz

U1 = inputs[0].PointData["U1"] 
U2 = inputs[0].PointData["U2"]
U3 = inputs[0].PointData["U3"]

dUdx = inputs[0].PointData["dUdx"]
dUdy = inputs[0].PointData["dUdy"]
dUdz = inputs[0].PointData["dUdz"]

dVdx = inputs[0].PointData["dVdx"]
dVdy = inputs[0].PointData["dVdy"]
dVdz = inputs[0].PointData["dVdz"]

dWdx = inputs[0].PointData["dWdx"]
dWdy = inputs[0].PointData["dWdy"]
dWdz = inputs[0].PointData["dWdz"]

Bigunu1 = U1 * dUdx + U2 * dUdy + U3 * dUdz 
Bigunu2 = U1 * dVdx + U2 * dVdy + U3 * dVdz 
Bigunu3 = U1 * dWdx + U2 * dWdy + U3 * dWdz

unu1d = unu1 - Bigunu1
unu2d = unu2 - Bigunu2
unu3d = unu3 - Bigunu3

dotU = unu1 * u1 + unu2 * u2 + unu3 * u3

dotBigU = unu1d * U1 + unu2d * U2 + unu3d * U3

# Add the new array to the output
output.PointData.append(unu1, "u_nabla_u1")
output.PointData.append(unu2, "u_nabla_u2")
output.PointData.append(unu3, "u_nabla_u3")

# Add the new array to the output
output.PointData.append(Bigunu1, "Big_u_nabla_u1")
output.PointData.append(Bigunu2, "Big_u_nabla_u2")
output.PointData.append(Bigunu3, "Big_u_nabla_u3")

# Add the new array to the output
output.PointData.append(unu1d, "uU_diff")
output.PointData.append(unu2d, "uU_diff")
output.PointData.append(unu3d, "uU_diff")

output.PointData.append(dotBigU, "u_gradu_dotBigU")
output.PointData.append(dotU, "u_gradu_dotu")"""

programmableFilter1_1.RequestInformationScript = ''
programmableFilter1_1.RequestUpdateExtentScript = ''
programmableFilter1_1.CopyArrays = 1
programmableFilter1_1.PythonPath = ''

UpdatePipeline(time=0.0, proxy=programmableFilter1_1)


# create a new 'Programmable Filter'
programmableFilter1_2 = ProgrammableFilter(registrationName='ProgrammableFilter3', Input=programmableFilter1_1)

# Properties modified on programmableFilter1_1
programmableFilter1_2.Script = """from paraview.vtk.numpy_interface import dataset_adapter as dsa
import numpy
def make_tensor(xx,yy,zz, xy, yz, xz):
  t = numpy.vstack([xx,yy,zz,xy, yz, xz]).transpose().view(dsa.VTKArray)
  t.DataSet = xx.DataSet
  t.Association = xx.Association
  return t

input0 = inputs[0]

xx = inputs[0].PointData["dUdx"]
yy = inputs[0].PointData["dVdy"]
zz = inputs[0].PointData["dWdz"]
xy = (inputs[0].PointData["dUdy"] + inputs[0].PointData["dVdx"]) * 0.5
yz = (inputs[0].PointData["dVdz"] + inputs[0].PointData["dWdy"]) * 0.5
xz = (inputs[0].PointData["dUdz"] + inputs[0].PointData["dWdx"]) * 0.5

DDProd = xx * xx + yy * yy + zz * zz + 2.0 * xy * xy + 2.0 * xz * xz + 2.0 * yz * yz 
# Add the new array to the output
output.PointData.append(make_tensor(xx,yy,zz,xy,yz,xz), "D(U)")"""

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
calculator22 = Calculator(registrationName='Calculator22', Input=meshQuality1)
calculator22.AttributeType = 'Cell Data'
calculator22.Function = ''

# Properties modified on calculator10
calculator22.ResultArrayName = 'vol'
calculator22.Function = 'abs(Quality)'

UpdatePipeline(time=0.0, proxy=calculator22)

# create a new 'Python Calculator'
pythonCalculator1 = PythonCalculator(registrationName='PythonCalculator1', Input=calculator22)
pythonCalculator1.Expression = ''
pythonCalculator1.ArrayAssociation = 'Cell Data'

# Properties modified on pythonCalculator1
pythonCalculator1.Expression = 'sum(u_gradu_dotBigU*vol)'
pythonCalculator1.ArrayName = 'Ueff'

UpdatePipeline(time=0.0, proxy=pythonCalculator1)

# create a new 'Programmable Filter'
programmableFilter2 = ProgrammableFilter(registrationName='ProgrammableFilter2', Input=pythonCalculator1)
programmableFilter2.Script = ''
programmableFilter2.RequestInformationScript = ''
programmableFilter2.RequestUpdateExtentScript = ''
programmableFilter2.PythonPath = ''

# Properties modified on programmableFilter2
programmableFilter2.Script =f"""
inp = self.GetInput()
out = self.GetOutput()

numCells  = inp.GetNumberOfCells()
data = inp.GetCellData().GetArray("Ueff")

i = 0
t = inp.GetInformation().Get(vtk.vtkDataObject.DATA_TIME_STEP())
val = data.GetValue(i)
print("val: ", val, t)
"""

programmableFilter2.RequestInformationScript = ''
programmableFilter2.RequestUpdateExtentScript = ''
programmableFilter2.CopyArrays = 1
programmableFilter2.PythonPath = ''

UpdatePipeline(time=0.0, proxy=programmableFilter2)