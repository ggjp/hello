<mule xmlns:ee="http://www.mulesoft.org/schema/mule/ee/core" xmlns:http="http://www.mulesoft.org/schema/mule/http"
      xmlns:db="http://www.mulesoft.org/schema/mule/db" xmlns="http://www.mulesoft.org/schema/mule/core"
      xmlns:doc="http://www.mulesoft.org/schema/mule/documentation" 
      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
      xsi:schemaLocation="http://www.mulesoft.org/schema/mule/core http://www.mulesoft.org/schema/mule/core/current/mule.xsd
      http://www.mulesoft.org/schema/mule/http http://www.mulesoft.org/schema/mule/http/current/mule-http.xsd
      http://www.mulesoft.org/schema/mule/db http://www.mulesoft.org/schema/mule/db/current/mule-db.xsd">

    <flow name="exampleFlow">
        <http:listener doc:name="Listener" config-ref="HTTP_Listener_config" path="/example"/>
        <set-variable variableName="inputArray" value="#[payload.aaa]" doc:name="Set Variable"/>
        <db:select doc:name="Select" config-ref="Database_Config">
            <db:sql>
                <![CDATA[
                SELECT * FROM products WHERE column IN (
                    <foreach collection="#[vars.inputArray]" separator="," >?</foreach>
                )
                ]]>
            </db:sql>
            <db:input-parameters>
                <db:foreach config-ref="Database_Config" collection="#[vars.inputArray]">
                    <db:dynamic-input-parameter>
                        <ee:expression><![CDATA[#[payload]]]></ee:expression>
                    </db:dynamic-input-parameter>
                </db:foreach>
            </db:input-parameters>
        </db:select>
    </flow>

</mule>
