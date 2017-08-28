#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

class Three_door(object):
    def __init__(self):
        print '本次测试次数：'
        self.times = input()
        self.printResult(self.times)

    def doorInit(self):
        door = [0,0,0,0]
        carDoor = random.choice([0,1,2,3])
        door[carDoor] = 1
        return door

    def choose(self,door):
        chooseDoor = random.choice(door)
        return chooseDoor

    # def swicth(self,door):
    #     firstChooseDoor = random.choice(door)
    #     if firstChooseDoor:
    #         return 0
    #     else:
    #         return 1

    def printResult(self,times):
        staySuccess = 0
        switchSuccess = 0
        i = 0
        while i < times:
            door_ = self.doorInit()
            # print door_
            if self.choose(door_) == 1:
                staySuccess += 1
            else:
                if random.choice([0,1]) == 1:
                    switchSuccess += 1
            i += 1
        print '不换赢车概率：%.4f'%(float(staySuccess)/times)
        print '换门赢车概率：%.4f'%(float(switchSuccess)/times)

        # print '不换赢车概率：',round(float(staySuccess)/times,5)
        # print '换门赢车概率：',round(float(switchSuccess)/times,5)

if __name__ == "__main__":
    td = Three_door()