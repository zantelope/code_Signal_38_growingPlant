def growingPlant(upSpeed, downSpeed, desiredHeight):

    ## variables for height and total days
    height = 0
    days = 0
    
    ### while loop that ends when plant is above certain height
    while height < desiredHeight:
    
        ### increase days and height gaines during the day
        days += 1
        height += upSpeed
        
        ### break loop if day growth pushes plant to or past desired height
        if height >= desiredHeight:
            break
            
        ### otherwise, subtract night loss
        else:
            height -= downSpeed
        print(height, days)
   
    return days
