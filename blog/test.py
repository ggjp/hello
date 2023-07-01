<mule xmlns:ee="http://www.mulesoft.org/schema/mule/ee/core" xmlns:http="http://www.mulesoft.org/schema/mule/http"
    xmlns:db="http://www.mulesoft.org/schema/mule/db" xmlns="http://www.mulesoft.org/schema/mule/core"
    xmlns:doc="http://www.mulesoft.org/schema/mule/documentation"
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xsi:schemaLocation="http://www.mulesoft.org/schema/mule/core http://www.mulesoft.org/schema/mule/core/current/mule.xsd
        http://www.mulesoft.org/schema/mule/http http://www.mulesoft.org/schema/mule/http/current/mule-http.xsd
        http://www.mulesoft.org/schema/mule/db http://www.mulesoft.org/schema/mule/db/current/mule-db.xsd">

    <flow name="exampleFlow">
        <http:listener doc:name="Listener" config-ref="HTTP_Listener_config" path="/example" />
        <ee:transform doc:name="Transform Payload">
            <ee:message>
                <ee:set-payload><![CDATA[%dw 2.0
output application/java
---
{
  "tenpo_cd": payload.tenpo_cd,
  "prd_cd": payload.prd_cd
}]]></ee:set-payload>
            </ee:message>
        </ee:transform>
        <set-variable variableName="placeholders" value="#[payload.prd_cd joinBy ',']" doc:name="Set Placeholders"/>
        <db:select doc:name="Select" config-ref="Database_Config">
            <db:sql><![CDATA[
                SELECT * FROM products WHERE tenpo_cd = :tenpo_cd AND product_code IN (:#[vars.placeholders])
            ]]></db:sql>
            <db:input-parameters>
                <db:input-parameter key="tenpo_cd" value="#[payload.tenpo_cd]" />
            </db:input-parameters>
        </db:select>
    </flow>

</mule>
