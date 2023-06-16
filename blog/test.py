<http:listener config-ref="HTTP_Listener_config" path="/yourApiPath" allowedMethods="POST" doc:name="HTTP Listener" />
<set-variable variableName="tenpo_cd" value="#[payload.tenpo_cd]" doc:name="Set Variable (tenpo_cd)" />
<set-variable variableName="prd_cds" value="#[payload.prd_cds]" doc:name="Set Variable (prd_cds)" />
<ee:transform doc:name="Prepare Query" >
    <ee:message >
        <ee:set-payload ><![CDATA[%dw 2.0
            output application/java
            ---
            "SELECT * FROM tableName WHERE tenpo_cd = '" ++ vars.tenpo_cd ++ "' AND prd_cd IN (" ++ vars.prd_cds joinBy "," ++ ")" ]]>
        </ee:set-payload>
    </ee:message>
</ee:transform>

<db:select doc:name="Run Query" config-ref="Database_Config">
    <db:sql>#[payload]</db:sql>
</db:select>
