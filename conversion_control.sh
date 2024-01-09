# Calling continue_convert.py in 20 processes in order to split audios
# 这个脚本用来控制convert.py, num_process 对应的是 json 文件的个数

num_process=20

process_json() {
    local json_id=$1
    exec -a "Splitting json_$json_id" python continue_convert.py "$json_id"
}

# Launch processes in parallel
for ((json_id=1; json_id<=$num_process; json_id++)); do
    process_json "$json_id" &
done
