from colorama import init, Fore, Style, Back
from colorama import init as colorama_init
import threading, datetime, time, os
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System 
from sty import fg, bg, ef, rs
from datetime import datetime
from os import get_terminal_size as _terminal_size

lock = threading.Lock()

red = Fore.RED + Style.BRIGHT
green = Fore.GREEN + Style.BRIGHT
blue = Fore.BLUE + Style.BRIGHT
cyan = Fore.CYAN + Style.BRIGHT
magenta = Fore.MAGENTA + Style.BRIGHT
yellow = Fore.YELLOW + Style.BRIGHT 
white = Fore.WHITE + Style.BRIGHT
pink = Fore.LIGHTMAGENTA_EX + Style.BRIGHT
reset = Style.RESET_ALL

class Center:

    """
    2 functions:
        XCenter()                  |             center the given text in X cords
        YCenter()                  |             center the given text in Y cords
        Center()                   |             center the given text in X and Y cords
        GroupAlign()               |             align the given text in a group
        TextAlign()                |             align the given text per lines
    NOTE: the functions of the class can be broken if the text argument has colors in it
    """

    center = 'CENTER'
    left = 'LEFT'
    right = 'RIGHT'

    def XCenter(text: str, spaces: int = None, icon: str = " "):
        if spaces is None:
            spaces = Center._xspaces(text=text)
        return "\n".join((icon * spaces) + text for text in text.splitlines())

    def YCenter(text: str, spaces: int = None, icon: str = "\n"):
        if spaces is None:
            spaces = Center._yspaces(text=text)

        return icon * spaces + "\n".join(text.splitlines())

    def Center(text: str, xspaces: int = None, yspaces: int = None, xicon: str = " ", yicon: str = "\n") -> str:
        if xspaces is None:
            xspaces = Center._xspaces(text=text)

        if yspaces is None:
            yspaces = Center._yspaces(text=text)

        text = yicon * yspaces + "\n".join(text.splitlines())
        return "\n".join((xicon * xspaces) + text for text in text.splitlines())

    def GroupAlign(text: str, align: str = center):
        align = align.upper()
        if align == Center.center:
            return Center.XCenter(text)
        elif align == Center.left:
            return text
        elif align == Center.right:
            length = _terminal_size().columns
            maxLineSize = max(len(line) for line in text.splitlines())
            return '\n'.join((' ' * (length - maxLineSize)) + line for line in text.splitlines())
        else:
            raise Center.BadAlignment()
    
    def TextAlign(text: str, align: str = center):
        align = align.upper()
        mlen = max(len(i) for i in text.splitlines())
        if align == Center.center:

            return "\n".join((' ' * int(mlen/2 - len(lin)/2)) + lin for lin in text.splitlines())
        elif align == Center.left:
            return text
        elif align == Center.right:
            ntext = '\n'.join(' ' * (mlen - len(lin)) + lin for lin in text.splitlines())
            return ntext
        else:
            raise Center.BadAlignment()



class Logger:

    checked, claimed, proxyError = 0, 0, 0

    def systemSize(x, y):
        System.Size(x, y)

    def Print_Logo():
        Write.Print("""
        ██╗   ██╗ █████╗ ███╗   ██╗██╗████████╗██╗   ██╗    ██╗   ██╗██████╗ ██╗     
        ██║   ██║██╔══██╗████╗  ██║██║╚══██╔══╝╚██╗ ██╔╝    ██║   ██║██╔══██╗██║     
        ██║   ██║███████║██╔██╗ ██║██║   ██║    ╚████╔╝     ██║   ██║██████╔╝██║     
        ╚██╗ ██╔╝██╔══██║██║╚██╗██║██║   ██║     ╚██╔╝      ██║   ██║██╔══██╗██║     
         ╚████╔╝ ██║  ██║██║ ╚████║██║   ██║      ██║       ╚██████╔╝██║  ██║███████╗
          ╚═══╝  ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝   ╚═╝      ╚═╝        ╚═════╝ ╚═╝  ╚═╝╚══════╝    
        """, Colors.rainbow, interval=0)

        Write.Print("""
        ███████╗██████╗  █████╗ ███╗   ███╗███╗   ███╗███████╗██████╗ 
        ██╔════╝██╔══██╗██╔══██╗████╗ ████║████╗ ████║██╔════╝██╔══██╗
        ███████╗██████╔╝███████║██╔████╔██║██╔████╔██║█████╗  ██████╔╝
        ╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝  ██╔══██╗
        ███████║██║     ██║  ██║██║ ╚═╝ ██║██║ ╚═╝ ██║███████╗██║  ██║
        ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝
        """, Colors.rainbow, interval=0)
        print("")
        Write.Print("                            dqwrwq ", Colors.purple_to_blue, interval=0)
        print("")
        Write.Print("                                version: 1.0.0", Colors.purple_to_blue, interval=0)
        print("")
        print("")
        print("")
        print("")

    def Print(text):
        lock = threading.Lock()
        lock.acquire()
        print(text)
        lock.release()

    def Debug(text):
        lock = threading.Lock()
        lock.acquire()
        print(f'[{Fore.MAGENTA}/{Fore.WHITE}] {text}')
        lock.release()

    def Warning(text):
        lock = threading.Lock()
        lock.acquire()
        print(f'[{Fore.YELLOW}!{Fore.WHITE}] {text}')
        lock.release()

    def Success(text):
        lock = threading.Lock()
        lock.acquire()
        print(f'[{Fore.GREEN}${Fore.WHITE}] {text}')
        lock.release()
    
    def Error(text):
        lock = threading.Lock()
        lock.acquire()
        print(f'[{Fore.RED}-{Fore.WHITE}] {text}')
        lock.release()
    
    def Question(text):
        lock = threading.Lock()
        lock.acquire()
        print(f'[{Fore.BLUE}?{Fore.WHITE}] {text}')
        lock.release()