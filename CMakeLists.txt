project(decklink-opencv)

cmake_minimum_required(VERSION 3.0.2 FATAL_ERROR)

set (CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -W -Wall")
set (CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")
set (CMAKE_CXX_FLAHS "${CMAKE_CXX_FLAGS} -march=native")
set (CMAKE_BUILD_TYPE Debug)

find_package (OpenCV REQUIRED)
#find_package (OpenCV 3.0 REQUIRED)

include_directories(include decklink-sdk/include)

add_executable(capture
    src/Capture.cpp
    src/Config.cpp
    decklink-sdk/src/DeckLinkAPIDispatch.cpp
    )
target_link_libraries(capture ${OpenCV_LIBS} -lm -ldl -lpthread)