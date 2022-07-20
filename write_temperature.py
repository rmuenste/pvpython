# -*- coding: utf-8 -*-
#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

#### uncomment the following to render all views
ans=GetAnimationScene()
for i in range(46):
  t=float(i)
  ans.AnimationTime=t
  iv=GetActiveSource()
  riv=servermanager.Fetch(iv)
  ivpd=riv.GetPointData()
  arr=ivpd.GetArray('T')
  arr2=ivpd.GetArray('vol')
  myval=arr.GetValue(0)/arr2.GetValue(0)
  print(str(i) + " " + str(arr.GetValue(0)) + " " + str(myval))

  RenderAllViews()

