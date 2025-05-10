# smartDorm
移动开发作业    
## 文件结构  
Mobile为树莓派所运行的代码  
mobile_frontend为前端代码  
    前端采取的框架为react + vite，运行在nodejs上，ui框架为antd。  
mobile_server为系统服务器代码  
    服务器采用nodejs，框架为express  
extra文件夹存放了树莓派内网穿透的相关配置
## 使用  
1.在对应的文件夹下运行终端，`pnpm install` 下载依赖  
2.在server路径下运行指令`noode server.js`  
3.frontend路径下运行指令`pnpm run dev`
