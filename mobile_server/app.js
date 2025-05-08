const http = require('http');

// 创建服务器
const server = http.createServer((req, res) => {
  // 设置HTTP响应的状态码和头信息
  res.writeHead(200, {
    // 设置内容类型为 HTML，并指定字符集为 UTF-8，这样中文不会乱码
    'Content-Type': 'text/html; charset=utf-8' 
  });

  // 发送响应体
  res.end('<h1>Hello, World!</h1><p>这是我的第一个 Node.js 应用。</p>');
});

// 监听端口
const PORT = 3000;
server.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});