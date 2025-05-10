import { message, Select } from "antd";
import "./device.css";
import { useEffect, useState } from "react";
import axios from "axios";

export default function Device() {
  const [lampVal, setLampVal] = useState("");
  const [fanVal, setFanVal] = useState("");
  const [lampIntsVal, setLampIntsVal] = useState("");
  useEffect(() => {
    axios
      .get("http://localhost:8848/api/device")
      .then((res) => {
        console.log(res, "res---");
        setLampVal(res.data.lamp);
        setFanVal(res.data.fan);
        setLampIntsVal(res.data.led_intensity);
      })
      .catch(() => {
        message.error("获取设备状态失败");
      });
  }, []);

  const handleLampChange = (val:string) => {
    setLampVal(val); // ✅ 更新状态
    axios
      .post("http://localhost:8848/api/device", {
        lamp: val,
      })
      .then((res) => {
        console.log(res);
        if(res.status===200){
            message.success("设置成功！");
        }
        
      });
  };


  const handleLampIntsChange = (val:string) => {
    setLampIntsVal(val);
    axios
      .post("http://localhost:8848/api/device", { led_intensity: val })
      .then((res) => {
        if(res.status===200){ 
            message.success("设置成功！");
        }
      })
      .catch(() => message.error("亮度设置失败"));
  };
  

  const handleFanChange = (val) => {
    setFanVal(val);
    axios
      .post("http://localhost:8848/api/device", { fan: val })
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
      <div className="lamp">
        <span style={{ marginRight: 10 }}>灯光控制：</span>
        <Select
          value={lampVal}
          style={{ width: 120 }}
          options={[
            { value: "OFF", label: "关闭" },
            {value:"AUTO",label:"自动"},
            { value: "ON", label: "打开" },
          ]}
          onChange={handleLampChange}
        />
      </div>

      <div className="lamp_intensity">
        <span style={{ marginRight: 10 }}>亮度控制：</span>
        <Select
          value={lampIntsVal}
          style={{ width: 120 }}
          disabled={lampVal === "OFF"} 
          options={[
            { value: "0", label: "0" },
            { value: "1", label: "1" },
            { value: "2", label: "2" },
            { value: "3", label: "3" },
            { value: "4", label: "4" },
            { value: "5", label: "5" },
            { value: "6", label: "6" },
            { value: "7", label: "7" },
            { value: "8", label: "8" },
            { value: "9", label: "9" },
            { value: "10", label: "10" },
          ]}
          onChange={handleLampIntsChange}
        />
      </div>

      <div className="fan">
        <span style={{ marginRight: 10 }}>风扇控制：</span>
        <Select
          value={fanVal}
          style={{ width: 120 }}
          options={[
            { value: "OFF", label: "关闭" },
            { value: "ON", label: "打开" },
            { value: "AUTO", label: "自动" },
          ]}
          onChange={handleFanChange}
        />
      </div>
    </div>
  );
}
