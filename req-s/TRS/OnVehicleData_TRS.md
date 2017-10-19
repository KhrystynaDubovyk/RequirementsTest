## Functional Requirements

1. 
In case SDL received valid OnVehicleData notification from HMI

and this notification is allowed by Policies

SDL must:

- store OnVehicleData notification internally
- transfer this notification to all registered mobile applications successfully subscribed on waypoints-related data

_Note:_ In case of receiving new OnVehicleData notification from HMI, SDL must rewrite previously saved notification and transfer new notification to all subscribed applications.

2. 
In case SDL received valid OnVehicleData notification from HMI

and this notification is NOT allowed by Policies

SDL must:

- log corresponding error internally
- ignore this notification and not transfer it to subscribed mobile applications

## Non-Functional Requirements

a. "OnVehicleData" notification must be added to "Notifications" in PolicyTable:

```json
"Notifications": {
          "rpcs": {
"OnWayPointChange": {
              "hmi_levels": [
                "BACKGROUND",
                "FULL",
                "LIMITED"
              ],
            }
      }
}
```

## Diagram

OnVehicleData

![OnVehicleData](https://github.com/smartdevicelink/sdl_requirements/blob/OnWayPointChange/detailed_docs/accessories/OnVehicleData.png)



