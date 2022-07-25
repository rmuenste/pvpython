""" We run a ParaView animation and trigger a x3d write here """
import sys
import os
import argparse
import pathlib
# -*- coding: utf-8 -*-
### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

outpath = "/home/user/rmuenste/nobackup/IANUS/blender_camera/particleCase3_20e-3/x3d/fluid"
path = outpath

#path = "/home/user/rmuenste/nobackup/IANUS/blender_camera/particleCase3_20e-3/x3d/particle"
#          /home/user/rmuenste/nobackup/IANUS/blender_camera/particleCase3_20e-3/VTK/x3d

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--total-frames", help="Total number of frames to process", type=int, default=0)
    parser.add_argument("--target-frames", help="Target number of frames for the output", type=int, default=0)
    parser.add_argument("--output-path", help="Output folder for the converted files", type=pathlib.Path, default="")
    parser.add_argument("--data-name", help="Name of the data set (used in output name)", default="")
    args = parser.parse_args()
    print(args)

    print("Hello")

    # get active view
    renderView1 = GetActiveViewOrCreate('RenderView')
    # uncomment following to set a specific view size
    # renderView1.ViewSize = [1389, 540]

    # destroy renderView1
    Delete(renderView1)
    del renderView1

    kinematicCloud_5000vtkFileNames = ['/home/user/rmuenste/nobackup/IANUS/blender_camera/particleCase3_20e-3/VTK/lagrangian/kinematicCloud/kinematicCloud_%s.vtk' %i for i in range(0,13001, 100)]

    particleCase3_20e3FileNames = ['/home/warehouse13/rmuenste/nobackup/IANUS/blender_camera/particleCase3_20e-3/VTK/particleCase3_20e-3_%s.vtk' %i for i in range(0,13001, 100)]

    LoadState('/home/user/rmuenste/nobackup/IANUS/blender_camera/particleCase3_20e-3/fluid_state.pvsm', DataDirectory='/home/user/rmuenste/nobackup/IANUS/blender_camera/particleCase3_20e-3',
              particleCase3_20e3_FileNames=particleCase3_20e3FileNames)

    # get animation scene
    animationScene1 = GetAnimationScene()

    animationScene1.GoToFirst()

    # get the exportes module
    exporters = servermanager.createModule("exporters")

    #### uncomment the following to render all views
    ans = GetAnimationScene()

    # find view
    renderView1 = FindViewOrCreate('RenderView1', viewtype='RenderView')
    # uncomment following to set a specific view size
    # renderView1.ViewSize = [1310, 781]

    # get layout
    layout1_1 = GetLayoutByName("Layout #1")

    # set active view
    SetActiveView(renderView1)

    sourceStr1 = 'Glyph1'
    sourceStr2 = 'Slice1'

    # find source
    ac = FindSource(sourceStr2)

    # set active source
    SetActiveSource(ac)

    total_frames = 5
    if args.total_frames != 0: 
        total_frames = args.total_frames

    target_frames = 5
    if args.target_frames != 0: 
        target_frames = args.target_frames

    step = int(total_frames/target_frames)

    if args.output_path != "":
        if args.output_path.exists():
            print("Settings path to args.output_path")
            path = args.output_path
        else:
            print("Path does not exist")
            sys.exit(2)

    data_name = ''
    if args.data_name != "":
        print("Setting data name")
        data_name = args.data_name
    else:
        print("Data set name not set")
        sys.exit(2)

    idx = 0
    filename = path / data_name 
    for i in range(0,total_frames,step):
        t = float(i)
        ans.AnimationTime=t

        iv = GetActiveSource()
        Render()
        view = GetRenderView()
        x3dExporter = exporters.X3DExporter(FileName="%s.%04d.x3d" %(filename, idx))
        x3dExporter.SetView(view)
        x3dExporter.Write()
        print("%s.%04d.x3d" %(filename, idx))
        idx += 1

main()
