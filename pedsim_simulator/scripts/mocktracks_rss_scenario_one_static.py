#!/usr/bin/env python
# Author: Timm Linder, linder@cs.uni-freiburg.de
#
# Publishes fake tracked persons and the corresponding detections
# (if not occluded) at
# /spencer/perception/tracked_persons and /spencer/perception/detected_persons.

import rospy
import tf
from spencer_tracking_msgs.msg import TrackedPersons, TrackedPerson
from math import cos, sin, radians
import numpy as np

np.random.seed(42)  # Use the whole truth


def createTrackedPerson(track_id, x, y, theta, speed):
    tracked_persons = TrackedPerson()

    # theta = radians(theta) + pi / 2.0
    theta = radians(theta)

    tracked_persons.track_id = track_id
    quaternion = tf.transformations.quaternion_from_euler(0, 0, theta)

    tracked_persons.pose.pose.position.x = x
    tracked_persons.pose.pose.position.y = y

    tracked_persons.pose.pose.orientation.x = quaternion[0]
    tracked_persons.pose.pose.orientation.y = quaternion[1]
    tracked_persons.pose.pose.orientation.z = quaternion[2]
    tracked_persons.pose.pose.orientation.w = quaternion[3]

    tracked_persons.pose.covariance[0 + 0 * 6] = 0.001  # x
    tracked_persons.pose.covariance[1 + 1 * 6] = 0.001  # y
    tracked_persons.pose.covariance[2 + 2 * 6] = 999999  # z
    tracked_persons.pose.covariance[3 + 3 * 6] = 999999  # x rotation
    tracked_persons.pose.covariance[4 + 5 * 6] = 999999  # y rotation
    tracked_persons.pose.covariance[4 + 5 * 6] = 999999  # z rotation

    # tracked_persons.twist.twist.linear.x = 0.0
    # tracked_persons.twist.twist.linear.y = 0.0

    tracked_persons.twist.twist.linear.x = speed * cos(theta)
    tracked_persons.twist.twist.linear.y = speed * sin(theta)

    for i in range(0, 3):
        tracked_persons.twist.covariance[i + i * 6] = 1.0  # linear velocity
    for i in range(3, 6):
        tracked_persons.twist.covariance[
            i + i * 6] = float("inf")  # rotational velocity

    return tracked_persons


