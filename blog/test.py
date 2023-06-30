<ee:transform doc:name="Prepare SQL Query" doc:id="d3b81e0a-75ad-4f66-8ef6-9885773d2e1b">
    <ee:message>
        <ee:set-payload>
            #[%
                "SELECT * FROM products WHERE tenpo_cd = '" ++ payload.tenpo_cd ++ "' AND product_code IN (" ++ (payload.prd_cd map "'" ++ $ ++ "'" joinBy ',') ++ ")"
            %]
        </ee:set-payload>
    </ee:message>
</ee:transform>
<db:select doc:name="Select" doc:id="8d88c75a-3062-4b33-bc6a-43f800aa0cb3" config-ref="Database_Config">
    <db:sql>
        #[payload]
    </db:sql>
</db:select>
