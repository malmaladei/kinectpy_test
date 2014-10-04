"""
Install Visual Studio 2013 with Python extension
Install Git
Install Python 2.7.6 from python.org (make sure to add it as an environment-variable in Windows and as a Python-environment in VS13 if you have multiple Pythons installed)
Kinect 1.0 SDK from http://www.microsoft.com/en-us/download/details.aspx?id=28782 => interacts with Kinect hardware
Python-Kinect wrapper Pykinect: http://pypi.python.org/pypi/pykinect/1.0 => implements Kinect functionality in Python
vpykinect module from https://sites.google.com/site/erfarmer/downloads => integrates with Pykinect to get input from Kinect
VPython from http://www.vpython.org/ => displays output from vpykinect

after the tutorial http://possiblywrong.wordpress.com/2012/11/04/kinect-skeleton-tracking-with-visual-python/
"""

from visual import *
import vpykinect
 
skeleton = vpykinect.Skeleton(frame(visible=False))
skeleton.frame.visible = False
raised = False
 
while True:
    rate(30)
    skeleton.frame.visible = skeleton.update()
    if skeleton.frame.visible:
        right_hand = skeleton.joints[11]
        right_shoulder = skeleton.joints[8]
        spine = skeleton.joints[1]
        if right_hand.y > right_shoulder.y and not raised:
            raised = True
            print('Recognized right hand wave.')
        elif right_hand.y < spine.y and raised:
            raised = False