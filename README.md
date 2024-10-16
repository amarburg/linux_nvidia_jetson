# BSP for Xavier-NX / Antmicro Nano baseboard / Alvium / IMX477

This is a fork of the Allied Vision [linux_nvidia_jetson](https://github.com/alliedvision/linux_nvidia_jetson) repo which builds a kernel for Jetson boards including support for the AVT Alvium cameras.  Onto this base the patches for the
[AntMicro Nano baseboard](https://github.com/antmicro/jetson-nano-baseboard/tree/master/linux-patches) and Ridgerun's [support for the IMX477 (aka Raspberry Pi HQ) camera](https://github.com/RidgeRun/NVIDIA-Jetson-IMX477-RPIV3) have been applied

The core instructions work well:

```
./setup.sh <build_dir> nx 
./build.sh <build_dir> nx all all
```

In addition to patching an existing system, the `sd-card` method works well using an SD image downloaded from Nvidia ([link for Xavier NX](https://developer.nvidia.com/embedded/downloads#?tx=$product,jetson_xavier_nx)) by doing:

```
./deploy.sh <build_dir> nx sd-image <path to original sd image>
```

then writing the resulting image as per the original Nvidia instructions.

----
----

**README from the original Allied Vision repo below.**

----


Driver for Allied Vision Alvium cameras with MIPI CSI-2 interface for NVIDIA Jetson with JetPack 4.5.1 (L4T 32.5.1)     
https://developer.nvidia.com/embedded/jetpack
![Alvium camera](https://cdn.alliedvision.com/fileadmin/content/images/cameras/Alvium/various/alvium-cameras-models.png)

## Overview

The scripts in this project build and install the Allied Vision CSI-2 driver to the NVIDIA Jetson boards.   
:bulb: **This driver version supports V4L2 and GenICam for CSI-2 (camera usage with [Vimba's](https://www.alliedvision.com/en/products/vimba-sdk/) CSI-2 transport layer)**

Platforms: AGX Xavier and Xavier NX development kits.    
:bulb: Nano and TX2 are supported by driver version [2.1.0](https://github.com/alliedvision/linux_nvidia_jetson/tree/l4t-32.5.1-2.1.0)    
JetPack 4.5.1 (L4T 32.5.1)  
The scripts require Git on the host PC.

***Before starting the installation, make sure to create a backup of your Jetson system.***

## Prerequisites: Install JetPack 4.5.1 to AGX Xavier or Xavier NX developer kit.
 
Install JetPack 4.5.1 (L4T 32.5.1) as per NVIDIA's instructions https://developer.nvidia.com/embedded/jetpack      

Recommendation: Use NVIDIA SDK Manager to install JetPack and useful tools such as CUDA.   
https://docs.nvidia.com/sdk-manager/  
	
### Accidental overwriting of the driver
As of JetPack 4.4, users can update L4T directly on the board with `apt-upgrade`. 
Doing this may install newer L4T kernel and device tree files, which overwrite the driver for Allied Vision cameras. 
If you use `apt-upgrade` nevertheless, please prevent overwriting the driver with:

 `sudo apt-mark hold 'nvidia-l4t-*'`

Note that both reinstalling the driver or putting the update on hold may cause unavailable features or bugfixes from NVIDIA.

## Install Alvium CSI-2 driver to Jetson AGX Xavier or Xavier NX

**Method A: Use precompiled binaries**   
 
  Install the precompiled kernel including driver and installation instructions.   

  1. Extract the tarball on a host PC.

  2. The tarball contains helper scripts and another tarball with the precompiled binaries named AlliedVision_NVidia_L4T_32.5.1_<git-rev>.tar.gz.   
     Copy the tarball to the target board. On the target board, extract the tarball and run the included install script.   
     Reboot the board. Now you can use the driver. 	

 **Method B: Cross-compile binaries from source**      
  The scripts require a host PC with Ubuntu (we recommend version 18.04) installed.

  1. Download sources and scripts from https://github.com/alliedvision/linux_nvidia_jetson to the host PC.   
     On the host PC:
    
  2. Run setup.sh, which prepares the directory structure, extracts the file archive, etc.:   
     `$ ./setup.sh <WORK_DIR> <TARGET_BOARD> # For example, $ ./setup.sh work_dir xavier` 
	 
  3. Run build.sh, which builds the kernel, modules, device tree files, and the bootloader:   
     `# Use the same WORK_DIR for all scripts`   
     `# Example: $ ./build.sh work_dir xavier all all`   
     `$ ./build.sh <WORK_DIR> <TARGET_BOARD> <BUILD_OPTIONS> <COMPONENTS> <OPTIONS>`    
	 
  4. Create a tarball with the kernel image and modules.   
     `$ ./deploy.sh <WORK_DIR> <TARGET_BOARD> tarball`
		 
  5. Copy the tarball to the target board. On the target board, extract the tarball and run the included install script.   
     Reboot the board. Now you can use the driver. 

 ## Additional information
 :open_book:
 https://github.com/alliedvision/documentation/blob/master/NVIDIA.rst



