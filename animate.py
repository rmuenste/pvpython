#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

#### uncomment the following to render all views
ans = GetAnimationScene()
for i in range(34):
    t = float(i)
    ans.AnimationTime=t
    iv = GetActiveSource()
    riv = servermanager.Fetch(iv)
    ivpd = riv.GetPointData()
    arr = ivpd.GetArray('T')
    print(str(i) + " " + str(arr.GetValue(0)/1.5))

    RenderAllViews()

