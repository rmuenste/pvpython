#### import the simple module from the paraview
from paraview.simple import *
import os 
import glob
import re
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

def try_int(s):
  try: return int(s)
  except: return s

def natsort_key(s):
  import re
  return map(try_int, re.findall(r'(\d+|\D+)', s))

def natcmp(a, b):
  return cmp(natsort_key(a), natsort_key(b))

def natcasecmp(a, b):
  return natcmp(a.lower(), b.lower())

pattern = os.path.join('/data/warehouse14/rmuenste/IANUS/radiation/rad_case_300_ex_trans/VTK/SOLID', '*.vtk')
files = glob.glob(pattern)
files.sort(natcasecmp)

# create a new 'Legacy VTK Reader'
rad_case_300_ex_trans_22331vtk = LegacyVTKReader(FileNames=files)

# get animation scene
animationScene1 = GetAnimationScene()

# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1617, 795]

# create a new 'Clean to Grid'
cleantoGrid1 = CleantoGrid(Input=rad_case_300_ex_trans_22331vtk)

# create a new 'Gradient Of Unstructured DataSet'
gradientOfUnstructuredDataSet1 = GradientOfUnstructuredDataSet(Input=cleantoGrid1)
gradientOfUnstructuredDataSet1.ScalarArray = ['POINTS', 'T']
gradientOfUnstructuredDataSet1.ComputeGradient = 1
gradientOfUnstructuredDataSet1.ResultArrayName = 'Gradients'
gradientOfUnstructuredDataSet1.FasterApproximation = 0
gradientOfUnstructuredDataSet1.ComputeDivergence = 0
gradientOfUnstructuredDataSet1.DivergenceArrayName = 'Divergence'
gradientOfUnstructuredDataSet1.ComputeVorticity = 0
gradientOfUnstructuredDataSet1.VorticityArrayName = 'Vorticity'
gradientOfUnstructuredDataSet1.ComputeQCriterion = 0
gradientOfUnstructuredDataSet1.QCriterionArrayName = 'Q-criterion'

ans=GetAnimationScene()
for i in range(1):
  # create a new 'Slice'
  slice1 = Slice(Input=gradientOfUnstructuredDataSet1)
  slice1.SliceType = 'Plane'
  slice1.Crinkleslice = 0
  slice1.Triangulatetheslice = 1
  slice1.SliceOffsetValues = [0.0]

  # init the 'Plane' selected for 'SliceType'
  slice1.SliceType.Origin = [-1.125, -0.0500000007450581, 0.0]
  slice1.SliceType.Normal = [1.0, 0.0, 0.0]
  slice1.SliceType.Offset = 0.0

  # create a new 'Calculator'
  calculator1 = Calculator(Input=slice1)
  calculator1.AttributeMode = 'Point Data'
  calculator1.CoordinateResults = 0
  calculator1.ResultNormals = 0
  calculator1.ResultTCoords = 0
  calculator1.Function = ''
  calculator1.ReplaceInvalidResults = 1
  calculator1.ReplacementValue = 0.0
  # Properties modified on calculator1
  calculator1.ResultArrayName = 'A'
  calculator1.Function = '1'

  # create a new 'Integrate Variables'
  integrateVariables1 = IntegrateVariables(Input=calculator1)
  iv=integrateVariables1
  riv=servermanager.Fetch(iv)
  ivpd=riv.GetPointData()
  arr=ivpd.GetArray('T')
  arr2=ivpd.GetArray('A')
  #myval=arr.GetValue(0)/arr2.GetValue(0)
  print("step: " + str(i) + " area: " + str(arr2.GetValue(0)))



