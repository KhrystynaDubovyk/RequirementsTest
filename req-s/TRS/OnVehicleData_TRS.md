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
1.
```
<function name="OnVehicleData" functionID="OnVehicleDataID" messagetype="notification">
            :
    <param name="fuelRange" type="FuelRange" minsize="0" maxsize="100" array="true" mandatory="false">
        <description>The estimate range in KM the vehicle can travel based on fuel level and consumption</description>
    </param>
</function>
```
```xml
<enum name="VehicleDataType">
            :
    <element name="VEHICLEDATA_ENGINEOILLIFE" />
</enum>
```
2.
```
<function name="OnVehicleData" functionID="OnVehicleDataID" messagetype="notification">
            :
    <param name="engineOilLife" type="Float" minvalue="0" maxvalue="100" mandatory="false">
        <description>The estimated percentage of remaining oil life of the engine.</description>
    </param>
</function>
```


## Diagram

OnVehicleData

![](.png)



