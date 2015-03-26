Name:           ros-indigo-robot-calibration
Version:        0.2.0
Release:        0%{?dist}
Summary:        ROS robot_calibration package

Group:          Development/Libraries
License:        Apache2
URL:            http://ros.org/wiki/robot_calibration
Source0:        %{name}-%{version}.tar.gz

AutoProv:       0
Requires:       ceres-solver-devel
Requires:       protobuf-compiler
Requires:       protobuf-devel
Requires:       ros-indigo-actionlib
Requires:       ros-indigo-camera-calibration-parsers
Requires:       ros-indigo-control-msgs
Requires:       ros-indigo-cv-bridge
Requires:       ros-indigo-geometry-msgs
Requires:       ros-indigo-kdl-parser
Requires:       ros-indigo-moveit-msgs
Requires:       ros-indigo-nav-msgs
Requires:       ros-indigo-orocos-kdl
Requires:       ros-indigo-pcl-ros
Requires:       ros-indigo-robot-calibration-msgs
Requires:       ros-indigo-rosbag
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-sensor-msgs
Requires:       ros-indigo-std-msgs
Requires:       suitesparse-devel
BuildRequires:  ceres-solver-devel
BuildRequires:  gflags-devel
BuildRequires:  protobuf-compiler
BuildRequires:  protobuf-devel
BuildRequires:  ros-indigo-actionlib
BuildRequires:  ros-indigo-camera-calibration-parsers
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-control-msgs
BuildRequires:  ros-indigo-cv-bridge
BuildRequires:  ros-indigo-geometry-msgs
BuildRequires:  ros-indigo-kdl-parser
BuildRequires:  ros-indigo-moveit-msgs
BuildRequires:  ros-indigo-nav-msgs
BuildRequires:  ros-indigo-orocos-kdl
BuildRequires:  ros-indigo-pcl-ros
BuildRequires:  ros-indigo-robot-calibration-msgs
BuildRequires:  ros-indigo-rosbag
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-sensor-msgs
BuildRequires:  ros-indigo-std-msgs
BuildRequires:  suitesparse-devel

%description
Calibrate a Robot

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Wed Mar 25 2015 Michael Ferguson <mferguson@fetchrobotics.com> - 0.2.0-0
- Autogenerated by Bloom

