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


Driver for Allied Vision Alvium cameras with MIPI CSI-2 interface for NVIDIA Jetson with JetPack 4.4.1 (L4T 32.4.4)     
https://developer.nvidia.com/embedded/jetpack
![Alvium camera](https://cdn.alliedvision.com/fileadmin/content/images/cameras/Alvium/various/alvium-cameras-models.png)

## Overview

The scripts in this project build and install the Allied Vision CSI-2 driver to the NVIDIA Jetson boards.

Platforms: Nano, Nano 2GB, TX2, AGX Xavier, Xavier NX    
JetPack 4.4.1 (L4T 32.4.4)  
The scripts require Git on the host PC.

***Before starting the installation, make sure to create a backup of your Jetson system.***

## Prerequisites: Install JetPack 4.4.1 to Jetson Nano, Nano 2GB, TX2, AGX Xavier or Xavier NX
 
1. Install JetPack 4.4.1 (L4T 32.4.4) as per NVIDIA's instructions https://developer.nvidia.com/embedded/jetpack   
    Recommendation: Use NVIDIA SDK Manager to install JetPack and useful tools such as CUDA.   
    https://docs.nvidia.com/sdk-manager/  
	
2. Update and upgrade the host PC and the Jetson board:   
   `# sudo apt update`   
   `# sudo apt upgrade`

## Install Alvium CSI-2 driver to Jetson Nano, Nano 2GB, TX2, AGX Xavier or Xavier NX

 **Method A: Use precompiled binaries**   
  Install the precompiled kernel including driver and installation instructions:   
  https://www.alliedvision.com/en/products/software/embedded-software-and-drivers/

  1. Extract the tarball on a host PC.

  2. The tarball contains helper scripts and another tarball with the precompiled binaries named AlliedVision_NVidia_L4T_32.4.4_<git-rev>.tar.gz.   
     Copy the tarball to the target board. On the target board, extract the tarball and run the included install script.   
     Reboot the board. Now you can use the driver. 

 **Method B: Cross-compile binaries from source**    
  These scripts require a host PC with Ubuntu (16.04 or 18.04) installed.

  1. Download sources and scripts from https://github.com/alliedvision/linux_nvidia_jetson to the host PC.   
     On the host PC:
    
  2. Run setup.sh, which prepares the directory structure, extracts the file archive, etc.:   
     `$ ./setup.sh <WORK_DIR> <TARGET_BOARD> # For example, $ ./setup.sh work_dir nano` 
	 
  3. Run build.sh, which builds the kernel, modules, device tree files, and the bootloader:   
     `# Use the same WORK_DIR for all scripts`   
     `# Example: $ ./build.sh work_dir nano all all`   
     `$ ./build.sh <WORK_DIR> <TARGET_BOARD> <BUILD_OPTIONS> <COMPONENTS> <OPTIONS>`    
	 
  4. Create a tarball with the kernel image and modules.   
     `$ ./deploy.sh <WORK_DIR> <TARGET_BOARD> tarball`
		 
  5. Copy the tarball to the target board. On the target board, extract the tarball and run the included install script.   
     Reboot the board. Now you can use the driver. 

 ## Additional information
 :open_book:
 https://github.com/alliedvision/documentation/blob/master/NVIDIA.md

