# Image Enhancement for Visual-Inertial SLAM in Dark Scenarios

Mobile Robotics Winter 2023 Team 2

This repository contains the code for our final project for Mobile Robotics. Our project was based on a previous team's final project (Winter 2022 Team 22) and compares different image enhancement techniques used alongside a visual SLAM algorithm called ORBSLAM3 in order to reduce tracking error/absolute translational error. 
Our use case is specifically for dark environments, as opposed to the previous team's emphasis on underwater only environments. 

The winter 2022 Team's Repository is found [here](https://github.com/Maithilishetty/Mobile_Robotics_Team22). 

Here is our final [presentation](https://docs.google.com/presentation/d/1JiwIiU2ep6RfWaUEhsucTmFSWXvVtnpb/edit#slide=id.p1), [video](https://www.youtube.com/watch?v=Kg4_dr7qAi8), and final [report](https://drive.google.com/drive/u/0/folders/1EeNf3pVsSfgrlBif_ObC9zKsfOXbuV2S). A copy of our Google Drive folder with the datasets is located [here](https://drive.google.com/drive/u/0/folders/1EeNf3pVsSfgrlBif_ObC9zKsfOXbuV2S) as uploading full datasets into GitHub is not effecient. To access a dataset, go to the 'Full Dataset' folder on our Google Drive.

Our project uses the [TartanAir](https://theairlab.org/tartanair-dataset/) Dataset, which is known for its difficulty. Within TartanAir, we chose two separate environments: Abandoned Factory Night and Hospital. Abandoned Factory Night is a dark outdoor dataset, and served as the main dataset we used to develop & test our image enhacement techniques. We compared our performance to the previous team's image enhancement method as well as baseline ORBSLAM3. The Hospital dataset was chosen as a stretch objective, because it is a very bright indoor dataset, and we wanted to challenge our image enhancement algorithm. 

## Project Features 
Within this repository there are python files to convert the raw dataset into a form that can be easily used by ORBSLAM3 (ie Kitti form, in our case), image ehancement technique files in the form of jupyter notebooks used to improve the dataset, and much of the ORBSLAM3 repo which is required to run our project. We've also included our modifications to the Settings.cc file (within ORBSLAM3), as well as files for setup of a Docker environment in order to run ORBSLAM3.

## Dataset conversion
In order to use the TartanAir dataset it is critical to convert the dataset to a form compatible with ORBSLAM. As mentioned in the ORBSLAM3 documentation, two of such compatible forms are the Euroc and Kitti Formats. Our team used the Kitti Format. While the original datasets can be pulled directly from TartanAir, our Google Drive also contains the Dataset Files converted for use. 

To convert the ground truth file into Kitti format run
```
xyzq2kitti.py
```

To covert the dataset into Kitti format run 
```
tartan_to_kitt.py
```

## Building Orbslam3
Refer to [ORBSLAM3](https://github.com/UZ-SLAMLab/ORB_SLAM3)
We have provided an easy way to build and run ORBSLAM3 using docker(modified volumn in [compose file](https://github.com/p123hx/ImageEnhancementfor-Visual-Inertial-SLAM-in-Dark/blob/main/Docker/docker-compose.yaml) to mount dataset path to the container):
```
cd Dockerfile
docker-compose up
```
To run ORBSLAM3 on a TartanAir Data set: 
```
./Examples/Stereo/stereo_kitti Vocabulary/ORBvoc.txt /media/dataset/tartanair.yaml /media/dataset /media/dataset/timestamp.txt
```

## Image Enhancement
Go to image_enhancement.
There are 4 jupyter notebooks.
They read data from Google Drive. We also recommend using Google Colab and taking advantage of CUDA (URetinext_Net.ipynd uses CUDA). 
Notice that you have to change the Google Drive location to the location you want to use.


## Calculating Absolute Translational Errror 
To calculate Absolute Translational Error, our team used resources from the evo library located [here](https://github.com/MichaelGrupp/evo). 
```
evo_ape kitti gt.txt pred.txt -va -p
```

