<set-variable variableName="prd_cd" value="#[payload.prd_cd joinBy "','"]" doc:name="Variable" />

<db:select doc:name="Select" doc:id="8d88c75a-3062-4b33-bc6a-43f800aa0cb3" config-ref="Database_Config">
    <db:sql>
        <![CDATA[
        SELECT * FROM products WHERE tenpo_cd = :tenpo_cd AND product_code IN (#[vars.prd_cd])
        ]]>
    </db:sql>
    <db:input-parameters>
        <db:input-parameter key="tenpo_cd" value="#[payload.tenpo_cd]" />
        <db:input-parameter key="prd_cd" value="#[vars.prd_cd]" />
    </db:input-parameters>
</db:select>
