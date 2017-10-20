## Functional Requirements

1.
In case mobile application sent valid and allowed by Policies SubscribeVehicleData_request to SDL

SDL must: 
- transfer SubscribeVehicleData_request_ to HMI
- respond with `<resultCode>` received from HMI to mobile app 

2.
In case mobile application sent valid SubscribeVehicleData_request to SDL

and this request is NOT allowed by Policies

SDL must: 

respond "DISALLOWED, success:false" to mobile application


3.
In case mobile application sends valid SubscribeVehicleData_request 

trying to subscribe the parameter the application has already subscribed for (even if the request contains at least one non-subscribed parameter)

SDL must: 
- ignore alredy subscribed items and transfer not subscribed params of SubscribeVehicleData to HMI
- get the response with general_result_Code_from_HMI and newly-subscribed parameters with their correponding individual-result-codes from HMI 
- respond to mobile application with "ResultCode: IGNORED, success: <applicable flag>" + "info" parameter+ all parameters and their correponding individual result codes got from HMI and all ignored parameter(s) with the individual result code(s): DATA_ALREADY_SUBSCRIBED for items ignored by SDL



5.
In case mobile application is subscribed on WayPoints-related parameters unexpectedly disconnects 

SDL must:
- store the status of subscription on wayPoints-related data for this application
- send UnsubscribeWayPoints_request to HMI ONLY if ther are no other applications currently subscribed to WayPoints-related data 
- restore status of subscription on WayPoints-related data for this application right after the same mobile application re-connects within the same ignition cycle with the same <'hashID'> as before unexpected disconnect
- after successful resumption send SubscribeWayPoints request to HMI only if ther are no other applications currently subscribed to WayPoints-related data 

6.
In case mobile application subscribed on WayPoints-related data in previous ignition cycle
registers during next ignition cycle with the same <'hashID'> as in previous ignition cycle

SDL must:

restore status of subscription on WayPoints-related data being in previous ignition cycle for this application

7.
In case mobile application is already subscribed on WayPoints-related data

and another application sends SubscribeWayPoints_request to SDL

SDL must:
- remember this other application as subscribed on WayPoints-related data
- respond SubscribeWayPoints (SUCCESS) to this other application without transferring second SubscribeWayPoints_request to HMI 
- send to this newly subscribed application stored OnWayPointChange-related data 


## Non-Functional Requirements

## Diagrams

SubscribeVehicleData

![SubscribeVehicleData](https://github.com/smartdevicelink/sdl_requirements/blob/SubscribeWayPoints/detailed_docs/accessories/SubscribeVehicleData.png)

