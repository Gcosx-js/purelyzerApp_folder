import easygui
import sys,psutil,os,signal
from funcs import force_quit_all

def kill_all_python_processes():
    current_pid = os.getpid()  # Şu anki scriptin PID'sini al
    for proc in psutil.process_iter(attrs=["pid", "name"]):
        try:
            # Süreç ismi "python" veya "python3" olanları bul
            if "python" in proc.info["name"].lower() and proc.info["pid"] != current_pid:
                print(f"Killing Python process: {proc.info['pid']}")
                os.kill(proc.info["pid"], signal.SIGTERM)  # SIGKILL yerine SIGTERM kullanmak daha güvenlidir
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

if __name__ == '__main__':
    force_quit_all()
    if len(sys.argv) > 1:
        arg = sys.argv[1]
        easygui.msgbox(title='Purelyzer got crash!', msg=arg)
        force_quit_all()
        kill_all_python_processes()
    else:
        easygui.msgbox(title='Purelyzer got crash!', msg="An unknown error occurred.")
        force_quit_all()
        kill_all_python_processes()