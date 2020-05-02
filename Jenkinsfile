pipeline {
   agent any
   stages {
      stage('pull code') {
         steps {
            git 'https://github.com/zhouxy1990/website'
         }
      }
      stage('buid images') {
         steps {
            sh 'docker build -t zhouxiangyu8786/website:${version} .'
         }
      }
      stage('run images') {
         steps {
            sh 'docker run -p 5000:5000 -e CONNECT_DB_HOST=192.168.33.10 -d zhouxiangyu8786/website:${version}'
         }
      }
      stage('pull images') {
         steps {
            sh 'docker login -u zhouxiangyu8786 -p zhou12369874'
            sh 'docker push zhouxiangyu8786/website:${version}'
         }
      }
   }
}