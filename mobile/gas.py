# ==================== 硬件配置区块 ====================
import time
import spidev
from luma.core.interface.serial import spi

# SPI配置
spi = spidev.SpiDev()
spi.open(0, 0)  # SPI通道0，设备0 (CE0)
spi.max_speed_hz = 1350000

# 硬件参数
MCP3008_VREF = 3.3
LOAD_RESISTOR = 10000
CLEAN_AIR_RESISTOR = 7600

# 校准参数
GAS_CALIBRATION = {
    'CO2': {'a': 116.602, 'b': -2.769},
    'CO': {'a': 425.865, 'b': -3.302}
}
# =====================================================

# ==================== 核心功能函数 ====================
def read_mcp3008(channel):
    """读取MCP3008 ADC值"""
    adc = spi.xfer2([1, (8 + channel) << 4, 0])
    return ((adc[1] & 3) << 8) + adc[2]

def calculate_gas(adc_value, gas_type):
    """计算气体浓度"""
    params = GAS_CALIBRATION[gas_type]
    
    voltage = adc_value * MCP3008_VREF / 1023
    if voltage < 0.01:
        return 0.0
    
    Rs = (MCP3008_VREF - voltage) * LOAD_RESISTOR / voltage
    ratio = Rs / CLEAN_AIR_RESISTOR
    ppm = params['a'] * (ratio ** params['b'])
    return max(0.0, round(ppm, 2))

def get_result():
    """获取传感器读数并返回浓度元组(CO2, CO)"""
    try:
        adc_value = read_mcp3008(0)
        co2 = calculate_gas(adc_value, 'CO2')
        co = calculate_gas(adc_value, 'CO')
        return (co2, co)
    except Exception as e:
        print(f"读取错误: {str(e)}")
        return (0.0, 0.0)
    finally:
        spi.close()  # 根据实际需求决定是否关闭SPI连接
# =====================================================