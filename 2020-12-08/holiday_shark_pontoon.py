def shark(pontoon_distance, shark_distance, you_speed, shark_speed, dolphin):
    if dolphin == True:
        if pontoon_distance / you_speed <= 2 * shark_distance / shark_speed:
            return "Alive!"
        else:
            return "Shark Bait!"
    elif pontoon_distance / you_speed <= shark_distance / shark_speed:
        return "Alive!"
    else:
        return "Shark Bait!"


#This way from ramkicoder, I think is the python way, congratz
#def shark(pontoonDistance, sharkDistance, youSpeed, sharkSpeed, dolphin):
    # Using the boolean to be used as 1 or 0 when multiplying
#    return "Alive!" if (pontoonDistance / youSpeed) < sharkDistance / (sharkSpeed - (sharkSpeed * 0.5 * dolphin)) else "Shark Bait!"