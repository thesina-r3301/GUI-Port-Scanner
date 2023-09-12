import tkinter as tk
import socket

class PortScanner:
    def __init__(self, master):
        self.master = master
        master.title("Port Scanner")

        self.target_label = tk.Label(master, text="Enter target IP or URL:")
        self.target_label.grid(row=0, column=0, sticky="W")

        self.target_entry = tk.Entry(master)
        self.target_entry.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        self.ports_label = tk.Label(master, text="Enter ports range (ex: 1-100):")
        self.ports_label.grid(row=2, column=0, sticky="W")

        self.ports_entry = tk.Entry(master)
        self.ports_entry.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

        self.scan_button = tk.Button(master, text="Scan", command=self.scan_ports)
        self.scan_button.grid(row=4, column=0, pady=10)

        self.output_text = tk.Text(master, height=10, width=50)
        self.output_text.grid(row=5, column=0, padx=10, pady=10, columnspan=2)

    def scan_ports(self):
        # Get target and ports range from input fields
        target = self.target_entry.get()
        ports_range = self.ports_entry.get()

        # Check if input fields are not empty
        if target == '' or ports_range == '':
            self.output_text.insert(tk.END, "Please enter a target and a ports range.")
            return

        # Parse the ports range
        ports = ports_range.split("-")
        if len(ports) != 2:
            self.output_text.insert(tk.END, "Invalid ports range. Please enter a valid range (ex: 1-100).")
            return

        start_port = int(ports[0])
        end_port = int(ports[1])

        # Clear output text
        self.output_text.delete("1.0", tk.END)

        # Scan ports
        for port in range(start_port, end_port+1):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            result = s.connect_ex((target, port))
            if result == 0:
                self.output_text.insert(tk.END, f"Port {port} is open.\n")
            s.close()

# Create GUI window
root = tk.Tk()
app = PortScanner(root)

root.mainloop()