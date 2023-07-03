<ee:transform doc:name="Generate dynamic in-clause and inputParameters" doc:id="8f6a02fd-4bdf-40e8-8c90-c23d39510944">
    <ee:message />
    <ee:variables >
        <ee:set-variable variableName="tenpo_cd" ><![CDATA[%dw 2.0
output application/java
---
payload.tenpo_cd]]></ee:set-variable>
        <ee:set-variable variableName="inClause" ><![CDATA[%dw 2.0
output application/java
---
(payload.prd_cd map (val, index) -> ":arg" ++ (index as String)) joinBy ", "]]></ee:set-variable>
        <ee:set-variable variableName="inputParameters" ><![CDATA[%dw 2.0
output application/java
---
(payload.prd_cd map (val, index) -> {("arg" ++ (index as String)) : val})
    ++ {"tenpo_cd": vars.tenpo_cd}]]></ee:set-variable>
    </ee:variables>
</ee:transform>
