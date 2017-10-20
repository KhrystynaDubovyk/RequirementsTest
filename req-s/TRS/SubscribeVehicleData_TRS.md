## Functional Requirements

1.
In case mobile application sent valid and allowed by Policies SubscribeVehicleData_request to SDL

SDL must: 
- transfer SubscribeVehicleData_request to HMI
- respond with `<resultCode>` received from HMI to mobile app 

2.
In case mobile application sends valid SubscribeVehicleData_request to SDL

and this request is NOT allowed by Policies

SDL must: 

respond "DISALLOWED, success:false" to mobile application




[19968] 1.

In case app_1 sends SubscribeVehicleData (param_1) to SDL  
AND SDL does not have this param_1 in list of stored successfully subscribed params  
SDL must:
- transfer SubscribeVehicleData(param_1) to HMI
- in case SDL receives SUCCESS from HMI for param_1 SDL must store this param in list AND respond SubscribeVehicleData (SUCCESS) to app_1
- respond with corresponding result SUCCESS received from HMI to app_1

[19978] 2. 

In case app_2 sends SubscribeVehicleData (param_1, param_2) to SDL  
AND SDL has successfully already subscribed param_1 and param_2 via SubscribeVehicleData to app_1  
SDL must:
1) NOT send SubscribeVehicleData(param_1, param_2) to HMI.
2) respond via SubscribeVehicleData (SUCCESS) to app_2

[19997] 3. 

In case mobile application sends valid SubscribeVehicleData_request 

trying to subscribe the parameter the application has already subscribed for (even if the request contains at least one non-subscribed parameter)

SDL must: 
- ignore alredy subscribed items and transfer not subscribed params of SubscribeVehicleData to HMI
- get the response with general_result_Code_from_HMI and newly-subscribed parameters with their correponding individual-result-codes from HMI 
- respond to mobile application with "ResultCode: IGNORED, success: <applicable flag>" + "info" parameter+ all parameters and their correponding individual result codes got from HMI and all ignored parameter(s) with the individual result code(s): DATA_ALREADY_SUBSCRIBED for items ignored by SDL.


[] 4. INVALID_DATA
In case mobile application sends SubscribeVehicleData_request to SDL  
- with wrong json syntax 
- with wrong type parameters (including parameters of the structures)
- without parameters defined as mandatory in mobile API

SDL must:  
respond "INVALID_DATA, success:"false" to mobile application

5. GENERIC_ERROR
In case mobile application sends SubscribeVehicleData_request to SDL and:
- either unknown issue happened 
- either something went wrong

SDL must:  
respond with "GENERIC_ERROR, success:"false" to mobile application

[15509]
In case 
HMI sends invalid response by any reason that SDL must transfer to mobile app
SDL must: 
log the error internally
respond GENERIC_ERROR (success:false, info: "Invalid message received from vehicle") to mobile app

Information: 
1. Invalid response means the response contains:
a. params out of bounds
b. mandatory params are missing
c. params of wrong type
d. invalid json
Note: in case SDL cannot parse 'method_name' from json then SDL must respond to mobile app GENERIC_ERROR, info: "'%component-name%' component does not respond"
e.incorrect combination of params

[19624]6. IGNORED
In case app already subscribed on a single or multiple <vehicleData>
and sends SubscribeVehicleData_request with all <vehicleData> subscribed by the application before
SDL must:
1) not transfer a resuest to HMI
2) respond with (IGNORED, success:false {<vehicleData>: DATA_ALREADY_SUBSCRIBED} ) to mobile app


## Non-Functional Requirements

## Diagrams

SubscribeVehicleData

![SubscribeVehicleData](https://github.com/smartdevicelink/sdl_requirements/blob/SubscribeWayPoints/detailed_docs/accessories/SubscribeVehicleData.png)

