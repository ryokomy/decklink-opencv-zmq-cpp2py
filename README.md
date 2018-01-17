# decklink-opencv-zmq-cpp2py

this is a repository to use decklink(blackmagic) video with python  

structure is like the following  
```
captured frame (decklink): c++  
-> convert to opencv format: c++  
-> send data using zmq: cpp2py  
-> opencv format: python  
```

## tested environment
- Ubuntu 16.04
- python 2.7
- DeckLink SDK 10.9.5

## requirement
- opencv (both c++ & python)
- zmq (cppzmq & pyzmq)

## how to use

### build
```
./build.sh
```

### run c++ publisher
```
cpp/build/publisher
```

### run python subscriber
```
python py/subscriber.py
```
