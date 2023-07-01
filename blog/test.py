<set-variable variableName="inputArray" value="#[payload.aaa]" doc:name="Set Variable"/>
<set-variable variableName="placeholders" value="#[vars.inputArray collect ('?' as String)]" doc:name="Set Placeholders"/>
<db:select doc:name="Select" config-ref="Database_Config">
    <db:sql>
        <![CDATA[
        SELECT * FROM products WHERE column IN (#[vars.placeholders joinBy ','])
        ]]>
    </db:sql>
    <db:input-parameters>
        <db:input-parameter key="inputArray" value="#[vars.inputArray]" />
    </db:input-parameters>
</db:select>
