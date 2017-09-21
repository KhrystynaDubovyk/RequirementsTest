## Functional Requirements  

1.  
In case device was connected over Bluetooth and SDL received signal about USB connection of the same device  

SDL must:
- start "AppTransportChangeTimer" + "AppTransportChangeTimerAddition"*N
- after receiving switch signal from external system  
*Note:* N is the number of applications that need to be re-registered

2.  
In case mobile app sends `<RegisterAppInterface>` during "AppTransportChangeTimer" + "AppTransportChangeTimerAddition"*N timer
and "UUID" and appID parameters match with closed session

SDL must:
- consider such app as re-registered app
- update data in PolicyTable ("device_identifier" section)
- send `<UpdataDeviceList>` to HMI  
SDL must NOT:
send `<BC.OnAppRegistered>` to HMI  
*Note:* For HMI during re-connection all applications remain registered and active, HMILevel resumption is not applicable

3.  
In case mobile app was not re-registered during "AppTransportChangeTimer" + "AppTransportChangeTimerAddition"*N
due to transport type change

SDL must:
- send `<BC.OnAppUnregistered>` (appID, unexpectedDisconnect:true) to HMI for such app

4.  
In case mobile app sends `<RegisterAppInterface>` during "AppTransportChangeTimer" + "AppTransportChangeTimerAddition"*N timer
and "UUID" of reconnected device matches
and "appID" parameter does not match with closed session  

SDL must:
- register such app as a new app
- send `<BC.OnAppRegistered>` to HMI
- send `<BC.UpdateAppList>` to HMI

5.  
In case mobile app sends `<RegisterAppInterface>` during "AppTransportChangeTimer" + "AppTransportChangeTimerAddition"*N timer
and "appID" parameter matches with appID of closed session
and "UUID" does not match  

SDL must:
- respond `<RegisterAppInterface>` (DUPLICATE_NAME, success:false)

6.  
In case iOS device is connected over one of the available transports

SDL must:
- write hashed "UUID" to "device identifier" in Device Data section of Policy Table

7.  
In case iOS device was connected over USB
and USB connection was lost  

SDL must:
- NOT start "AppTransportChangeTimer" + "AppTransportChangeTimerAddition"*N timer for reconnection  
*Note:* In case of USB connection lost, SDL must proceed with unexpected disconnect flow 