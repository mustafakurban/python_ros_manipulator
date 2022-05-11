#include <ros/ros.h>
#include <tf2_ros/transform_listener.h>
#include <geometry_msgs/TransformStamped.h>
#include <geometry_msgs/Twist.h>
#include <webots_ros/set_float.h>


int main(int argc, char** argv){
  ros::init(argc, argv, "tf2_listener");

  ros::NodeHandle node;

  ros::service::waitForService("/TurtleBot3Burger/wheel_left_joint/set_velocity");
  ros::ServiceClient velocity_giver =
    node.serviceClient<webots_ros::set_float>("set_velocity");
  webots_ros::set_float vel_with_float;

  vel_with_float.request.value = 2.0;

  velocity_giver.call(vel_with_float);

  

  tf2_ros::Buffer tfBuffer;
  tf2_ros::TransformListener tfListener(tfBuffer);

  ros::Rate rate(10.0);
  while (node.ok()){
    geometry_msgs::TransformStamped transformStamped;
    try{
      transformStamped = tfBuffer.lookupTransform("odom", "base_footprint",
                               ros::Time(0));
        std::cout << transformStamped.transform.translation.x << std::endl;
    }
    catch (tf2::TransformException &ex) {
      ROS_WARN("%s",ex.what());
      ros::Duration(1.0).sleep();
      continue;
    }

    rate.sleep();
  }
  return 0;
};