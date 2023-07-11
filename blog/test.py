<ee:transform doc:name="Generate dynamic in-clause" doc:id="8f6a02fd-4bdf-40e8-8c90-c23d39510944">
    <ee:message>
    </ee:message>
    <ee:variables >
        <ee:set-variable variableName="inClause" ><![CDATA[%dw 2.0
output application/java
---
(payload map "'" ++ $ ++ "'" reduce ((item, accumulator = "") -> accumulator ++ (if (accumulator != "") ", " else "") ++ "'" ++ item ++ "'"))]]></ee:set-variable>
    </ee:variables>
</ee:transform>
<ee:transform doc:name="Generate dynamic inputParameters" doc:id="bb25debf-54a2-4a30-a670-346939c8a667">
    <ee:message />
    <ee:variables>
        <ee:set-variable variableName="inputParameters" ><![CDATA[%dw 2.0
output application/java
---
payload map {"arg$$" : "'" ++ $ ++ "'"} reduce ((item, accumulator = {}) -> item ++ accumulator)]]></ee:set-variable>
    </ee:variables>
</ee:transform>
