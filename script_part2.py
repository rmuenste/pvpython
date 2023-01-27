# trace generated using paraview version 5.9.1

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# find source
main16926pvtu = FindSource('main.16926.pvtu')

# create a new 'Gradient Of Unstructured DataSet'
gradientOfUnstructuredDataSet1 = GradientOfUnstructuredDataSet(registrationName='GradientOfUnstructuredDataSet1', Input=main16926pvtu)

# Properties modified on gradientOfUnstructuredDataSet1
gradientOfUnstructuredDataSet1.ScalarArray = ['POINTS', 'Velocity']

UpdatePipeline(time=0.0, proxy=gradientOfUnstructuredDataSet1)

# create a new 'Point Data to Cell Data'
pointDatatoCellData1 = PointDatatoCellData(registrationName='PointDatatoCellData1', Input=gradientOfUnstructuredDataSet1)

UpdatePipeline(time=0.0, proxy=pointDatatoCellData1)

# create a new 'Calculator'
calculator1 = Calculator(registrationName='Calculator1', Input=pointDatatoCellData1)
calculator1.AttributeType = 'Cell Data'

# Properties modified on calculator1
calculator1.ResultArrayName = 'dudx'
calculator1.Function = 'Gradients_0'

UpdatePipeline(time=0.0, proxy=calculator1)

# create a new 'Calculator'
calculator2 = Calculator(registrationName='Calculator2', Input=calculator1)
calculator2.AttributeType = 'Cell Data'

# Properties modified on calculator2
calculator2.ResultArrayName = 'dudy'
calculator2.Function = 'Gradients_1'

UpdatePipeline(time=0.0, proxy=calculator2)

# create a new 'Calculator'
calculator3 = Calculator(registrationName='Calculator3', Input=calculator2)
calculator3.AttributeType = 'Cell Data'

# Properties modified on calculator3
calculator3.ResultArrayName = 'dudz'
calculator3.Function = 'Gradients_2'

UpdatePipeline(time=0.0, proxy=calculator3)

# create a new 'Calculator'
calculator4 = Calculator(registrationName='Calculator4', Input=calculator3)
calculator4.AttributeType = 'Cell Data'

# Properties modified on calculator4
calculator4.ResultArrayName = 'dvdx'
calculator4.Function = 'Gradients_3'

UpdatePipeline(time=0.0, proxy=calculator4)

# create a new 'Calculator'
calculator5 = Calculator(registrationName='Calculator5', Input=calculator4)
calculator5.AttributeType = 'Cell Data'

# Properties modified on calculator5
calculator5.ResultArrayName = 'dvdy'
calculator5.Function = 'Gradients_4'

UpdatePipeline(time=0.0, proxy=calculator5)

# create a new 'Calculator'
calculator6 = Calculator(registrationName='Calculator6', Input=calculator5)
calculator6.AttributeType = 'Cell Data'

# Properties modified on calculator6
calculator6.ResultArrayName = 'dvdz'
calculator6.Function = 'Gradients_5'

UpdatePipeline(time=0.0, proxy=calculator6)

# create a new 'Calculator'
calculator7 = Calculator(registrationName='Calculator7', Input=calculator6)
calculator7.AttributeType = 'Cell Data'

# Properties modified on calculator7
calculator7.ResultArrayName = 'dwdx'
calculator7.Function = 'Gradients_6'

UpdatePipeline(time=0.0, proxy=calculator7)

# create a new 'Calculator'
calculator8 = Calculator(registrationName='Calculator8', Input=calculator7)
calculator8.AttributeType = 'Cell Data'

# Properties modified on calculator8
calculator8.ResultArrayName = 'dwdy'
calculator8.Function = 'Gradients_7'

UpdatePipeline(time=0.0, proxy=calculator8)

# create a new 'Calculator'
calculator9 = Calculator(registrationName='Calculator9', Input=calculator8)
calculator9.AttributeType = 'Cell Data'

# Properties modified on calculator8
calculator9.ResultArrayName = 'dwdz'
calculator9.Function = 'Gradients_8'

UpdatePipeline(time=0.0, proxy=calculator9)

# set active source
SetActiveSource(calculator9)

# create a new 'Programmable Filter'
programmableFilter1_1 = ProgrammableFilter(registrationName='ProgrammableFilter1', Input=calculator9)

