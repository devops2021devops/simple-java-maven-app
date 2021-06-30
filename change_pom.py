import xml.etree.ElementTree as ET
import argparse
import sys


def argparser():
    print("getting parameters from argparse")
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--artifactId', action='store', dest='artifactId',
                        required=False, help="artifactId")
    parser.add_argument('-v', '--version', action='store', dest='version',
                        required=False, help="version")
    args = parser.parse_args()
    if len(sys.argv) < 2:
        return False
    else:
        return args


def change_version_and_artifactId(filename, version, asrtifactId):
    try:
        ET.register_namespace('', "http://maven.apache.org/POM/4.0.0")
        ET.register_namespace(
            'xsi', "http://www.w3.org/2001/XMLSchema-instance")
        ET.register_namespace(
            'schemaLocation', 'http://maven.apache.org/POM/4.0.0 http://maven.apache.org/maven-v4_0_0.xsd')

        tree = ET.parse(filename)
        tree.write(filename)
        root = tree.getroot()
        artifactIdxml = root.find(
            './/{http://maven.apache.org/POM/4.0.0}artifactId')
        versionxml = root.find(
            './{http://maven.apache.org/POM/4.0.0}version')

        for elem in root.iter():
            print(elem.tag)
        oldartifactId = artifactIdxml.text
        oldversion = versionxml.text
        artifactIdxml.text = asrtifactId
        versionxml.text = version
        print("artifact id will be converted from {} to {}".format(
            oldartifactId, asrtifactId))
        print("version will be converted from {} to {}".format(oldversion, version))

        tree.write(filename)
    except Exception as e:
        print("error {}".format(e))


def check_for_version_and_arifactId():
    pass


def main():
    debug = 0
    filename = "pom.xml"
    if(debug):
        version = "2.2.2"
        artifactId = "my-app"
    else:
        args = argparser()
        version = args.version
        artifactId = args.artifactId
    change_version_and_artifactId(filename, version, artifactId)


if __name__ == '__main__':
    main()
