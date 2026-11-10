import os
import time 
import numpy as np 

WIDTH, HEIGHT = 80, 40
R_BULGE = 5.0
ARMS = 2.0
PITCH = 0.5 
OMEGA = 0.5 # Shpejtesia e rrotullimit 

# Karakteret e perdorura nga me e zbehta te me e ndjeshmja 
DENSITY_CHARS = " .:-=+*#%@"

def render_frame(t):
    screen = [[" " for _ in range(WIDTH)] for _ in range(HEIGHT)]

    #Qendra e ekranit
    cx, cy = WIDTH / 2, HEIGHT / 2

    for y in range(HEIGHT):
        for x in range(WIDTH):
            #Perkthen kordinatat ne hapesire polare relative me qendren
            dx = (x - cx) * 0.5 #Korrigjim i aspektit te karaktereve ne terminal
            dy = (y - cy) * 1.0

            r = np.sqrt(dx * dx + dy * dy)
            th = np.arctan2(dy, dx)

            if r > 35: #Jashte rrezes se galaktikes
                continue

            #Llogaritja e kraheve te spirales dhe pluhurit
            #Krahet spirale bazohen te logaritmi i rrexes
            spiral = th - PITCH * np.log(r + 1e-3) + OMEGA * t

            #Intensiteti i drites per qendren
            bulge = 2.5 * np.exp(-(r * r) / (R_BULGE * R_BULGE))

            #Intensiteti i kraheve
            arm_intensity = (np.cos(ARMS * spiral) + 1.0) / 2.0
            # Zbehja e drites sa me larg qendres
            brightness = (bulge + arm_intensity * (10.0 / (r + 2.0))) * 1.2

            #Zgjedhja e karakterit ASCII bazuar te dendesia
            char_idx = int(brightness * (len(DENSITY_CHARS) - 1))
            char_idx = max(0, min(char_idx, len(DENSITY_CHARS) - 1))

            if char_idx > 0:
                #Perdorim karaktere special ose ASCII standart
                screen[y][x] = DENSITY_CHARS[char_idx]

    # Për ta vizualizuar në terminal, bashkojmë rreshtat.
    output = "\n".join("".join(row) for row in screen)
    return output

def main():
    t = 0.0
    #Pastro ekranin dhe fshij kursin nese deshiron 
    print("\033[2J", end="")

    try:
        while True:
            #Kthen kursin ne fillim te ekranit per animacion te lemuar 
            print("\033[H", end="")
            print(f"galaxy.py • 2026\narms {ARMS} • tilt 0.0°")
            print("-" * WIDTH)
            print(render_frame(t))

            t += 0.1
            time.sleep(0.03) 
    except KeyboardInterrupt:
        print("\nU ndalua nga perdoruesi.")


if __name__ == "__main__":
    main()        
