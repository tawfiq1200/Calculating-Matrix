#!/usr/bin/env python

import sys
import copy
import geometry_msgs.msg
from geometry_msgs.msg import PoseStamped
import tf
import roslib
import traceback
import numpy as np
import math
from numpy.linalg import inv
from std_msgs.msg import String

def trans():

  y = np.loadtxt('/home/tawfiq/matrix_transform/src/mat_trans/src/grip.txt')
  print("grip",y)

  quaternion1 = (y[3],y[4],y[5],y[6])
  euler = tf.transformations.euler_from_quaternion(quaternion1) # axes='szyx' will provide result in x, y,z sequence
  roll=euler[0]
  pitch=euler[1]
  yaw=euler[2]

  C00=math.cos(yaw)*math.cos(pitch)
  C01=math.cos(yaw)*math.sin(pitch)*math.sin(roll) - math.sin(yaw)*math.cos(roll)
  C02=math.cos(yaw)*math.sin(pitch)*math.cos(roll) + math.sin(yaw)*math.sin(roll)
  C03=y[0]
  C10=math.sin(yaw)*math.cos(pitch)
  C11=math.sin(yaw)*math.sin(pitch)*math.sin(roll) + math.cos(yaw)*math.cos(roll)
  C12=math.sin(yaw)*math.sin(pitch)*math.cos(roll) -math.cos(yaw)*math.sin(roll)
  C13=y[1]
  C20= -math.sin(pitch)
  C21=math.cos(pitch)*math.sin(roll)
  C22=math.cos(pitch)*math.cos(roll)
  C23=y[2]
  C30=0
  C31=0
  C32=0
  C33=1

  grip_mat=np.array([[C00, C01, C02, C03],[C10, C11, C12, C13],[C20, C21, C22, C23],[C30, C31, C32, C33]])
  
  print("grip_mat", grip_mat)

  z = np.loadtxt('/home/tawfiq/matrix_transform/src/mat_trans/src/obj.txt')
  print("object",z)

  quaternion2 = (z[3],z[4],z[5],z[6])
  euler = tf.transformations.euler_from_quaternion(quaternion2)
  roll=euler[0]
  pitch=euler[1]
  yaw=euler[2]

  C00=math.cos(yaw)*math.cos(pitch)
  C01=math.cos(yaw)*math.sin(pitch)*math.sin(roll) - math.sin(yaw)*math.cos(roll)
  C02=math.cos(yaw)*math.sin(pitch)*math.cos(roll) + math.sin(yaw)*math.sin(roll)
  C03=z[0]
  C10=math.sin(yaw)*math.cos(pitch)
  C11=math.sin(yaw)*math.sin(pitch)*math.sin(roll) + math.cos(yaw)*math.cos(roll)
  C12=math.sin(yaw)*math.sin(pitch)*math.cos(roll) -math.cos(yaw)*math.sin(roll)
  C13=z[1]
  C20= -math.sin(pitch)
  C21=math.cos(pitch)*math.sin(roll)
  C22=math.cos(pitch)*math.cos(roll)
  C23=z[2]
  C30=0
  C31=0
  C32=0
  C33=1

  object_mat=np.array([[C00, C01, C02, C03],[C10, C11, C12, C13],[C20, C21, C22, C23],[C30, C31, C32, C33]])
  print("object_mat", object_mat)

  transformation_mat=np.dot(inv(object_mat), grip_mat)
  np.savetxt('/home/tawfiq/matrix_transform/src/mat_trans/src/transform.txt', transformation_mat)
  load = np.loadtxt('/home/tawfiq/matrix_transform/src/mat_trans/src/transform.txt')
  print("Transformation Matrix",load)


if __name__=='__main__':
  try:
    trans()
  except rospy.ROSInterruptException:
    pass