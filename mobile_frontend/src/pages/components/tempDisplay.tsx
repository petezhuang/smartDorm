import { useState, useEffect } from "react";
import axios from "axios";
import { Line } from "@ant-design/charts";
import { Button } from "antd";

export default function TempDisplay() {
  const [data, setData] = useState([]);

  useEffect(() => {
    axios.get("http://localhost:8848/api/data")
      .then(response => {
        const raw = response.data;
        const formatted = raw.time.map((t, i) => ({
          时间: t,
          温度: Number(raw.values[i])
        }));
        setData(formatted);
      })
      .catch(error => {
        console.error("请求失败:", error);
      });
  }, []);
  console.log(data)
  const config = {
    data,
    title: {
      visible: true,
      text: "温度展示",
    },
    xField: "时间",
    yField: "温度",
    // interactions: [
    //   {
    //     type: 'slider',
    //     cfg: {
    //       start: 0.1,
    //       end: 0.2,
    //     },
    //   },
    // ],
  };

  return (
    <>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
        <p style={{ fontSize: '1.5em', fontWeight: 'bold', margin: '0.83em 0', color: '' }}>温度显示</p>
        <Button style={{ margin: '0.83em 0' }}
        onClick={()=>{
          axios.get("http://localhost:8848/api/data")
            .then(response => {
              const raw = response.data;
              const formatted = raw.time.map((t, i) => ({
                时间: t,
                温度: Number(raw.values[i])
              }));
              setData(formatted);
            })
            .catch(error => {
              console.error("请求失败:", error);
            });
        }}
        >
          获取最新温度
        </Button>
      </div>
      <Line {...config} />
    </>


  )
}
