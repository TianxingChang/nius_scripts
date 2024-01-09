# scripts 
根据指定json的 start & end time 进行多进程切割 opus源音频文件成若干【单通道，16k采样率】的.wav 文件并存储到processed_wav 文件夹


## ffmpeg usage: 
如果要更改ffmpeg命令， 去continue_convert.py 的 47 行（subprocess 执行的操作那里）。


## 使用 ✅
先给conversion_control.sh 执行权限 <br>
`chmod +x conversion_control.sh` <br>

之后在当前目录下运行 `nohup ./conversion_control.sh >log/split.log 2>&1 &` <br>
-> 程序将在后台运行，日志将存储与log/split.log 中 <br>
* continue_convert.py 应该在dataset 目录下，就是说要和 audio/ 在同一个目录内 
* 支持暂定process 后继续切分未完成的任务 
* 更改output folder，到continue_convert.py 的第12行


