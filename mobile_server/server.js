// server.js
const express = require('express');
const cors = require('cors');
const app = express();
const port = 8848;
const fs = require('fs');
const path = require('path');


// 允许所有跨域请求
app.use(cors());
app.use(express.json());

var deviceStatus = {//设备状态
  lamp: "AUTO",
  fan: "AUTO",
  led_intensity: '5',
  sitTime: '0',
  pending: false
};


function handleTempData(data) {
  // 读取温度数据文件
  const dataFilePath = path.join(__dirname, 'temp_data.json');
  let tempData = [];

  try {
    if (fs.existsSync(dataFilePath)) {
      const fileContent = fs.readFileSync(dataFilePath, 'utf8');
      tempData = JSON.parse(fileContent);
    }
  } catch (error) {
    console.error('读取温度数据文件时出错:', error);
    return { time: [], values: [] };
  }

  // 如果没有数据，返回空数组
  if (tempData.length === 0) {
    return { time: [], values: [] };
  }

  // 将数据整理成需要的格式
  const result = {
    time: [],
    values: []
  };

  // 提取最近的5条数据（如果不足5条则全部提取）
  const recentData = tempData.slice(-30);

  // 遍历数据并整理
  recentData.forEach(item => {
    result.time.push(item.time);
    result.values.push(item.value.toString());
  });

  return result;
}

app.get('/api/data', (req, res) => {
  console.log(req.body)
  // res.json({
  //   time: [
  //       '2025-05-08 20:00:03',
  //       '2025-05-08 20:01:03',
  //       '2025-05-08 20:02:03',
  //       '2025-05-08 20:03:03',
  //       '2025-05-08 20:04:03',
  //   ],
  //   values: [
  //       '22', 
  //       '25', 
  //       '24', 
  //       '23', 
  //       '22',
  //   ]
  // });
  res.json(handleTempData())
});



app.get('/api/sit', (req, res) => {
  console.log(req.body)

  console.log(deviceStatus.sitTime)
  // 获取久坐时间(秒)
  const sit_Time = deviceStatus.sitTime;

  // 将字符串转为整数
  const seconds = parseInt(sit_Time);

  let formattedTime;
  if (seconds < 60) {
    // 如果不到一分钟，以秒为单位显示
    formattedTime = `${seconds}秒`;
  } else {
    // 一分钟及以上，以分钟为单位显示并四舍五入
    const minutes = Math.round(seconds / 60);
    formattedTime = `${minutes}分钟`;
  }

  res.json({
    last_sit_time: formattedTime
  });
})

app.get('/api/device', (req, res) => {
  console.log(req.body)
  res.json(deviceStatus);
});

// POST 接口：更新设备状态（前端传 { lamp: 'on' } 或 { fan: 'off' }）
app.post('/api/device', (req, res) => {
  console.log(req.body)
  const updates = req.body;

  // 验证并更新状态
  if ('lamp' in updates) {
    if (updates.lamp === 'ON' || updates.lamp === 'OFF' || updates.lamp === 'AUTO') {
      deviceStatus.lamp = updates.lamp;
      deviceStatus.pending = true;
    }
  }

  if ('fan' in updates) {
    if (updates.fan === 'ON' || updates.fan === 'OFF' || 'AUTO') {
      deviceStatus.fan = updates.fan;
      deviceStatus.pending = true;
    }
  }

  if ('led_intensity' in updates) {
    if (updates.led_intensity === '0' || updates.led_intensity === '1' || updates.led_intensity === '2'
      || updates.led_intensity === '3' || updates.led_intensity === '4' || updates.led_intensity === '5'
      || updates.led_intensity === '6' || updates.led_intensity === '7' || updates.led_intensity === '8'
      || updates.led_intensity === '9' || updates.led_intensity === '10'
    ) {
      deviceStatus.led_intensity = updates.led_intensity;
      deviceStatus.pending = true;
    }
  }

  res.json({
    message: '设备状态已更新',
    status: deviceStatus
  });
});

// 测试接口：接收 POST 请求并返回接收到的数据
app.post('/api/test', (req, res) => {
  // 输出请求体内容
  console.log('Received data:', req.body);

  // 返回接收到的数据作为响应
  res.json({
    message: '数据已接收',
    receivedData: req.body
  });
});


app.post('/api/get_data_from_raspi', (req, res) => {
  console.log(req.body)

  let data = req.body

  // 提取温度和时间戳
  const tempData = {
    value: data.temperature,
    time: data.timestamp
  };

  // 读取现有数据（如果存在）
  const dataFilePath = path.join(__dirname, 'temp_data.json');
  let existingData = [];

  try {
    if (fs.existsSync(dataFilePath)) {
      const fileContent = fs.readFileSync(dataFilePath, 'utf8');
      existingData = JSON.parse(fileContent);
    }
  } catch (error) {
    console.error('读取温度数据文件时出错:', error);
  }
  //其他状态保存在内存
  if (deviceStatus.pending === false) {//前端不做更改时才更新数据
    try {
      deviceStatus.lamp = data.led_mode
      deviceStatus.fan = data.fan_mode
      deviceStatus.led_intensity = data.led_intensity
      deviceStatus.sitTime = data.sit_time
    } catch (error) {
      console.error('保存其他状态时出错:', error);
    }
  }else{
    try{
      deviceStatus.sitTime = data.sit_time
    }catch(error){
      console.error('保存其他状态时出错:', error);
    }
  }


  // 添加新数据
  existingData.push(tempData);

  // 保存到文件
  try {
    fs.writeFileSync(dataFilePath, JSON.stringify(existingData, null, 2), 'utf8');
    console.log('温度数据已保存到temp_data.json');
  } catch (error) {
    console.error('保存温度数据时出错:', error);
  }

  console.log('deviceStatus', deviceStatus)
  // 返回响应
  res.json({
    message: '数据已接收并记录',
  });
})

app.get('/api/echo', (req, res) => {
  console.log('树莓派请求最新状态')
  new_status = {
    lamp: deviceStatus.lamp,
    fan: deviceStatus.fan,
    led_intensity: deviceStatus.led_intensity
  }
  res.json(new_status)
  deviceStatus.pending = false;
})



// 启动服务器
app.listen(port, '0.0.0.0', () => {
  console.log(`🚀 服务器运行在 http://localhost:${port}`);
});
