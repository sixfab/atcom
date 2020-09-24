#!/usr/bin/env bash

sudo bash ecm_watch.sh |& sudo tee -a ./logs/$(date "+%Y_%m_%d_%H:%M:%S").log
