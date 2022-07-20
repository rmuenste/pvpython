#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'Legacy VTK Reader'
oven_trans_hf_ = LegacyVTKReader(FileNames=['/home/user/rmuenste/nobackup/IANUS/oven_trans_hf/VTK2/FLUID/oven_trans_hf_0.vtk', '/home/user/rmuenste/nobackup/IANUS/oven_trans_hf/VTK2/FLUID/oven_trans_hf_369.vtk', '/home/user/rmuenste/nobackup/IANUS/oven_trans_hf/VTK2/FLUID/oven_trans_hf_592.vtk', '/home/user/rmuenste/nobackup/IANUS/oven_trans_hf/VTK2/FLUID/oven_trans_hf_815.vtk', '/home/user/rmuenste/nobackup/IANUS/oven_trans_hf/VTK2/FLUID/oven_trans_hf_1038.vtk', '/home/user/rmuenste/nobackup/IANUS/oven_trans_hf/VTK2/FLUID/oven_trans_hf_1261.vtk', '/home/user/rmuenste/nobackup/IANUS/oven_trans_hf/VTK2/FLUID/oven_trans_hf_1484.vtk', '/home/user/rmuenste/nobackup/IANUS/oven_trans_hf/VTK2/FLUID/oven_trans_hf_1707.vtk', '/home/user/rmuenste/nobackup/IANUS/oven_trans_hf/VTK2/FLUID/oven_trans_hf_1930.vtk', '/home/user/rmuenste/nobackup/IANUS/oven_trans_hf/VTK2/FLUID/oven_trans_hf_2153.vtk', '/home/user/rmuenste/nobackup/IANUS/oven_trans_hf/VTK2/FLUID/oven_trans_hf_2376.vtk', '/home/user/rmuenste/nobackup/IANUS/oven_trans_hf/VTK2/FLUID/oven_trans_hf_2599.vtk', '/home/user/rmuenste/nobackup/IANUS/oven_trans_hf/VTK2/FLUID/oven_trans_hf_2822.vtk', '/home/user/rmuenste/nobackup/IANUS/oven_trans_hf/VTK2/FLUID/oven_trans_hf_3045.vtk', '/home/user/rmuenste/nobackup/IANUS/oven_trans_hf/VTK2/FLUID/oven_trans_hf_3268.vtk'])

# get animation scene
animationScene1 = GetAnimationScene()

# update animation scene based on data timesteps
animationScene1.UpdateAnimationUsingDataTimeSteps()

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1527, 783]

# show data in view
oven_trans_hf_Display = Show(oven_trans_hf_, renderView1)

## init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
#oven_trans_hf_Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
#
## init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
#oven_trans_hf_Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
#
## reset view to fit data
#renderView1.ResetCamera()

# create a new 'Calculator'
calculator1 = Calculator(Input=oven_trans_hf_)
calculator1.AttributeMode = 'Point Data'
calculator1.CoordinateResults = 0
calculator1.ResultNormals = 0
calculator1.ResultTCoords = 0
calculator1.ResultArrayName = 'Result'
calculator1.Function = ''
calculator1.ReplaceInvalidResults = 1
calculator1.ReplacementValue = 0.0

# Properties modified on calculator1
calculator1.ResultArrayName = 'volp'
calculator1.Function = '1'

# show data in view
calculator1Display = Show(calculator1, renderView1)
# init the 'PiecewiseFunction' selected for 'OSPRayScaleFunction'
calculator1Display.OSPRayScaleFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
calculator1Display.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
calculator1Display.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]

# hide data in view
Hide(oven_trans_hf_, renderView1)

# show color bar/color legend
calculator1Display.SetScalarBarVisibility(renderView1, True)

# create a new 'Integrate Variables'
integrateVariables1 = IntegrateVariables(Input=calculator1)

# show data in view
integrateVariables1Display = Show(integrateVariables1, spreadSheetView1)
# trace defaults for the display properties.
integrateVariables1Display.FieldAssociation = 'Point Data'
integrateVariables1Display.CompositeDataSetIndex = [0]

#### uncomment the following to render all views
ans=GetAnimationScene()
for i in range(2):
  t=float(i)
  ans.AnimationTime=t
  iv=integrateVariables1
  riv=servermanager.Fetch(iv)
  ivpd=riv.GetPointData()
  arr=ivpd.GetArray('T')
  arr2=ivpd.GetArray('volp')
  myval=arr.GetValue(0)/arr2.GetValue(0)
  print(str(i) + " " + str(arr.GetValue(0)) + " " + str(myval))

  RenderAllViews()

