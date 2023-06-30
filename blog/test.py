<!-- set-variable を使用する場合 -->
<ee:transform doc:name="Prepare SQL Parameters">
    <ee:message>
        <ee:set-payload>
            <![CDATA[%dw 2.0
            output application/java
            ---
            {
                'tenpo_cd': payload.tenpo_cd,
                'prd_cd': payload.prd_cd splitBy ',' map ((item) -> "'" ++ item ++ "'") joinBy ','
            }]]>
        </ee:set-payload>
    </ee:message>
</ee:transform>

<set-variable variableName="tenpo_cd" value="#[payload.tenpo_cd]" doc:name="Variable" />
<set-variable variableName="prd_cd" value="#[payload.prd_cd splitBy ',' map ((item) -> "'" ++ item ++ "'") joinBy ',']" doc:name="Variable" />

<db:select doc:name="Select" doc:id="8d88c75a-3062-4b33-bc6a-43f800aa0cb3" config-ref="Database_Config">
    <db:sql>
        SELECT * FROM products WHERE tenpo_cd = :tenpo_cd AND product_code IN (:prd_cd)
    </db:sql>
    <db:input-parameters>
        <db:input-parameter key="tenpo_cd" value="#[vars.tenpo_cd]" />
        <db:input-parameter key="prd_cd" value="#[vars.prd_cd]" />
    </db:input-parameters>
</db:select>
