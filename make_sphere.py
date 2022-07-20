#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# create a new 'Sphere'
sphere3 = Sphere()

# find source
slice1 = FindSource('Slice1')

# find source
sphere1 = FindSource('Sphere1')

# find source
main = FindSource('main.*')

# find source
sphere2 = FindSource('Sphere2')

# Properties modified on sphere3
sphere3.Center = [0.730469, 0.15, 0.0]
sphere3.Radius = 0.01
sphere3.ThetaResolution = 24
sphere3.PhiResolution = 24

# get active view
renderView1 = GetActiveViewOrCreate('RenderView')
# uncomment following to set a specific view size
# renderView1.ViewSize = [1355, 592]


#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).