mvn process-classes -nsu -Dmaven.test.skip=true
<plugins>
    <plugin>
        <groupId>org.apache.maven.plugins</groupId>
        <artifactId>maven-compiler-plugin</artifactId>
        <version>3.8.1</version>
        <configuration>
            <skip>true</skip>
        </configuration>
    </plugin>
</plugins>
