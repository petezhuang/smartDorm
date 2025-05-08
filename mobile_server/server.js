// server.js
const express = require('express');
const cors = require('cors');
const app = express();
const port = 3000;

// 允许所有跨域请求
app.use(cors());
app.use(express.json());

var deviceStatus = {//设备状态
  lamp: "off",
  fan: "off"
};

app.get('/api/data', (req, res) => {
  res.json({
    time: [
        '2025-05-08 20:00:03',
        '2025-05-08 20:01:03',
        '2025-05-08 20:02:03',
        '2025-05-08 20:03:03',
        '2025-05-08 20:04:03',
    ],
    values: [
        '22', 
        '25', 
        '24', 
        '23', 
        '22',
    ]
  });
});



app.get('/api/sit',(req,res)=>{
  res.json({
    last_sit_time:"75min"
  })
})

app.get('/api/device', (req, res) => {
  res.json(deviceStatus);
});

// POST 接口：更新设备状态（前端传 { lamp: 'on' } 或 { fan: 'off' }）
app.post('/api/device', (req, res) => {
  const updates = req.body;

  // 验证并更新状态
  if ('lamp' in updates) {
    if (updates.lamp === 'on' || updates.lamp === 'off') {
      deviceStatus.lamp = updates.lamp;
    }
  }

  if ('fan' in updates) {
    if (updates.fan === 'on' || updates.fan === 'off' || 'auto') {
      deviceStatus.fan = updates.fan;
    }
  }

  res.json({
    message: '设备状态已更新',
    status: deviceStatus
  });
});


// 启动服务器
app.listen(port, () => {
  console.log(`🚀 服务器运行在 http://localhost:${port}`);
});
