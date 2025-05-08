import { useState,useEffect } from "react";
import axios from "axios";
import { message } from "antd";

export default function Sit() {
    const [sitTime,setSitTime] = useState('')
    
  useEffect(() => {
    axios
      .get("http://localhost:3000/api/sit")
      .then((res) => {
        console.log(res, "久坐");
        setSitTime(res.data.last_sit_time)
      })
      .catch(() => {
        message.error("获取久坐状态失败");
      });
  }, []);
  return (
    <div
        style={{
            display: 'flex',
            flexDirection: 'column',/* 垂直排列灯和风扇 */
            justifyContent: 'center', /* 垂直居中 */
            alignItems: 'center',
        }}
    >
      <h2>上一次久坐至今{sitTime}</h2>
      <h4 style={{ color: 'red', visibility: parseInt(sitTime) > 45 ? 'visible' : 'hidden' }}>
      请站起来活动一下！
    </h4>
    </div>
  );
}
