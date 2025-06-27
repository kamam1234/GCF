# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 14:31:21 2022

@author: ANKUR (AMD Ryzen)
"""

dict_exam={"Exam":"AISSCE", "Year":2023}
dict_result={"Total":500, "Pass_Marks":165} 
dict_exam.update(dict_result)
print(dict_exam)