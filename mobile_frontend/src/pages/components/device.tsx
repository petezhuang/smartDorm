import { message, Select } from "antd";
import "./device.css";
import { useEffect, useState } from "react";
import axios from "axios";

export default function Device() {
  const [lampVal, setLampVal] = useState("");
  const [fanVal, setFanVal] = useState("");

  useEffect(() => {
    axios
      .get("http://localhost:3000/api/device")
      .then((res) => {
        console.log(res, "res---");
        setLampVal(res.data.lamp);
        setFanVal(res.data.fan);
      })
      .catch(() => {
        message.error("获取设备状态失败");
      });
  }, []);

  const handleLampChange = (val) => {
    setLampVal(val); // ✅ 更新状态
    axios
      .post("http://localhost:3000/api/device", {
        lamp: val,
      })
      .then((res) => {
        console.log(res);
        if(res.status===200){
            message.success("设置成功！");
        }
        
      });
  };

  const handleFanChange = (val) => {
    setFanVal(val);
    axios
      .post("http://localhost:3000/api/device", { fan: val })
      .then((res) => {
        if(res.status===200){
            message.success("设置成功！");
        }
      })
      .catch(() => message.error("风扇设置失败"));
  };
  return (
    <div className="wrapper">
        <h2>设备控制</h2>
      <div className="lamp" style={{ marginBottom: 20 }}>
        <span style={{ marginRight: 10 }}>灯：</span>
        <Select
          value={lampVal}
          style={{ width: 120 }}
          options={[
            { value: "off", label: "关闭" },
            { value: "on", label: "打开" },
          ]}
          onChange={handleLampChange}
        />
      </div>

      <div className="fan">
        <span style={{ marginRight: 10 }}>风扇：</span>
        <Select
          value={fanVal}
          style={{ width: 120 }}
          options={[
            { value: "off", label: "关闭" },
            { value: "on", label: "打开" },
            { value: "auto", label: "自动" },
          ]}
          onChange={handleFanChange}
        />
      </div>
    </div>
  );
}
