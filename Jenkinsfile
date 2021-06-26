properties(pipelineTriggers([pollSCM('* * * * *')]))
node {
    stage("one") {
        git branch: 'main', url: 'https://github.com/imanuelg-GitHub/MySoftware.git'
    }
}