import platform
import subprocess
import sys

def install_whl(whl_file):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", whl_file])
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Failed to install {whl_file}: {e}")

# Load the correct extension depending on the operating system
if platform.system() == 'Linux':
    install_whl("path/to/resize_event_linux.whl")
    from ResizeEvent import resize_event
elif platform.system() == 'Darwin':
    install_whl("path/to/resize_event_macos.whl")
    from ResizeEvent import resize_event
elif platform.system() == 'Windows':
    install_whl("path/to/resize_event_windows.whl")
    from ResizeEvent import resize_event
else:
    raise RuntimeError(f"Unsupported OS: {platform.system()}")