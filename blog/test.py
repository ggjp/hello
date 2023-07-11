<?xml version="1.0" encoding="UTF-8"?>
<mule xmlns:cloudhub="http://www.mulesoft.org/schema/mule/cloudhub" xmlns:ee="http://www.mulesoft.org/schema/mule/ee/core"
	xmlns:db="http://www.mulesoft.org/schema/mule/db"
	xmlns:http="http://www.mulesoft.org/schema/mule/http" xmlns="http://www.mulesoft.org/schema/mule/core" xmlns:doc="http://www.mulesoft.org/schema/mule/documentation" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.mulesoft.org/schema/mule/core http://www.mulesoft.org/schema/mule/core/current/mule.xsd
http://www.mulesoft.org/schema/mule/http http://www.mulesoft.org/schema/mule/http/current/mule-http.xsd
http://www.mulesoft.org/schema/mule/db http://www.mulesoft.org/schema/mule/db/current/mule-db.xsd
http://www.mulesoft.org/schema/mule/ee/core http://www.mulesoft.org/schema/mule/ee/core/current/mule-ee.xsd
http://www.mulesoft.org/schema/mule/cloudhub http://www.mulesoft.org/schema/mule/cloudhub/current/mule-cloudhub.xsd">
	<http:listener-config name="HTTP_Listener_config" doc:name="HTTP Listener config" doc:id="3e5ac227-d030-4464-9b9b-13993a4dcb41">
		<http:listener-connection host="0.0.0.0" port="8081" />
	</http:listener-config>
	<db:config name="Database_Config" doc:name="Database Config" doc:id="19f71360-9d83-4241-b6aa-0bad635a4ced">
		<db:generic-connection url="jdbc:h2:tcp://localhost/~/testdb,sa" driverClassName="org.h2.Driver" />
	</db:config>
	<flow name="databasepocFlow" doc:id="a4cab55a-138c-4dcd-86e1-30114bdaa7f2">
		<http:listener doc:name="Listener" doc:id="6f78fcb0-2d71-4dc6-ac0b-53e9237845b8" config-ref="HTTP_Listener_config" path="/test" />
		<set-payload value="#[['orange','banana']]" doc:name="Set Payload" doc:id="5dc8f2d2-4c26-4a88-bd18-a71e13140d7a" />
		<ee:transform doc:name="Generate dynamic in-clause" doc:id="8f6a02fd-4bdf-40e8-8c90-c23d39510944">
			<ee:message />
			<ee:variables>
				<ee:set-variable variableName="inClause"><![CDATA[%dw 2.0
output application/java
---
payload map ("'" ++ (if (typeof($) == "number") "'" ++ $ ++ "'" else $) ++ "'") reduce ((item, accumulator) -> accumulator ++ ", " ++ item)]]></ee:set-variable>
			</ee:variables>
		</ee:transform>
		<ee:transform doc:name="Generate dynamic inputParameters" doc:id="bb25debf-54a2-4a30-a670-346939c8a667">
			<ee:message />
			<ee:variables>
				<ee:set-variable variableName="inputParameters"><![CDATA[%dw 2.0
output application/java
---
payload map {"arg$$": $} reduce ((item, accumulator = {}) -> item ++ accumulator)]]></ee:set-variable>
			</ee:variables>
		</ee:transform>
		<db:select doc:name="Select" doc:id="a4bafc22-6a69-44d5-8ba4-3949573bcd21" config-ref="Database_Config">
			<db:sql>#['SELECT * FROM TEST4 WHERE NAME IN ($(vars.inClause))']</db:sql>
			<db:input-parameters><![CDATA[#[vars.inputParameters]]]></db:input-parameters>
		</db:select>
		<ee:transform doc:name="Transform Message" doc:id="fa970ecc-fe9d-49df-a965-604dbe5fd52e">
			<ee:message>
				<ee:set-payload><![CDATA[%dw 2.0
output application/json
---
payload]]></ee:set-payload>
			</ee:message>
		</ee:transform>
	</flow>
</mule>
