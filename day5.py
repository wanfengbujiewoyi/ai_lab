scores={2.5,3.0,1.5,2.0,2.5,3.5,1.0}
total=0
for a in scores:
    total+=a
average=total/len(scores)
print("训练总时长为：",total,)
print(f"平均训练时长为：{average:.1f}")
for day,score in enumerate(scores,start=1):
    print(f"the{day}day:{score}hours")