properties(pipelineTriggers([pollSCM('* * * * *')]))
node {
    stage("one") {
        git branch: 'master', url: 'https://github.com/imanuelg-GitHub/MySoftware.git'
    }
}