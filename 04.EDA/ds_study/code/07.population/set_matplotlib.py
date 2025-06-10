
import platform
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

path = "c:/Windows/Fonts/malgun.ttf" # 폰트 경로

if platform.system() == "Windows":
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
    print("Korean font set to Windows default.")
elif platform.system() == "Darwin":
    rc('font', family='Arial Unicode MS')
    print("Korean font set to Mac default.")
else:
    print("Unknown platform. Korean font may not be set correctly.")

plt.rcParams["axes.unicode_minus"] = False
