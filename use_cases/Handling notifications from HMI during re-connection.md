

## Use Case 1: Handling notifications from HMI during re-connection

**Main Flow:**

_Pre-conditions:_  
 1. iOS device is connected over Bluetooth
 2. Device is consented and N applications from this device are registered in SDL  
 
_Steps:_  
 3. User connects the same device over USB  
 
_Expected:_   
 4. SDL starts `<AppTransportChangeTimer> + <AppTransportChangeTimerAddition>*N` timer for reconnection  
 5. SDL does not unregister the applications until `<AppTransportChangeTimer> + <AppTransportChangeTimerAddition>*N` timer expires

_Exception 1:_  
In case due to transport change SDL started <AppTransportChangeTimer> + <AppTransportChangeTimerAddition>*N reconnection timer  
and  
HMI sends any notifications and requests to <appID> that needs to be reconnected  
SDL must:  
- store all the notifications and requests from HMI internally  
- transfer all notifications and requests from HMI right after the <appID> will be reconnected 
 
 
_Exception 2:_  
In case due to transport change SDL started <AppTransportChangeTimer> + <AppTransportChangeTimerAddition>*N reconnection timer  
and  
HMI sends any responses to <appID> on requests that were sent before reconnection  
SDL must:  
- discard all responses to such <appID> from HMI
