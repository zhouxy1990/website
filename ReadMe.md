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
           stage('run images') {
              steps {
                 sh 'docker run -p 5000:5000 -e CONNECT_DB_HOST=${host_ip} -d zhouxiangyu8786/website:${version}'
              }
           }
           stage('pull images') {
              steps {
                 sh 'docker login -u zhouxiangyu8786 -p ${dockerhub_pwd}'
                 sh 'docker push zhouxiangyu8786/website:${version}'
              }
           }
        }
     }
     ```

   - 构建触发器

     1.触发远程构建，配置身份验证令牌

     2.在`github`项目中配置`Webhooks`，实现提交后自动触发`jenkins`构建


