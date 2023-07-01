<set-variable variableName="inputArray" value="#[payload.aaa]" doc:name="Set Variable"/>
<db:select doc:name="Select" config-ref="Database_Config">
    <db:sql>
        <![CDATA[
        SELECT * FROM products WHERE column IN (
            <foreach collection="#[vars.inputArray]" separator="," >?</foreach>
        )
        ]]>
    </db:sql>
    <db:input-parameters>
        <db:foreach config-ref="Database_Config" collection="#[vars.inputArray]">
            <db:input-parameter value="#[payload]" />
        </db:foreach>
    </db:input-parameters>
</db:select>
