该项目主要通过`jenkins`+`github`+`docker`+`ansible`实现CI/CD简单流程，一个简单的DEMO

1. 在`jenkins`中配置源码管理和构建触发器、构建步骤

   - 构建步骤:

     构建流水线

     ```
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
     ```

   - 构建触发器

     1.触发远程构建，配置身份验证令牌

     2.在`github`项目中配置`Webhooks`，实现提交后自动触发`jenkins`构建


