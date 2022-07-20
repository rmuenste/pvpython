#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

old_source=GetActiveSource()
for i in range(3,9):

  renderView1 = GetActiveViewOrCreate('RenderView')
  sl=FindSource("Slice%i" % i)
  SetActiveSource(sl)

  slice3Display = Show(sl, renderView1)

  # hide data in view
  Hide(old_source, renderView1)

  # get active view
  renderView1 = GetActiveViewOrCreate('RenderView')
  # uncomment following to set a specific view size
  # renderView1.ViewSize = [1617, 795]

  # get display properties
  slice1Display = GetDisplayProperties(sl, view=renderView1)

  # hide color bar/color legend
  slice1Display.SetScalarBarVisibility(renderView1, False)

  # get color transfer function/color map for 'U'
  uLUT = GetColorTransferFunction('U')

  # Rescale transfer function
  uLUT.RescaleTransferFunction(0.0, 15.0)

  # get opacity transfer function/opacity map for 'U'
  uPWF = GetOpacityTransferFunction('U')

  # Rescale transfer function
  uPWF.RescaleTransferFunction(0.0, 15.0)

  # change representation type
  slice1Display.SetRepresentationType('Surface LIC')

  # Properties modified on slice1Display
  slice1Display.EnhanceContrast = 'Color Only'

  # get layout
  layout1 = GetLayout()
  old_source=sl
  # save screenshot
  SaveScreenshot('/home/user/rmuenste/nobackup/IANUS/oven_trans2/brenner_alle/LIC%i.png' %i, layout=layout1, magnification=1, quality=100)


