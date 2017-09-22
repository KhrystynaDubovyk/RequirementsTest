## Use Case 1: iAP over BT - Data resumption

**Main Flow:**

_Pre-conditions:_  
a. iOS device is connected over Bluetooth  
b. App from iOS device is registred and running on SDL  

_Steps:_  
1. User connects the same iOS device over USB

_Expected:_  
2. SDL starts `<AppTransportChangeTimer> + <AppTransportChangeTimerAddition>*N` reconnection timer  
3. SDL receives RegisterAppInterface request before timer expires
4. SDL validates "hashID" received with RegisterAppInterface request
5. SDL sends succesful response to the app  
6. SDL successfully resumes data for this app

_Exception 1:_  
 SDL receives `<RegisterAppInterface>` request with valid "hashID" **after** timer expiration  
When `<AppTransportChangeTimer> + <AppTransportChangeTimerAddition>*N` reconnection timer
 SDL notifies HMI about app being unregistred  
 SDL removes all notifications from HMI that were saved during reconnection timer 
 When the app re-registers SDL checks `<hashID>`
it would be considered as a fresh registration.
Since the app provides a valid hash id, SDL core will perform data resumption.

_Exception 2:_  
3.1.a SDL receives `<RegisterAppInterface>` request with **invalid** "hashID" or no "hashID" at all  
3.1.b SDL responds RESUME_FAILED, success:true to the app    
3.1.c SDL clears all data created/stored by this app  
3.1.d SDL sends to HMI following RPCs:  
OnButtonSubscription (isSubscribed=false)  
UnsubscribeVehicleData  
UnsubscribeWayPoints
ResetGlobalProperties  
DeleteSubMenu  
DeleteCommand  
DeleteCommands for choiseSets (CreateInteractionChoiceSet)  

Alt flo
after timer with valid hash id

**_Note:_**
