## Description:
_As an iOS device I want to be able to register apps on the Head Unit wirelessly using Bluetooth and to change transports seamlessly._




## .ini file change ## [to remove]
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
