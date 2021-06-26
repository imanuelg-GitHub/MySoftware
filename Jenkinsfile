properties([parameters([string(defaultValue: 'Imanuel', name: 'NAME')]), pipelineTriggers([pollSCM('* * * * *')])])
node {
    stage("one") {
        git branch: 'main', url: 'https://github.com/imanuelg-GitHub/MySoftware.git'
        bat "more Imanuel.txt"
    }
}