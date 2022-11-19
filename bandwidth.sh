#/bin/bash
PORT=8000

for i in {10..300..5}
do 
    for j in {1..100..1}
    do
        sudo tc qdisc add dev eno1 root tbf rate $i"mbit" burst 16kbit latency 50ms
        python3 client.py --port=$PORT --bw=$i
        PORT=$(($PORT+1))
        echo "CURRENT PORT: "$PORT
        sudo tc qdisc del dev eno1 root 
    done
done

