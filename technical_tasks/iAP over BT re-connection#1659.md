## Description:
When the device connects over USB, SDL core shall notify HMI about the change in transportType via the UpdateDeviceList RPC. To mitigate the disruption to the user’s UI experience SDL Core must hold off on sending to HMI the information about disconnect of the applications till a pre-configured “reconnection” timer expires. This “reconnection” timer would be added to the SmartDeviceLink.ini file. Application is expected to be re-registered during "reconnection" timer and in case if re-registration was unsuccessful, SDL core must proceed with "unexpectedDisconnect" 


1. In case device was connected over Bluetooth and SDL received signal about USB connection of the same device
SDL must
start "AppTransportChangeTimer" + "AppTransportChangeTimerAddition"*N
after receiving switch signal from external system
*Note:* N is the number of applications that need to be re-registered

2. In case mobile app sends RegisterAppInterface during "AppTransportChangeTimer" + "AppTransportChangeTimerAddition"*N timer
and "UUID" and appID parameters match with closed session
SDL must:
consider such app as re-registered app
update data in PolicyTable ("device_identifier" section)
send UpdataDeviceList to HMI
SDL must NOT:
send BC.OnAppRegistered to HMI
*Note:* For HMI during re-connection all applications remain registered and active, HMILevel resumption is not applicable

3. In case mobile app was not re-registered during "AppTransportChangeTimer" + "AppTransportChangeTimerAddition"*N
due to transport type change
SDL must
send BC.OnAppUnregistered (appID, unexpectedDisconnect:true) to HMI for such app

4. In case mobile app sends RegisterAppInterface during "AppTransportChangeTimer" + "AppTransportChangeTimerAddition"*N timer
and "UUID" of reconnected device matches
and "appID" parameter does not match with closed session
SDL must:
register such app as a new app
send BC.OnAppRegistered to HMI
send BC.UpdateAppList to HMI

5. In case mobile app sends RegisterAppInterface during "AppTransportChangeTimer" + "AppTransportChangeTimerAddition"*N timer
and "appID" parameter matches with appID of closed session
and "UUID" does not match
SDL must:
respond RegisterAppInterface (DUPLICATE_NAME, success:false)

6. In case iOS device is connected over one of the available transports
SDL must:
write hashed "UUID" to "device identifier" in Device Data section of Policy Table

7. In case iOS device was connected over USB
and USB connection was lost
SDL must
NOT to start "AppTransportChangeTimer" + "AppTransportChangeTimerAddition"*N timer for reconnection
*Note:* In case of USB connection lost, SDL must proceed with unexpected disconnect flow 

## .ini file change ##
1. 
``` xml
[IAP] 
; defines the timeout for waiting the mobile app to reconnect between Bluetooth and USB transports change
"AppTransportChangeTimer" = 500 ms
```

2. 
```xml
[IAP] 
"AppTransportChangeTimerAddition" = 0ms
Defines the timeout  for waiting of every mobile app to reconnect between Bluetooth and USB transports change in case the number of connected apps is more than one
```
## Related Diagrams:

N/A

## Links:

- **Requirement:** GitHub issue number + summary
- **Parent task:** 

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