# Properties modified on programmableFilter1_1
programmableFilter1_1.Script = """from paraview.vtk.numpy_interface import dataset_adapter as dsa
import numpy
def make_tensor(xx,yy,zz, xy, yz, xz):
  t = numpy.vstack([xx,yy,zz,xy, yz, xz]).transpose().view(dsa.VTKArray)
  t.DataSet = xx.DataSet
  t.Association = xx.Association
  return t

input0 = inputs[0]

grads = input0.CellData["Gradients"]
xx = inputs[0].CellData["dudx"]
yy = inputs[0].CellData["dvdy"]
zz = inputs[0].CellData["dwdz"]
xy = (inputs[0].CellData["dudy"] + inputs[0].CellData["dvdx"]) * 0.5
yz = (inputs[0].CellData["dvdz"] + inputs[0].CellData["dwdy"]) * 0.5
xz = (inputs[0].CellData["dudz"] + inputs[0].CellData["dwdx"]) * 0.5

DDProd = xx * xx + yy * yy + zz * zz + 2.0 * xy * xy + 2.0 * xz * xz + 2.0 * yz * yz 
# Add the new array to the output
output.CellData.append(make_tensor(xx,yy,zz,xy,yz,xz), "DefTensor")
output.CellData.append(DDProd, "DoubleDot")"""

programmableFilter1_1.RequestInformationScript = ''
programmableFilter1_1.RequestUpdateExtentScript = ''
programmableFilter1_1.CopyArrays = 1
programmableFilter1_1.PythonPath = ''

UpdatePipeline(time=0.0, proxy=programmableFilter1_1)

# create a new 'Mesh Quality'
meshQuality1 = MeshQuality(registrationName='MeshQuality1', Input=programmableFilter1_1)

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

# create a new 'Python Calculator'
pythonCalculator1 = PythonCalculator(registrationName='PythonCalculator1', Input=calculator10)
pythonCalculator1.Expression = ''
pythonCalculator1.ArrayAssociation = 'Cell Data'

# Properties modified on pythonCalculator1
pythonCalculator1.Expression = 'sum(DoubleDot*vol)*2.0/729.0'
pythonCalculator1.ArrayName = 'NormShearSqr'

UpdatePipeline(time=0.0, proxy=pythonCalculator1)

# create a new 'Calculator'
calculator11 = Calculator(registrationName='Calculator11', Input=pythonCalculator1)
calculator11.AttributeType = 'Cell Data'

# Properties modified on calculator11
calculator11.ResultArrayName = 'AvgShearRate'
calculator11.Function = 'sqrt(NormShearSqr)'

UpdatePipeline(time=0.0, proxy=calculator11)


# create a new 'Programmable Filter'
programmableFilter2 = ProgrammableFilter(registrationName='ProgrammableFilter2', Input=calculator11)
programmableFilter2.Script = ''
programmableFilter2.RequestInformationScript = ''
programmableFilter2.RequestUpdateExtentScript = ''
programmableFilter2.PythonPath = ''


# Properties modified on programmableFilter2
programmableFilter2.Script = """
inp = self.GetInput()
out = self.GetOutput()

numCells  = inp.GetNumberOfCells()
data = inp.GetCellData().GetArray("AvgShearRate")

i = 0
t = inp.GetInformation().Get(vtk.vtkDataObject.DATA_TIME_STEP())
val = data.GetValue(i)
with open("avg-shear.txt", "a") as f:
  f.write("%i %s\\n" %(int(t), str(val)))
  print("val: ", val, t)
"""
programmableFilter2.RequestInformationScript = ''
programmableFilter2.RequestUpdateExtentScript = ''
programmableFilter2.CopyArrays = 1
programmableFilter2.PythonPath = ''

UpdatePipeline(time=0.0, proxy=programmableFilter2)



ans = GetAnimationScene()    
frames = 0
"""
for i in range(frames):
  t = float(i)
  ans.AnimationTime=t
  iv=calculator11

  name = '/home/smramuen/nobackup/test/test.%04d.pvd' % i    
  # Get the name of the first CellData Array
  #print("Name: " + iv.CellData.GetArray(0).Name)

  # Get the 0th scripting level array
  #shearRateArr = iv.CellData.GetArray(0)
 
  # Get the actual data from the server
  data = paraview.servermanager.Fetch(iv)

  # Get the actual cell data
  cellData = data.GetCellData()

  # Get the name from the 4th actual array
  with open("shearrates_9999.txt", "a") as f:
    val = cellData.GetArray("AvgShearRate").GetValue(0) * 1.059
    f.write("%i %s\n" %(i, str(val)))    
    print("Value: ",str(val))

  #gradientArray = cellData.GetArray(4)
  # Get the first value
  #gradientArray.GetValue(0)

  print(name)
"""
