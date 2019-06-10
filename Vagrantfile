# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|

  # allow download (wins10)
  config.vm.box_download_insecure = true
  
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.
 
  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://vagrantcloud.com/search.
  config.vm.box = "ubuntu/bionic64"
  config.vm.box_version = "~> 20190314.0.0"

  config.vm.synced_folder ".", "/vagrant"
 
  # map vm กับเครื่อง สามารถใช้ port 8000
  # runserver 0.0.0.0:8000 บน VM
  config.vm.network "forwarded_port", guest: 8000, host: 8000
 
  config.vm.provision "shell", inline: <<-SHELL
    systemctl disable apt-daily.service
    systemctl disable apt-daily.timer
  
    sudo apt-get update
    sudo apt-get upgrade
    sudo apt-get install -y python3
    sudo apt-get install -y python3-pip

    # update python
    sudo apt-get install python3.7
    sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6 1
    sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.7 2
    # sudo update-alternatives --config python3

    # pipenv install
    pip3 install pipenv



  SHELL
 end