import { useState,useEffect } from "react";
import axios from "axios";
import { message } from "antd";

export default function Sit() {
    const [sitTime,setSitTime] = useState('')
    
    const fetchSitTime = () => {
      axios
        .get("http://localhost:8848/api/sit")
        .then((res) => {
          console.log(res, "久坐");
          setSitTime(res.data.last_sit_time)
        })
        .catch(() => {
          message.error("获取久坐状态失败");
        });
    };
    
    useEffect(() => {
      // 首次加载时获取数据
      fetchSitTime();
      
      // 设置定时器，每隔一段时间（如3秒）获取一次数据
      const timer = setInterval(() => {
        fetchSitTime();
      }, 3000); // 3秒更新一次
      
      // 组件卸载时清除定时器
      return () => clearInterval(timer);
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
      <h4 style={{ 
        color: 'red', 
        visibility: sitTime.includes('分') && parseInt(sitTime) > 45 ? 'visible' : 'hidden' 
      }}>
      请站起来活动一下！
    </h4>
    </div>
  );
}
