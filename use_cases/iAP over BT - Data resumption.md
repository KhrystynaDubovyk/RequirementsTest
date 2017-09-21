## Use Case 1: iAP over BT - Data resumption

**Main Flow:**

_Pre-conditions:_  
a. iOS device is connected over Bluetooth  
b. App from iOS device is registred and running on SDL  

_Steps:_  
1. User connects the same iOS device over USB

_Expected:_  
2. SDL starts `<AppTransportChangeTimer> + <AppTransportChangeTimerAddition>*N` reconnection timer  
3. SDL receives RegisterAppInterface request with valid "hashID" during timer  
4. SDL sends succesful response to app  
5. SDL keeps all data created/stored by this app

_Exception 1:_  
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

_Exception 2:_  
3.2.a SDL receives `<RegisterAppInterface>` request with valid "hashID" **after** timer expiration  
3.2.b SDL notifies HMI about app being unregistred  
3.2.c If the app re-registers it would be considered as a fresh registration.
Since the app provides a valid hash id, SDL core will perform data resumption.





**Alternative flow 1:**

**_Note:_**
