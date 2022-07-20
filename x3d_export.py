""" We run a ParaView animation and trigger a x3d write here """
import sys
import os
import argparse
# -*- coding: utf-8 -*-
### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--total-frames", help="Total number of frames to process", type=int, default=0)
    parser.add_argument("--target-frames", help="Target number of frames for the output", type=int, default=0)
    args = parser.parse_args()
    print(args)

    # get the exportes module
    exporters = servermanager.createModule("exporters")

    #### uncomment the following to render all views
    ans = GetAnimationScene()

    total_frames = 293
    if args.total_frames != 0: 
        total_frames = args.total_frames

    target_frames = 293
    if args.target_frames != 0: 
        target_frames = args.target_frames

    step = total_frames/target_frames

    idx = 0
    for i in range(0,total_frames,step):
        t = float(i)
        ans.AnimationTime=t
        iv = GetActiveSource()
        Render()
        view = GetRenderView()
        x3dExporter = exporters.X3DExporter(FileName="/path/to/data.%04d.x3d" % idx)
        x3dExporter.SetView(view)
        x3dExporter.Write()
        print("file written to: /path/to/data.%04d.x3d" % idx)
        idx += 1

if __name__ == '__main__':
    main()

