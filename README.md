# PCDSharing


- Use two servers for server and client

- Server
* run `python server.py` and waiting.


- Client 
* For just checking TCP communication, run `python client.py`.
* If you want to test while adjusting the egree bandwidth of client machine, run `bash bandwidth.sh`.


- TODOs
* convert python socket programming into C++ socket programming
* integrate Draco and G-PCC codebase to compress point cloud (As of now, we are sending the compressed data)