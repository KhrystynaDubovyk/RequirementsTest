_Techical task must have the following labels:_

**Technical Task**

**Priority:** _High, Medium or Low_


## Description:

_Currently SDL keeps data created by app in case of transport switching independenlty on value of <hashID>.
It may cause a lot of issues from mobile app perspective if app sends invalid "hashID" but SDL still keeps all data for this app.
As a result, to avoid all concerns -> SDL will keep data ONLY if app sends valid "hashID" during "reconnection_timer".
Otherwise, SDL will remove all data internally and trigger HMI to remove all data related to this app.
If mobile app re-registers after "reconnection_timer" -> SDL must behave per existing rules for Data Resumption._

1. In case
app re-registers during "AppTransportChangeTimer" + "AppTransportChangeTimerAddition"*N
and sends valid "hashID" param via RegisterAppInterface_request to SDL
SDL must:
respond RegisterAppInterface (SUCCESS, success:true) to mobile app (in case of no other failures)
keep all data created/stored by this app BEFORE re-registration (transport switching)

2. In case
app re-registers during "AppTransportChangeTimer" + "AppTransportChangeTimerAddition"*N 
and sends invalid "hashID" param via RegisterAppInterface_request to SDL
OR omits "hashID" at all
SDL must:
respond RegisterAppInterface (RESUME_FAILED, success:true) to mobile app (in case of no other failures)
clear all data related to this app internally except "AppIconsFolder"
send requests to remove data in HMI (please see list of RPCs below)

3. In case
app re-register AFTER "AppTransportChangeTimer" + "AppTransportChangeTimerAddition"*N expiration 
and sends valid "hashID" param via RegisterAppInterface_request to SDL 
SDL must:
start data resumption process according to existing rules

4. In case
app re-registers AFTER "AppTransportChangeTimer" + "AppTransportChangeTimerAddition"*N expiration 
and sends invalid "hashID" param via RegisterAppInterface_request to SDL
or omits "hasID" at all
SDL must:
behave according to existing rules 

**Info:** 
 List of RPCs to be sent to HMI:
DeleteCommand
DeleteSubMenu
DeleteCommands for choiseSets (CreateInteractionChoiceSet)
ResetGlobalProperties
OnButtonSubscription (isSubscribed=false)
UnsubscribeVehicleData (ONLY if no other apps currently subscribed to the same vehicleData-related params)
UnsubscribeWayPoints (ONLY if no other apps currently subscribed to wayPoints-related data)

## Related Diagrams:

![iap_over_bt_data_resumption](https://user-images.githubusercontent.com/23719788/28126364-f09111d6-6731-11e7-8cf3-bb3bbd84c2ee.png)

## Links:

- **Requirement:** GitHub issue number + summary
- **Parent task:** Link to parent task issue + summary **or empty**

## Expected Delivery (Definition of Done)

- [ ] Requirements analysis and updates
- [ ] Source code updates
- [ ] Code comments
- [ ] UTs add/update
- [ ] Integration tests add/update
- [ ] **Manual tests (not required)**
- [ ] Add/update CI plans/jobs
- [ ] SDD updates
- [ ] SAD updates
- [ ] Guidelines update 1 ([sdl_core_guides](https://github.com/smartdevicelink/sdl_core_guides))
- [ ] Guidelines update 2 ([sdl_hmi_integration_guidelines](https://github.com/smartdevicelink/sdl_hmi_integration_guidelines))
