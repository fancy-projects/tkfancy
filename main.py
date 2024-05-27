from tkfancy import App, Button, ctk

app = App()
Button(left="left", right="right", up="up", down="down", text='center',
        command=lambda: ctk.filedialog.askopenfile('hasdf')).show(row=0, column=0)

app.mainloop()