import { useState, useEffect } from "react";
import axios from "axios";
import { Line } from "@ant-design/charts";

export default function TempDisplay() {
  const [data, setData] = useState([]);

  useEffect(() => {
    axios.get("http://localhost:3000/api/data")
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
    interactions: [
      {
        type: 'slider',
        cfg: {
          start: 0.1,
          end: 0.2,
        },
      },
    ],
  };

  return <Line {...config} />;
}