def main():
    # Main code
    trackPublisher = rospy.Publisher(
        '/spencer/perception/tracked_persons', TrackedPersons)

    rospy.init_node('mock_tracked_persons')
    rate = rospy.Rate(10)

    # create speeds
    speeds = np.random.normal(1.34, 0.26, size=50)

    while not rospy.is_shutdown():
        index = 0
        counter = 0

        tracked_persons = TrackedPersons()
        tracked_persons.header.seq = counter
        tracked_persons.header.frame_id = "odom"
        tracked_persons.header.stamp = rospy.Time.now()

        # (createTrackedPerson( trackId, x, y, theta, speed ) )
        tracked_persons.tracks.append(
            createTrackedPerson(01, 5, 4, 90, speeds[index]))
        tracked_persons.tracks.append(
            createTrackedPerson(02, 6, 5.45878, 270, speeds[index]))
        tracked_persons.tracks.append(
            createTrackedPerson(03, 1.3 + 7.22, 5.70, 90, speeds[index]))
        tracked_persons.tracks.append(
            createTrackedPerson(04, 7.22, 7.33, 290, speeds[index]))

        tracked_persons.tracks.append(
            createTrackedPerson(05, 2 + 8.92, 8.42, 90, speeds[index]))
        tracked_persons.tracks.append(
            createTrackedPerson(06, 2 + 7.92, 10.41, 90, speeds[index]))
        tracked_persons.tracks.append(
            createTrackedPerson(07, 2 + 7.2, 9.44, 90, speeds[index]))

        tracked_persons.tracks.append(
            createTrackedPerson(8, 2 + 7, 14 - 2, 90, speeds[index]))
        tracked_persons.tracks.append(
            createTrackedPerson(9, 2 + 5.5, 14.4123 - 2, 90, speeds[index]))
        tracked_persons.tracks.append(
            createTrackedPerson(10, 5 - 1, 18.595 - 5, 280, speeds[index]))
        tracked_persons.tracks.append(
            createTrackedPerson(11, 5 - 1, 20 - 5, 270, speeds[index]))
        tracked_persons.tracks.append(
            createTrackedPerson(12, 6 - 1, 21.5491 - 5, 240, speeds[index]))
        tracked_persons.tracks.append(
            createTrackedPerson(13, 7.48044 - 1, 19 - 5.7, 90, speeds[index]))
        tracked_persons.tracks.append(
            createTrackedPerson(14, 6, 24.5463, 45, speeds[index]))
        tracked_persons.tracks.append(
            createTrackedPerson(15, 8, 28, 90, speeds[index]))
        tracked_persons.tracks.append(
            createTrackedPerson(16, 10.4458, 23, 68, speeds[index]))
        tracked_persons.tracks.append(
            createTrackedPerson(17, 11.5004, 27, 88, speeds[index]))
        tracked_persons.tracks.append(
            createTrackedPerson(18, 14, 25.4389, 20, speeds[index]))
        tracked_persons.tracks.append(
            createTrackedPerson(19, 15, 21, 90, speeds[index]))
        tracked_persons.tracks.append(
            createTrackedPerson(20, 15, 22.4308, 92, speeds[index]))
        tracked_persons.tracks.append(
            createTrackedPerson(21, 15.4676, 24, 91, speeds[index]))
        tracked_persons.tracks.append(
            createTrackedPerson(22, 16.5423, 25.4178, 90, speeds[index]))
        tracked_persons.tracks.append(
            createTrackedPerson(23, 18, 20, 90, speeds[index]))
        tracked_persons.tracks.append(
            createTrackedPerson(24, 18.5532, 21.5011, 90, speeds[index]))
        tracked_persons.tracks.append(
            createTrackedPerson(25, 15.4739, 16.5314, 45, speeds[index]))
        tracked_persons.tracks.append(
            createTrackedPerson(26, 20, 25.5746, 90, speeds[index]))
        tracked_persons.tracks.append(
            createTrackedPerson(27, 21.5327, 24, 90, speeds[index]))
        tracked_persons.tracks.append(
            createTrackedPerson(28, 22, 26.4632, 90, speeds[index]))
        tracked_persons.tracks.append(
            createTrackedPerson(29, 21, 18, 45, speeds[index]))
        tracked_persons.tracks.append(
            createTrackedPerson(30, 23, 20.4335, 90, speeds[index]))
        tracked_persons.tracks.append(
            createTrackedPerson(31, 23.4972, 21.4055, 90, speeds[index]))
        tracked_persons.tracks.append(
            createTrackedPerson(32, 23.4025, 22.4749, 90, speeds[index]))
        tracked_persons.tracks.append(
            createTrackedPerson(33, 24.5281, 18.5868, 54, speeds[index]))
        tracked_persons.tracks.append(
            createTrackedPerson(34, 16.554, 3.40568 - 2, 94, speeds[index]))
        tracked_persons.tracks.append(
            createTrackedPerson(35, 14.8, 6 - 3, 94, speeds[index]))
        tracked_persons.tracks.append(
            createTrackedPerson(36, 20, 4, 0, speeds[index]))
        tracked_persons.tracks.append(
            createTrackedPerson(37, 19, 12, 25, speeds[index]))
        tracked_persons.tracks.append(
            createTrackedPerson(38, 23, 8, 50, speeds[index]))
        tracked_persons.tracks.append(
            createTrackedPerson(39, 24, 10, 90, speeds[index]))
        tracked_persons.tracks.append(
            createTrackedPerson(40, 25, 12, 120, speeds[index]))
        tracked_persons.tracks.append(
            createTrackedPerson(41, 7.51, 22.41, 80, speeds[index]))
        tracked_persons.tracks.append(
            createTrackedPerson(42, 8.21, 25.7, 81, speeds[index]))
        tracked_persons.tracks.append(
            createTrackedPerson(43, 3.31, 27.7, 81, speeds[index]))
        tracked_persons.tracks.append(
            createTrackedPerson(44, 11.421, 18.7, 75, speeds[index]))
        tracked_persons.tracks.append(
            createTrackedPerson(45, 25.21, 27.0, 85, speeds[index]))
        tracked_persons.tracks.append(
            createTrackedPerson(46, 18.23, 6.87, -91, speeds[index]))
        tracked_persons.tracks.append(
            createTrackedPerson(47, 18.6, 8.90, -90, speeds[index]))
        tracked_persons.tracks.append(
            createTrackedPerson(48, 20.4, 7.87, 85, speeds[index]))
        tracked_persons.tracks.append(
            createTrackedPerson(49, 15.684, 10.74, 75, speeds[index]))
        tracked_persons.tracks.append(
            createTrackedPerson(50, 15.72, 13.51, 70, speeds[index]))

        trackPublisher.publish(tracked_persons)

        counter += 1
        index += 1
        rate.sleep()


# Constants

