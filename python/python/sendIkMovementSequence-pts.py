# Make sure to have CoppeliaSim running, with followig scene loaded:
#
# scenes/messaging/ikMovementViaRemoteApi.ttt
#
# Do not launch simulation, then run this script
#
# The client side (i.e. this script) depends on:
#
# sim.py, simConst.py, and the remote API library available
# in programming/remoteApiBindings/lib/lib
# Additionally you will need the python math and msgpack modules

try:
    import sim
except:
    print ('--------------------------------------------------------------')
    print ('"sim.py" could not be imported. This means very probably that')
    print ('either "sim.py" or the remoteApi library could not be found.')
    print ('Make sure both are in the same folder as this file,')
    print ('or appropriately adjust the file "sim.py"')
    print ('--------------------------------------------------------------')
    print ('')

import time
import math
import msgpack

print ('Program started')
sim.simxFinish(-1) # just in case, close all opened connections
clientID=sim.simxStart('127.0.0.1',19997,True,True,5000,5) # Connect to CoppeliaSim
if clientID!=-1:
    print ('Connected to remote API server')

    executedMovId='notReady'

    targetArm='/LBR4p'
    stringSignalName=targetArm+'_executedMovId'

    def waitForMovementExecuted(id):
        global executedMovId
        global stringSignalName
        while executedMovId!=id:
            retCode,s=sim.simxGetStringSignal(clientID,stringSignalName,sim.simx_opmode_buffer)
            if retCode==sim.simx_return_ok:
                if type(s)==bytearray:
                    s=s.decode('ascii') # python2/python3 differences
                executedMovId=s

    # Start streaming stringSignalName string signal:
    sim.simxGetStringSignal(clientID,stringSignalName,sim.simx_opmode_streaming)

    # Set-up some movement variables:
    times=[0.500,0.550,0.600,0.650,0.700,0.750,0.800,0.850,0.900,0.950,1.000,1.050,1.100,1.150,1.200,1.250,1.300,1.350,1.400,1.450,1.500,1.550,1.600,1.650,1.700,1.750,1.800,1.850,1.900,1.950,2.000,2.050,2.100,2.150,2.200,2.250,2.300,2.350,2.400,2.450,2.500,2.550,2.600,2.650,2.700,2.750,2.800,2.850,2.900,2.950,3.000,3.050,3.100,3.150,3.200,3.250,3.300,3.350,3.400,3.450,3.500,3.550,3.600,3.650,3.700,3.750,3.800,3.850,3.900,3.950,4.000,4.050,4.100,4.150,4.200,4.250,4.300,4.350,4.400,4.450,4.500,4.550,4.600,4.650,4.700,4.750,4.800,4.850,4.900,4.950,5.000,5.050,5.100,5.150,5.200,5.250,5.300,5.350,5.400,5.450,5.500,5.550,5.600,5.650,5.700,5.750,5.800,5.850,5.900,5.950,6.000,6.050,6.100,6.150,6.200,6.250,6.300,6.350,6.400,6.450,6.500,6.550,6.600,6.650,6.700,6.750,6.800,6.850,6.900,6.950,7.000,7.050,7.100,7.150,7.200,7.250,7.300,7.350,7.400,7.450,7.500,7.550,7.600,7.650,7.700,7.750,7.800,7.850,7.900,7.950,8.000,8.050,8.100,8.150,8.200,8.250,8.300,8.350,8.400,8.450,8.500,8.550,8.600,8.650,8.700,8.750,8.800,8.850,8.900,8.950,9.000,9.050,9.100,9.150,9.200,9.250,9.300,9.350,9.400,9.450,9.500,9.550,9.600,9.650,9.700,9.750,9.800,9.850,9.900,10.250,10.300,10.350,10.400,10.450,10.500,10.550,10.600,10.650,10.700,10.750,10.800,10.850,10.900,10.950,11.000,11.050,11.100,11.150,11.200,11.250,11.300,11.350,11.400,11.450,11.500,11.550,11.600,11.650,11.700,11.750,11.800,11.850,11.900,11.950,12.000,12.050,12.100,12.150,12.200,12.250,12.300,12.350,12.400,12.450,12.500,12.550,12.600,12.650,12.700,12.750,12.800,12.850,12.900,12.950,13.000,13.050,13.100,13.150,13.200,13.250,13.300,13.350,13.400,13.450,13.500,13.550,13.600,13.650,13.700,13.750,13.800,13.850,13.900,13.950,14.000,14.050,14.100,14.150,14.200,14.250,14.300,14.350,14.400,14.450,14.500,14.550,14.600,14.650,14.700,14.750,14.800,14.850,14.900,14.950,15.000,15.050,15.100,15.150,15.200,15.250,15.300,15.350,15.400,15.450,15.500,15.550,15.600,15.650,15.700,15.750,15.800,15.850,15.900,15.950,16.000,16.050,16.100,16.150,16.200,16.250,16.300,16.350,16.400,16.450,16.500,16.550,16.600,16.650,16.700,16.750,16.800,16.850,16.900,16.950,17.000,17.050,17.100,17.150,17.200,17.250,17.300,17.350,17.400,17.450,17.500,17.550,17.600,17.650,17.700,17.750,17.800,17.850,17.900,17.950,18.000,18.050,18.100,18.150,18.150,18.200,18.250,18.300,18.350,18.400,18.450,18.500,18.550,18.600,18.650,18.700,18.750,18.800,18.850,18.900,18.950,19.000,19.050,19.100,19.150,19.200,19.250,19.300,19.350,19.400,19.450,19.500,19.550,19.600,19.650,19.700,19.750,19.800,19.850,19.900,19.950,20.000,20.050,20.100,20.150,20.200,20.250,20.300,20.350,20.400,20.450,20.500,20.550,20.600,20.650,20.700,20.750,20.800,20.850,20.900,20.950,21.000,21.050,21.100,21.150,21.200,21.250,21.300,21.350,21.400,21.450,21.500,21.550,21.600,21.650,21.700,21.750,21.800,21.850,21.900,21.950,22.000,22.050,22.100,22.150,22.200,22.250,22.300,22.350,22.400,22.450,22.500,22.550,22.600,22.650,22.700,22.750,22.800,22.850,22.900,22.950,23.000,23.050,23.100,23.150,23.200,23.250,23.300,23.350,23.400,23.450,23.500,23.550,23.600,23.650,23.700,23.750,23.800,23.850,23.900,23.950,24.000,24.050,24.100,24.150,24.200,24.250,24.300,24.350,24.400,24.450,24.500,24.550,24.600,24.650,24.700,24.750,24.800,24.850,24.900,24.950,25.000,25.050,25.100,25.150,25.200,25.250,25.300,25.350,25.400,25.450,25.500,25.550,25.600,25.650,25.700,25.750,25.800,25.850,25.900,25.950,26.000,26.050,26.100,26.150,26.200,26.250,26.300,26.350,26.400,26.450,26.500,26.550,26.600,26.650,26.700,26.750,26.800,26.850,26.900,26.950,27.000,27.050,27.100,27.150,27.200,27.250,27.300,27.350,27.400,27.450,27.500,27.550,27.600,27.650,27.700,27.750,27.800,27.850,27.900,27.950,28.000,28.050,28.100,28.150,28.200,28.250,28.300,28.350,28.400,28.450,28.500,28.550]

    x=[0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.004,0.004,0.004,0.004,0.004,0.004,0.004,0.004,0.004,0.004,0.004,0.004,0.004,0.004,0.004,0.004,0.004,0.004,0.004,0.004,0.004,0.004,0.004,0.004,0.004,0.004,0.004,0.004,0.003,0.003,0.003,0.003,0.003,0.003,0.003,0.003,0.003,0.003,0.003,0.003,0.003,0.003,0.003,0.003,0.003,0.003,0.003,0.003,0.003,0.002,0.002,0.002,0.002,0.002,0.002,0.002,0.002,0.002,0.002,0.002,0.002,0.002,0.002,0.002,0.002,0.002,0.002,0.002,0.002,0.002,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.002,0.002,0.002,0.002,0.002,0.002,0.002,0.002,0.002,0.002,0.002,0.002,0.002,0.002,0.002,0.002,0.002,0.002,0.002,0.002,0.002,0.002,0.002,0.003,0.003,0.003,0.003,0.003,0.003,0.003,0.003,0.003,0.003,0.003,0.003,0.003,0.003,0.003,0.003,0.003,0.003,0.003,0.003,0.003,0.003,0.003,0.004,0.004,0.004,0.004,0.004,0.004,0.004,0.004,0.004,0.004,0.004,0.004,0.004,0.004,0.004,0.004,0.004,0.004,0.004,0.004,0.004,0.004,0.004,0.004,0.004,0.004,0.004,0.004,0.004,0.004,0.004,0.004,0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.005,0.005]

    y=[-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000]

    z=[1.073,1.073,1.073,1.072,1.072,1.072,1.072,1.072,1.072,1.071,1.071,1.071,1.071,1.070,1.070,1.069,1.069,1.069,1.068,1.068,1.067,1.067,1.066,1.065,1.065,1.064,1.064,1.063,1.062,1.061,1.061,1.060,1.059,1.058,1.057,1.056,1.056,1.055,1.054,1.053,1.052,1.051,1.050,1.048,1.047,1.046,1.045,1.044,1.043,1.041,1.040,1.039,1.038,1.036,1.035,1.033,1.032,1.031,1.029,1.028,1.026,1.025,1.023,1.021,1.020,1.018,1.017,1.015,1.013,1.011,1.010,1.008,1.006,1.004,1.002,1.000,0.999,0.997,0.995,0.993,0.991,0.989,0.987,0.984,0.982,0.980,0.978,0.976,0.974,0.971,0.969,0.967,0.965,0.962,0.960,0.958,0.955,0.953,0.951,0.948,0.946,0.944,0.942,0.940,0.938,0.936,0.934,0.932,0.930,0.928,0.926,0.924,0.922,0.920,0.918,0.916,0.914,0.913,0.911,0.909,0.907,0.906,0.904,0.902,0.901,0.899,0.898,0.896,0.895,0.893,0.892,0.890,0.889,0.887,0.886,0.885,0.883,0.882,0.881,0.880,0.879,0.877,0.876,0.875,0.874,0.873,0.872,0.871,0.870,0.869,0.868,0.867,0.866,0.865,0.864,0.863,0.863,0.862,0.861,0.860,0.860,0.859,0.858,0.858,0.857,0.856,0.856,0.855,0.855,0.854,0.854,0.854,0.853,0.853,0.852,0.852,0.852,0.851,0.851,0.851,0.851,0.851,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.850,0.851,0.851,0.851,0.851,0.851,0.852,0.852,0.852,0.853,0.853,0.853,0.854,0.854,0.854,0.855,0.855,0.856,0.856,0.857,0.857,0.858,0.859,0.859,0.860,0.860,0.861,0.862,0.863,0.863,0.864,0.865,0.866,0.866,0.867,0.868,0.869,0.870,0.871,0.872,0.873,0.874,0.875,0.876,0.877,0.878,0.879,0.880,0.881,0.882,0.883,0.884,0.886,0.887,0.888,0.889,0.891,0.892,0.893,0.894,0.896,0.897,0.899,0.900,0.901,0.903,0.904,0.906,0.907,0.909,0.911,0.912,0.914,0.915,0.917,0.919,0.920,0.922,0.924,0.926,0.927,0.929,0.931,0.933,0.935,0.936,0.938,0.940,0.942,0.944,0.946,0.948,0.950,0.952,0.954,0.956,0.958,0.960,0.963,0.965,0.967,0.969,0.971,0.973,0.975,0.977,0.979,0.981,0.983,0.985,0.987,0.988,0.990,0.992,0.994,0.996,0.997,0.999,1.001,1.003,1.004,1.006,1.008,1.009,1.011,1.012,1.014,1.015,1.017,1.019,1.020,1.021,1.023,1.024,1.026,1.027,1.028,1.030,1.031,1.032,1.034,1.035,1.036,1.037,1.039,1.040,1.041,1.042,1.043,1.044,1.045,1.046,1.047,1.048,1.049,1.050,1.051,1.052,1.053,1.054,1.055,1.056,1.056,1.057,1.058,1.059,1.060,1.060,1.061,1.062,1.062,1.063,1.064,1.064,1.065,1.065,1.066,1.066,1.067,1.067,1.068,1.068,1.069,1.069,1.069,1.070,1.070,1.070,1.071,1.071,1.071,1.071,1.072,1.072,1.072,1.072,1.072,1.072,1.073,1.073,1.073,1.073,1.073]

    qx=[-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,0.000,0.000,0.001,0.001,0.002,0.003,0.004,0.005,0.006,0.007,0.009,0.010,0.012,0.014,0.016,0.018,0.020,0.022,0.025,0.027,0.030,0.033,0.036,0.039,0.042,0.045,0.049,0.052,0.056,0.060,0.064,0.068,0.072,0.076,0.081,0.085,0.090,0.095,0.100,0.105,0.110,0.115,0.121,0.126,0.132,0.138,0.143,0.149,0.156,0.162,0.168,0.175,0.181,0.188,0.195,0.202,0.209,0.216,0.223,0.230,0.238,0.245,0.253,0.261,0.269,0.277,0.285,0.293,0.301,0.310,0.318,0.327,0.336,0.344,0.353,0.362,0.371,0.380,0.389,0.398,0.407,0.416,0.424,0.433,0.441,0.449,0.457,0.465,0.472,0.480,0.487,0.494,0.501,0.508,0.515,0.522,0.528,0.534,0.541,0.547,0.553,0.559,0.564,0.570,0.575,0.581,0.586,0.591,0.596,0.601,0.605,0.610,0.614,0.619,0.623,0.627,0.631,0.635,0.639,0.642,0.646,0.649,0.652,0.656,0.659,0.662,0.665,0.668,0.670,0.673,0.675,0.678,0.680,0.682,0.684,0.686,0.688,0.690,0.692,0.693,0.695,0.696,0.698,0.699,0.700,0.701,0.702,0.703,0.704,0.705,0.705,0.706,0.706,0.707,0.707,0.707,0.707,0.707,0.707,0.707,0.707,0.707,0.706,0.706,0.706,0.705,0.705,0.705,0.704,0.703,0.703,0.702,0.701,0.701,0.700,0.699,0.698,0.697,0.696,0.695,0.693,0.692,0.691,0.690,0.688,0.687,0.685,0.684,0.682,0.680,0.679,0.677,0.675,0.673,0.671,0.669,0.667,0.665,0.663,0.661,0.658,0.656,0.654,0.651,0.649,0.646,0.643,0.641,0.638,0.635,0.632,0.629,0.626,0.623,0.620,0.616,0.613,0.610,0.606,0.603,0.599,0.595,0.592,0.588,0.584,0.580,0.576,0.572,0.568,0.563,0.559,0.555,0.550,0.546,0.541,0.536,0.532,0.527,0.522,0.517,0.512,0.507,0.501,0.496,0.491,0.485,0.479,0.474,0.468,0.462,0.456,0.450,0.444,0.438,0.432,0.425,0.419,0.412,0.406,0.399,0.392,0.386,0.379,0.372,0.365,0.358,0.351,0.345,0.338,0.331,0.325,0.318,0.312,0.305,0.299,0.293,0.287,0.280,0.274,0.268,0.262,0.256,0.250,0.245,0.239,0.233,0.227,0.222,0.216,0.211,0.206,0.200,0.195,0.190,0.185,0.180,0.175,0.170,0.165,0.160,0.155,0.151,0.146,0.142,0.137,0.133,0.129,0.124,0.120,0.116,0.112,0.108,0.104,0.100,0.097,0.093,0.089,0.086,0.082,0.079,0.076,0.072,0.069,0.066,0.063,0.060,0.057,0.054,0.052,0.049,0.046,0.044,0.041,0.039,0.036,0.034,0.032,0.030,0.028,0.026,0.024,0.022,0.020,0.019,0.017,0.016,0.014,0.013,0.011,0.010,0.009,0.008,0.007,0.006,0.005,0.004,0.003,0.003,0.002,0.002,0.001,0.001,0.001,0.000,0.000,0.000,0.000]

    qy=[0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000,0.000]

    qz=[-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.001,-0.001,-0.001,-0.001,-0.001,-0.001,-0.001,-0.001,-0.001,-0.001,-0.001,-0.001,-0.001,-0.001,-0.001,-0.001,-0.001,-0.001,-0.001,-0.001,-0.001,-0.001,-0.001,-0.001,-0.001,-0.001,-0.001,-0.001,-0.001,-0.001,-0.001,-0.001,-0.001,-0.001,-0.001,-0.001,-0.001,-0.001,-0.001,-0.001,-0.001,-0.001,-0.001,-0.001,-0.001,-0.001,-0.001,-0.001,-0.001,-0.001,-0.001,-0.001,-0.001,-0.001,-0.001,-0.001,-0.001,-0.001,-0.001,-0.001,-0.001,-0.001,-0.001,-0.001,-0.001,-0.001,-0.001,-0.001,-0.001,-0.001,-0.001,-0.001,-0.001,-0.001,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,0.000,0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000,-0.000]

    qw=[1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,0.999,0.999,0.999,0.999,0.999,0.999,0.999,0.998,0.998,0.998,0.998,0.997,0.997,0.997,0.996,0.996,0.995,0.995,0.994,0.994,0.993,0.993,0.992,0.991,0.990,0.990,0.989,0.988,0.987,0.986,0.985,0.983,0.982,0.981,0.979,0.978,0.976,0.975,0.973,0.971,0.969,0.967,0.965,0.963,0.961,0.959,0.956,0.953,0.951,0.948,0.945,0.942,0.939,0.936,0.932,0.929,0.925,0.921,0.917,0.913,0.909,0.906,0.902,0.898,0.894,0.890,0.886,0.882,0.877,0.873,0.869,0.865,0.861,0.857,0.853,0.849,0.845,0.841,0.837,0.833,0.829,0.826,0.822,0.818,0.814,0.811,0.807,0.803,0.800,0.796,0.793,0.789,0.786,0.782,0.779,0.776,0.773,0.770,0.767,0.764,0.761,0.758,0.755,0.752,0.750,0.747,0.745,0.742,0.740,0.738,0.735,0.733,0.731,0.729,0.727,0.726,0.724,0.722,0.721,0.719,0.718,0.716,0.715,0.714,0.713,0.712,0.711,0.710,0.710,0.709,0.708,0.708,0.708,0.707,0.707,0.707,0.707,0.707,0.707,0.707,0.708,0.708,0.708,0.708,0.709,0.709,0.710,0.710,0.711,0.711,0.712,0.713,0.714,0.714,0.715,0.716,0.717,0.718,0.719,0.721,0.722,0.723,0.724,0.725,0.727,0.728,0.730,0.731,0.733,0.734,0.736,0.738,0.739,0.741,0.743,0.745,0.747,0.749,0.751,0.753,0.755,0.757,0.759,0.761,0.763,0.766,0.768,0.770,0.773,0.775,0.777,0.780,0.782,0.785,0.787,0.790,0.793,0.795,0.798,0.801,0.803,0.806,0.809,0.812,0.815,0.817,0.820,0.823,0.826,0.829,0.832,0.835,0.838,0.841,0.844,0.847,0.850,0.853,0.856,0.859,0.862,0.865,0.868,0.871,0.874,0.878,0.881,0.884,0.887,0.890,0.893,0.896,0.899,0.902,0.905,0.908,0.911,0.914,0.917,0.920,0.923,0.926,0.928,0.931,0.934,0.936,0.939,0.941,0.944,0.946,0.948,0.950,0.952,0.954,0.956,0.958,0.960,0.962,0.963,0.965,0.967,0.968,0.970,0.971,0.972,0.974,0.975,0.976,0.977,0.979,0.980,0.981,0.982,0.983,0.984,0.985,0.985,0.986,0.987,0.988,0.989,0.989,0.990,0.991,0.991,0.992,0.992,0.993,0.993,0.994,0.994,0.995,0.995,0.995,0.996,0.996,0.996,0.997,0.997,0.997,0.997,0.998,0.998,0.998,0.998,0.998,0.999,0.999,0.999,0.999,0.999,0.999,0.999,0.999,0.999,0.999,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000,1.000]
    
    # Start simulation:
    sim.simxStartSimulation(clientID,sim.simx_opmode_blocking)

    # Wait until ready:
    waitForMovementExecuted('ready') 

    # Send the movement sequence:
    movementData={"id":"movSeq1","type":"pts","times":times,"x":x,"y":y,"z":z,"qx":qx,"qy":qy,"qz":qz,"qw":qw}
    packedMovementData=msgpack.packb(movementData)
    sim.simxCallScriptFunction(clientID,targetArm,sim.sim_scripttype_childscript,'legacyRapiMovementDataFunction',[],[],[],packedMovementData,sim.simx_opmode_oneshot)

    # Execute movement sequence:
    sim.simxCallScriptFunction(clientID,targetArm,sim.sim_scripttype_childscript,'legacyRapiExecuteMovement',[],[],[],'movSeq1',sim.simx_opmode_oneshot)
    
    # Wait until above movement sequence finished executing:
    waitForMovementExecuted('movSeq1')

    sim.simxStopSimulation(clientID,sim.simx_opmode_blocking)
    sim.simxGetStringSignal(clientID,stringSignalName,sim.simx_opmode_discontinue)
    sim.simxGetPingTime(clientID)

    # Now close the connection to CoppeliaSim:
    sim.simxFinish(clientID)
else:
    print ('Failed connecting to remote API server')
print ('Program ended')

