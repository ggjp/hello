
<flow name="database-query-flow">
    <set-variable variableName="tenpo_cd" value="#[attributes.queryParams.tenpo_cd]" doc:name="Set Variable" />
    <set-variable variableName="prd_cds" value="#[attributes.queryParams.prd_cds]" doc:name="Set Variable" />
    <db:select doc:name="Run Query" config-ref="Database_Config">
        <db:sql>SELECT * FROM tableName WHERE storeColumn = :tenpo_cd AND productColumn IN (:prd_cds)</db:sql>
        <db:input-parameters>#[{ 'tenpo_cd' : vars.tenpo_cd, 'prd_cds' : vars.prd_cds }]</db:input-parameters>
    </db:select>
</flow>
