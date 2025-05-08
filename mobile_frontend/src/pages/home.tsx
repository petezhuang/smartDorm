import { useEffect } from "react";
import "./home.css";
import TempDisplay from "./components/tempDisplay";
import Device from "./components/device";
import Sit from "./components/sit";

export default function Home() {
  useEffect(() => {
    document.title = "主页 - 我的应用";
  }, []);
  return (
    <div style={{ height: "100vh", width: "100vw" }}>
      <div
        style={{
          height: "10vh",
          backgroundColor: "#3d4785",
          display: "flex",
          alignItems: "center", // 垂直居中
          paddingLeft: "20px", // 左侧内边距
          color: "#fff", // 白色字体
          fontSize: "1.5rem", // 可根据需要调整大小
          fontWeight: "bold", // 加粗
        }}
      >
        智能宿舍管理系统
      </div>
      <div
        style={{
          display: "grid",
          gridTemplateColumns: "70vw 30vw",
          gridTemplateRows: "60vh 30vh",
          height: "90vh",
          width: "100vw",
          backgroundColor: "#dce5f4",
        }}
      >
        <div className="tempreature">
          <h2 style={{color:''}}>温度显示</h2>
          <TempDisplay />
        </div>

        <div className="device">
          <Device />
        </div>

        <div className="sit">
          <Sit />
        </div>
      </div>
    </div>
  );
}
