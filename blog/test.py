            </ee:message>
            <ee:variables >
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
(payload.prd_cd map ":prd_cd$$") joinBy ", "]]></ee:set-variable>
                <ee:set-variable variableName="inputParameters" ><![CDATA[%dw 2.0
output application/java
---
{
  tenpo_cd: payload.tenpo_cd,
  (payload.prd_cd mapObject (value, key) -> {
    ("prd_cd$$" ++ (key as String)): value
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
</mule>
