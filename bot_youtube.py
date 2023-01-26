# load libraries
import random
import time

# load selenium (a suite of tools for automating web browsers)
from selenium import webdriver # pip install selenium
from selenium.webdriver.common.by import By


# define constants
PATH_DRIVER = './chromedriver_linux64/' # path for the driver
DEFAULT_LINK = r'https://www.youtube.com/watch?v=XlGLf7cWOJA' # link for the video
DEFAULT_TIME = 56*60 # video duration time in seconds
DEFAULT_N = 2 # number of times to see the video
DEFAULT_N_DRIVERS = 3 # number of windows tha will be open for watching the video


# download chrome driver for the correspondent chrome and s.o. (e.g., 100.0.4896.20 for linux):
# https://chromedriver.storage.googleapis.com/index.html


# input link video
url = input(f'\n1. Input here your desired YouTube link ...\n[ Sugestion: >>> {DEFAULT_LINK}, Cornelius Lanczos interview ]:\n\n>>> ')
# note: the Lanczos video has 55:51 min = ~(56 x 60)s = ~3600 s

# check input
if not url:
    url = DEFAULT_LINK
print(f'>>> Url choosed: {url}')

# input time of video
duration = input(f'\n\n2. Input here the duration tme of the video in seconds ...\n[ E.g.: >>> {DEFAULT_TIME}, for the Lanczos video because it has approximately 1h 3600 s ]:\n\n>>> ')

# check input
if not duration:
    duration = DEFAULT_TIME
else:
    duration = int(duration)
print(f'>>> Duration time choosed: {duration}')

# define the number of times that the bot will open for watching the video
n = input(f'\n\n3. Input here a integer N correspondent to the number of times that the bot will open for watching the video ...\n[ Sugestion: >>> {DEFAULT_N}]:\n\n>>> ')

# check input
if not n:
    n = DEFAULT_N
else:
    n = int(n)
print(f'>>> N choosed: {n}')

# define the number of drivers = number of windows that will be considered
n_drivers = input(f'\n\n4. Input here a integer M correspondent to the number of windows that the bot will open for watching the video ...\n[ Sugestion: >>> {DEFAULT_N_DRIVERS}]:\n\n>>> ')

# check input
if not n_drivers:
    n_drivers = DEFAULT_N_DRIVERS
else:
    n_drivers = int(n_drivers)
print(f'>>> M choosed: {n_drivers}')


# watching the video n times in m windows open
for k in range(n):    
    print(f'\n\n----- {k+1} of {n} times -----')
    
    time_to_refresh = int(duration+2*n_drivers)
    
    drivers = []
    print(f'Opening {n_drivers} web drivers . . .')
    
    for i in range(n_drivers):
        drivers.append(webdriver.Chrome(executable_path=PATH_DRIVER+'chromedriver'))
        drivers[i].get(url)

        time.sleep(random.randint(1, 3))
        
        video = drivers[i].find_element(By.ID, 'movie_player')
        
        video.send_keys('k') # hits k        
        
        time.sleep(random.randint(1, 3))
        
        #drivers[i].minimize_window()
        print(f'  > Opened driver[{i}]')
    
    print(f'  > Watching the videos [{time_to_refresh} seconds] . . .')
    time.sleep(time_to_refresh)

    print('')
    print(f'Closing {n_drivers} web drivers . . .')
    for i in range(n_drivers):
        drivers[i].close()
        print(f'  > Finished browser[{i}]')


# references
# https://stackoverflow.com/questions/67456411/youtube-automation-with-python-and-selenium
# https://www.selenium.dev/
