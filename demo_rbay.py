import time
import datetime
import dateutil
import sys

from dateutil import parser

print("vroom vroom RBay Express")

#Import libraries
#Connect to database
#Sync tables

def getWeather():
    
    #weatherCheck = wuCheckCity("Kennedy_International", "NY")  
    #Call to weather underground for New York, NY - Kennedy (JFK), occurs for all locations in a list
    print ("Get Weather: New York, NY - Kennedy (JFK)")
    #weatherCheck = wuCheckCity("La_Guardia", "NY")                                 #New York, NY - La Guardia (LGA)
    print ("Get Weather: New York, NY - La Guardia (LGA)")
    #weatherCheck = wuCheckCity("Newark_International", "NJ")                       #Newark, NJ (EWR)
    print ("Get Weather: Newark, NJ (EWR)")

    #timestamp the init file
    with open('init.txt', 'r') as file:
        data = file.readlines()
    print (data)
    current_time = datetime.datetime.now()
    new_line = 'weather,' + str(current_time) + '\n'
    data[2] = new_line #weather is on the 3rd line of init.txt
    print (data)
    with open('init.txt', 'w') as file:
        file.writelines( data )
    
    #timestamp the log file
    with open('server_log.txt', 'a') as file:
        file.write(str(current_time) + ' weather done' + '\n')
        

def getNymex(file_tick):
    nymex_future = 'nymex_future' + str(file_tick) + '.csv'
    #downloadFTP('ftp://ftp.cmegroup.com/pub/settle/nymex_future.csv', nymex_future)

    #loop through rows of downloaded csv file to scrape data to database
    print ("Data Scraped Successfully: Nymex")

#timestamp the init file
    with open('init.txt', 'r') as file:
        data = file.readlines()
    print (data)
    current_time = datetime.datetime.now()
    new_line = 'nymex,' + str(current_time) + '\n'
    data[0] = new_line #nymex is on the 1st line of init.txt
    print (data)
    with open('init.txt', 'w') as file:
        file.writelines( data )

#timestamp the log file
    with open('server_log.txt', 'a') as file:
        file.write(str(current_time) + ' nymex done' + '\n')

def getEIA(file_tick):
    wngsr = 'wngsr' + str(file_tick) + '.csv'
    #downloadHTTP('http://ir.eia.gov/ngs/wngsr.csv', wngsr)

    #harvest data from specific rows of the file
    print ("Data Scraped Successfully: EIA")


#timestamp the init file
    with open('init.txt', 'r') as file:
        data = file.readlines()
    print (data)
    current_time = datetime.datetime.now()
    new_line = 'eia,' + str(current_time) + '\n'
    data[1] = new_line #eia is on the 2nd line of init.txt
    print (data)
    with open('init.txt', 'w') as file:
        file.writelines( data )

#timestamp the log file
    with open('server_log.txt', 'a') as file:
        file.write(str(current_time) + ' eia done' + '\n')
    
    

def initrbayexpress(nymex_val, eia_val):
    n_val = nymex_val
    e_val = eia_val
    init_time = datetime.datetime.now()
    last_time_f = open('init.txt', 'r')
    #NYMEX
    last_nymex = last_time_f.readline()
    #'nymex,2018-02-27 08:32:26.135111\n'
    nymex_time_ps = last_nymex.split(",")[1]
    #'2018-02-27 08:32:26.135111\n'
    nymex_time_s = nymex_time_ps.splitlines()
    #'2018-02-27 08:32:26.135111'
    nymex_time = parser.parse(nymex_time_s[0])
    time_diff = init_time - nymex_time
    print(str(time_diff) + ' nymex time diff')
    #now checking to see if difference is greater than 1 day
    #if time_diff.days >= 1:#MODIFIED TICK HERE
    if time_diff.seconds >= 2.5:
        #date/time based name of locally saved file
        date_tick_pre = str(init_time)
        date_tick = ''.join( c for c in date_tick_pre if  c not in '- :.' )
        #
        print ("fetching nymex")
        #timestamp the log file
        with open('server_log.txt', 'a') as file:
            file.write(str(init_time) + ' nymex fetch' + '\n')
        #run process
        getNymex(date_tick)
        n_val += 1
    #EIA
    init_time_2 = datetime.datetime.now()
    last_eia = last_time_f.readline()
    eia_ps = last_eia.split(",")[1]
    eia_s = eia_ps.splitlines()
    eia_time = parser.parse(eia_s[0])
    time_diff_2 = init_time_2 - eia_time
    print(str(time_diff_2) + ' eia time diff')
    #1 week
    #if time_diff_2.days >= 7:#MODIFIED TICK HERE
    if time_diff_2.seconds >= 5:
        #date/time based name of locally saved file
        date_tick_pre = str(init_time_2)
        date_tick = ''.join( c for c in date_tick_pre if  c not in '- :.' )
        #
        print ("fetching eia")
        #timestamp the log file
        with open('server_log.txt', 'a') as file:
            file.write(str(init_time_2) + ' eia fetch' + '\n')
        #run process
        getEIA(date_tick)
        e_val += 1
    #WEATHER
    init_time_3 = datetime.datetime.now()
    last_weather = last_time_f.readline()
    weather_ps = last_weather.split(",")[1]
    weather_s = weather_ps.splitlines()
    weather_time = parser.parse(weather_s[0])
    time_diff_3 = init_time_3 - weather_time
    print(str(time_diff_3) + ' weather time diff')
    #1 hour
    weather_hours = time_diff_3.seconds//3600 #no remainder
    #if weather_hours >= 2:#MODIFIED TICK HERE
    if time_diff_3.seconds >= 1:
        ##date/time based name of locally saved file (if ever required)
        #date_tick_pre = str(init_time_3)
        #date_tick = ''.join( c for c in date_tick_pre if  c not in '- :.' )
        ##
        print ("fetching weather")
        #timestamp the log file
        with open('server_log.txt', 'a') as file:
            file.write(str(init_time_3) + ' weather fetch' + '\n')
        #run process
        getWeather()

    return(n_val,e_val)



###########################################################################################################
############                                                                                   ############
############ MAIN                                                                           v  ############
############                                                                                   ############
###########################################################################################################
vroom_time = datetime.datetime.now()
with open('server_log.txt', 'a') as file: #change w to a and append?
        file.write(str(vroom_time) + ' server initialized' + '\n')

ticks = (0,0)
demo_tick_count = 0
demo_tick_stop = 44
#if greater, stop demo

starttime=time.time()
while True:
    print ("tick")
    nymex_tick = ticks[0]
    eia_tick = ticks[1]
    ticks = initrbayexpress(nymex_tick, eia_tick) #pass in n_val and e_val for writing ticks to log file?
    #time.sleep(600) #checks every 10 minutes #MODIFIED TICK HERE
    if demo_tick_count > demo_tick_stop:
        print ("simulated abrubt shutdown")
        sys.exit(0)

    demo_tick_count += 1
    time.sleep(0.25) #checks every quarter second for demo
    


print("main init")

###########################################################################################################
############                                                                                   ############
############ MAIN                                                                           ^  ############
############                                                                                   ############
###########################################################################################################
