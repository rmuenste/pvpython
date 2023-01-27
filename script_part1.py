# trace generated using paraview version 5.9.1

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# find source
main16926pvtu = FindSource('main.16926.pvtu')

# create a new 'Gradient Of Unstructured DataSet'
gradientOfUnstructuredDataSet1 = GradientOfUnstructuredDataSet(registrationName='GradientOfUnstructuredDataSet1', Input=main16926pvtu)

# Properties modified on gradientOfUnstructuredDataSet1
gradientOfUnstructuredDataSet1.ScalarArray = ['POINTS', 'Velocity']

UpdatePipeline(time=0.0, proxy=gradientOfUnstructuredDataSet1)

# create a new 'Point Data to Cell Data'
pointDatatoCellData1 = PointDatatoCellData(registrationName='PointDatatoCellData1', Input=gradientOfUnstructuredDataSet1)

UpdatePipeline(time=0.0, proxy=pointDatatoCellData1)

# create a new 'Calculator'
calculator1 = Calculator(registrationName='Calculator1', Input=pointDatatoCellData1)
calculator1.AttributeType = 'Cell Data'

# Properties modified on calculator1
calculator1.ResultArrayName = 'dudx'
calculator1.Function = 'Gradients_0'

UpdatePipeline(time=0.0, proxy=calculator1)

# create a new 'Calculator'
calculator2 = Calculator(registrationName='Calculator2', Input=calculator1)
calculator2.AttributeType = 'Cell Data'

# Properties modified on calculator2
calculator2.ResultArrayName = 'dudy'
calculator2.Function = 'Gradients_1'

UpdatePipeline(time=0.0, proxy=calculator2)

# create a new 'Calculator'
calculator3 = Calculator(registrationName='Calculator3', Input=calculator2)
calculator3.AttributeType = 'Cell Data'

# Properties modified on calculator3
calculator3.ResultArrayName = 'dudz'
calculator3.Function = 'Gradients_2'

UpdatePipeline(time=0.0, proxy=calculator3)

# create a new 'Calculator'
calculator4 = Calculator(registrationName='Calculator4', Input=calculator3)
calculator4.AttributeType = 'Cell Data'

# Properties modified on calculator4
calculator4.ResultArrayName = 'dvdx'
calculator4.Function = 'Gradients_3'

UpdatePipeline(time=0.0, proxy=calculator4)

# create a new 'Calculator'
calculator5 = Calculator(registrationName='Calculator5', Input=calculator4)
calculator5.AttributeType = 'Cell Data'

# Properties modified on calculator5
calculator5.ResultArrayName = 'dvdy'
calculator5.Function = 'Gradients_4'

UpdatePipeline(time=0.0, proxy=calculator5)

# create a new 'Calculator'
calculator6 = Calculator(registrationName='Calculator6', Input=calculator5)
calculator6.AttributeType = 'Cell Data'

# Properties modified on calculator6
calculator6.ResultArrayName = 'dvdz'
calculator6.Function = 'Gradients_5'

UpdatePipeline(time=0.0, proxy=calculator6)

# create a new 'Calculator'
calculator7 = Calculator(registrationName='Calculator7', Input=calculator6)
calculator7.AttributeType = 'Cell Data'

# Properties modified on calculator7
calculator7.ResultArrayName = 'dwdx'
calculator7.Function = 'Gradients_6'

UpdatePipeline(time=0.0, proxy=calculator7)

# create a new 'Calculator'
calculator8 = Calculator(registrationName='Calculator8', Input=calculator7)
calculator8.AttributeType = 'Cell Data'

# Properties modified on calculator8
calculator8.ResultArrayName = 'dwdy'
calculator8.Function = 'Gradients_7'

UpdatePipeline(time=0.0, proxy=calculator8)

# create a new 'Calculator'
calculator9 = Calculator(registrationName='Calculator9', Input=calculator8)
calculator9.AttributeType = 'Cell Data'

# Properties modified on calculator8
calculator9.ResultArrayName = 'dwdz'
calculator9.Function = 'Gradients_8'

UpdatePipeline(time=0.0, proxy=calculator9)
