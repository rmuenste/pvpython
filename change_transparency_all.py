#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

for i in range(1,9):
  sl=FindSource("Slice%i" % i)
  SetActiveSource(sl)
  # get active view
  renderView1 = GetActiveViewOrCreate('RenderView')
  # uncomment following to set a specific view size
  # renderView1.ViewSize = [1502, 795]
  # get display properties
  slice3Display = GetDisplayProperties(sl, view=renderView1)
  # set scalar coloring
  ColorBy(slice3Display, ('POINTS', 'T'))
  # rescale color and/or opacity maps used to include current data range
  slice3Display.RescaleTransferFunctionToDataRange(True)
  # show color bar/color legend
  slice3Display.SetScalarBarVisibility(renderView1, True)




