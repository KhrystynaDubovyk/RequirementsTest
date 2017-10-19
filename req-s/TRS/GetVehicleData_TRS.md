## Functional Requirements

1.
In case mobile application sends valid and allowed by Policies GetVehicleData_request to SDL

SDL must: 
- transfer GetVehicleData_request to HMI
- respond with `<resultCode>` received from HMI to mobile application
- provide the requested wayPoints at the same order as received from HMI to mobile application (in case of successful response)

2.
In case mobile application sends valid GetVehicleData_request to SDL

and this request is NOT allowed by Policies

SDL must:
respond "DISALLOWED, success:false" to mobile application

3. 
In case mobile application sends valid and allowed by Policies GetWayPoints_request to SDL

and Navigation interface is not available on HMI

or

 "getWayPointsEnabled": false in HMI capabilities
 
 SDL must:
 
 respond "UNSUPPORTED_RESOURCE, success:false" to mobile application and not transfer this request to HMI

## Non-Functional Requirements
Additions to mobile API, HMI_API  
Changes to enums and functions should be applied

```xml
<enum name="FuelType">
    <element name="GASOLINE" />
    <element name="DIESEL" />
    <element name="CNG">
        <description>
            For vehicles using compressed natural gas.
        </description>
    </element>
    <element name="LPG">
        <description>
            For vehicles using liquefied petroleum gas.
        </description>
    </element>
    <element name="HYDROGEN">
        <description>For FCEV (fuel cell electric vehicle).</description>
    </element>
    <element name="BATTERY">
        <description>For BEV (Battery Electric Vehicle), PHEV (Plug-in Hybrid Electric Vehicle), solar vehicles and other vehicles which run on a battery.</description>
    </element>
</enum>

<struct name="FuelRange">
    <param name="type" type="FuelType" mandatory="false"/>
    <param name="range" type="Float" minvalue="0" maxvalue="10000" mandatory="false">
        <description>
            The estimate range in KM the vehicle can travel based on fuel level and consumption.
        </description>
    </param>
</struct>

<enum name="VehicleDataType">
            :
    <element name="VEHICLEDATA_FUELRANGE" />
</enum>

<function name="SubscribeVehicleData" functionID="SubscribeVehicleDataID" messagetype="request">
            :
    <param name="fuelRange" type="Boolean" mandatory="false">
        <description>The estimate range in KM the vehicle can travel based on fuel level and consumption</description>
    </param>
</function>
<function name="SubscribeVehicleData" functionID="SubscribeVehicleDataID" messagetype="response">
            :
    <param name="fuelRange" type="VehicleDataResult" mandatory="false">
        <description>The estimate range in KM the vehicle can travel based on fuel level and consumption</description>
    </param>
</function>

<function name="UnsubscribeVehicleData" functionID="UnsubscribeVehicleDataID" messagetype="request">
            :
    <param name="fuelRange" type="Boolean" mandatory="false">
        <description>The estimate range in KM the vehicle can travel based on fuel level and consumption</description>
    </param>
</function>
<function name="UnsubscribeVehicleData" functionID="UnsubscribeVehicleDataID" messagetype="response">
            :
    <param name="fuelRange" type="VehicleDataResult" mandatory="false">
        <description>The estimate range in KM the vehicle can travel based on fuel level and consumption</description>
    </param>
</function>
<param name="fuelRange" type="FuelRange" minsize="0" maxsize="100" array="true" mandatory="false">
<function name="GetVehicleData" functionID="GetVehicleDataID" messagetype="request">
            :
    <param name="fuelRange" type="Boolean" mandatory="false">
        <description>The estimate range in KM the vehicle can travel based on fuel level and consumption</description>
    </param>
</function>
<function name="GetVehicleData" functionID="GetVehicleDataID" messagetype="response">
            :
    <param name="fuelRange" type="FuelRange" minsize="0" maxsize="100" array="true" mandatory="false">
        <description>The estimate range in KM the vehicle can travel based on fuel level and consumption</description>
    </param>
</function>

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

<function name="SubscribeVehicleData" functionID="SubscribeVehicleDataID" messagetype="request">
            :
    <param name="engineOilLife" type="Boolean" mandatory="false">
        <description>The estimated percentage of remaining oil life of the engine.</description>
    </param>
</function>
<function name="SubscribeVehicleData" functionID="SubscribeVehicleDataID" messagetype="response">
            :
    <param name="engineOilLife" type="VehicleDataResult" mandatory="false">
        <description>The estimated percentage of remaining oil life of the engine.</description>
    </param>
</function>

<function name="UnsubscribeVehicleData" functionID="UnsubscribeVehicleDataID" messagetype="request">
            :
    <param name="engineOilLife" type="Boolean" mandatory="false">
        <description>The estimated percentage of remaining oil life of the engine.</description>
    </param>
</function>
<function name="UnsubscribeVehicleData" functionID="UnsubscribeVehicleDataID" messagetype="response">
            :
    <param name="engineOilLife" type="VehicleDataResult" mandatory="false">
        <description>The estimated percentage of remaining oil life of the engine.</description>
    </param>
</function>

<function name="GetVehicleData" functionID="GetVehicleDataID" messagetype="request">
            :
	<param name="engineOilLife" type="Boolean" mandatory="false">
        <description>The estimated percentage of remaining oil life of the engine.</description>
    </param>
</function>
<function name="GetVehicleData" functionID="GetVehicleDataID" messagetype="response">
            :
    <param name="engineOilLife" type="Float" minvalue="0" maxvalue="100" mandatory="false">
        <description>The estimated percentage of remaining oil life of the engine.</description>
    </param>
</function>

<function name="OnVehicleData" functionID="OnVehicleDataID" messagetype="notification">
            :
    <param name="engineOilLife" type="Float" minvalue="0" maxvalue="100" mandatory="false">
        <description>The estimated percentage of remaining oil life of the engine.</description>
    </param>
</function>
```


## Diagram

GetVehicleData

![GetVehicleData](https://github.com/smartdevicelink/sdl_requirements/blob/GetVehicleData/detailed_docs/accessories/GetVehicleData.png)
