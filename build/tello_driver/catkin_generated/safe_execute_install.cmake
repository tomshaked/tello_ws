execute_process(COMMAND "/home/tom/Dev/tello_ws/build/tello_driver/catkin_generated/python_distutils_install.sh" RESULT_VARIABLE res)

if(NOT res EQUAL 0)
  message(FATAL_ERROR "execute_process(/home/tom/Dev/tello_ws/build/tello_driver/catkin_generated/python_distutils_install.sh) returned error code ")
endif()
