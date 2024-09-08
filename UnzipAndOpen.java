/*
 * Inspired by: Josh Long
 * 
*/

import java.io.File;
import java.util.Set;

public class UnzipAndOpen {
    public static void main(String[] args) throws Exception {
        // Ensure an argument is passed
        if (args.length == 0) {
            System.out.println("You must specify a zip file to open.");
            return;
        }

        var zipFile = new File(args[0]);

        // Check if the file exists and is a .zip file
        if (!zipFile.exists() || !zipFile.getName().endsWith(".zip")) {
            System.out.println("Zip file not found or invalid file type.");
            return;
        }

        var zipFileAbsolutePath = zipFile.getAbsolutePath();
        var folder = new File(zipFileAbsolutePath.substring(0, zipFileAbsolutePath.lastIndexOf(".")));

        try {
            // Unzipping the file
            new ProcessBuilder().command("unzip", "-a", zipFileAbsolutePath).inheritIO().start().waitFor();
        } catch (Exception e) {
            System.out.println("Error during unzip process: " + e.getMessage());
        }

        // Check for build files (Gradle Groovy, Kotlin, or Maven POM)
        for (var k : Set.of("build.gradle", "build.gradle.kts", "pom.xml")) {
            var buildFile = new File(folder, k);
            if (buildFile.exists()) {
                try {
                    // Open in IntelliJ IDEA
                    new ProcessBuilder().command("idea", buildFile.getAbsolutePath()).inheritIO().start().waitFor();
                } catch (Exception e) {
                    System.out.println("Error opening file in IDEA: " + e.getMessage());
                }
            }
        }
    }
}
