<ee:transform doc:name="Transform Message" >
    <ee:message>
        <ee:set-payload><![CDATA[%dw 2.0
            output application/java
            ---
            {
                'tenpo_cd': payload.tenpo_cd,
                'prd_cd': payload.prd_cd splitBy ',' map (product_code) -> '\'' ++ product_code ++ '\'' joinBy ','
            }]]></ee:set-payload>
    </ee:message>
</ee:transform>

<db:select doc:name="Select" doc:id="8d88c75a-3062-4b33-bc6a-43f800aa0cb3" config-ref="Database_Config">
    <db:sql>
        <![CDATA[
            SELECT * FROM products WHERE tenpo_cd = :tenpo_cd AND product_code IN (:prd_cd)
        ]]>
    </db:sql>
    <db:input-parameters>
        #[payload]
    </db:input-parameters>
</db:select>
