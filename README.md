# IOT_Project_Home_Invasion
Home invasion detection backend API using flask, marshmellow, mongoDB, time series collections
Milestone 1 PDF: [Milestone_1_Proposal_and_Design_Document_Mohit-Maxime-Paul.pdf](https://github.com/dufourmax1738/IOT_Project_Home_Invasion/files/10292208/Milestone_1_Proposal_and_Design_Document_Mohit-Maxime-Paul.pdf)
Milestone 2 PDF: [Milestone_2_MongoDB_Schema_Design_Api_Endpoints_Mohit-Maxime-Paul.pdf](https://github.com/dufourmax1738/IOT_Project_Home_Invasion/files/10292209/Milestone_2_MongoDB_Schema_Design_Api_Endpoints_Mohit-Maxime-Paul.pdf)
Complete-Milestone 3 PDF: [Milestone_3_Flask_Api_Intergration.pdf](https://github.com/dufourmax1738/IOT_Project_Home_Invasion/files/10292213/Milestone_3_Flask_Api_Intergration.pdf)

PROJECT INTRODUCTION 

With technology advancing more and more throughout the years, a particular industry that has 
taken advantage and thrived over the changing environment is security. Following this trend, we 
have decided to create a security device. Utilizing the Arduino Nano as well as using various 
sensors such as motion and sound to detect the presence and individuals in a given location. This 
device can be placed in any location based on the user’s desire. The main goal is for the user to 
be bale to detect and be aware of any intruder and general activity in a given location. Using 
have the device set up. By using sound, the user will be able to detect more abnormal activity 
and if the area warrants further inspection. 

TARGET AUDIENCE

The target Audience are both teenagers and adults between the ages of 16 to mid 40’s. More 
specifically anyone who owns a type of property or has access to a specific location they want 
monitored. The reason our target demographic is so large is simply because of the many ways our 
device can be used based on your age. A teenager might want to use it to make sure his siblings 
don’t enter his room. An adult who is a homeowner might want to use it in his front door or any 
access point in his house to prevent or monitor break-ins, lastly a business owner might use it to 
monitor activity in his store. All these scenarios target a wide array of ages and people which is 
why we have an immense demographic. 


Sensors used: KY-037 sound detection Sensor, PIR Motion Sensor 

Hardware and assecsories used: Breadboard, Arduino Nano, Wires


SENSOR DATA SAMPLING SPECIFICATION

For our device in terms of sampling the sound data for the K-037 sound detection sensor, we take 
the averaging out the sound data and sending it only to the server when it goes above or below a 
certain margin. For the PIR motion sensor data sampling, it will simply send data to the backend 
when motion is detected.



API ENDPOINTS

Api url =
http://127.0.0.1:5000

GET /homes/
Gets all the homes in the system
GET /homes/<homeName>
Gets information about home with homeName 
POST /homes/
Creates new home with name variable sent in request
PUT /home/<homeName>
Updates homeName to variable sent in requesr
DELETE /home/<homeName>
Deletes home by its name

GET /homes/<homeName>/devices
Gets information about all devices in home
GET /homes/<homeName>/devices/<deviceName>
Gets all information for one device
POST /home/<homeName>/devices
Creates new device with name, motionSensorId and soundSensorId sent in request
PUT /home/<homeName>/devices/<deviceName>
Update device with deviceName with name, motionSensorId and soundSensorId sent in request
DELETE /home/<homeName>/devices/<deviceName>
Deletes device by its name


POST /sensors/<sensorId>/motion
Used by motionSensor, creates new motion input with the motion variable sent in the request
GET /sensors/<sensorId>/motion
Returns the count of how many times motion was detected
Arguments:

POST /sensors/sensorId>/sound
Used by sound sensor, creates new sound input with sound variable in the request
GET /sensors/<sensorId>/sound
Gets the count of how often sound was heard

Start
Defines start time of when records should be returned
End
Defines end time of when records should be returned


PRODUCT DEMONSTRATION

The following is a link to a video demonstration where our team explains our full product 
and process ran for recording and querying data:  
https://www.dropbox.com/s/t6hpf4c21p0gdmd/HomeInvasionPresentation_IOT.mp4?dl=0

GitHub repository link: https://github.com/dufourmax1738/IOT_Project_Home_Invasion

