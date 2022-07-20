#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# get active source.
cleantoGrid1 = GetActiveSource()

ans = GetAnimationScene()    
frames = 81

for i in range(frames):
  t = float(i)
  ans.AnimationTime=t
  iv=GetActiveSource()

  name = '/home/smramuen/nobackup/test/test.%04d.pvd' % i    
  print(name)
  # save data
  SaveData(name, proxy=cleantoGrid1)

#### uncomment the following to render all views
# RenderAllViews()
# alternatively, if you want to write images, you can use SaveScreenshot(...).
