<ee:set-variable variableName="inClause"><![CDATA[%dw 2.0
output application/java
---
payload map ((item) -> "'" ++ (if (item is :number) "'" ++ item as String ++ "'" else item) ++ "'") reduce ((item, accumulator) -> accumulator ++ ", " ++ item)]]></ee:set-variable>
