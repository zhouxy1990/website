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
      stage('save images') {
         steps {
            sh 'docker save zhouxiangyu8786/website:${version} -o website:${version}.tar'
         }
      }
      stage('test images') {
         steps {
         sh 'ansible-playbook /etc/ansible/playbooks/build_test.yaml -e "project_path=/var/lib/jenkins/workspace/website_build_pepiline_test/website:${version}.tar image_name=website:${version} host_ip=${host_ip}" '
         }
      }
   }
}