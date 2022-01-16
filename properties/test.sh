#!/bin/bash
echo "Testen des Netzwerks (5 Klassen)"
./darknet detector test ycb.cfg yolov3-ycb-test.cfg backup/yolov3-ycb-train_last.weights
