from os import system, name
from time import sleep

def clear_screen():
    # windows
    if name == 'nt':
        _ = system('cls')
    # unix based
    else :
        _ = system('clear')

class MidiMenu:
    def __init__(self, midi_in):
        clear_screen()
        self.midi_in = midi_in
        self.refresh_port_count()

    def get_device_port(self):
        return self.device_port

    def refresh_port_count(self):
        self.port_count = self.midi_in.get_port_count()

    def print_device(self, port_number):
        print(f"[{port_number}] :: {self.midi_in.get_port_name(port_number)}")

    def select_device(self):
        selected_device_str = input("\nSelect device: ")

        try:
            selected_device = int(selected_device_str)
            if selected_device >= 0 and selected_device <= self.port_count:
                self.device_port = selected_device
            else:
                clear_screen()
                print("Invalid selection.\n")
                self.show_menu()
        except ValueError as ve:
            clear_screen()
            print(f"You entered '{selected_device_str}', which is not a positive number.\n")
            self.show_menu()

    def show_menu(self):
        while(self.port_count <= 0):
            sleep(1)
            self.refresh_port_count()
        
        for i in range(self.port_count):
            self.print_device(i)
            
        self.select_device()
