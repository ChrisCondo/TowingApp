import tkinter as tk

def main():
    # Color scheme - modern and appealing
    COLORS = {
        'primary': '#2563eb',      # Blue
        'primary_hover': '#1d4ed8', # Darker blue
        'secondary': '#64748b',     # Slate gray
        'secondary_hover': '#475569', # Darker secondary
        'success': '#059669',       # Green
        'error': '#dc2626',         # Red
        'background': '#f8fafc',    # Light gray
        'card': '#ffffff',          # White
        'text': '#1e293b',          # Dark gray
        'text_light': '#64748b',    # Light gray
        'border': '#e2e8f0'         # Border gray
    }

    def on_submit():
        try:
            # Clear any previous error styling
            for entry in [entry1, entry2, entry3]:
                entry.config(highlightbackground=COLORS['border'])

            val1 = float(entry1.get())
            val2 = float(entry2.get())
            val3 = float(entry3.get())
            total = val1 + val2 + val3

            # Update result with success styling
            result_label.config(
                text=f"✓ Calculation Complete",
                foreground=COLORS['success'],
                font=('Segoe UI', 12, 'bold')
            )

            # Update detailed results
            details_label.config(
                text=f"Numbers: {val1:,.2f} + {val2:,.2f} + {val3:,.2f}\nSum: {total:,.2f}",
                foreground=COLORS['text']
            )

        except ValueError:
            # Highlight invalid entries
            for entry in [entry1, entry2, entry3]:
                if not is_valid_number(entry.get()):
                    entry.config(highlightbackground=COLORS['error'])

            result_label.config(
                text="⚠ Please enter valid numbers",
                foreground=COLORS['error'],
                font=('Segoe UI', 12, 'bold')
            )
            details_label.config(text="")

    def is_valid_number(value):
        try:
            float(value)
            return True
        except ValueError:
            return False

    def clear_all():
        entry1.delete(0, tk.END)
        entry2.delete(0, tk.END)
        entry3.delete(0, tk.END)
        result_label.config(text="Enter numbers above and click Calculate", fg=COLORS['text_light'])
        details_label.config(text="")
        update_status_message("💡 All fields cleared. Ready for new input!")
        # Reset entry styling
        for entry in [entry1, entry2, entry3]:
            entry.config(highlightbackground=COLORS['border'])
        # Focus back to first entry
        entry1.focus()

    def on_enter_key(event):
        # Move to next field on Enter key
        if event.widget == entry1:
            entry2.focus()
        elif event.widget == entry2:
            entry3.focus()
        elif event.widget == entry3:
            on_submit()  # Calculate when Enter is pressed on last field

    def on_button_hover_enter(event):
        # Button hover effect
        button = event.widget
        if button == submit_btn:
            button.config(bg=COLORS['primary_hover'])
        elif button == clear_btn:
            button.config(bg=COLORS['secondary_hover'])

    def on_button_hover_leave(event):
        # Button hover effect
        button = event.widget
        if button == submit_btn:
            button.config(bg=COLORS['primary'])
        elif button == clear_btn:
            button.config(bg=COLORS['secondary'])

    def on_entry_change(event):
        # Real-time validation feedback
        entry = event.widget
        value = entry.get()

        if value == "":
            # Empty field - neutral state
            entry.config(highlightbackground=COLORS['border'])
            update_status_message("")
        elif not is_valid_number(value):
            # Invalid input - error state
            entry.config(highlightbackground=COLORS['error'])
            update_status_message("⚠ Please enter a valid number (e.g., 123, 45.67, -89)")
        else:
            # Valid input - success state
            entry.config(highlightbackground=COLORS['success'])
            update_status_message("✓ Valid number entered")

    def update_status_message(message):
        # Update the status message below the inputs
        # This function will be redefined after status_label is created
        pass

    def on_entry_focus_in(event):
        # Show helpful hint when user focuses on an entry
        entry = event.widget
        if entry == entry1:
            update_status_message("💡 Enter your first number here (integers or decimals)")
        elif entry == entry2:
            update_status_message("💡 Enter your second number here")
        elif entry == entry3:
            update_status_message("💡 Enter your third number here")

    def on_entry_focus_out(event):
        # Clear hint when user leaves the entry
        entry = event.widget
        if entry.get() == "":
            update_status_message("")
        elif is_valid_number(entry.get()):
            update_status_message("✓ Ready to calculate")
        else:
            update_status_message("⚠ Please enter a valid number")

    # Create main window
    root = tk.Tk()
    root.title("Number Calculator")
    root.geometry("500x600")
    root.configure(bg=COLORS['background'])
    root.resizable(False, False)

    # Main container with padding
    main_frame = tk.Frame(root, bg=COLORS['background'])
    main_frame.pack(fill='both', expand=True, padx=30, pady=30)

    # Header section
    header_frame = tk.Frame(main_frame, bg=COLORS['card'], relief='flat', bd=0)
    header_frame.pack(fill='x', pady=(0, 20))

    # Title
    title_label = tk.Label(
        header_frame,
        text="Number Calculator",
        font=('Segoe UI', 24, 'bold'),
        fg=COLORS['text'],
        bg=COLORS['card'],
        pady=20
    )
    title_label.pack()

    subtitle_label = tk.Label(
        header_frame,
        text="Enter three numbers to calculate their sum",
        font=('Segoe UI', 12),
        fg=COLORS['text_light'],
        bg=COLORS['card']
    )
    subtitle_label.pack(pady=(0, 20))

    # Input section
    input_frame = tk.Frame(main_frame, bg=COLORS['card'], relief='solid', bd=1)
    input_frame.configure(highlightbackground=COLORS['border'])
    input_frame.pack(fill='x', pady=(0, 20), padx=10)

    # Input fields with modern styling
    input_container = tk.Frame(input_frame, bg=COLORS['card'])
    input_container.pack(fill='x', padx=30, pady=30)

    # First number
    tk.Label(
        input_container,
        text="First Number",
        font=('Segoe UI', 11, 'bold'),
        fg=COLORS['text'],
        bg=COLORS['card']
    ).pack(anchor='w', pady=(0, 5))

    entry1 = tk.Entry(
        input_container,
        font=('Segoe UI', 14),
        relief='solid',
        bd=1,
        highlightthickness=2,
        highlightcolor=COLORS['primary'],
        highlightbackground=COLORS['border']
    )
    entry1.pack(fill='x', pady=(0, 15), ipady=8)
    entry1.bind('<KeyRelease>', on_entry_change)
    entry1.bind('<FocusIn>', on_entry_focus_in)
    entry1.bind('<FocusOut>', on_entry_focus_out)
    entry1.bind('<Return>', on_enter_key)

    # Second number
    tk.Label(
        input_container,
        text="Second Number",
        font=('Segoe UI', 11, 'bold'),
        fg=COLORS['text'],
        bg=COLORS['card']
    ).pack(anchor='w', pady=(0, 5))

    entry2 = tk.Entry(
        input_container,
        font=('Segoe UI', 14),
        relief='solid',
        bd=1,
        highlightthickness=2,
        highlightcolor=COLORS['primary'],
        highlightbackground=COLORS['border']
    )
    entry2.pack(fill='x', pady=(0, 15), ipady=8)
    entry2.bind('<KeyRelease>', on_entry_change)
    entry2.bind('<FocusIn>', on_entry_focus_in)
    entry2.bind('<FocusOut>', on_entry_focus_out)
    entry2.bind('<Return>', on_enter_key)

    # Third number
    tk.Label(
        input_container,
        text="Third Number",
        font=('Segoe UI', 11, 'bold'),
        fg=COLORS['text'],
        bg=COLORS['card']
    ).pack(anchor='w', pady=(0, 5))

    entry3 = tk.Entry(
        input_container,
        font=('Segoe UI', 14),
        relief='solid',
        bd=1,
        highlightthickness=2,
        highlightcolor=COLORS['primary'],
        highlightbackground=COLORS['border']
    )
    entry3.pack(fill='x', pady=(0, 15), ipady=8)
    entry3.bind('<KeyRelease>', on_entry_change)
    entry3.bind('<FocusIn>', on_entry_focus_in)
    entry3.bind('<FocusOut>', on_entry_focus_out)
    entry3.bind('<Return>', on_enter_key)

    # Status message area
    status_label = tk.Label(
        input_container,
        text="💡 Click on any field above to start entering numbers",
        font=('Segoe UI', 10),
        fg=COLORS['text_light'],
        bg=COLORS['card'],
        wraplength=400
    )
    status_label.pack(anchor='w', pady=(0, 20))

    # Redefine update_status_message now that status_label exists
    def update_status_message(message):
        status_label.config(text=message)

    # Button section
    button_frame = tk.Frame(input_container, bg=COLORS['card'])
    button_frame.pack(fill='x')

    # Calculate button
    submit_btn = tk.Button(
        button_frame,
        text="Calculate Sum",
        command=on_submit,
        font=('Segoe UI', 12, 'bold'),
        bg=COLORS['primary'],
        fg='white',
        relief='flat',
        bd=0,
        padx=30,
        pady=12,
        cursor='hand2'
    )
    submit_btn.pack(side='left', padx=(0, 10))
    submit_btn.bind('<Enter>', on_button_hover_enter)
    submit_btn.bind('<Leave>', on_button_hover_leave)

    # Clear button
    clear_btn = tk.Button(
        button_frame,
        text="Clear All",
        command=clear_all,
        font=('Segoe UI', 12),
        bg=COLORS['secondary'],
        fg='white',
        relief='flat',
        bd=0,
        padx=30,
        pady=12,
        cursor='hand2'
    )
    clear_btn.pack(side='left')
    clear_btn.bind('<Enter>', on_button_hover_enter)
    clear_btn.bind('<Leave>', on_button_hover_leave)

    # Results section
    result_frame = tk.Frame(main_frame, bg=COLORS['card'], relief='solid', bd=1)
    result_frame.configure(highlightbackground=COLORS['border'])
    result_frame.pack(fill='x', pady=(0, 20), padx=10)

    result_container = tk.Frame(result_frame, bg=COLORS['card'])
    result_container.pack(fill='x', padx=30, pady=30)

    tk.Label(
        result_container,
        text="Result",
        font=('Segoe UI', 16, 'bold'),
        fg=COLORS['text'],
        bg=COLORS['card']
    ).pack(anchor='w', pady=(0, 15))

    result_label = tk.Label(
        result_container,
        text="Enter numbers above and click Calculate",
        font=('Segoe UI', 12),
        fg=COLORS['text_light'],
        bg=COLORS['card']
    )
    result_label.pack(anchor='w', pady=(0, 10))

    details_label = tk.Label(
        result_container,
        text="",
        font=('Segoe UI', 14),
        fg=COLORS['text'],
        bg=COLORS['card'],
        justify='left'
    )
    details_label.pack(anchor='w')

    # Footer with exit button
    footer_frame = tk.Frame(main_frame, bg=COLORS['background'])
    footer_frame.pack(fill='x', pady=(10, 0))

    exit_btn = tk.Button(
        footer_frame,
        text="Exit Application",
        command=root.destroy,
        font=('Segoe UI', 10),
        bg=COLORS['background'],
        fg=COLORS['text_light'],
        relief='flat',
        bd=0,
        cursor='hand2'
    )
    exit_btn.pack()

    # Keyboard shortcuts
    root.bind('<Control-q>', lambda _: root.destroy())

    # Focus on first entry
    entry1.focus()

    root.mainloop()

if __name__ == "__main__":
    main()