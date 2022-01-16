#!/bin/bash
echo "Starte Training (5 Klassen)"
./darknet detector train ycb.cfg yolov3-ycb-train.cfg darknet53.conv.74
