'''
Inspired by: Josh Long
'''

import subprocess
import sys
import os

def run(c):
    print('running: %s' % c)
    return subprocess.check_call(c, shell=True)

if __name__ == '__main__':
    # Check for .zip argument
    assert len(sys.argv) > 1 and sys.argv[1].endswith('.zip'), 'You must specify a .zip file to open.'
    
    zip_file = os.path.abspath(sys.argv[1])
    assert os.path.exists(zip_file), 'Zip file not found.'
    
    folder_name = os.path.splitext(os.path.basename(zip_file))[0]  # Correct way to get the folder name
    try:
        run(f'unzip -a {zip_file}')  # Use f-string for better readability
    except subprocess.CalledProcessError:
        print("Non-zero exit code, but proceeding anyway...")

    # Define build files for Gradle (Groovy and Kotlin) and Maven (pom.xml)
    gradle_build_groovy = os.path.join(folder_name, 'build.gradle')
    gradle_build_kotlin = os.path.join(folder_name, 'build.gradle.kts')
    mvn_pom = os.path.join(folder_name, "pom.xml")
    
    success = False
    build_files = [gradle_build_groovy, gradle_build_kotlin, mvn_pom]

    # Check for the existence of any build file and open it in IntelliJ IDEA
    for fn in build_files:
        if os.path.exists(fn):
            run(f'idea {fn}')
            success = True
    
    # If no build file is found, raise an error
    assert success, 'Valid build file (one of: %s) not found' % ', '.join(build_files)
    print("....Done")
