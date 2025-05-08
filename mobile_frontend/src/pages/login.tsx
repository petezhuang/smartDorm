import { useNavigate } from "react-router-dom";
import { useState, useEffect } from "react";
import "./login.css";
import { Button, ConfigProvider, Input, Space, Form, FormProps } from "antd";

type FieldType = {
  username?: string;
  password?: string;
};

export default function Login() {
  const navigate = useNavigate();

  const handleLogin = (username,password) => {
    // 模拟登录逻辑（这里可以替换成实际的 API）
    if (username === "admin" && password === "123") {
      localStorage.setItem('isLoggedIn', 'true');
      navigate("/home"); // 登录成功跳转
    } else {
      alert("用户名或密码错误");
    }
  };

  useEffect(() => {
    document.title = "登录";
  }, []);

  const onFinish: FormProps<FieldType>["onFinish"] = (values) => {
    handleLogin(values.username,values.password)
  };

  const onFinishFailed: FormProps<FieldType>["onFinishFailed"] = (
    errorInfo
  ) => {
    console.log("Failed:", errorInfo);
  };

  return (
    <div
      style={{
        display: "grid",
        justifyContent: "center",
        alignItems: "center",
        width: "100vw",
        height: "100vh",
        backgroundColor: "#dce5f4",
        margin: 0,
        padding: 0,
      }}
    >
      <Form onFinish={onFinish} onFinishFailed={onFinishFailed}>
        <div
          style={{
            backgroundColor: "#f1f7fe",
            borderRadius: "12px",
            padding: "24px",
            width: "500px",
            margin: "0 auto", // 水平居中整个容器
            display: "flex",
            flexDirection: "column",
            alignItems: "center", // 每个子项水平居中
            gap: "16px", // 子项之间间距
          }}
        >
          <div
            style={{
              backgroundColor: "#3d4785",
              borderRadius: "8px",
              color: "#ffffff",
              width: "150px",
              display: "flex",
              justifyContent: "center",
            }}
          >
            <p>智能宿舍管理系统</p>
          </div>
          <Space
            direction="vertical"
            size="large"
            style={{
              marginTop: "40px",
            }}
          >
            <Form.Item<FieldType> name="username">
              <div className="textfield">
                用户名
                <Input placeholder="请输入用户名" />
              </div>
            </Form.Item>

            <Form.Item<FieldType> name="password">
              <div className="textfield">
                用户名
                <Input placeholder="请输入用户名" />
              </div>
            </Form.Item>
          </Space>
          <Form.Item>
            <ConfigProvider
              theme={{
                components: {
                  Button: {
                    defaultBg: "#3f4684",
                    defaultColor: "white",
                  },
                },
              }}
            >
              <Button htmlType="submit"
                style={{
                  marginTop: "40px",
                }}
              >
                登录
              </Button>
            </ConfigProvider>
          </Form.Item>
        </div>
      </Form>
    </div>
  );
}
