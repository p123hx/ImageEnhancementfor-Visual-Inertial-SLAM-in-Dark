# ImageEnhancementfor-Visual-Inertial-SLAM-in-Dark

Image Enhancement for Visual Inertial SLAM in Dark Scenarios

Mobile Robotics Winter 2023 Team 2

This repository contains the code for our final project for Mobile Robotics. Our project was built off of a previous team's final project (Winter 2022 Team 22) and compares different image enhancement techniques used alongside the visual SLAM algorith called ORB-SLAM3 in order to reduces tracking/ translational error. 
This repository contains the code for our final project for Mobile Robotics. Our project was built off of a previous team's final project (Winter 2022 Team 22) and compares different image enhancement techniques used alongside the visual SLAM algorith called ORB-SLAM3 in order to reduces tracking/ translational error. Our use case is specifically for dark environments. 

Thew winter 2022 Team's Repository is found [here](https://github.com/Maithilishetty/Mobile_Robotics_Team22). 

Here is our final [presentation](https://docs.google.com/presentation/d/1JiwIiU2ep6RfWaUEhsucTmFSWXvVtnpb/edit#slide=id.p1), [video]() , and final [report](https://drive.google.com/drive/u/0/folders/1EeNf3pVsSfgrlBif_ObC9zKsfOXbuV2S). A copy of our google drive folder with the datasets is located [here](https://drive.google.com/drive/u/0/folders/1EeNf3pVsSfgrlBif_ObC9zKsfOXbuV2S) as uploading full datasets into git is not effecient.  

Our project uses the Dataset [TartanAir](https://theairlab.org/tartanair-dataset/) which is known for its difficulty. Within Tartan Air we chose two separate two separate environments called Abandoned Factory Night and Hospital. Abandoned Factory Night was the main dataset around which we tested image enhacement for dark scenarios and Hospital was a secondary dataset used for testing our model on an indoor environment (note this environment however is not dark). 

## Project Features 
Within this repository there are the image ehancement technique files in the form of jupyter notebooks used to improve the dataset, python files to convert the dataset, there is much of the orbslam 3 repo including our modifications to the Settings.cc file, as well as files for setup of a Docker environment in order to run ORB-SLAM  

## Dataset conversion
In order to use the Tartan Air dataset it is critical to covert the dataset to a form compatible with ORBSLAM. As mentioned in the ORB-SLAM3 documentation two of such compatible forms are the Euroc and Kitti Formats. Our team used the Kitti Format. While the original datasets can be pulled directly from TartanAir, our google drive also contains the Dataset Files converted for use. 

To convert the ground truth file into Kitti format run
```
xyzq2kitti.py
```

To covert the dataset into Kitti format run 
```
tartan_to_kitt.py
```

## Building Orbslam3
Refer to [ORB-SLAM3](https://github.com/UZ-SLAMLab/ORB_SLAM3)
We have provided an easy way to build and run Orbslam3 using docker(modified volumn in [compose file](https://github.com/p123hx/ImageEnhancementfor-Visual-Inertial-SLAM-in-Dark/blob/main/Docker/docker-compose.yaml) to mount dataset path to the container):
```
cd Dockerfile
docker-compose up
```
To run ORBSLAM3 on a TartanAir Data set: 
```
./Examples/Stereo/stereo_kitti Vocabulary/ORBvoc.txt /media/dataset/tartanair.yaml /media/dataset /media/dataset/timestamp.txt
```
## Calculating Absolute Translational Errror 
To calculate Absolute Translational Error our team used resources from the evo library located [here](https://github.com/MichaelGrupp/evo). 
```
evo_ape kitti gt.txt pred.txt -va -p
```

