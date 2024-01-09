# scripts segmentation + conversion
## 脚本任务 🤖
根据指定json的 start & end time 进行多进程切割 opus源音频文件操作，将这些文件转成若干【单通道，16k采样率】的.wav 文件并存储到processed_wav 文件夹


## 更改ffmpeg : 🛠️
如果要更改ffmpeg命令， 去continue_convert.py 的 47 行（subprocess 执行的操作那里）。


## 使用 ✅
先给conversion_control.sh 执行权限 <br>
`chmod +x conversion_control.sh` <br>

之后在当前目录下运行 `nohup ./conversion_control.sh >log/split.log 2>&1 &` <br>
-> 程序将在后台运行，日志将存储于`log/split.log` 中 <br>
* `continue_convert.py` 应该在 `dataset` 目录下，就是说要和 `audio` 在同一个目录内 
* 支持暂定process 后继续切分未完成的任务 
* 如果要更改output folder，到`continue_convert.py` 的第12行


