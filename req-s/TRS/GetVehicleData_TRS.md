## Functional Requirements

1.
In case mobile application sends valid and allowed by Policies GetVehicleData_request to SDL

SDL must: 
- transfer GetVehicleData_request to HMI
- respond with `<resultCode>` received from HMI to mobile application
- provide the requested wayPoints at the same order as received from HMI to mobile application (in case of successful response)

2.
In case mobile application sends valid GetVehicleData_request to SDL

and this request is NOT allowed by Policies

SDL must:
respond "DISALLOWED, success:false" to mobile application

3. 
In case mobile application sends valid and allowed by Policies GetWayPoints_request to SDL

and Navigation interface is not available on HMI

or

 "getWayPointsEnabled": false in HMI capabilities
 
 SDL must:
 
 respond "UNSUPPORTED_RESOURCE, success:false" to mobile application and not transfer this request to HMI

## Non-Functional Requirements

## Diagram

GetVehicleData

![GetVehicleData](https://github.com/smartdevicelink/sdl_requirements/blob/GetVehicleData/detailed_docs/accessories/GetVehicleData.png)
