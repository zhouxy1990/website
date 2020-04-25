该项目主要通过`jenkins`+`github`+`docker`+`ansible`实现CI/CD简单流程，一个简单的DEMO

1. 在`jenkins`中配置源码管理和构建触发器、构建步骤

   - 构建步骤:

     ```shell
     #shell脚本
     #版本号已写死，在实际中可用脚本生成新的版本
     #运行Dockefile,build镜像
     docker build -t zhouxiangyu8786/website:1.0.2 .
     #将镜像推送至dockerhub镜像仓库
     docker login -u zhouxiangyu8786  -p xxx
     docker push zhouxiangyu8786/website:1.0.2
     ```

   - 构建触发器

     1.触发远程构建，配置身份验证令牌

     2.在`github`项目中配置`Webhooks`，实现提交后自动触发`jenkins`构建

2. 添加部署和交付脚本

   - 在构建步骤中添加脚本

     ```shell
     #从dockerhub下拉取镜像
     ansible WEB -m shell -a "docker pull zhouxiangyu8786/website:1.0.2"
     #生成容器
     ansible WEB -m shell -a "docker run -p 5000:5000 -d zhouxiangyu8786/website:1.0.2"
     ```

     

