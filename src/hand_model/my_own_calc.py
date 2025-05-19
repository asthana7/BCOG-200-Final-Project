from src.hand_model import app
import threading
import time

i_i_distance = 0
r_distance = 0
l_distance = 0


def distance(dx, dy):
    return (dx**2 + dy**2) ** 0.5

def update_loop():
    global i_i_distance, r_distance, l_distance
    while app.is_running:
        coords = app.latest_coords
        if coords['Left'] and coords['Right']:
            left_thumb, left_index = coords['Left']
            right_thumb, right_index = coords['Right']

            i_i_dx = left_index[0] - right_index[0]
            i_i_dy = left_index[1] - right_index[1]
            i_i_distance = distance(i_i_dx, i_i_dy)
            #print(f"Distance between index fingers: {i_i_distance}")

            r_dx = right_index[0] - right_thumb[0]
            r_dy = right_index[1] - right_index[1]
            r_distance = distance(r_dx, r_dy)
            #print(f'Distance between RIGHT index and thumb: {r_distance}')

            l_dx = left_index[0] - left_thumb[0]
            l_dy = left_index[1] - left_thumb[1]
            l_distance = distance(l_dx, l_dy)
            #print(f"Distance between LEFT thumb and index: {l_distance}")
        time.sleep(0.1)

def start_tracking():
    print("Calling app.main()")
    threading.Thread(target = app.main, daemon = True).start()
    threading.Thread(target = update_loop, daemon = True).start()
    print("Threading started, location: my_own_calc")

def ii_distance():
    return i_i_distance

def rdistance():
    return r_distance

def ldistance():
    return l_distance

def hands_detected():
    #returns True if hands are currently tracked
    return app.latest_coords['Left'] is not None or app.latest_coords['Right'] is not None