<http:listener-config name="HTTP_Listener_config" doc:name="HTTP Listener config" doc:id="3e5ac227-d030-4464-9b9b-13993a4dcb41" >
	<http:listener-connection host="0.0.0.0" port="8081" />
</http:listener-config>
<db:config name="Database_Config" doc:name="Database Config" doc:id="19f71360-9d83-4241-b6aa-0bad635a4ced" >
	<db:generic-connection url="jdbc:h2:tcp://localhost/~/testdb,sa" driverClassName="org.h2.Driver" />
</db:config>
<flow name="databasepocFlow" doc:id="a4cab55a-138c-4dcd-86e1-30114bdaa7f2" >
	<http:listener doc:name="Listener" doc:id="6f78fcb0-2d71-4dc6-ac0b-53e9237845b8" config-ref="HTTP_Listener_config" path="/test"/>
    <ee:transform doc:name="Transform Message" doc:id="fa970ecc-fe9d-49df-a965-604dbe5fd52e">
        <ee:message>
        </ee:message>
        <ee:variables>
            <ee:set-variable variableName="tenpo_cd" ><![CDATA[%dw 2.0
output application/java
---
payload.tenpo_cd]]></ee:set-variable>
            <ee:set-variable variableName="prd_cd" ><![CDATA[%dw 2.0
output application/java
---
payload.prd_cd]]></ee:set-variable>
            <ee:set-variable variableName="inClause" ><![CDATA[%dw 2.0
output application/java
---
(payload.prd_cd map (value, index) -> "'prd_cd" ++ (index + 1) ++ "'") joinBy ", "]]></ee:set-variable>
            <ee:set-variable variableName="inputParameters" ><![CDATA[%dw 2.0
output application/java
---
{
  tenpo_cd: payload.tenpo_cd,
  (payload.prd_cd mapObject (value, index) -> {
    ("prd_cd" ++ (index + 1)): value
  })
}]]></ee:set-variable>
        </ee:variables>
    </ee:transform>
	<db:select doc:name="Select" doc:id="a4bafc22-6a69-44d5-8ba4-3949573bcd21" config-ref="Database_Config">
		<db:sql>#["SELECT * FROM your_table WHERE tenpo_cd = :tenpo_cd AND prd_cd IN (" ++ vars.inClause ++ ")"]</db:sql>
		<db:input-parameters><![CDATA[#[vars.inputParameters]]]></db:input-parameters>
	</db:select>
	<ee:transform doc:name="Transform Message" doc:id="fa970ecc-fe9d-49df-a965-604dbe5fd52e" >
		<ee:message >
			<ee:set-payload ><![CDATA[%dw 2.0
output application/json
---
payload]]></ee:set-payload>
		</ee:message>
	</ee:transform>
</flow>
