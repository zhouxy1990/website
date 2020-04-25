pipeline {
   agent any
   environment {
       MYTOOL_VERSION = '1.0.4'
   }
   stages {
      stage('pull code') {
         steps {
            git 'https://github.com/zhouxy1990/website'
         }
      }
      stage('buid project') {
         steps {
            sh 'docker build -t zhouxiangyu8786/website:$MYTOOL_VERSION .'
         }
      }
      stage('run project') {
         steps {
            sh 'docker run -p 5000:5000 -e CONNECT_DB_HOST=192.168.33.10 -d zhouxiangyu8786/website:$MYTOOL_VERSION'
      }
   }
   }
}