## Functional Requirements

1.
In case mobile application sent valid and allowed by Policies SubscribeVehicleData_request to SDL

SDL must: 
- transfer SubscribeVehicleData_request to HMI
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



[19968] 1. 
In case app_1 sends SubscribeVehicleData (param_1) to SDL  
AND SDL does not have this param_1 in list of stored successfully subscribed params  
SDL must:
1) transfer SubscribeVehicleData(param_1) to HMI
2) in case SDL receives SUCCESS from HMI for param_1 SDL must store this param in list AND respond SubscribeVehicleData (SUCCESS) to app_1
3) respond with corresponding result SUCCESS received from HMI to app_1

[19978] 2. 
In case app_2 sends SubscribeVehicleData (param_1, param_2) to SDL  
AND SDL has successfully already subscribed param_1 and param_2 via SubscribeVehicleData to app_1  
SDL must:
1) NOT send SubscribeVehicleData(param_1, param_2) to HMI.
2) respond via SubscribeVehicleData (SUCCESS) to app_2





## Non-Functional Requirements

## Diagrams

SubscribeVehicleData

![SubscribeVehicleData](https://github.com/smartdevicelink/sdl_requirements/blob/SubscribeWayPoints/detailed_docs/accessories/SubscribeVehicleData.png)

