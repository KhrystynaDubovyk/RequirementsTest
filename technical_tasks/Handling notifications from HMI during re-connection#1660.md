## Description:

_Responses to any requests made by the app just prior to the transport switch would be discarded by SDL Core. If the user triggers any interaction to the app, such interactions will be buffered by SDL Core till the app reconnects (within reconnection timeout period) at which point the requests will be sent to the app or till the expiry of the reconnection timer after which the requests will be discarded. HMI can use the UpdateDeviceList request from SDL core to display any message to the user informing about the transport switch._

1. In case iAP session was closed due to transport type change
SDL must:
keep all applications registered for reconnecting device
during "AppTransportChangeTimer" + "AppTransportChangeTimerAddition"*N reconnection timer

2. In case due to transport change SDL started "AppTransportChangeTimer" + "AppTransportChangeTimerAddition"*N reconnection timer
and
HMI sends any notifications and requests to "appID" that needs to be reconnected
SDL must:
store all the notifications and requests from HMI internally
transfer all notifications and requests from HMI right after the "appID" will be reconnected

3. In case due to transport change SDL started "AppTransportChangeTimer" + "AppTransportChangeTimerAddition"*N reconnection timer
and
HMI sends any responses to "appID" on requests that were sent before reconnection
SDL must:
discard all responses to such "appID" from HMI

## Related Diagrams:

![iap transport change reconnection](https://user-images.githubusercontent.com/23719788/28126084-2df0e89a-6731-11e7-8cb7-4f653b1eeb1e.png)

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
