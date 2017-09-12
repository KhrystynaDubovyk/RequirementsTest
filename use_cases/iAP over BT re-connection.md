## Use Case 1: iAP over BT re-connection

**Main Flow:**

_Pre-conditions:_  
a. Application is registered with SDL  
b. Application is running on iOS device connected over Bluetooth [Device is consented and application <app_1> from this device is registered in SDL]  

_Steps:_  
1. User connects the same device connects over USB

_Expected:_  
2. SDL receives signal about USB connection of the same device [SDL receives `<UUID>` of the connected device]  
3. SDL receives signal about transport switch of the same device  
4. SDL starts <AppTransportChangeTimer> + <AppTransportChangeTimerAddition>*N reconnection timer

**_Note:_** N is the number of applications that need to be re-registered

_Exception 1:_ 

**Alternative flow 1:**
