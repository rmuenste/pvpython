#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# get active source.
slice1 = GetActiveSource()

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1502, 795]

# get display properties
slice1Display = GetDisplayProperties(slice1, view=renderView1)

# Properties modified on slice1Display
slice1Display.Opacity = 1.0

#### saving camera placements for all active views

# current camera placement for renderView1
renderView1.CameraPosition = [11.960407626344102, 6.177351482248439, 7.728312075039721]
renderView1.CameraFocalPoint = [0.32761948807723407, -0.6385730032508099, 0.42002472502818206]
renderView1.CameraViewUp = [-0.37516372119563546, 0.8958051663847617, -0.23829663484198235]
renderView1.CameraParallelScale = 2.5114962918538857
renderView1.CameraParallelProjection = 1

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).