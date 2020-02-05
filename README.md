# ros_nerf_turret_driver

sudo cp resources/50-sensor.rules /etc/udev/rules.d/50-sensor.rules
replace the idVendor and idProduct with correct ones from running "lsusb"
sudo service udev restart
sudo udevadm trigger
