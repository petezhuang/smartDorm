const axios = require('axios');

// 要发送的测试数据
const testData = {
  key: 'value',
  message: 'Hello from test.js!'
};

// 发送 POST 请求
axios.post('https://www.u2601175.nyat.app:15108/api/test', testData)
  .then(response => {
    console.log('Response status:', response.status);
    console.log('Response data:', response.data);
  })
  .catch(error => {
    console.error('Error occurred:', error);
  });
