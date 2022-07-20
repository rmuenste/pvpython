#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

LoadState("/my/path/to/file.pvsm")

# get active source.
mySource = GetActiveSource()

ans = GetAnimationScene()    
frames = 81

for i in range(frames):
  t = float(i)
  ans.AnimationTime=t
  iv=GetActiveSource()

  name = '/home/smramuen/nobackup/test/test.%04d.pvd' % i    
  print(name)

  RenderAllViews()

  # save screenshot
  SaveScreenshot('/home/user/rmuenste/nobackup/IANUS/oven_uu_trans/oben/slice7.png', magnification=1, quality=100, view=renderView1)

