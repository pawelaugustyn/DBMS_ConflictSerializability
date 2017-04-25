from Schedule import Schedule

if __name__=="__main__":
    schedules = [
        "w1x w2x w3x r4x w1x",
        "r1x w2x r2y w2y",
        "r2x r2y w1x w2y",
        "r2x r2y w1x w2y r2y",
        "r2x r2y w1y w1x w2y w1y",
        "r1x r2z r1z r3y r3y w1x w3y r2y w2x w2y",
        "r1x r2x w1x w2x",
        "r1x r2y w3x r2x r1y",
        "r1x w2x w1x r3x"
    ]

    for i in range(0, len(schedules)):
        schedule = Schedule(schedules[i])
        print("S{}:".format(str(i+1)), schedule.get_printable_schedule())
        if schedule.is_conflict_serializable():
            print("\tConflict serializable")
        else:
            print("\tNot conflict serializable")
        print("")