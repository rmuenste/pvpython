#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1502, 795]

# current camera placement for renderView1
renderView1.CameraPosition = [0.01015784341387747, 14.683288777265103, -0.49098716656172336]
renderView1.CameraFocalPoint = [0.01015784341387747, 0.011804535984992981, -0.49098716656172336]
renderView1.CameraViewUp = [1.0, 0.0, -6.661338147750939e-16]
renderView1.CameraParallelScale = 2.236017813897033
renderView1.CameraParallelProjection = 1

# save screenshot
SaveScreenshot('/home/user/rmuenste/nobackup/IANUS/oven_uu_trans/oben/slice7.png', magnification=1, quality=100, view=renderView1)

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [0.01015784341387747, 14.683288777265103, -0.49098716656172336]
renderView1.CameraFocalPoint = [0.01015784341387747, 0.011804535984992981, -0.49098716656172336]
renderView1.CameraViewUp = [1.0, 0.0, -6.661338147750939e-16]
renderView1.CameraParallelScale = 2.236017813897033
renderView1.CameraParallelProjection = 1

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).