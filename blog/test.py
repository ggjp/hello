<ee:set-variable variableName="inClause"><![CDATA[%dw 2.0
output application/java
---
payload map ("'" ++ $ ++ "'") reduce ((item, accumulator) -> accumulator ++ ", " ++ item)]]></ee:set-variable>
