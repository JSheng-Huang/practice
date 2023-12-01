#!/bin/bash
#
#
#
# Refer to:
#   #1. https://welson327.gitbooks.io/code_notes/content/Linux/shell-script.html
#   #2. https://tw.gitbook.net/shell/case-esac-statement.html
#   #3. https://stackoverflow.com/questions/49657982/multiple-variables-in-a-case-statement-bash
# Created by Jason5_Huang <Jason5_Huang@asus.com>
#
main() {
    while [ $# -gt 0 ]; do
        case "$1" in
        --param1=*)
            echo "param1 = ${1#*=}"
            ;;
        --param2=*)
            echo "param2 = ${1#*=}"
            ;;
        *) ;;
        esac
        shift
    done

    option="${1}"
    case ${option} in
    -f)
        FILE="${2}"
        echo "File name is $FILE"
        ;;
    -d)
        DIR="${2}"
        echo "Dir name is $DIR"
        ;;
    *)
        echo "$(basename ${0}):usage: [-f file] | [-d directory]"
        exit 1 # Command to come out of the program with status 1
        ;;
    esac

}
