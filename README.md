> Python 3.6 or higher is required to run this repository, because files include f-strings, that appeared only in version 3.6.
> Tested on Ubuntu 16.04 LTS and Python 3.6.6

# Usage
   1. Firstly clone the repository to both server and client computers within one network.
   
`git clone https://github.com/yuriimchg/stream_video`

`cd stream_video`
    
    
    
The scripts of the repository can run on a single machine, in this case the second step should be omitted.

   Data type| Client | Server
   ---------|--------|---------
   _Text data_ | Send | Receive 
   _Text files_ | Send | Receive 
   _Image files_ | Send | Receive
   _Video Streaming_ | Share | Broadcast

   2. Then instead of `host = '127.0.0.1'` in the files _test_cli.py_, _send_file_cli_.py, _share_a_pic_clt.py_ and _stream_video_clt.py_ on client PC write down the IP address of server. The default host is _localhost_ and it is for the case, when one computer has both server and client roles.
   
   3. Specify the path to the file to be sent on client PC and the path, where to save the file on the server.
   
   4. Run `pip3 install numpy opencv-contrib-python` on both computers.
   
   5. Run the **server** with command `python3 [script_name]_serv.py`. On receiving the message that server is listening on port, run the **client** with command `python3 [script_name]_clt.py` 