OBSTACLE_YAML = """
header:
  seq: 48860
  stamp:
    secs: 0
    nsecs: 0
  frame_id: world
cell_width: 1.0
cell_height: 1.0
cells:
  -
    x: -0.5
    y: -0.5
    z: 0.0
  -
    x: 0.5
    y: -0.5
    z: 0.0
  -
    x: 1.5
    y: -0.5
    z: 0.0
  -
    x: 2.5
    y: -0.5
    z: 0.0
  -
    x: 3.5
    y: -0.5
    z: 0.0
  -
    x: 4.5
    y: -0.5
    z: 0.0
  -
    x: 5.5
    y: -0.5
    z: 0.0
  -
    x: 6.5
    y: -0.5
    z: 0.0
  -
    x: 7.5
    y: -0.5
    z: 0.0
  -
    x: 8.5
    y: -0.5
    z: 0.0
  -
    x: 9.5
    y: -0.5
    z: 0.0
  -
    x: 10.5
    y: -0.5
    z: 0.0
  -
    x: 11.5
    y: -0.5
    z: 0.0
  -
    x: 12.5
    y: -0.5
    z: 0.0
  -
    x: 13.5
    y: -0.5
    z: 0.0
  -
    x: 14.5
    y: -0.5
    z: 0.0
  -
    x: 15.5
    y: -0.5
    z: 0.0
  -
    x: 16.5
    y: -0.5
    z: 0.0
  -
    x: 17.5
    y: -0.5
    z: 0.0
  -
    x: 18.5
    y: -0.5
    z: 0.0
  -
    x: 19.5
    y: -0.5
    z: 0.0
  -
    x: 20.5
    y: -0.5
    z: 0.0
  -
    x: 21.5
    y: -0.5
    z: 0.0
  -
    x: 22.5
    y: -0.5
    z: 0.0
  -
    x: 23.5
    y: -0.5
    z: 0.0
  -
    x: 24.5
    y: -0.5
    z: 0.0
  -
    x: 25.5
    y: -0.5
    z: 0.0
  -
    x: 26.5
    y: -0.5
    z: 0.0
  -
    x: 27.5
    y: -0.5
    z: 0.0
  -
    x: -0.5
    y: -0.5
    z: 0.0
  -
    x: -0.5
    y: 0.5
    z: 0.0
  -
    x: -0.5
    y: 1.5
    z: 0.0
  -
    x: -0.5
    y: 2.5
    z: 0.0
  -
    x: -0.5
    y: 3.5
    z: 0.0
  -
    x: -0.5
    y: 4.5
    z: 0.0
  -
    x: -0.5
    y: 5.5
    z: 0.0
  -
    x: -0.5
    y: 6.5
    z: 0.0
  -
    x: -0.5
    y: 7.5
    z: 0.0
  -
    x: -0.5
    y: 8.5
    z: 0.0
  -
    x: -0.5
    y: 9.5
    z: 0.0
  -
    x: -0.5
    y: 10.5
    z: 0.0
  -
    x: -0.5
    y: 11.5
    z: 0.0
  -
    x: -0.5
    y: 12.5
    z: 0.0
  -
    x: -0.5
    y: 13.5
    z: 0.0
  -
    x: -0.5
    y: 14.5
    z: 0.0
  -
    x: -0.5
    y: 15.5
    z: 0.0
  -
    x: -0.5
    y: 16.5
    z: 0.0
  -
    x: -0.5
    y: 17.5
    z: 0.0
  -
    x: -0.5
    y: 18.5
    z: 0.0
  -
    x: -0.5
    y: 19.5
    z: 0.0
  -
    x: -0.5
    y: 20.5
    z: 0.0
  -
    x: -0.5
    y: 21.5
    z: 0.0
  -
    x: -0.5
    y: 22.5
    z: 0.0
  -
    x: -0.5
    y: 23.5
    z: 0.0
  -
    x: -0.5
    y: 24.5
    z: 0.0
  -
    x: -0.5
    y: 25.5
    z: 0.0
  -
    x: -0.5
    y: 26.5
    z: 0.0
  -
    x: -0.5
    y: 27.5
    z: 0.0
  -
    x: -0.5
    y: 28.5
    z: 0.0
  -
    x: -0.5
    y: 29.5
    z: 0.0
  -
    x: -0.5
    y: 30.5
    z: 0.0
  -
    x: -0.5
    y: 31.5
    z: 0.0
  -
    x: -0.5
    y: 31.5
    z: 0.0
  -
    x: 0.5
    y: 31.5
    z: 0.0
  -
    x: 1.5
    y: 31.5
    z: 0.0
  -
    x: 2.5
    y: 31.5
    z: 0.0
  -
    x: 3.5
    y: 31.5
    z: 0.0
  -
    x: 4.5
    y: 31.5
    z: 0.0
  -
    x: 5.5
    y: 31.5
    z: 0.0
  -
    x: 6.5
    y: 31.5
    z: 0.0
  -
    x: 7.5
    y: 31.5
    z: 0.0
  -
    x: 8.5
    y: 31.5
    z: 0.0
  -
    x: 9.5
    y: 31.5
    z: 0.0
  -
    x: 10.5
    y: 31.5
    z: 0.0
  -
    x: 11.5
    y: 31.5
    z: 0.0
  -
    x: 12.5
    y: 31.5
    z: 0.0
  -
    x: 13.5
    y: 31.5
    z: 0.0
  -
    x: 14.5
    y: 31.5
    z: 0.0
  -
    x: 15.5
    y: 31.5
    z: 0.0
  -
    x: 16.5
    y: 31.5
    z: 0.0
  -
    x: 17.5
    y: 31.5
    z: 0.0
  -
    x: 18.5
    y: 31.5
    z: 0.0
  -
    x: 19.5
    y: 31.5
    z: 0.0
  -
    x: 20.5
    y: 31.5
    z: 0.0
  -
    x: 21.5
    y: 31.5
    z: 0.0
  -
    x: 22.5
    y: 31.5
    z: 0.0
  -
    x: 23.5
    y: 31.5
    z: 0.0
  -
    x: 24.5
    y: 31.5
    z: 0.0
  -
    x: 25.5
    y: 31.5
    z: 0.0
  -
    x: 26.5
    y: 31.5
    z: 0.0
  -
    x: 27.5
    y: 31.5
    z: 0.0
  -
    x: 27.5
    y: -0.5
    z: 0.0
  -
    x: 27.5
    y: 0.5
    z: 0.0
  -
    x: 27.5
    y: 1.5
    z: 0.0
  -
    x: 27.5
    y: 2.5
    z: 0.0
  -
    x: 27.5
    y: 3.5
    z: 0.0
  -
    x: 27.5
    y: 4.5
    z: 0.0
  -
    x: 27.5
    y: 5.5
    z: 0.0
  -
    x: 27.5
    y: 6.5
    z: 0.0
  -
    x: 27.5
    y: 7.5
    z: 0.0
  -
    x: 27.5
    y: 8.5
    z: 0.0
  -
    x: 27.5
    y: 9.5
    z: 0.0
  -
    x: 27.5
    y: 10.5
    z: 0.0
  -
    x: 27.5
    y: 11.5
    z: 0.0
  -
    x: 27.5
    y: 12.5
    z: 0.0
  -
    x: 27.5
    y: 13.5
    z: 0.0
  -
    x: 27.5
    y: 14.5
    z: 0.0
  -
    x: 27.5
    y: 15.5
    z: 0.0
  -
    x: 27.5
    y: 16.5
    z: 0.0
  -
    x: 27.5
    y: 17.5
    z: 0.0
  -
    x: 27.5
    y: 18.5
    z: 0.0
  -
    x: 27.5
    y: 19.5
    z: 0.0
  -
    x: 27.5
    y: 20.5
    z: 0.0
  -
    x: 27.5
    y: 21.5
    z: 0.0
  -
    x: 27.5
    y: 22.5
    z: 0.0
  -
    x: 27.5
    y: 23.5
    z: 0.0
  -
    x: 27.5
    y: 24.5
    z: 0.0
  -
    x: 27.5
    y: 25.5
    z: 0.0
  -
    x: 27.5
    y: 26.5
    z: 0.0
  -
    x: 27.5
    y: 27.5
    z: 0.0
  -
    x: 27.5
    y: 28.5
    z: 0.0
  -
    x: 27.5
    y: 29.5
    z: 0.0
  -
    x: 27.5
    y: 30.5
    z: 0.0
  -
    x: 27.5
    y: 31.5
    z: 0.0
  -
    x: 26.5
    y: 3.5
    z: 0.0
  -
    x: 26.5
    y: 4.5
    z: 0.0
  -
    x: 26.5
    y: 5.5
    z: 0.0
  -
    x: 26.5
    y: 6.5
    z: 0.0
  -
    x: 26.5
    y: 7.5
    z: 0.0
  -
    x: 26.5
    y: 9.5
    z: 0.0
  -
    x: 26.5
    y: 10.5
    z: 0.0
  -
    x: 26.5
    y: 11.5
    z: 0.0
  -
    x: 26.5
    y: 12.5
    z: 0.0
  -
    x: 26.5
    y: 13.5
    z: 0.0
"""

if __name__ == '__main__':
    main()
