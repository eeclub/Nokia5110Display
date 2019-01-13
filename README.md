# Nokia5110Display

Nokia5110Display 可以将 Nokia5110 屏幕变成一个电脑的一个附加显示屏，可以通过 `nokia5110_player.py` 播放视频

### 食用方法

Nokia5110Display 使用了 [PCD8544](https://github.com/carlosefr/pcd8544) 驱动 Nokia5110 显示屏, 需要按照如下方式连接 Nokia5110 到 Arduino

Display Pin       | Arduino Pin
------------------|------------
Pin 1             | +3.3V Pin
Pin 2 (SCLK)      | Digital Pin 3
Pin 3 (SDIN/MOSI) | Digital Pin 4
Pin 4 (D/C)       | Digital Pin 5
Pin 5 (SCE)       | Digital Pin 7
Pin 6             | Ground Pin
Pin 7             | 10uF capacitor to Ground Pin
Pin 8 (RST)       | Digital Pin 6

安装 [platformio](platformio.org) 参考 https://platformio.org/platformio-ide 上传 Arduino 程序

运行播放脚本
```bash
pip install -r requirements.txt
python nokia5110_player.py -t video -p {串口地址} -f {视频文件}
# enjoy 🌈
```
