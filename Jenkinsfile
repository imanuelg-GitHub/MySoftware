properties([parameters([string(defaultValue: 'Imanuel', name: 'NAME')]), pipelineTriggers([pollSCM('* * * * *')])])
node {
    stage("one") {
        git branch: 'master', url: 'https://github.com/imanuelg-GitHub/MySoftware.git'
        bat "more Imanuel.txt"
    }
}