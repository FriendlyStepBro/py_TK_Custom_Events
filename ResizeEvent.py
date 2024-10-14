import platform
import sys

# Load the correct extension depending on the operating system
if platform.system() == 'Linux':
    from .linux import resize_event
elif platform.system() == 'Darwin':
    from .macos import resize_event
elif platform.system() == 'Windows':
    from .windows import resize_event
else:
    raise RuntimeError(f"Unsupported OS: {platform.system()}")