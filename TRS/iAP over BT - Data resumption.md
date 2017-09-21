## Functional Requirements  

1. In case  
app re-registers during "AppTransportChangeTimer" + "AppTransportChangeTimerAddition"*N  
and sends valid "hashID" param via RegisterAppInterface_request to SDL  

SDL must:
- respond RegisterAppInterface (SUCCESS, success:true) to mobile app (in case of no other failures)
- keep all data created/stored by this app BEFORE re-registration (transport switching)

2. In case  
app re-registers during "AppTransportChangeTimer" + "AppTransportChangeTimerAddition"*N   
and sends invalid "hashID" param via RegisterAppInterface_request to SDL  
OR omits "hashID" at all  

SDL must:
- respond RegisterAppInterface (RESUME_FAILED, success:true) to mobile app (in case of no other failures)
- clear all data related to this app internally except "AppIconsFolder"
- send requests to remove data in HMI (please see list of RPCs below)

3. In case  
app re-register AFTER "AppTransportChangeTimer" + "AppTransportChangeTimerAddition"*N expiration  
and sends valid "hashID" param via RegisterAppInterface_request to SDL  

SDL must:  
- start data resumption process according to existing rules

4. In case  
app re-registers AFTER "AppTransportChangeTimer" + "AppTransportChangeTimerAddition"*N expiration  
and sends invalid "hashID" param via RegisterAppInterface_request to SDL  
or omits "hasID" at all  

SDL must:
- behave according to existing rules 
