
Precondition:
 1. iOS device is connected over Bluetooth
 2. Device is consented and N applications from this device are registered in SDL  
 
 Steps:  
 3. User connects the same device over USB  
 
 Expected result:  
 4. SDL starts `<AppTransportChangeTimer> + <AppTransportChangeTimerAddition>*N` timer for reconnection  
 5. SDL does not unregister the applications until `<AppTransportChangeTimer> + <AppTransportChangeTimerAddition>*N` timer expires
